from fastapi import FastAPI
from pydantic import BaseModel
print("3")
app= FastAPI()

@app.get("/")

def home():
    return {"Message": "Inside Home"}

@app.get("/about/{input}")

def about(input):
    return {f'This is under {input} page'}

class Updatelist(BaseModel):
    name: str
    Age: int

@app.post("/profile")

def profile(item: Updatelist):
    return {
        "name": item.name,
        "Age": item.Age
    }