import os

from aiogram import Bot, Dispatcher, executor, types

from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

bot = Bot(TELEGRAM_TOKEN)
dispatcher = Dispatcher(bot)


@dispatcher.message_handler()
async def send_dice(message: types.Message):
    user = message.from_user.username
    user_id = message.from_user.id
    await bot.send_message(user_id, f'Привет, {user}')
    dice = await bot.send_dice(user_id)
    dice_value = dice['dice']['value']
    await bot.send_message(user_id,f'Выпало {dice_value}')
if __name__ == '__main__':
    executor.start_polling(dispatcher)
