count=0
arr=["dsndsnmdsn","dsnmdmnnmds","'ssnsdsdsbd"]
import time
while True:
    time.sleep(5)
    count =count+1
    print(count)
    if(count==6):
        arr.clear()
        count=0
    else:
        arr.append("dnmdnmdsnmds")
        print(arr)
