# 👨‍🎓 Student Attendance System using Face Recognition

A smart student attendance system built with **Django** and **OpenCV** that uses **facial recognition** to automate and streamline attendance marking.

---

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/Django-4.x-darkgreen?style=for-the-badge&logo=django)
![OpenCV](https://img.shields.io/badge/OpenCV-Face%20Detection-red?style=for-the-badge&logo=opencv)


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

## 🧪 Run Locally

Get the project up and running on your machine with a few simple steps! 🚀

```bash
# Clone the repository


# Navigate into the project directory
cd student_attendance_system

# Create a virtual environment
virtualenv env

# Activate the virtual environment (Windows)
env\Scripts\activate

# If requirements.txt is missing, install manually
pip install django opencv deepface numpy scikit-learn joblib

# Run the Django development server
python manage.py runserver
