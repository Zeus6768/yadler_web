from fastapi.responses import FileResponse
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
	return FileResponse('index.html')
