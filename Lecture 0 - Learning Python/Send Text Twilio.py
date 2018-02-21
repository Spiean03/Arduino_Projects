# -*- coding: utf-8 -*-

from twilio.rest import TwilioRestClient

#account sid and auth token from twilio.com/user/account
account_sid = "ACbaab71006de263f97f09d40b40e8b47a" #put your SID here
auth_token = "f9c1eed94c936f347c3805c161c1c9ee" #put your token here
client = TwilioRestClient(account_sid,auth_token)


def send_message(phone_nr,text): # both phone_nr and body need to be a string
    message = client.sms.messages.create(
    body = text,
    to = phone_nr, #replace with your phone number
    _from = "+14388004585") #replace "" with your Twilio number
    print message.sid
    

send_message("+15145889479", "Hi Siobhan, this message has been generated from a computer")