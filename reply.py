# message="Hi 🙂👍"
# client_id=client.get_me().data.id
# while True:
#     response=client.get_users_mentions(client_id)
#     if response.data!= None:
#         for tweet in response.data:
#             try:
#                 print(tweet.text)
#                 client.create_tweet(in_reply_to_tweet_id=tweet.id,text=message)
#             except:
#                 pass
#     time.sleep(1)