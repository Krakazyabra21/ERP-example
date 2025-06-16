from fastapi import FastAPI
import uvicorn
app = FastAPI(title="ERP-example", version="0.1")

@app.on_event("startup")
async def startupEvent():
    await print("123")

app.include_router()

if __name__=="__main__":
    uvicorn.run("main:app", host="0.0.0.0", port="8000", reload=True)