import tweepy
from secret import consumer_key, consumer_secret, access_token, access_token_secret

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
    # client = tweepy.Client(bearer_token,consumer_key, consumer_secret, access_token, access_token_secret)


    # Upload image
    # media = ['test.jpg']
    media = api.media_upload("test.jpg")

    # Post tweet with image
    tweet = "Test Toot from Bubo-2T.\nThese are not the droids you're looking for. Move along."
    post_result = api.update_status(status=tweet, media_ids=[media.media_id])
    # client.text = tweet
    # result = client.create_tweet(text = tweet, media_ids=media)
    print(f'result is: {result}')
if __name__ == "__main__":
    main()