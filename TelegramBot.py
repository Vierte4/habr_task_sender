import asyncio
import random

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery, BotCommand
from config import admin_id, key_words, initial_url
from habr_tasks_checker import start_webdriver, checker
from initiator import dp, bot


async def send_to_admin(dp):
    # Сообщает админу, что бот запущен
    await bot.send_message(chat_id=admin_id, text='Бот запущен, мой капитан')


@dp.message_handler(text='Start', user_id=admin_id)
async def start_bot(call: CallbackQuery):
    driver = start_webdriver(initial_url)

    # Запускает бесконечный цикл отправления лидов по всем активным клиентам
    last_tasks = [0] * 25
    while True:
        i = 0
        while i < 25:
            tasks = []
            tasks = checker(last_tasks, key_words, driver)  # Возвращает список и ссылки всех найденных новых заголовков
            for task in tasks:
                last_tasks[i] = task
                i += 1
                await bot.send_message(chat_id=admin_id, text=task)
            await asyncio.sleep(random.randint(100, 200))
