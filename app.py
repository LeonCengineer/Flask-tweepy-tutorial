from flask import Flask, render_template, request
import tweepy

app = Flask(__name__)

@app.route('/')
def index():
	
	
	auth = tweepy.OAuth1UserHandler(
	   consumer_key, consumer_secret, access_token, access_token_secret
	)

	api = tweepy.API(auth)

	public_tweets = api.home_timeline()
	for tweet in public_tweets:
	    print(tweet.text)

	return render_template('home.html', tweets=public_tweets)

if __name__=='__main__':
	app.run(debug=True)
