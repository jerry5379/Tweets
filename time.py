
# import datetime as dt

# # Save the current time to a variable ('t')
# t = dt.datetime.now()

# while True:
#     delta = dt.datetime.now()-t
#     print(delta.minute)
#     if delta.seconds >= 60:
#         print("1 Min")
#         # Update 't' variable to new time
#         t = dt.datetime.now()


from timeit import default_timer as timer

start =timer()
freq=10
last_time =0.0
while True:
    ctime=timer()
    print(ctime)
    if ctime-last_time >= freq:
        print("value")
        last_time=ctime
        break



# # import the time module 
# import time 


# def time_convert(sec):
#     mins = sec // 60
#     sec = sec % 60
#     hours = mins // 60
#     mins = mins % 60
#     print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))
# input("Press Enter to start")
# start_time = time.time()
# input("Press Enter to stop")
# end_time = time.time()
# time_lapsed = end_time - start_time
# time_convert(time_lapsed)

# # with  open('stopwords.txt','r') as st:
# # f_content = "Based on the fact you are facing performance issues. I would suggest using the subprocess library (for Python2, or for Python3) to call the sed linux command."


# # f_content
# #     processed = re.split('[^a-zA-Z]', f_content)
# #     processed = [x.lower() for x in processed]
# #     processed = [PT(x) for x in processed]
# #     #print(processed)

# #     st_content = st.read()
# #     st_list = set(st_content.split())

# #     clean_text = [x for x in processed if x not in st_list]
# #     print (clean_text)



# # s=" Post a tweet from Python api.update_status 'm tweeting from #Python in my ... Now you are ready to search Twitter for recent tweets!"
# # for w in stop_words:
# #     pattern = r'\b'+w+r'\b'
# #     s = re.sub(pattern, "", s)
# #     print(s)
# # print(stop_words)
  
# # define the countdown func. 
# # def countdown(): 
# #     t=60
# #     while t: 
# #         mins, secs = divmod(t, 60) 
# #         timer = '{:02d}:{:02d}'.format(mins, secs) 
# #         print(timer, end="\r") 
# #         time.sleep(1) 
# #         t -= 1
      
# #     print('Fire in the hole!!') 
  
  

# # # input time in seconds 
# # # t = input("Enter the time in seconds: ") 
  
# # # function call 
# # countdown() 
