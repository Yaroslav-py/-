from aiogram.fsm.state import StatesGroup, State


class Quest(StatesGroup):
    quest = State()
    wait = State()
    