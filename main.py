import logging
import os

import telegram
from telegram import Update
from telegram.ext import Updater, CallbackContext, MessageHandler, Filters, BaseFilter, CommandHandler

TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
WELCOME = 'welcome.ogg'
WELCOME_CAPTION = "Vrrrrr'ELcome! 😸"

updater = Updater(TELEGRAM_TOKEN)
updater.bot.set_my_commands([('start', 'Start interacting with this bot')], scope=telegram.BotCommandScopeAllPrivateChats())


def command_handler(command, **kwargs):
    """Decorator for registering a `CommandHandler`."""
    def _register(func):
        updater.dispatcher.add_handler(CommandHandler(command, func, **kwargs))
    return _register


def message_handler(filter: BaseFilter, **kwargs):
    """Decorator for registering a `MessageHandler`."""
    def _register(func):
        updater.dispatcher.add_handler(MessageHandler(filter, func, **kwargs))
    return _register


@command_handler('start', filters=Filters.chat_type.private)
def _start(update: Update, _context: CallbackContext):
    first_name = update.message.from_user.first_name
    update.message.reply_text(f'Hi {first_name}! To use me, just invite me to your group!')
    update.message.reply_text('I\'ll send this reply to all new users who join the group:')
    with open(WELCOME, 'rb') as f:
        update.message.reply_voice(f, quote=True, caption=WELCOME_CAPTION)


@message_handler(Filters.status_update.new_chat_members)
def _on_message(update: Update, _context: CallbackContext):
    if update.message and update.message.new_chat_members:
        # Send "Vrrrrr'elcome!" when a new user joins the chat
        logging.info(
            'Sent WELCOME to %s in %s %r (%d)',
            ', '.join(f'{u.username!r} ({u.id})' for u in update.message.new_chat_members),
            update.message.chat.type,
            update.message.chat.title,
            update.message.chat_id)

    with open(WELCOME, 'rb') as f:
        update.message.reply_voice(f, quote=True, caption=WELCOME_CAPTION)


def main():
    logging.basicConfig(level=logging.INFO)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()