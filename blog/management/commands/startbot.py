import telebot
from blog.models import Post


token = "5341878378:AAHxEcneN2k6OKIZkHR0eR5uiwKqyKErb0s"
bot = telebot.TeleBot(token, parse_mode="html")


@bot.message_handler(commands=["start"])
def welcome(message):
    bot.send_message(chat_id=message.from_user.id, text="Hello")


@bot.message_handler(commands=["new"])
def get_new_posts(message):
    latest_post = Post.objects.all().order_by("-created_time")[0]
    bot.send_message(message.from_user.id, f"latest post is {latest_post.title}")


bot.polling()
