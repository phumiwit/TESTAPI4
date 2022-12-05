from fastapi import FastAPI
from key import Keyword_Spotting_Service
import uvicorn
app = FastAPI()

@app.get('/')
def Hello():
    return {'Hello':'Hello'}

@app.get('/predict')
def predict_genre(path :str):
    kss = Keyword_Spotting_Service()
    keyword1,keyword2= kss.prediction(path)
    return {"prediction":keyword1}

@app.get('/value')
def value_genre(path : str):
    kss = Keyword_Spotting_Service()
    keyword1,keyword2 = kss.prediction(path)
    
    return keyword2


if __name__ == "__main__":
     uvicorn.run(app,host='127.0.0.1',port=8000)