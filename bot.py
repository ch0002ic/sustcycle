from sympy import cancel
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import ApplicationBuilder, CommandHandler, filters, MessageHandler, ConversationHandler, ContextTypes
import time
import os
from dotenv import load_dotenv
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
OPTION, RESPOND = range(2)
async def channels(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    keyboard = [["Tips", "FAQ", "Contact", "Feedback"]]
    await update.message.reply_text(f'Hello, {update.effective_user.first_name}. ' "Choose from the available channels below to assist your business.", reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True))
    return OPTION
async def tips(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    ReplyKeyboardRemove()
    await update.message.reply_text("Here is a list of tips that your business can follow to help perform and promote recycling in Singapore.\n\n1. Explore RecycleBites and learn more about materials that make up items that you and your business wish to dispose of.\n\n2. Dispose of used materials in appropriate recycling bins. If materials cannot be disposed of, reuse them wisely for useful purposes such as artworks and laboratory experiments.\n\n3. Participate in and organise recycling activities supported by the Singapore government and environmental organisations. Such activities are tasks that we assign to you and your business to earn EnvCredits, which can be converted to money in a credit card, and guide you along your recycling journey.")
    keyboard = [["FAQ", "Contact", "Feedback"]]
    time.sleep(2)
    await update.message.reply_text("Any other available channels to choose from?", reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True))
    return OPTION
async def faq(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    ReplyKeyboardRemove()
    await update.message.reply_text("Here are some of the commonly asked questions that our users have raised while using our app.\n\n<b>1. What is Sustcycle? What does it offer?</b>\nSustcycle is a one-stop platform to assist your business in performing and promoting recycling in Singapore. Powered by AI and deep learning, Sustcycle contains a wide variety of features that help your business develop and enhance abilities in recycling efforts. Moreover, our team works closely with the Singapore government, authorities and environmental stakeholders in ensuring that your business is able to minimise time and resource wastage in the process of meeting recycling goals.\n\n<b>2. Is my business required to follow the tips?</b>\nWhile not mandatory by law, it is strongly encouraged that your business follow the tips as they can not only reward your business with EnvCredits, which can be converted to money for the purchase and use of eco-friendly goods and services, but also provide your business with a cleaner and safer environment, and contribute positively to the achievement of Singapore's environmental sustainability goals through recycling.\n\n<b>3. My business is not sure of what to do to perform and promote recycling. What can I do?</b>\nFeel free to explore RecycleBites, which provide useful information about materials and useful guidelines on how to recycle them, as well as how recycling on different scales can be enhanced. Alternatively, feel free to contact us by pressing the Contact button in the chatbox. Our team can be reached 24/7 by phone, WhatsApp, Telegram and email, which are easily accessible for your convenience. Moreover, there are other features that you can explore with great convenience to help your business make sound decisions that will ensure environmental protection and sustainability for future generations.\n\n<b>4. Will there be more opportunities for my business to perform and promote recycling in the future?</b>\nSustcycle is consistently being reviewed and upgraded in tandem with technological and environmental developments to meet the ever-changing demands of people and businesses in Singapore and abroad, alongside legal requirements. This would provide greater opportunities for your business to play its part in protecting and sustaining the environment for future generations through recycling.", parse_mode='HTML')
    keyboard = [["Tips", "Contact", "Feedback"]]
    time.sleep(2)
    await update.message.reply_text("Any other available channels to choose from?", reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True))
    return OPTION
async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    ReplyKeyboardRemove()
    await update.message.reply_text("Feel free to contact us via the following platforms.\n\nPhone/WhatsApp - 9316 5429\nTelegram - @envisagesg\nEmail - envisagesg@gmail.com")
    keyboard = [["Tips", "FAQ", "Feedback"]]
    time.sleep(2)
    await update.message.reply_text("Any other available channels to choose from?", reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True))
    return OPTION
async def feedback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    ReplyKeyboardRemove()
    await update.message.reply_text("What are your thoughts and feelings about our app? Is there anything we can improve on?\n\nFeel free to type them below and then send your response.")
    return RESPOND
async def respond(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Thank you so much! We really appreciate your feedback, and will do whatever is possible to improve and even upgrade our app with new features that will hopefully benefit your business and Singapore in their recycling efforts in the long term.", reply_markup=ReplyKeyboardRemove())
    keyboard = [["Tips", "FAQ", "Contact"]]
    time.sleep(2)
    await update.message.reply_text("Any other available channels to choose from?", reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True))
    return OPTION
async def browse(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Thank you for using our chatbot. We hope you have a nice day ahead!", reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END
def main() -> None:
    bot = ApplicationBuilder().token(BOT_TOKEN).build()
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("channels", channels)],
        states={
            OPTION: [MessageHandler(filters.Regex("^Tips$"), tips), MessageHandler(filters.Regex("^FAQ$"), faq), MessageHandler(filters.Regex("^Contact$"), contact), MessageHandler(filters.Regex("^Feedback$"), feedback)],
            RESPOND: [MessageHandler(filters.TEXT & ~filters.COMMAND, respond)],
        },
        fallbacks=[CommandHandler("browse", browse)],
    )
    bot.add_handler(conv_handler)
    bot.run_polling()
if __name__ == "__main__":
    main()