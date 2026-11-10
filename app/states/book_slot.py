from aiogram.fsm.state import State, StatesGroup


class BookSlot(StatesGroup):
    job = State()
    price = State()
    grade = State()


__all__ = ["BookSlot"]