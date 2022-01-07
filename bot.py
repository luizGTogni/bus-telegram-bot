import os
import logging
from Command import Command

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


from dotenv import load_dotenv
load_dotenv('.env')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def main() -> None:
    token = os.environ["TOKEN"]

    updater = Updater(token=token)

    dispatcher = updater.dispatcher

    cmd = Command()

    dispatcher.add_handler(CommandHandler("start", cmd.start))
    dispatcher.add_handler(CommandHandler("help", cmd.help_command))
    dispatcher.add_handler(CommandHandler(
        "bus_number", cmd.get_bus_schedules_number))

    dispatcher.add_handler(MessageHandler(
        Filters.text & ~Filters.command, cmd.echo))

    updater.start_polling(poll_interval=3.0)

    updater.idle()


if __name__ == '__main__':
    main()
