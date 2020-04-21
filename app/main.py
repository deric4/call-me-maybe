import time
import asyncio
from typing import List, Dict
from fastapi import BackgroundTasks, FastAPI, Request
from urllib.parse import parse_qs

from app.utils.twil import dial_me_in, dial_office_in, check_the_phone_line


app = FastAPI()


async def looper():
    while True:
        check_the_phone_line()
        await asyncio.sleep(300)

def call_me_maybe(event: Dict):
    dial_office_in(event['ConferenceSid'][0])

@app.get("/")
async def root(background_tasks: BackgroundTasks):
    """initialiazes the looper function"""
    background_tasks.add_task(looper)
    return {"message": "hello world"}


@app.post("/conference_events")
async def conference_events(request: Request, background_tasks: BackgroundTasks):
    body = await request.body()
    new_body = parse_qs(body.decode())

    #only when a new conference is created
    if new_body['StatusCallbackEvent'][0] == 'participant-join' and new_body['SequenceNumber'][0] == '1':
        background_tasks.add_task(call_me_maybe,new_body)
    return 200

@app.post("/office_events")
async def office_events(request: Request, background_tasks: BackgroundTasks):
    """ respond to events when calling the office """

    body = await request.body()
    new_body = parse_qs(body.decode())
    background_tasks.add_task(dial_me_in, new_body['CallSid'][0])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
