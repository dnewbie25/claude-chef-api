from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
  print('holiwi')
  return {"message": "Hello World asas"}