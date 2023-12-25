import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import hlink
from parser import parser_news


token = "" # your token
user_id = # your user id

bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

async def news_every_hour():
    while True:
        new_news_dict = parser_news()
        if len(new_news_dict) >= 1:
            for k, v in sorted(new_news_dict.items()):
                news = f"{hlink(v['article_title'], v['article_url'])}"
                await bot.send_message(user_id, news, disable_notification=True)
        else:
            pass
            # you can use this line if you want message that there are no posts
            # await bot.send_message(user_id, "No new posts...", disable_notification=True)

        await asyncio.sleep(3600)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(news_every_hour())
    executor.start_polling(dp)
