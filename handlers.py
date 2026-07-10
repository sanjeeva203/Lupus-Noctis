from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler, MessageHandler, CommandHandler, filters

PHYSICS, MATHS, PC, OC, IOC, REVISION, EXERCISE, SLEEP = range(8)

mission_data = {}

async def mission(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🐺 Mission Initialization\n\nPhysics Target?")
    return PHYSICS

async def physics(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mission_data["physics"] = update.message.text
    await update.message.reply_text("Maths Target?")
    return MATHS

async def maths(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mission_data["maths"] = update.message.text
    await update.message.reply_text("Physical Chemistry Target?")
    return PC

async def pc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mission_data["pc"] = update.message.text
    await update.message.reply_text("Organic Chemistry Target?")
    return OC

async def oc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mission_data["oc"] = update.message.text
    await update.message.reply_text("Inorganic Chemistry Target?")
    return IOC

async def ioc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mission_data["ioc"] = update.message.text
    await update.message.reply_text("Revision Target?")
    return REVISION

async def revision(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mission_data["revision"] = update.message.text
    await update.message.reply_text("Exercise Target?")
    return EXERCISE

async def exercise(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mission_data["exercise"] = update.message.text
    await update.message.reply_text("Sleep Target?")
    return SLEEP

async def sleep(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mission_data["sleep"] = update.message.text

    summary = f"""
🐺 Mission Locked

Physics : {mission_data['physics']}
Maths : {mission_data['maths']}
PC : {mission_data['pc']}
OC : {mission_data['oc']}
IOC : {mission_data['ioc']}
Revision : {mission_data['revision']}
Exercise : {mission_data['exercise']}
Sleep : {mission_data['sleep']}
"""

    await update.message.reply_text(summary)
    return ConversationHandler.END


mission_handler = ConversationHandler(
    entry_points=[CommandHandler("mission", mission)],
    states={
        PHYSICS: [MessageHandler(filters.TEXT & ~filters.COMMAND, physics)],
        MATHS: [MessageHandler(filters.TEXT & ~filters.COMMAND, maths)],
        PC: [MessageHandler(filters.TEXT & ~filters.COMMAND, pc)],
        OC: [MessageHandler(filters.TEXT & ~filters.COMMAND, oc)],
        IOC: [MessageHandler(filters.TEXT & ~filters.COMMAND, ioc)],
        REVISION: [MessageHandler(filters.TEXT & ~filters.COMMAND, revision)],
        EXERCISE: [MessageHandler(filters.TEXT & ~filters.COMMAND, exercise)],
        SLEEP: [MessageHandler(filters.TEXT & ~filters.COMMAND, sleep)],
    },
    fallbacks=[],
)