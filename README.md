# 🧠 Emotion Detection with Flask and Watson AI

This is a web application built with **Flask** that integrates with **IBM Watson AI** to detect the **predominant emotions** in a given text.

The system analyzes the input phrase, returns **a score from 0 to 10** for each emotion (like **anger**, **joy**, **fear**, **disgust**, etc.), and highlights the **dominant emotion** in the sentence.

This application includes:

- ✅ **Error handling**
- 🧪 **Unit testing** with `unittest`

---

## 🎓 Final Project – IBM AI Course

This app was developed as the final project for the course:

> **"Developing AI Applications with Python and Flask"**  
> by **IBM**.

---

## 🚀 How to Run the Project

### Prerequisites

- Python 3 installed
- Flask installed
- IBM Watson NLU API credentials (API key and endpoint)

### Running the app

```bash
# 1. Clone the repository
git clone https://github.com/your-username/your-repo.git](https://github.com/vitor115/EmotionDetector.git
cd EmotionDetector

# 2. Install Flask
pip install flask

# 3. Run the server
python server.py
```

Then, open your browser and go to:

```
http://localhost:5000
```

---

## 🧪 Running Tests

To run the unit tests:

```bash
python test_emotion_detection.py
```

---

## 📁 Project Structure

```
.
├── EmotionDetection/           # Core logic and emotion analysis module
├── static/                     # Static files (CSS, JS, images)
├── templates/                  # HTML templates for rendering views
├── .gitignore
├── LICENSE
├── README.md
├── server.py                   # Flask application entry point
└── test_emotion_detection.py   # Unit tests
```

---

## 🛠️ Technologies Used

- [Flask](https://flask.palletsprojects.com/)
- [IBM Watson Natural Language Understanding API](https://www.ibm.com/cloud/watson-natural-language-understanding)
- Python 3.x

---

## 🤖 Credits

Developed by Vitor Ravacci as part of the IBM AI Applications course using Python and Flask.

---
