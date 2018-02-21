# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 15:08:45 2017

@author: Administrator
"""

import webbrowser
import time
new = 2 # open in a new tab, if possible

total_breaks = 3
repeat = 0

print "This program started on "+time.ctime()
while repeat < total_breaks:
    # open a public URL, in this case, a youtube video
    url = "https://www.youtube.com/watch?v=2Z4m4lnjxkY"
    webbrowser.open(url, new=new)

    repeat += 1

    time.sleep(7200)
