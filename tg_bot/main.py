import asyncio
from aiogram import Bot, Dispatcher
from appp.handlers import router

TOKEN = '6602653534:AAHr0guKS3kf9rpayxgnZgC_Vl0X5kXHRWY'
bot = Bot(token=TOKEN)
dp = Dispatcher()
dp.include_router(router)


#Polling - постоянная работа бота.
async def main():
    await dp.start_polling(bot)

# def main() запускается только с этого файла.
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')