# Time module in python are very essentials module

import time

print(time.ctime(0)) #this will give me my epoch time, yeah i have already talked about epoch time in previous session, but generally epoch means that particular time from where couting is started(for python its jan 1, 1970)
# You may be wondering why there is argument 0? well it is nothing but hwo much seconds later do you want epoch to print times.

print(time.ctime(100000)) #i am saying here, give me the time after 10000..... seconds 
