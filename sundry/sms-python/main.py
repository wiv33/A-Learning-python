# Download the helper library from https://www.twilio.com/docs/python/install
import random

from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC5cc9692a097bf823e7944c12c2c739f8'
auth_token = '47929A3303CD22AB358169A3284D2F3C'
client = Client(account_sid, auth_token)

r = range(1, 46)
sample = str(random.sample(r, 6))
sample = sample.replace("[", "").replace("]", "")
bonus = random.choice(r)

''' This is for you. '''
body = "{} + {} ".format(sample, bonus)
message = client.messages \
                .create(
                     body=body,
                     from_='+18509403211',
                     to='+821025004313'
                 )
print(message)

print(message.sid)

# Change last 4, 반전