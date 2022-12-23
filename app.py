from flask import Flask, render_template, request
import tweepy

app = Flask(__name__)

@app.route('/')
def index():
	
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
	api = tweepy.API(auth, wait_on_rate_limit=True)

	public_tweets = api.home_timeline()
	for tweet in public_tweets:
	    print(tweet.text)

	return render_template('home.html', tweets=public_tweets)

if __name__=='__main__':
	app.run(debug=True)
