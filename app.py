from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

TOKEN="8575857385:AAFnEMYvSuTAbp6ikK8wJ3wnjK5e_m3BYyo"


bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)



menustart = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="KIRISH",
                                 web_app=WebAppInfo(url="https://register-sayt-bfa056d0e2fe.herokuapp.com/"),
                                 )
         ]
    ]
)


@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer(message.text,reply_markup=menustart)


if __name__ == '__main__':
    executor.start_polling(dp)
