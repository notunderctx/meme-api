import random
import praw
import settings
import json

reddit = praw.Reddit(
    client_id=settings.ClIENT_ID,
    client_secret=settings.ClIENT_SECRET,
    user_agent=settings.USER_AGENT,
)

def RedditMemes( limit=1,SUB_reddit:str=None):
    SUB_REDDITS = [SUB_reddit] if SUB_reddit else ['dankmemes', 'memes', 'funny', 'adhdmeme']
    random_subreddit = random.choice( SUB_REDDITS)

    try:
        subreddit = reddit.subreddit(random_subreddit)
    except Exception as e:
        print(f"Error accessing subreddit r/{random_subreddit}: {e}")
        return

    posts = []
    for submission in subreddit.hot(limit=limit): 
        try:
            if submission.is_video:
                continue

            title = submission.title if submission.title else "No title available"
            author = submission.author.name if submission.author else "Unknown author"
        
            image_url = submission.url_overridden_by_dest or submission.url
            if not image_url:
                image_url = "No image available."

            nsfw = True if submission.over_18 else False
            spoiler = True if submission.spoiler else False
            ups = submission.ups

            post = {
                "sub_reddit": f"{submission.subreddit}",
                "title": title,
                "url": image_url,
                "author": author,
                "nsfw": nsfw,
                "spoiler": spoiler,
                "upvotes": ups,
            }

            posts.append(post)

            

        except AttributeError as e:
            print(f"Error processing submission: {e}")
            continue
        except Exception as e:
            print(f"Unexpected error: {e}")
            continue
    print(posts)
    return posts



