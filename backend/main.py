from flask import Flask
import praw
from reddit_credentials import Reddit_Credentials
from parser import Parser

app = Flask(__name__)

rc = Reddit_Credentials()
reddit = praw.Reddit(client_id=rc.client_id,
                     client_secret=rc.client_secret,
                     redirect_uri=rc.redirect_uri,
                     user_agent=rc.user_agent)
# print(reddit.auth.url(['identity'], '...', 'permanent'))

@app.route("/search/<item>")
def keyboard(item):
    subreddit = reddit.subreddit('buildapcsales')
    hot = subreddit.hot()
    p = Parser(hot, item)
    return p.return_json()

if __name__ == "__main__":
    app.run(debug=True)