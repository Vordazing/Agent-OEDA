from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import requests
import connectiondb as db
import search


app = FastAPI()


class Message(BaseModel):
    chat_id: int
    text: str


@app.post("/send_message")
def send_ip_to_telegram(message: Message):
    telegram_bot_token = "6155412112:AAHf07zUQi5dJC0y2MpyjbedqQwkRRUErtU"
    url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage"
    text = f'{message.text}\n Объект: {search.find_network(message.text)}'
    params = {
        'chat_id': message.chat_id,
        'text': text,
    }
    response = requests.post(url, data=params)
    if response.status_code != 200:
        return {"status": "Failed to send message"}
    else:
        return {"status": "Message sent successfully"}


@app.get("/forward")
def forward_to_telegram(ip_address: str = Query(...)):
    post_url = "http://0.0.0.0:8888/send_message"
    cursor = db.connection.cursor()
    query = f"SELECT chat_id FROM umcbot.users_umc WHERE apireport = 'yes';"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    for row in result:
        chat_id = row[0]
        message_data = {
            'chat_id': chat_id,
            'text': ip_address,
        }
        response = requests.post(post_url, json=message_data)
        if response.status_code != 200:
            return JSONResponse(content={"status": "Failed to forward message"}, status_code=response.status_code)

    return JSONResponse(content={"status": "Messages forwarded successfully"})


