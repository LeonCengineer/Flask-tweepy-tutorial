from flask import Flask, render_template
import tweepy

app = Flask(__name__)

@app.route('/')
def index():
	auth = tweepy.OAuthHandler('7UzudjdAzuBxfRBDI8yo0KhXh', 'gXcSE0AYYDSZDOUaAtEgUDYJ9QCV1ifXgLLEM6EOUDjbZrmXQA')
	auth.set_access_token('2638191615-S6kii5fXiPPdSqJrasLYxrEVnJZRfhMaEj307y0', 'U3VrNfUoNkscC8DkYJhRpYVdt9WcYYzUCOBgd9sFIFy3B')
	api = tweepy.API(auth)
	public_tweets = api.user_timeline('shambekela_')

	return render_template('home.html', tweets=public_tweets, count=100)

if __name__=='__main__':
	app.run(debug=True)