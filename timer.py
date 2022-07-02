import time 
seconds=int(input('enter the number of seconds you want to count down from : '))
for i in range(seconds):
    print(str(seconds-i)+'seconds remain ')
    time.sleep(1)
print('ohhh..hoo .. times up !!')