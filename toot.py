import tweepy
from secrets import consumer_key, consumer_secret, access_token, access_token_secret

def main():
    twitter_auth_keys = {
        "consumer_key"        : consumer_key,
        "consumer_secret"     : consumer_secret,
        "access_token"        : access_token,
        "access_token_secret" : access_token_secret
    }

    auth = tweepy.OAuthHandler(
            twitter_auth_keys['consumer_key'],
            twitter_auth_keys['consumer_secret']
            )
    auth.set_access_token(
            twitter_auth_keys['access_token'],
            twitter_auth_keys['access_token_secret']
            )
    api = tweepy.API(auth)


    # Upload image
    media = api.media_upload("william_gibson.jpg")

    # Post tweet with image
    tweet = "Great scifi author or greatest scifi author? #williamgibson"
    post_result = api.update_status(status=tweet, media_ids=[media.media_id])

if __name__ == "__main__":
    main()