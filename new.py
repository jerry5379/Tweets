# def seq(x,y):
#     count=0
#     # [x,y]= [1,2]
#     while (count<9):
#         print(x,end=",")
#         for i in range(x):
#             print(y,end=",")
#         for i in range(x):
#             print(x,end=",")
#             for i in range(y):
#                 print(y,end=",")
        
#         print(x,end=",")
#         for i in range(x):
#             print(y,end=",")
#         for i in range(y):
#             print(x,end=",")
#             for i in range(y):
#                 print(y,end=",")
#         # count = count + 1
    

# x=int(input("Enter x value :"))
# y=int(input("Enter y value :"))

# seq(x,y)
import datetime as dt
from tqdm import tqdm
import time
import tweepy
import urllib3
import re
# from hashids import Hashids
import pyshorteners
from collections import Counter
from pprint import pprint
import operator
# from time import time, sleep
import time
# authorization tokens


api_key = "NZ4TPL7OyglfftcvpRyyFyOge"
api_secret_key = "QOEaS8MUGRxP4iT0qBL5sPzK4MfPC7b1o5oHp1YEGWsrVi7eu6"
access_token = "2798327630-wo7LtpjwfajQwXnZskqHv3XWzQetTbXFrung4ZV"
access_token_secret = "yczzU5gk2tfQ7WaedjJA4j2kS7FpELbtTvt5PAT3H78BN"


authentication = tweepy.OAuthHandler(api_key, api_secret_key)
authentication.set_access_token(access_token, access_token_secret)




api = tweepy.API(authentication,wait_on_rate_limit=True)


# from alive_progress import showtime

# Save the current time to a variable ('t')
# t = dt.datetime.now()

print("Enter the keywords")
search_words = input()
arr=[]
temp=[]


# def twee(tweets):
#     # sleep(60 - time() % 60)
#     # delay=60*1    ###for 15 minutes delay 
#     # close_time=time.time()+delay
#     # while True:
#     count =0
#     for tweet in tweets:
#         if count <= 60:
#             print(tweet.text)
#             arr.append(tweet.text)
#             time.sleep(1)
#             count= count +1
#         else:
#             break
        
        # if time.time()>close_time:
        #     break

            # arr.append(tweet.text)
        



try:
    tweets = tweepy.Cursor(api.search,q=search_words,lang="en").items(10)
    # twee(tweets)
    for tweet in tweets:
        print(tweet.text)
    print("new value is donee")
    # print(arr)
    
   
except KeyboardInterrupt:
    print('Program has been closed.')
