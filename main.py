import asyncio

from src.excel_reader import get_today_schedule
from src.formatter import format_message
from src.telegram_sender import send_message


async def main():
    schedule = get_today_schedule()
    message = format_message(schedule)
    await send_message(message)


asyncio.run(main())
