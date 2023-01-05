import logging
from aiogram import Bot, Dispatcher, executor, types
from random import randrange

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import json

API_TOKEN = '5915871838:AAGbY9o8eUHkn40J1ftQhcb8zXYaPv70NhM'
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
storage = MemoryStorage()


def read(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        FileNotFoundError("create file with predictions!")


class ZodiacSign:
    def __init__(self, name, age):
        if isinstance(name, str) and isinstance(age, int):
            self.name = name
            self.age = age
        else:
            raise TypeError("name should be string and age should be int!")

    def predict(self):
        prediction = read("pred.json")
        str1 = str(randrange(12))
        return prediction[str1]["prediction"]

    def sayHi(self):
        saying = "Hello user!!"
        return saying


class Aries(ZodiacSign):
    def __init__(self, name, age):
        super().__init__(name, age)

    def sayHi(self):
        saying = "Hello Aries!!"
        return saying

    def __str__(self):
        return "Aries"


class Taurus(ZodiacSign):
    def __init__(self, name, age):
        super().__init__(name, age)

    def sayHi(self):
        saying = "Hello Taurus!!"
        return saying

    def __str__(self):
        return "Taurus"


class Gemini(ZodiacSign):
    def __init__(self, name, age):
        super().__init__(name, age)

    def sayHi(self):
        saying = "Hello Gemini!!"
        return saying

    def __str__(self):
        return "Gemini"


class Cancer(ZodiacSign):
    def __init__(self, name, age):
        super().__init__(name, age)

    def sayHi(self):
        saying = "Hello Cancer!!"
        return saying

    def __str__(self):
        return "Cancer"


class Leo(ZodiacSign):
    def __init__(self, name, age):
        super().__init__(name, age)

    def sayHi(self):
        saying = "Hello Leo!!"
        return saying

    def __str__(self):
        return "Leo"


class Virgo(ZodiacSign):
    def __init__(self, name, age):
        super().__init__(name, age)

    def sayHi(self):
        saying = "Hello Virgo!!"
        return saying

    def __str__(self):
        return "Virgo"


class Libra(ZodiacSign):
    def __init__(self, name, age):
        super().__init__(name, age)

    def sayHi(self):
        saying = "Hello Libra!!"
        return saying

    def __str__(self):
        return "Libra"


class Scorpio(ZodiacSign):
    def __init__(self, name, age):
        super().__init__(name, age)

    def sayHi(self):
        saying = "Hello Scorpio!!"
        return saying

    def __str__(self):
        return "Scorpio"


class Saggitarius(ZodiacSign):
    def __init__(self, name, age):
        super().__init__(name, age)

    def sayHi(self):
        saying = "Hello Saggitarius!!"
        return saying

    def __str__(self):
        return "Saggitarius"


class Capricorn(ZodiacSign):
    def __init__(self, name, age):
        super().__init__(name, age)

    def sayHi(self):
        saying = "Hello Capricorn!!"
        return saying

    def __str__(self):
        return "Capricorn"


class Aquarius(ZodiacSign):
    def __init__(self, name, age):
        super().__init__(name, age)

    def sayHi(self):
        saying = "Hello Aquarius!!"
        return saying

    def __str__(self):
        return "Aquarius"


class Pisces(ZodiacSign):
    def __init__(self, name, age):
        super().__init__(name, age)

    def sayHi(self):
        saying = "Hello Pisces!!"
        return saying

    def __str__(self):
        return "Pisces"


class Compatibility(StatesGroup):
    def __init__(self, obj1):
        self.obj = obj1

    def compare(self):
        if self.obj == "Aries":
            return "55%"
        elif self.obj == "Pisces":
            return "100%"
        elif self.obj == "Leo":
            return "35%"
        elif self.obj == "Libra":
            return "95%"
        elif self.obj == "Cancer":
            return "10%"
        elif self.obj == "Aquarius":
            return "105%!!!!!!"
        else:
            return "Oops, something wrong, try again typing /compatibility"


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Hi! Welcome to zodiac sign bot!! \nUse /predictions to check your horoscope for today!")


button1 = InlineKeyboardButton(text="Aries", callback_data="predForAries")
button2 = InlineKeyboardButton(text="Taurus", callback_data="predForTaurus")
button3 = InlineKeyboardButton(text="Gemini", callback_data="predForGemini")
button4 = InlineKeyboardButton(text="Cancer", callback_data="predForCancer")
button5 = InlineKeyboardButton(text="Leo", callback_data="predForLeo")
button6 = InlineKeyboardButton(text="Virgo", callback_data="predForVirgo")
button7 = InlineKeyboardButton(text="Libra", callback_data="predForLibra")
button8 = InlineKeyboardButton(text="Scorpio", callback_data="predForScorpio")
button9 = InlineKeyboardButton(text="Saggitarius", callback_data="predForSaggitarius")
button10 = InlineKeyboardButton(text="Capricorn", callback_data="predForCapricorn")
button11 = InlineKeyboardButton(text="Aquarius", callback_data="predForAquarius")
button12 = InlineKeyboardButton(text="Pisces", callback_data="predForPisces")
butForYes = InlineKeyboardButton(text="Yes", callback_data="showCompatibility")
butForNo = InlineKeyboardButton(text="No", callback_data="exit")

keyboard_inline = InlineKeyboardMarkup().add(button1, button2, button3, button4, button5, button6, button7, button8,
                                             button9, button10, button11, button12)
answer_inline = InlineKeyboardMarkup().add(butForYes, butForNo)


@dp.message_handler(commands=['predictions'])
async def answer(message: types.Message):
    await message.reply("Select your sign:", reply_markup=keyboard_inline)


@dp.callback_query_handler(text=["predForAries", "predForTaurus", "predForGemini", "predForCancer", "predForLeo",
                                 "predForVirgo", "predForLibra", "predForScorpio", "predForSaggitarius",
                                 "predForCapricorn", "predForAquarius"])
async def preds(call: types.CallbackQuery):
    if call.data == "predForAries":
        sign = Aries("user1", 18)
        await call.message.answer(sign.sayHi())
        await call.message.answer(sign.predict())
    if call.data == "predForTaurus":
        sign = Taurus("user1", 18)
        await call.message.answer(sign.sayHi())
        await call.message.answer(sign.predict())
    if call.data == "predForGemini":
        sign = Gemini("user1", 18)
        await call.message.answer(sign.sayHi())
        await call.message.answer(sign.predict())
    if call.data == "predForCancer":
        sign = Cancer("user1", 18)
        await call.message.answer(sign.sayHi())
        await call.message.answer(sign.predict())
    if call.data == "predForLeo":
        sign = Leo("user1", 18)
        await call.message.answer(sign.sayHi())
        await call.message.answer(sign.predict())
    if call.data == "predForVirgo":
        sign = Virgo("user1", 18)
        await call.message.answer(sign.sayHi())
        await call.message.answer(sign.predict())
    if call.data == "predForLibra":
        sign = Libra("user1", 18)
        await call.message.answer(sign.sayHi())
        await call.message.answer(sign.predict())
    if call.data == "predForScorpio":
        sign = Scorpio("user1", 18)
        await call.message.answer(sign.sayHi())
        await call.message.answer(sign.predict())
    if call.data == "predForSaggitarius":
        sign = Saggitarius("user1", 18)
        await call.message.answer(sign.sayHi())
        await call.message.answer(sign.predict())
    if call.data == "predForCapricorn":
        sign = Capricorn("user1", 18)
        await call.message.answer(sign.sayHi())
        await call.message.answer(sign.predict())
    if call.data == "predForAquarius":
        sign = Aquarius("user1", 18)
        await call.message.answer(sign.sayHi())
        await call.message.answer(sign.predict())
    await call.message.answer("what next? /compatibility")


@dp.message_handler(commands=['compatibility'])
async def answer(message: types.Message):
    await message.reply("Alright then!! Check your chances for love!!\nEnter sign of your crush!!")


@dp.message_handler(state='*')
async def process_answers(message: types.Message, state: FSMContext):
    await state.finish()
    str1 = message.text
    comp = Compatibility(str1)
    await message.reply(comp.compare())
    await message.answer("by the way you can check other signs day! type /predictions\nor find out more "
                         "/compatibility")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
