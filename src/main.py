from . import scrape
from fastapi import FastAPI

app = FastAPI()


@app.get("/iamalive")
async def iamalive():
    return {"message": "True"}

@app.get("/whois/{name}")
async def whois(name: str):
    return {"message": scrape.whois(name)}
