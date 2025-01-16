# test
import uvicorn
from fastapi import FastAPI
from UrlData import UrlData
from API import get_prediction
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(debug=True)

# ------------------------------------------

# Enabling CORS policy

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------------------------------


@app.post("/predict")
def predict(url: str):

    prediction = get_prediction(url)
    print(prediction)

    return prediction



if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
