from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

# 启用日志
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# 定义关键词和相应信息的字典
keyword_responses = {
    "关键词1": "关键词1的回复信息。",
    "关键词2": "https://pan.baidu.com/s/1uIIHLr0cwezRbTlC02K6Xg?pwd=8888",
    # 可以继续添加更多的关键词和回复信息
}

# 处理/start命令
def start(update, context):
    update.message.reply_text('你好！我是关键词机器人。请发送关键词，我会回复相应的信息。')

# 处理用户发送的消息
def reply_to_keyword(update, context):
    user_input = update.message.text.lower()  # 将用户输入的文本转换为小写
    if user_input in keyword_responses:
        # 如果消息中包含关键词，回复相应的信息
        response = keyword_responses[user_input]
        if response.startswith("http"):
            update.message.reply_text(response)
        else:
            update.message.reply_text(response)
    else:
        # 如果消息中不包含关键词，回复固定的信息
        update.message.reply_text('抱歉，没有找到相关信息。')
        send_message_to_admin(context.bot, update.message)

# 发送消息给管理员
def send_message_to_admin(bot, message):
    admin_id = '1960790445'  # 将此处替换为你的 Telegram 管理员 ID
    bot.send_message(chat_id=admin_id, text=f'用户消息：{message}')

# 处理错误
def error(update, context):
    logger.error(f'更新 {update} 由错误 {context.error}')

def main():
    # 创建 Updater 并获取 Telegram bot token
    updater = Updater("6759690211:AAGlJUx3kqbrwP2eb_WurcYBbdqi0R9e9b0", use_context=True)

    # 获取 Dispatcher 来注册处理程序
    dp = updater.dispatcher

    # 注册处理/start命令
    dp.add_handler(CommandHandler("start", start))

    # 注册处理用户发送的消息
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, reply_to_keyword))

    # 注册处理错误
    dp.add_error_handler(error)

    # 开始运行 bot
    updater.start_polling()

    # 持续运行 bot 直到按下 Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
