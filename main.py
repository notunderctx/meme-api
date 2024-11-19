from flask import Flask, jsonify, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from meme import RedditMemes

app = Flask(__name__)
limiter = Limiter(
    get_remote_address,
    app=app,
)

@app.errorhandler(429)
def ratelimit_handler(e):
    return jsonify({
        "error": "Too Many Requests",
        "message": "You have exceeded your request limit. Please try again later."
    }), 429

@app.route("/meme")
@limiter.limit("20 per minute")  
def home():
    try:
        return jsonify(RedditMemes(limit=1))
    except Exception as e:
        return jsonify({
            "error": "Internal Server Error",
            "message": str(e)
        }), 500

@app.route('/gimme')
@limiter.limit('20 per minute')
def gimme():
    try:
       
        limit = int(request.args.get("limit", 1)) 
        sub_reddit = request.args.get("sub_reddit")

        
        memes = RedditMemes(limit=limit, SUB_reddit=sub_reddit)
        return jsonify(memes)
    
        return jsonify({
            "error": "Invalid Input",
            "message": "The 'limit' parameter must be an integer."
        }), 400
    except Exception as e:
        return jsonify({
            "error": "Internal Server Error",
            "message": str(e)
        }), 500


    

if __name__ == "__main__":
    app.run(port=8080)
