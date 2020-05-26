import os
from quart import Quart, request
from werkzeug.utils import secure_filename
from requests import get
import re
import threading
import rfc6266
app = Quart(__name__)

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

@app.route('/receive', methods=['POST'])
async def foo():
    data = await request.form
    url = data['link']
    filename = data['filename']
    x = threading.Thread(target=background_task, args=(url,filename,))
    x.start()
    return data

app.run("0.0.0.0", port=5000)