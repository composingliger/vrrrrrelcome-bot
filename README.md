# vrrrrrelcome-bot

![Vrrrrr'ELCOME bot!](https://user-images.githubusercontent.com/67404553/147509116-b4fec164-aa60-4b79-bf12-a14458f45ba1.png)

Telegram Bot that sends the [classic Furcadia "welcome"](https://youtu.be/TrR9YKOeZA0) when a new user joins a chat.

## How to use

Simply invite [`@vrrrrrelcome_bot`](https://t.me/vrrrrrelcome_bot) to your Telegram channel and it will automatically start welcoming new users.

![Vrrrrr'ELCOME! 😸](https://user-images.githubusercontent.com/67404553/145514823-37048f6e-c71e-4bfe-b919-a591fbb0b5ea.png)

## How to run your own bot

### Requirements
- [Python 3.x](https://www.python.org/)
- [python-telegram-bot](https://python-telegram-bot.org/)

### Steps

1. Install the [latest version of Python](https://www.python.org/downloads/)
2. Use the command shell to install [`python-telegram-bot`](https://pypi.org/project/python-telegram-bot/) from PyPI:
   ```
   pip install python-telegram-bot
   ```
3. [Create a new bot account](https://core.telegram.org/bots#creating-a-new-bot) using [BotFather](https://t.me/botfather)
   - Use the `/newbot` command to create a new bot
   - Be sure to note the **token** (keep it safe and store it securely!)
4. Start the bot using the newly minted token:
   ```
   set TELEGRAM_TOKEN=...
   python vrrrrrelcome-bot
   ```
