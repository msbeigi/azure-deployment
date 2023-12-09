
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import uvicorn
# import mlflow
import pandas as pd
from pydantic import BaseModel
import distance_cities as ds

app = FastAPI()

class Geo(BaseModel):
    name:str
    long:float
    lat:float


@app.post("/locaction")
async def get_cities_loc(city:str):
    df_cities=ds.create_cities_dataframe()
    city_data = df_cities[df_cities['city'] == city]
    if city_data.empty:
        raise HTTPException(status_code=404, detail="City not found")
    
    
    citi_latitude = city_data['latitude'].values[0]
    citi_longitude = city_data['longitude'].values[0]
    
    my_location = Geo(name=city, lat=citi_latitude, long=citi_longitude)

    result=JSONResponse( jsonable_encoder(my_location))
    return result



if __name__ == '__main__':
    uvicorn.run(app,port=8007,host='0.0.0.0')