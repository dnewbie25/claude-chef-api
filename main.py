from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from chef import chef_claude

app = FastAPI()

# origins = [
#     "https://my-ai-chef.netlify.app/",
#     "http://localhost:"
# ]

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RecipeRequest(BaseModel):
  ingredients: list[str]

@app.post("/recipe")
async def read_item(item: RecipeRequest):
  return chef_claude(item.ingredients)