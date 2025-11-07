#!/usr/bin/env python3
"""
Скрипт для запуска Telegram-ботов из БД.
Запускает всех активных ботов, зарегистрированных в системе.
"""

import os
import django
import logging
import asyncio
from telegram.ext import Application
from asgiref.sync import sync_to_async
from asyncio.exceptions import CancelledError

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bot_builder.settings')
django.setup()

from api.models import Bot
from api.telegram_bot import start_bot

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@sync_to_async
def get_active_bots():
    return list(Bot.objects.filter(is_active=True))


async def main():
    """Основной цикл — запускает всех ботов из БД."""
    # Получаем активных ботов асинхронно
    active_bots = await get_active_bots()

    if not active_bots:
        logger.warning("Нет активных ботов в базе данных.")
        return

    logger.info(f"Найдено {len(active_bots)} активных ботов. Запуск...")

    # Запускаем всех ботов параллельно
    bot_applications = []
    for bot in active_bots:
        app = await start_bot(bot.token)
        if app:
            bot_applications.append(app)

    # Держим цикл активным
    try:
        while True:
            await asyncio.sleep(60)  # Проверка раз в минуту
    except (KeyboardInterrupt, CancelledError):
        logger.info("Остановка ботов по запросу пользователя...")
        for app in bot_applications:
            await app.stop()
        logger.info("Все боты остановлены.")


if __name__ == '__main__':
    asyncio.run(main())