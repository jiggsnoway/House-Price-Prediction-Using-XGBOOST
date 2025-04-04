from fastapi import FastAPI
from pydantic import BaseModel
import pickle

app = FastAPI()

# Load the trained model
with open("trained_model.pkl", "rb") as file:
    model = pickle.load(file)

# Define input data model
class FeaturesInput(BaseModel):
    features: list[float]  # Expecting a list of floats

@app.post("/predict/")
async def predict(input_data: FeaturesInput):
    prediction = model.predict([input_data.features])
    return {"prediction": prediction.tolist()}
