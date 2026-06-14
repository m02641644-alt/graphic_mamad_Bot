import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# فعال کردن لاگ برای مشاهده خطاها
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# گرفتن توکن از Environment Variables (ایمن)
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# تابع ساخت منوی اصلی
def get_main_keyboard():
    keyboard = [
        [InlineKeyboardButton("🛡 پشتیبانی 🗣", callback_data='support')],
        [InlineKeyboardButton("🆔 آیدی بنده 🫦", callback_data='my_id')],
        [InlineKeyboardButton("🎨 گرافیک بنده 🎨", callback_data='my_graphic')],
        [InlineKeyboardButton("💥 ابزار رایگان 💥", callback_data='free_tools')]
    ]
    return InlineKeyboardMarkup(keyboard)

# دستور /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # متن خوش آمدگویی با لینک‌دهی به mamad
    welcome_text = (
        "درود 🙂‍↕️\n"
        "به ربات [mamad](https://t.me/graphic_mamad) خوش آمدید . ♻️\n\n"
        "لطفاً یکی از گزینه‌های زیر رو انتخاب کن:"
    )
    
    # ارسال پیام با منوی شیشه‌ای
    await update.message.reply_text(
        welcome_text,
        parse_mode='Markdown',
        reply_markup=get_main_keyboard()
    )

# تابع مدیریت کلیک روی دکمه‌ها
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()  # برای بستن نوتیفیکیشن لودینگ
    
    data = query.data
    
    if data == 'support':
        text = (
            "دوست عزیز اگر مشکلی داری به آیدی زیر مراجعه کن 👀\n"
            "[@iWas_Mamad](https://t.me/iWas_Mamad)"
        )
        await query.edit_message_text(
            text,
            parse_mode='Markdown',
            reply_markup=get_main_keyboard()
        )
    
    elif data == 'my_id':
        text = (
            "کاری بود آنلاینم ✍\n"
            "[@iWas_Mamad](https://t.me/iWas_Mamad)"
        )
        await query.edit_message_text(
            text,
            parse_mode='Markdown',
            reply_markup=get_main_keyboard()
        )
    
    elif data == 'my_graphic':
        text = (
            "نمونه های جذاب بنده 🫟\n"
            "[@graphic_mamad](https://t.me/graphic_mamad)"
        )
        await query.edit_message_text(
            text,
            parse_mode='Markdown',
            reply_markup=get_main_keyboard()
        )
    
    elif data == 'free_tools':
        text = "فعلا هیچ ابزار رایگان برای شما در نظر نگرفتم 💫"
        await query.edit_message_text(
            text,
            parse_mode='Markdown',
            reply_markup=get_main_keyboard()
        )

# تابع اصلی
def main():
    # ساختن اپلیکیشن
    app = Application.builder().token(TOKEN).build()
    
    # اضافه کردن هندلرها
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    
    # شروع کردن ربات
    print("🤖 ربات روشن شد و آماده کار است...")
    app.run_polling()

if __name__ == "__main__":
    main()
