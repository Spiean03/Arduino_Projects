# -*- coding: utf-8 -*-

from twilio.rest import TwilioRestClient

#account sid and auth token from twilio.com/user/account
account_sid = "put your SID here"
auth_token = "put your token here"
client = TwilioRestClient(account_sid,auth_token)


def send_message(phone_nr,text): # both phone_nr and body need to be a string
    message = client.sms.messages.create(
    body = text,
    to = phone_nr, #replace with your phone number
    _from = "+14123456789") #replace "" with your Twilio number
    print message.sid
    

send_message("+15141234567", "Hi, this message has been sent from a computer")
