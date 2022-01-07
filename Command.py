# coding: utf8

from telegram import Update, ForceReply
from telegram.ext import CallbackContext
from utils.BotBusSearch import BotBusSearch
from utils.Viewer import Viewer


class Command():
    def __init__(self) -> None:
        return None

    def start(self, update: Update, context: CallbackContext) -> None:
        user = update.effective_user
        update.message.reply_markdown_v2(
            fr'Hi {user.mention_markdown_v2()}\!',
            reply_markup=ForceReply(selective=True),
        )

        return None

    def help_command(self, update: Update, context: CallbackContext) -> None:
        update.message.reply_text('Help!')

        return None

    def echo(self, update: Update, context: CallbackContext) -> None:
        update.message.reply_text(update.message.text)

        return None

    def get_bus_schedules_number(self, update: Update, context: CallbackContext) -> None:
        username = update.effective_user.username
        bus_number = context.args[0]

        botSearch = BotBusSearch()
        viewer = Viewer()

        id_bus_line, name_bus_line, number_bus_line = botSearch.search_bus_line(
            bus_number)

        schedules = botSearch.search_schedules(
            id_bus_line, 1)

        name_paths = botSearch.search_paths(
            id_bus_line, 1)

        filename = 'schedule_{}_{}'.format(number_bus_line, username)

        viewer.create_pdf(schedules, name_paths,
                          path='tmp', filename=filename)

        update.message.reply_document(document=open(
            'tmp/{}.pdf'.format(filename), 'rb'), filename='horarios_do_onibus.pdf')

        viewer.delete_file(path='tmp', filename=filename, extension='pdf')
