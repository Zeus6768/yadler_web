from fastapi.responses import FileResponse
from fastapi import FastAPI
from myfunc import mRound

app = FastAPI()

@app.get('/')
async def root():
	return FileResponse('index.html')
