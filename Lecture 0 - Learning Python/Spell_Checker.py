# -*- coding: utf-8 -*-
import urllib
file = "movie_quotes.txt"
#wdyl.com/profanity?q=shoot   #gives {response: true} or {response:false}

def read_text():
    quotes = open(file)
    contents_of_file = quotes.read()
    print contents_of_file
    quotes.close()
    check_profanity(contents_of_file)

def read_line_by_line():
    lines = [line.rstrip('\n') for line in open(file)]
    for element in lines:
        print element

def check_profanity(text_to_check):
    connection = urllib.urlopen("wdyl.com/profanity?q=" + text_to_check) 
    output = connection.read()
    print output
    connection.close()
    if "true" in output:
        print("Profanity Alert!!")
    elif "false" in output:
        print("This document has no curse words.")
    else:
        print "There was a problem in scanning the document."
    
read_text()