import time
import threading
import random
import string
import urllib.request
import json


# Function to generate a random username like (ASD213)
def generate_random_username():
  username = ''.join(
      random.choices(string.ascii_uppercase + string.digits, k=6))
  return f"({username})"


# Print a welcome message
print("Discord Webhook Spammer")

# Input message and webhook URL
webhook = input("Enter the Discord Webhook URL: ")
msg = input("Enter the message to send: ")
th = int(input('Number of threads (recommended: 200): '))
sleep = int(input("Sleep time between requests (recommended: 2): "))


# Function to send messages to the Discord webhook
def spam():
  while True:
    try:
      print("Sending ...:")
      username = generate_random_username()
      data = urllib.request.urlopen(
          webhook,
          json.dumps({
              'content': msg,
              'username': username,
          }).encode())
      if data.getcode() == 204:
        print(f"SENT, CONTINUE;")
    except:
      print("ERROR;")
    time.sleep(sleep)


# Create and start threads for spamming
threads = []
for x in range(th):
  t = threading.Thread(target=spam)
  t.start()
  threads.append(t)

# Wait for all threads to finish
for t in threads:
  t.join()
