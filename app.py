from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

def get_meme():
    url = "https://meme-api.com/gimme/wholesomememes"
    response = json.loads(requests.request("GET", url).text)
    title = response["title"]
    meme_pic = response["preview"][1]
    subreddit = response["subreddit"]
    return title,meme_pic,subreddit

@app.route("/")
def index():
    title,meme_pic,subreddit = get_meme()
    return render_template("index.html", title=title, meme_pic=meme_pic, subreddit=subreddit)

if __name__ == "__main__":
    app.run(debug=True)