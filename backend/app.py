from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn, os

app = FastAPI(title="GoGate Panel", version="0.1.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.get("/")
async def root():
    return {"service": "GoGate Panel", "status": "running", "version": "0.1.0"}

@app.get("/api/nodes")
async def list_nodes():
    return {"nodes": []}

@app.post("/api/nodes")
async def add_node(name: str, host: str, api_token: str):
    return {"node_id": "new", "name": name, "host": host, "status": "pending"}

@app.get("/api/users")
async def list_users():
    return {"users": []}

@app.post("/api/users")
async def create_user(name: str, protocol: str = "vmess"):
    return {"user_id": "new", "name": name, "protocol": protocol}

@app.get("/api/subscription")
async def subscription(token: str):
    return {"configs": []}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
