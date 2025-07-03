import json, os
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import WebAppInfo, ReplyKeyboardMarkup, KeyboardButton

TOKEN = '8166874935:AAE78IcasXx92bgw6S3HH4eAPZJ_CsFYWNI'
ADMIN_ID = 5050882022
bot = Bot(TOKEN, parse_mode="HTML")
dp  = Dispatcher()

WEBAPP_URL = "https://rodnoydsgn.github.io/zakumarik/"  

@dp.message(commands=["start"])
async def start(msg: types.Message):
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton("🛍 Открыть магазин", web_app=WebAppInfo(url=WEBAPP_URL)))
    await msg.answer("Добро пожаловать в ZAKUMAR! Жми кнопку ниже 👇", reply_markup=kb)

# приём данных из WebApp
@dp.message(F.web_app_data)
async def order(msg: types.Message):
    data = json.loads(msg.web_app_data.data)
    text = (
        "<b>🆕 Новый заказ</b>\n"
        f"Имя: {data['customer']['name']}\n"
        f"Телефон: {data['customer']['phone']}\n"
        f"Сумма: {data['total']} ₽\n"
        f"Скидка: {data['discountApplied']} ₽\n\n"
        "<b>Товары:</b>"
    )
    for item in data["items"]:
        text += f"\n• {item['name']} × {item['qty']}  —  {item['price']} ₽"
    await bot.send_message(chat_id=ADMIN_ID, text=text)

if __name__ == "__main__":
    import asyncio
    asyncio.run(dp.start_polling(bot))
