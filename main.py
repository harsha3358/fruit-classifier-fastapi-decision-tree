import pandas as pd
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from starlette.requests import Request

app = FastAPI()

# serve static & templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# -------------------------------
# Train model
# -------------------------------
data = {
    "Weight": [110,115,120,125,130,135,140,145,150,155,
               170,175,180,185,190,195,200,205,210,215],
    "Color": [
        "Red","Red","Green","Green","Red","Green","Red","Green","Red","Green",
        "Orange","Orange","Orange","Orange","Orange","Orange","Orange","Orange","Orange","Orange"
    ],
    "Texture": [
        "Smooth","Smooth","Smooth","Smooth","Smooth","Smooth","Smooth","Smooth","Smooth","Smooth",
        "Rough","Rough","Rough","Rough","Rough","Rough","Rough","Rough","Rough","Rough"
    ],
    "Fruit": [
        "Apple","Apple","Apple","Apple","Apple","Apple","Apple","Apple","Apple","Apple",
        "Orange","Orange","Orange","Orange","Orange","Orange","Orange","Orange","Orange","Orange"
    ]
}

df = pd.DataFrame(data)

le_color = LabelEncoder()
le_texture = LabelEncoder()
le_fruit = LabelEncoder()

df["Color"] = le_color.fit_transform(df["Color"])
df["Texture"] = le_texture.fit_transform(df["Texture"])
df["Fruit"] = le_fruit.fit_transform(df["Fruit"])

X = df[["Weight", "Color", "Texture"]]
y = df["Fruit"]

model = DecisionTreeClassifier(criterion="entropy", max_depth=3)
model.fit(X, y)

# -------------------------------
# Request schema
# -------------------------------
class FruitInput(BaseModel):
    weight: int
    color: str
    texture: str

# -------------------------------
# Routes
# -------------------------------
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict")
def predict(data: FruitInput):
    color_enc = le_color.transform([data.color])[0]
    texture_enc = le_texture.transform([data.texture])[0]

    test_df = pd.DataFrame([[data.weight, color_enc, texture_enc]],
                           columns=["Weight", "Color", "Texture"])

    pred = model.predict(test_df)
    return {"prediction": le_fruit.inverse_transform(pred)[0]}
