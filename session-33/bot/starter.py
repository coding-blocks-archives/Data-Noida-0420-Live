from flask import Flask, request
import requests
import random

app = Flask("chatbot")
token = ""

verify_token = "ham-honge-kamiyaab"

jokes = [
    "Hi, I am joker, But you can not laugh",
    "I invented a new word!  Plagiarism!",
    "No exams in corona. We care about you guys"
]

@app.route("/callback/", methods=["get"])
def handle_callback():
    print(request.args)
    if request.args["hub.verify_token"] == verify_token:
        return request.args["hub.challenge"]


@app.route("/callback/", methods=["post"])
def handle_event():
    content = request.get_json()

    if "entry" in content:
        entries = content["entry"]
        for entry in entries:
            if "messaging" in entry:
                messaging_list = entry["messaging"]
                for messaging in messaging_list:

                    sender = messaging["sender"]["id"]

                    if "message" in messaging:
                        message = messaging["message"]
                        if "text" in message:
                            text = message["text"]

                            print(sender, " : ", text)
                            respond(sender, text)




    return "Hola"

def process(message):
    if "joke" in message:
        return random.choice(jokes)
    else:
        return "Please ask me to tell you a joke"


def respond(sender, msg):

    if "image" in msg:
        respond_image(sender, msg)
        return

    processed = process(msg)

    message = {
        "recipient": {
            "id": sender
        },
        "message": {
            "text": processed
        }
    }

    url = "https://graph.facebook.com/v7.0/me/messages?access_token={}"
    requests.post(url.format(token), json=message)

def process_to_url(msg):
    if "dog" in msg:
        url = "https://d17fnq9dkz9hgj.cloudfront.net/uploads/2018/04/Pomeranian_02.jpg"
    elif "cat" in msg:
        url = "https://i.pinimg.com/originals/f3/bd/84/f3bd8497e15399201b634714ec5ed390.jpg"
    else:
        url = "https://www.hindustantimes.com/rf/image_size_1200x900/HT/p2/2019/09/25/Pictures/_115e3b3a-df82-11e9-b0cd-667d8786d605.jpg"

    return url

def respond_image(sender, msg):

    url = process_to_url(msg)

    message = {
      "recipient":{
        "id": sender
      },
      "message":{
        "attachment":{
          "type":"image",
          "payload":{
            "url": url,
            "is_reusable":True
          }
        }
      }
    }

    url = "https://graph.facebook.com/v7.0/me/messages?access_token={}"
    requests.post(url.format(token), json=message)



