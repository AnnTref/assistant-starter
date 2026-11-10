from aiogram import Router, types, F

router = Router()

@router.message(F.text == "FAQ")
async def on_faq_button(message: types.Message):
    await message.answer(f"Выберите вопрос...")
    await message.answer(f"Можно спросить у ИИ, выберите кнопку")

@router.message(F.text == "О нас")
async def on_faq_button(message: types.Message):
    await message.answer(f"О проекте...")