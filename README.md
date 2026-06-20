# Fruit Classifier

A small machine-learning web application that predicts whether a fruit is an apple or orange from its weight, color, and texture.

## Why it matters

The project demonstrates the complete path from a simple model to a usable product: collect inputs, make a prediction through an API, and show the result in a browser.

## Technology

Python, scikit-learn decision trees, FastAPI, HTML, CSS, and TypeScript.

## Run

```bash
pip install fastapi uvicorn scikit-learn pandas jinja2
tsc
uvicorn main:app --reload
```

Open `http://127.0.0.1:8000`.

This is an educational model trained on a small example dataset.
