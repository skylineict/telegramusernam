"""
 import the sync module from Telethon library.
"""
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import csv
"""
instantiate your client object using the credentials you got before.
"""

api_id = 8023816
api_hash = '4b001af86e084779d8d3dbeaf240c51c'
phone = '+2348101524926'
client = TelegramClient(phone, api_id, api_hash)


"""
 connecting to telegram and checking if you are already authorized. Otherwise send
 an OTP code request and ask user to enter the code they received on their telegram account.
"""

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter Code Here: '))


"""
offset_date and  offset_peer are used for filtering the chats.
We are sending empty values to these parameters so API returns all chats.
 offset_id and limit are used for pagination. Here we are getting last 300 chats of the user."""

chats = []
last_date = None
chuck_size = 300
groups = []


result = client(GetDialogsRequest(
    offset_date=last_date,  # offset_date and  offset_peer are used for filtering the chats
    offset_id=0,
    offset_peer=InputPeerEmpty(),
    limit=chuck_size,
    hash=0
))

"""
Listing All Telegram Groups
"""

chats.extend(result.chats)

for chat in chats:
    try:
        if chat.megagroup == True:
            groups.append(chat)
    except:
        continue

""""
Ask User to Select a Group to Scrape Members

After listing the groups, prompt the user to input a number and select the
 group they want. When this code is executed it loops through every group that you
 stored in previous step and print it’s name starting with a number.
  This number is the index of that is your group list.
"""
print('Choose a group to scrape members from: ')
icon = 0

for g in groups:

    print(str(icon) + "- " + g.title)

    icon += 1


"""
Ask user to enter a number associated with a group.
 Then use this number as index to get the target group.
"""

g_index = input("Enter a Number: ")
target_group = groups[int(g_index)]


"""
Get All Telegram Group Members

Set the aggressive parameter to True
otherwise you will not get more than 10k members.
 When aggressive is set to true, Telethon will perform an a-z search in the group’s

"""
print("geting all memebers.....")
"""91
Create an empty list of users and get members using the
 get_participants  function and populate the list.
"""
all_paticipant = []
all_paticipant = client.get_participants(target_group, aggressive=True)

with open("member.csv", "w", encoding='UTF-8') as f:
    writer = csv.writer(f, delimiter=",", lineterminator="\n")
    writer.writerow(['username', ])
    for user in all_paticipant:
        if user.username:
            username = user.username
            writer.writerow([username.strip()
                             ])
print('Members scraped successfully.')


# print('Saving In file...
# with open("members.csv", "w", encoding='UTF-8') as f:
#     writer = csv.writer(f, delimiter=",", lineterminator="\n")
#     writer.writerow(['username'])
#     for user in all_paticipant:
#         if user.username:
#             username = user.username

#         writer.writerow([username,
#                          ])
# print('Members scraped successfully.')
