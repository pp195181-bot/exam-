import tweepy
import pandas as pd

bearer_token="AAAAAAAAAAAAAAAAAAAAAJzw%2FAEAAAAAQNLuqrQPKVfldg%2BMQp9OGoPITqg%3D9Vxhyk5HMNGzZFWXnZapNnGoLjORjQFN8FG5W1KBfBXUrDKoL7"
client = tweepy.Client(
    bearer_token=bearer_token,
    wait_on_rate_limit=True
)


query = "digital marketing -is:retweet lang:en"

data = []

try:
    response = client.search_recent_tweets(
        query=query,
        max_results=20,
        tweet_fields=["created_at", "public_metrics", "author_id"]
    )

    if response.data:
        for tweet in response.data:
            data.append({
                "Tweet": tweet.text,
                "Date": tweet.created_at,
                "Author ID": tweet.author_id,
                "Likes": tweet.public_metrics["like_count"],
                "Retweets": tweet.public_metrics["retweet_count"],
                "Replies": tweet.public_metrics["reply_count"]
            })

    elif response.errors:
        print("Twitter API returned errors:")
        for error in response.errors:
            print(error)
    else:
        print("No tweets found for the current query.")

except Exception as e:
    print("Twitter API request failed.")
    print(f"Reason: {e}")
    print("Check your internet connection, bearer token, and Twitter API access.")

df = pd.DataFrame(data)

print(df)

df.to_csv("twitter_data.csv", index=False)

print("\nData collected successfully.")