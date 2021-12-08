import logging
import os

from telegram import Update
from telegram.ext import Updater, CallbackContext, MessageHandler, Filters, BaseFilter

TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
WELCOME = open('welcome.m4a', 'rb')
WELCOME_CAPTION = "Vrrrrr'ELcome! 😸"

updater = Updater(TELEGRAM_TOKEN)


def message_handler(filter: BaseFilter, **kwargs):
    """Decorator for registering a `MessageHandler`."""
    def _register(func):
        updater.dispatcher.add_handler(MessageHandler(filter, func, **kwargs))
    return _register


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
        update.message.reply_audio(WELCOME, quote=True, caption=WELCOME_CAPTION)


def main():
    logging.basicConfig(level=logging.INFO)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()