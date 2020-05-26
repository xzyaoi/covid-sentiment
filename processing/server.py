import os
from flask import Flask, request
from werkzeug.utils import secure_filename
from requests import get
from sentiment import wrapper
import re
import threading

app = Flask(__name__)

def background_task(url, filename):
    download(url, filename)

def download(url, filename):
    # open in binary mode
    print("I am downloding...")
    response = get(url)
    target = os.path.join("data", filename)
    with open(target, "wb") as file:
        # write to file
        file.write(response.content)
    print("Downloaded!")
    print("Now calls sentiment and wordcloud module...")
    wrapper(target)


@app.route('/receive', methods=['POST'])
def foo():
    data = request.form
    url = data['link']
    filename = data['filename']
    x = threading.Thread(target=background_task, args=(url,filename,))
    x.start()
    return data