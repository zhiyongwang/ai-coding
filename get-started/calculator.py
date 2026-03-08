from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import os

app = FastAPI()

# 1. 挂载静态目录（放在子路径以免拦截 API）
app.mount("/static", StaticFiles(directory="static", html=True), name="static")

# optional: serve index.html at root
@app.get("/")
def read_index():
    file_path = "static/index.html"
    if not os.path.exists(file_path):
        return HTMLResponse(content="<h1>index.html not found</h1>", status_code=404)
    return FileResponse(file_path)

class CalcRequest(BaseModel):
    a: float
    b: float
    op: str  # '+', '-', '*', '/'

class CalcResponse(BaseModel):
    result: float

@app.post("/api/calc", response_model=CalcResponse)
def calc(req: CalcRequest):
    a, b, op = req.a, req.b, req.op
    if op == "+":
        r = a + b
    elif op == "-":
        r = a - b
    elif op == "*":
        r = a * b
    elif op == "/":
        if b == 0:
            raise HTTPException(status_code=400, detail="division by zero")
        r = a / b
    else:
        raise HTTPException(status_code=400, detail="unknown operator")
    return {"result": r}

# --- optional: run with `uvicorn calculator:app --reload` ---