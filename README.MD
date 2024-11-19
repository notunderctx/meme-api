# Meme api

- A json api made with flask to get memes using the reddit api

> Make sure to go to `settings.example.py` and add the fields and rename the file
> run `pip install -r requirements.txt`

Example Response from [http://127.0.0.1:8080/meme](http://127.0.0.1:8080/meme):

```json
[
  {
    "author": "Niarodelle",
    "nsfw": false,
    "spoiler": false,
    "sub_reddit": "adhdmeme",
    "title": "We hear you loud and clear - NEW SUBREDDIT RULE",
    "upvotes": 1421,
    "url": "https://i.redd.it/n3oqvlqmqcbd1.png"
  }
]
```

Example response from [http://127.0.0.1:8080/gimme?limit=2](http://127.0.0.1:8080/gimme?limit=2):

```json

[
  {
    "author": "Alarmed-Ad-436",
    "nsfw": false,
    "spoiler": false,
    "sub_reddit": "memes",
    "title": "That one professor ",
    "upvotes": 10636,
    "url": "[https://i.redd.it/ik0c5lldjt1e1.jpeg](https://i.redd.it/ik0c5lldjt1e1.jpeg)"
  },
  {
    "author": "AimlessFacade",
    "nsfw": false,
    "spoiler": false,
    "sub_reddit": "memes",
    "title": "And I suppose you also hate Sunlight?",
    "upvotes": 5372,
    "url": "[https://i.redd.it/4580nrdgcs1e1.jpeg](https://i.redd.it/4580nrdgcs1e1.jpeg)"
  }
]
```

Example response from [http://127.0.0.1:8080/gimme?sub_reddit=dankmemes](http://127.0.0.1:8080/gimme?sub_reddit=dankmemes):

```json
[
  {
    "author": "AfterDark_thoughts",
    "nsfw": false,
    "spoiler": false,
    "sub_reddit": "dankmemes",
    "title": "Good job google",
    "upvotes": 1877,
    "url": "https://i.redd.it/sm4hggqtvu1e1.gif"
  }
]
```
