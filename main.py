from fastapi.responses import FileResponse
from fastapi import FastAPI

app = FastAPI()

@app.get('/yadler')
async def root():
	return FileResponse('index.html')
