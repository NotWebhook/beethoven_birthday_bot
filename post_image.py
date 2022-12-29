import tweepy


consumer_key = "cB1jhbE9wHOys40i0LGSuYbmY"
consumer_secret_key = "Bq5EbsMs74lxyL5EFg0q9cjty5pajgZ7LcAJlJiUARDL34UYTU"

access_token = "1435374080593731584-KFDvrUP3YEwH0t1panrAkEaRiVGeay"
access_token_secret = "UDUihTAWU1ivC8GpcTleBTwTfoquJZxJBTrijWSF4HeIU"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

def profile_image(filename):
    api.update_profile_image(filename)

def update_profile_info(name, url, location, description):
    api.update_profile(name, url, location, description)

def post_tweet(text):
    api.update_status(text)

def upload_media(text, filename):
    media = api.media_upload(filename)
    api.update_status(text, media_ids = [media.media_id_string])

upload_media("Only 354 days until Beethoven's birthday!", "354.png") # change the text to the supposed day and the pic to the suppoosed the day 
print("Image posted!")