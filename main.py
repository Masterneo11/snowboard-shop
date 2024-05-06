import json
from fastapi import FastAPI

from models import Snowboard, Brand

app = FastAPI()

with open("snowboards.json", "r") as f:
    snowboard_list = json.load(f)

snowboards: list = []
for i in snowboard_list:
    snowboard = Snowboard(**i)
    snowboards.append(snowboard)


@app.get("/snowboards")
async def get_snowboards() -> list[Snowboard]:
    return snowboards 

@app.get("/brands")
async def get_brands() -> list[Brand]:
    return Brand

@app.post("/snowboards")
async def create_snowboard(snowboard: Snowboard) -> None:
    snowboards.append(snowboard)

@app.put("/snowboards/{snow_id}")
async def update_snowboard_info(snow_id: int, updated_snowboard: Snowboard) -> None:
    index = int
    found = False
    for i, snowboard in enumerate(snowboards):
        if snowboard.id == snow_id:
            found = True
            index = i
    if found:
        snowboards[index] = updated_snowboard
    else:
        snowboards.append(updated_snowboard)

@app.delete("/snowboards/{snowboard_id}")
async def delete_snowboard_info(snowboard_id: int) -> None:
    for i, snowboard in enumerate(snowboards):
        if snowboard.id == snowboard_id:
            snowboards.pop(i)
            return
    