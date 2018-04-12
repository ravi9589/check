import webbrowser
import time
msg="hello world"
no_breaks=3
break_count=0
while (break_count<no_breaks):
    print(msg)
    break_count+=1
    print(no_breaks)
    time.sleep(10)
    webbrowser.open_new("https://www.youtube.com/watch?v=OJCkO1w9JoY")
#for a in range(3):

