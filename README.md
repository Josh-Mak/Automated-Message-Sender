# Automated-Message-Sender
A simple script that sends messages to your phone at pseudo-random times using Pushbullet.


**Intro:** This project is a very simple script I made to test out some automation tasks. As long as the program is running, every morning at 8:00 am it sends a motivational quote pulled from an email, and then at 3 random times a day, it sends a custome message.

**Important Notes:** The API key for pushbullet, and email information has been removed. To get it working for yourself you will have to set those up.

**Technical Overview:**
  1. Email is connected to using imaplib. It then grabs the body and formats it with the email module.
  2. The custom messages are stored in a list. Three times a day (morning, afternoon, and night) at random times, a random one of these messages is sent. All randomness is hnadled by the random module.
  3. Pushbullet app and API are used to send the messages to the Pushbullet app. These are scheduled using the schedule module.
