
from fastapi import FastAPI
from app.database import Base, engine
from app.routes import auth, sweets

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sweet Shop Management")

app.include_router(auth.router)
app.include_router(sweets.router)

@app.get("/")
def root():
    return {"status": "running"}
