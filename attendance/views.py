from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
import os
import cv2
import numpy as np
from deepface import DeepFace
from sklearn.preprocessing import Normalizer
import joblib
import base64
import json
from datetime import datetime, date

FACES_DIR = 'faces/'
ENCODINGS_FILE = 'face_data.pkl'
ATTENDANCE_FILE = 'attendance.json'
CASCADE_PATH = os.path.join(os.path.dirname(__file__), 'haarcascade_frontalface_default.xml')

# Load saved face encodings
if os.path.exists(ENCODINGS_FILE) and os.path.getsize(ENCODINGS_FILE) > 0:
    data = joblib.load(ENCODINGS_FILE)
    known_encodings = data['encodings']
    known_names = data['names']
    known_roles = data.get('roles', [])
    known_departments = data.get('departments', [])
else:
    known_encodings = []
    known_names = []
    known_roles = []
    known_departments = []

# Load attendance records
if os.path.exists(ATTENDANCE_FILE):
    with open(ATTENDANCE_FILE, 'r') as f:
        attendance_records = json.load(f)
else:
    attendance_records = []

def index(request):
    return render(request, 'attendance/index.html')

def add_student(request):
    return render(request, 'attendance/add_student.html')

def save_image(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data['name']
        role = data['role']
        department = data['department']
        image_data = data['image']
        folder_path = os.path.join(FACES_DIR, name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        image_count = len(os.listdir(folder_path)) + 1
        image_path = os.path.join(folder_path, f"{name}_{image_count}.jpg")
        image_data = base64.b64decode(image_data.split(',')[1])
        with open(image_path, 'wb') as f:
            f.write(image_data)
        if image_count == 10:
            encode_faces(name, role, department)
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

def encode_faces(name=None, role=None, department=None):
    global known_encodings, known_names, known_roles, known_departments
    if name:
        folder_path = os.path.join(FACES_DIR, name)
        if os.path.isdir(folder_path):
            for file in os.listdir(folder_path):
                if file.endswith('.jpg') or file.endswith('.png'):
                    file_path = os.path.join(folder_path, file)
                    try:
                        encoding = DeepFace.represent(file_path, model_name='Facenet', enforce_detection=False)[0]['embedding']
                        if not np.isnan(encoding).any():
                            known_encodings.append(Normalizer().fit_transform([encoding])[0])
                            known_names.append(name)
                            known_roles.append(role)
                            known_departments.append(department)
                        else:
                            print(f"Invalid encoding for {file_path}")
                    except Exception as e:
                        print(f"Error encoding {file_path}: {e}")
    else:
        for folder in os.listdir(FACES_DIR):
            folder_path = os.path.join(FACES_DIR, folder)
            if os.path.isdir(folder_path):
                for file in os.listdir(folder_path):
                    if file.endswith('.jpg') or file.endswith('.png'):
                        file_path = os.path.join(folder_path, file)
                        try:
                            encoding = DeepFace.represent(file_path, model_name='Facenet', enforce_detection=False)[0]['embedding']
                            if not np.isnan(encoding).any():
                                known_encodings.append(Normalizer().fit_transform([encoding])[0])
                                known_names.append(folder)
                                known_roles.append(role)
                                known_departments.append(department)
                            else:
                                print(f"Invalid encoding for {file_path}")
                        except Exception as e:
                            print(f"Error encoding {file_path}: {e}")

    # Save the updated encodings
    joblib.dump({'encodings': known_encodings, 'names': known_names, 'roles': known_roles, 'departments': known_departments}, ENCODINGS_FILE)
    print("Encodings updated and saved!")

def clear_and_reencode_faces():
    global known_encodings, known_names, known_roles, known_departments
    known_encodings = []
    known_names = []
    known_roles = []
    known_departments = []
    encode_faces()

def recognize_student(request):
    return render(request, 'attendance/recognize_student.html')

def recognize_face(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        image_data = data['image']
        image_data = base64.b64decode(image_data.split(',')[1])
        nparr = np.frombuffer(image_data, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier(CASCADE_PATH)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50))

        for (x, y, w, h) in faces:
            face = img[y:y+h, x:x+w]
            try:
                encoding = DeepFace.represent(face, model_name='Facenet', enforce_detection=False)[0]['embedding']
                if not np.isnan(encoding).any():
                    normalized_encoding = Normalizer().fit_transform([encoding])[0]

                    distances = [np.linalg.norm(normalized_encoding - enc) for enc in known_encodings]

                    if distances and min(distances) < 0.4:
                        index = distances.index(min(distances))
                        name = known_names[index]
                        role = known_roles[index]
                        department = known_departments[index]
                        today = date.today().strftime('%Y-%m-%d')
                        for record in attendance_records:
                            if record['name'] == name and record['time'].startswith(today):
                                return JsonResponse({'success': False, 'message': 'Your attendance is already marked'})
                        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        attendance_records.append({'name': name, 'role': role, 'department': department, 'time': time})
                        with open(ATTENDANCE_FILE, 'w') as f:
                            json.dump(attendance_records, f)
                        return JsonResponse({'success': True, 'name': name, 'role': role, 'department': department, 'time': time})
                    else:
                        print("No match found. Minimum distance:", min(distances))
                else:
                    print("Invalid encoding detected during recognition")
            except Exception as e:
                print(f"Error during face recognition: {e}")

        return JsonResponse({'success': False})
    return JsonResponse({'success': False})

def view_attendance(request):
    try:
        with open(ATTENDANCE_FILE, 'r') as f:
            attendance_records = json.load(f)
    except Exception as e:
        print(f"Error loading attendance records: {e}")
        attendance_records = []
    return render(request, 'attendance/view_attendance.html', {'records': attendance_records})

# Clear and re-encode faces on server start
clear_and_reencode_faces()