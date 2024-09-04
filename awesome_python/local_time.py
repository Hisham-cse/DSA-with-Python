import time
timestamp  = time.strftime('%H:%M:%S ')
print(timestamp)
hour=time.strftime('%H')
hour=int(hour)
hour=1
if 5<=hour<=12:
    print("Good Morning")
elif 13<=hour<16:
    print("Good afternoon")
elif 16<=hour<19:
    print("Good Evening")
else:
    print("Good Night")
print(hour)
print(type(hour))
