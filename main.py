import json
from fastapi import FastAPI

from models import Snowboard 

app = FastAPI()

with open("snowboards.json", "r") as f:
    snowboard_list = json.load(f)

snowboards = []
for i in snowboard_list:
    snowboard = Snowboard(**i)
    snowboards.append(snowboard)

@app.get("/snowboards")
async def get_snowboards() -> list[Snowboard]:
    return snowboards
    
@app.post("/snowboards")
async def create_snowboard(snowboard: Snowboard) -> None:
    snowboards.append(snowboard)

@app.put("/snowboards/{snow_id}")
async def update_snowboard_info(snow_id: int, updated_snowboard: Snowboard) -> None:
    for i, snowboard in enumerate(snowboards):
        if snowboard.id == snow_id:
            snowboards[i] = updated_snowboard
            return

@app.delete("/snowboards/{snowboard_id}")
async def delete_snowboard_info(snowboard_id: int) -> None:
    for i, snowboard in enumerate(snowboards):
        if snowboard.id == snowboard_id:
            snowboards.pop(i)
            return
    