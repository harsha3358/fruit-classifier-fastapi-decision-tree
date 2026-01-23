# 🍎🍊 Fruit Classifier using Decision Tree (FastAPI + Web UI)

This project is a simple Machine Learning web application that classifies
a fruit as **Apple** or **Orange** based on:

- Weight
- Color
- Texture

The ML model is built using **scikit-learn (Decision Tree)** and is served
through **FastAPI** with a modern HTML/CSS/TypeScript frontend.

---

## Features

- Decision Tree ML model
- FastAPI backend
- Web UI (HTML + CSS + TypeScript)
- Real-time prediction
- Orchard themed interface
- Clean project structure

---

## 🗂️ Project Structure

```
fruit_app/
│
├── main.py
├── tsconfig.json
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   ├── app.ts
│   ├── app.js
│   └── images/
│       └── bg.jpg
```

---

## 🧠 Tech Stack

- Python
- FastAPI
- scikit-learn
- Pandas
- HTML, CSS, TypeScript
- Uvicorn

---

## 🔧 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/fruit-classifier-fastapi-ui.git
cd fruit-classifier-fastapi-ui
```

### 2. Create virtual environment (optional but recommended)
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Python dependencies
```bash
pip install fastapi uvicorn scikit-learn pandas jinja2
```

### 4. Install TypeScript
```bash
npm install -g typescript
```

### 5. Compile TypeScript
```bash
tsc
```

### 6. Run the app
```bash
uvicorn main:app --reload
```

Open browser:
```
http://127.0.0.1:8000
```

---

## 🧪 Example Input

| Weight | Color  | Texture |
|--------|--------|---------|
| 165    | Orange | Rough   |

### Output
```
Predicted Fruit: Orange
```

---

## 📌 Notes
- `app.ts` is compiled into `app.js` using TypeScript compiler.
- The UI is served directly by FastAPI.
- `/predict` is the API endpoint used by the frontend.

---

## 🙌 Author
Built by **Harsha Vardhan Reddy**
