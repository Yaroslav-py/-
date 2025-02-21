from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton,CallbackQuery


main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Задать вопрос', callback_data='quest')]
])