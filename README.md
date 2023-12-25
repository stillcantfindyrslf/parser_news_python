<h1><b>Python News Parser</b></h1>

This is a Python-based news parser. It can send new articles to Telegram chats and channels every 30 minutes if site have new news. However, you can also remove the Telegram related parts and do what you need. For example, you can make it collect news in some file. Or something like that.

<h3>Installing Libraries</h3>

For stable working you must install these libraries:

for parser.py file:
```
$ pip install requests
$ pip install bs4
$ pip install lxml
```

and tg_bot.py file:
```
$ pip install asyncio
$ pip install --no-deps -v "aiogram==2.23.1"
```

<h3>Telegram Bot token</h3>

You also need to put your bot's token in `token = ""`, and your user id that you can find in [userinfobot](https://t.me/userinfobot) and put id in `user_id = `, so script can use your telegram bot to send messages.

<h3>Work example</h3>
In the picture below you can see examples of posts by this parser:

![exmpl](images/work_example.png)
