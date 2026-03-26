from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "SLOP-SCANNER ONLINE", "version": "0.1.0"}