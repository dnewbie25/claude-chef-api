from fastapi import FastAPI
from chef import chef_claude
app = FastAPI()

@app.post("/recipe")
async def read_item(item: str):
  return chef_claude(item.ingredients)