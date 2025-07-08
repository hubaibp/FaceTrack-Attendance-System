# 👨‍🎓 Student Attendance System using Face Recognition

A smart student attendance system built with **Django** and **OpenCV** that uses **facial recognition** to automate and streamline attendance marking.

---

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/Django-4.x-darkgreen?style=for-the-badge&logo=django)
![OpenCV](https://img.shields.io/badge/OpenCV-Face%20Detection-red?style=for-the-badge&logo=opencv)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

---

## 🚀 Features

- 👤 Add student details with webcam image capture
- 📸 Real-time face recognition using webcam
- 📝 Automatically marks attendance
- 📊 View attendance records in a table
- 🔒 Face encoding & storage using `DeepFace`, `OpenCV`, `NumPy`

---

## 🛠️ Technologies Used

- **Languages**: Python, HTML5, CSS3, JavaScript  
- **Framework**: Django  
- **Libraries**: OpenCV, DeepFace, NumPy, Scikit-learn, Joblib  
- **Database**: JSON (for attendance records & face encodings)

---

## 🧠 How It Works

1. **Add Student**  
   Capture student's name, role, department, and webcam image.

2. **Encode Faces**  
   Encode all student faces and store them using `DeepFace` and `Joblib`.

3. **Recognize Student**  
   Activate webcam, detect face, match with known encodings, and mark attendance.

4. **View Attendance**  
   View all attendance logs in an organized HTML table.

---

## 📂 Project Structure

### `views.py`
Handles the logic and processes for each route:
- `index()`: Homepage  
- `add_student()`: Render add student page  
- `save_image()`: Save student face images  
- `encode_faces()`: Encode student faces  
- `clear_and_reencode_faces()`: Refresh face encodings  
- `recognize_student()`: Render recognition page  
- `recognize_face()`: Process recognition and log attendance  
- `view_attendance()`: Show attendance logs

### `urls.py`
Maps URLs to views:
```plaintext
/ → index  
/add_student/ → add_student  
/save_image/ → save_image  
/recognize_student/ → recognize_student  
/recognize_face/ → recognize_face  
/view_attendance/ → view_attendance  
