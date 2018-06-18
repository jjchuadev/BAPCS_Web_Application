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

@app.route("/")
def index():
    subreddit = reddit.subreddit('buildapcsales')
    hot = subreddit.hot()
    ret = "\n".join(["<p><a href={}>{}</a></p>".format(s.shortlink, s.title) for s in hot if not s.stickied])
    return ret

@app.route("/monitor")
def monitors():
    subreddit = reddit.subreddit('buildapcsales')
    hot = subreddit.hot()
    p = Parser(hot, "Monitor")
    return p.return_links()

if __name__ == "__main__":
    app.run(debug=True)