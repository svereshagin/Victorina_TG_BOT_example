import asyncio
from telebot import types
from telebot.async_telebot import AsyncTeleBot
from telebot.states.asyncio import StateContext, StateMiddleware
from telebot.asyncio_storage import StateMemoryStorage
from telebot.states import StatesGroup, State
from telebot.asyncio_filters import StateFilter

TOKEN='7084142136:AAE-P9SMdAWgMzeyl9CpV9Qvd1WVwFp1CVY'
state_storage = StateMemoryStorage()
bot = AsyncTeleBot(token=TOKEN, state_storage=state_storage)
bot.add_custom_filter(StateFilter(bot))
bot.setup_middleware(StateMiddleware(bot))


class Victorina(StatesGroup):
    q1: State = State()
    q2: State  = State()
    q3: State  = State()
    q4: State  = State()
    q5: State  = State()
    q6: State  = State()
    q7: State  = State()
    q8: State  = State()
    q9: State  = State()
    q10: State  = State()
    last: State  = State()

questions = {
    Victorina.q1: ("Когда день рождения у вьюшки?", "16 ноября"),
    Victorina.q2: ("Сколько лет Асти?", "7"),
    Victorina.q3: ("Какие у мамы два высших образования?", "инженер и менеджер"),
    Victorina.q4: ("В какой школе училась мама?", "3"),
    Victorina.q5: ("Девичья фамилия бабушки Нины?", "тимофеевна"),
    Victorina.q6: ("Каких питомцев у нас не было?", "ящерица"),
    Victorina.q7: ("Какой вид был у рыбки?", "псевдотрофеус"),
    Victorina.q8: ("В какой школе учатся твои дети?", "5"),
    Victorina.q9: ("Второе название породы нашей собаки?", "серебряный призрак"),
    Victorina.q10: ("Любимое блюдо мамы?", "салат с баклажанами"),
}


def register_handlers(bot):
    @bot.message_handler(commands=['start'])
    async def start(message: types.Message,  state: StateContext):
        text = questions[Victorina.q1][0]
        await state.set(Victorina.q1)
        await bot.send_message(message.chat.id, text)


    @bot.message_handler(state=Victorina.q1)
    async def q1_question(message: types.Message, state: StateContext):
        await state.set(Victorina.q2)
        await state.add_data(q1_ans=message.text.lower())
        text = questions[Victorina.q2][0]
        await bot.send_message(message.chat.id, text)

    @bot.message_handler(state=Victorina.q2)
    async def q2_question(message: types.Message, state: StateContext):
        await state.set(Victorina.q3)
        await state.add_data(q2_ans=message.text.lower())
        text = questions[Victorina.q3][0]
        await bot.send_message(message.chat.id, text)

    @bot.message_handler(state=Victorina.q3)
    async def q3_question(message: types.Message, state: StateContext):
        await state.set(Victorina.q4)
        await state.add_data(q3_ans=message.text.lower())
        text = questions[Victorina.q4][0]
        await bot.send_message(message.chat.id, text)

    @bot.message_handler(state=Victorina.q4)
    async def q3_question(message: types.Message, state: StateContext):
        await state.set(Victorina.last)
        await state.add_data(q3_ans=message.text.lower())
        text = questions[Victorina.q4][0]
        await bot.send_message(message.chat.id, text)
    @bot.message_handler(state=Victorina.last)
    async def q3_question(message: types.Message, state: StateContext):

        async with state.data() as data:
            q1 = data["q1_ans"]
            q2 = data["q2_ans"]
            q3 = data["q3_ans"]
        msg = f'{q1}\n{q2}\n{q3}\n {message.text}'
        await bot.send_message(message.chat.id, msg)
        await state.delete()

async def start_bot():
    register_handlers(bot)
    await bot.polling()
async def main():
    await start_bot()


if __name__ == "main":
    asyncio.run(main())