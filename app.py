from flask import Flask, render_template, request
import tweepy

app = Flask(__name__)

@app.route('/')
def index():
	
	
	auth = tweepy.OAuth1UserHandler(
	   '7UzudjdAzuBxfRBDI8yo0KhXh', 'gXcSE0AYYDSZDOUaAtEgUDYJ9QCV1ifXgLLEM6EOUDjbZrmXQA', '2638191615-S6kii5fXiPPdSqJrasLYxrEVnJZRfhMaEj307y0', 'U3VrNfUoNkscC8DkYJhRpYVdt9WcYYzUCOBgd9sFIFy3B')
	)

	api = tweepy.API(auth)

	public_tweets = api.home_timeline()
	for tweet in public_tweets:
	    print(tweet.text)

	return render_template('home.html', tweets=public_tweets)

if __name__=='__main__':
	app.run(debug=True)
