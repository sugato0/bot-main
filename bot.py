from aiogram import executor
from create_bot import dp

async def on_startup(_):
    print('Start')

from handlers import user, admin, other

user.register_handlers_user(dp)
# admin.register_handlers_admin(dp)
# other.register_handlers_other(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup) 