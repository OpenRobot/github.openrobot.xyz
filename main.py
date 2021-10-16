import fastapi, uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse as redirect

app = FastAPI(docs_url=None, redoc_url=None)

@app.get('/')
async def homepage():
    return redirect('https://github.com/OpenRobot')

@app.get('/packages')
async def redirect_packages():
    return redirect('https://github.com/OpenRobot-Packages')

@app.get('/Packages')
async def redirect_packages():
    return redirect('https://github.com/OpenRobot-Packages')

@app.get('/packages/{name}')
async def redirect_packages(name: str):
    return redirect(f'https://github.com/OpenRobot-Packages/{name}')

@app.get('/Packages/{name}')
async def redirect_packages(name: str):
    return redirect(f'https://github.com/OpenRobot-Packages/{name}')

@app.get('/{name}')
async def redirect_specific(name: str):
    return redirect(f'https://github.com/OpenRobot/{name}')

def run():
    uvicorn.run(app, host="127.0.0.1", port="5000", loop="auto")

run()