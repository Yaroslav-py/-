from asyncio import sleep
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.filters.command import Command
from aiogram.utils.formatting import Text, Bold
from aiogram.fsm.context import FSMContext


from app.states import Quest
from app.utils import gpt_text
import app.keyboards as kb


user = Router()


@user.message(CommandStart())
async def cmd_start(message:Message):
    print('/start')
    await message.answer('Привет, это семейный Ai Bot. Можете задать мне вопрос',reply_markup=kb.main)
   
 
@user.message(Command('menu'))
async def cmd_menu(message: Message):
    print('меню')
    await message.answer('Привет, это семейный Ai Bot. Можете задать мне вопрос',reply_markup=kb.main)  


@user.message(Command('quest'))
async def cmd_quest(message: Message, state: FSMContext):
    await state.set_state(Quest.quest)
    await message.answer('Введите ваш вопрос')  


@user.callback_query(F.data == 'quest') 
async def but_quest(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Quest.quest)
    await callback.answer('') 
    await callback.message.edit_text('Введите ваш вопрос')
    await sleep(15)
    await callback.message.delete()
     
    
@user.message(Quest.quest)
async def chat_response(message: Message, state: FSMContext):
    await state.set_state(Quest.wait)
    response = await gpt_text(message.text, 'deepseek/deepseek-chat:free') #google/gemini-2.0-flash-001 deepseek/deepseek-chat:free
    await message.answer(response)
    await state.clear()


@user.message(Quest.wait)
async def wait_wait(message: Message):
    await message.answer('Ваш вопрос обрабатывается, подождите...')