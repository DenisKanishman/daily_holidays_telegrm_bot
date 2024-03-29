from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from get_holidays import get_holidays
from check_keyboard import check_keyboards

TOKEN: Final = '6882962671:AAF9c8C0fB27EMxL3kD77pXrdmv1GqJmsjE'
BOT_USERNAME: Final = '@daily_holiday_bot'


async def start_command(update: Update, contex: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Привет Изя! \nКак дела? ')


async def handle_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text.lower()

    if 'праздники' in user_message:
        await update.message.reply_text('пару секунд пожалуйста...')
        result_text = get_holidays()
        await update.message.reply_text(result_text)

    if 'клавиатура' in user_message:
        await update.message.reply_text('пару секунд пожалуйста...')
        keyboards = check_keyboards()
        for keyboard in keyboards:
            await update.message.reply_text(keyboard)


if __name__ == '__main__':
    print('starting...')
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(MessageHandler(filters.TEXT, handle_response))

    print('pulling...')
    app.run_polling(poll_interval=3)
