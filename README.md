# Student Attendance System

## 1. Technologies Used

- **Languages**: Python, HTML, CSS, JavaScript
- **Frameworks**: Django (Python web framework)
- **Libraries**: OpenCV, DeepFace, NumPy, Scikit-learn, Joblib
- **Database**: JSON files for storing attendance records and face encodings

## 2. Working of This Project

This project is a student attendance system that uses facial recognition to mark attendance. The system allows users to add students by capturing their images, recognize students using a webcam, and view attendance records. The main components of the project are:

1. **Add Student**: Capture images of a student and save them for future recognition.
2. **Recognize Student**: Use a webcam to recognize a student and mark their attendance.
3. **View Attendance**: Display the attendance records of all students.

## 3. Explanation of Each File

### `views.py`

This file contains the main logic for handling requests and processing data.

- **Functions**:
  - `index`: Renders the home page.
  - `add_student`: Renders the page for adding a new student.
  - `save_image`: Handles the saving of captured images.
  - `encode_faces`: Encodes the faces of students and saves the encodings.
  - `clear_and_reencode_faces`: Clears existing encodings and re-encodes all faces.
  - `recognize_student`: Renders the page for recognizing a student.
  - `recognize_face`: Handles the face recognition process.
  - `view_attendance`: Renders the page for viewing attendance records.

### `urls.py`

This file maps URLs to the corresponding view functions.

- **URL Patterns**:
  - `''`: Maps to the `index` view.
  - `'add_student/'`: Maps to the `add_student` view.
  - `'save_image/'`: Maps to the `save_image` view.
  - `'recognize_student/'`: Maps to the `recognize_student` view.
  - `'recognize_face/'`: Maps to the `recognize_face` view.
  - `'view_attendance/'`: Maps to the `view_attendance` view.

### `index.html`

This file contains the HTML for the home page.

- **Elements**:
  - Buttons to navigate to the add student, recognize student, and view attendance pages.

### `add_student.html`

This file contains the HTML and JavaScript for adding a new student.

- **Elements**:
  - Form to input the student's name, role, and department.
  - Video element to capture images using the webcam.
  - JavaScript to handle the image capture and saving process.

### `recognize_student.html`

This file contains the HTML and JavaScript for recognizing a student.

- **Elements**:
  - Video element to capture images using the webcam.
  - JavaScript to handle the face recognition process.

### `view_attendance.html`

This file contains the HTML for viewing attendance records.

- **Elements**:
  - Table to display the attendance records.

