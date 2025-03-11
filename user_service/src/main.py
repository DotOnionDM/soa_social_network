from fastapi import FastAPI

app = FastAPI()


@app.get("/v1/")
def read_root():
    return {"message": "Hello!"}
