import asyncio
import os
import sys
from pathlib import Path
from aiogram import Bot, Dispatcher, F
from aiogram.exceptions import TelegramConflictError, TelegramUnauthorizedError
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from dotenv import load_dotenv

def get_bot_token() -> str:
    # Load .env next to this script (works even if current working dir is different).
    env_path = Path(__file__).resolve().parent / ".env"
    load_dotenv(env_path)
    token = os.getenv("BOT_TOKEN", "").strip()
    if token:
        return token

    # Support manual launch without .env: ask token in terminal.
    if sys.stdin and sys.stdin.isatty():
        try:
            typed = input("Введите BOT_TOKEN из @BotFather: ").strip()
        except EOFError:
            typed = ""
        if typed:
            return typed

    raise RuntimeError(
        f"BOT_TOKEN не задан. Добавь BOT_TOKEN в {env_path} или в переменные окружения."
    )


TOKEN = get_bot_token()

bot = Bot(token=TOKEN)
dp = Dispatcher()


# ---------- КЛАВИАТУРЫ ----------

def main_menu_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="📚 Специальности/Мамандықтар", callback_data="spec_choice")
    builder.button(text="👩‍🏫 Преподаватели/Мұғалімдер", callback_data="teachers")
    builder.button(text="📝 Как оставить заявку/Заявканы қалдыру", url="https://youtu.be/837NCFc5q4M?si=IpAS7XMaEpiXbRnU")
    builder.button(text="🌐 Сайт", url="https://politcol.kz/")
    builder.button(text="📞 Контакты", callback_data="contact")
    builder.button(text="📍 Адрес", callback_data="address")
    builder.adjust(1)
    return builder.as_markup()


def language_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="🇷🇺 Русский язык", callback_data="spec_ru")
    builder.button(text="🇰🇿 Қазақ тілі", callback_data="spec_kz")
    builder.button(text="⬅️ Назад", callback_data="main_menu")
    builder.adjust(1)
    return builder.as_markup()


def back_to_lang_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="⬅️ Назад к выбору языка", callback_data="spec_choice")
    return builder.as_markup()


def teachers_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="⬅️ Назад в меню", callback_data="main_menu")
    return builder.as_markup()


# ---------- ОБРАБОТЧИКИ ----------

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "Здравствуйте! 👋\n"
        "Добро пожаловать в бот Политехнического колледжа им. Саламата Мукашева 🎓\n\n"
        "Выберите нужный раздел 👇",
        reply_markup=main_menu_keyboard()
    )


@dp.callback_query(F.data == "main_menu")
async def back_to_main(callback: CallbackQuery):
    await callback.message.edit_text(
        "Выберите нужный раздел 👇",
        reply_markup=main_menu_keyboard()
    )
    await callback.answer()


@dp.callback_query(F.data == "spec_choice")
async def spec_choice(callback: CallbackQuery):
    await callback.message.edit_text(
        "Выберите язык обучения 👇",
        reply_markup=language_keyboard()
    )
    await callback.answer()


# ---------- СПЕЦИАЛЬНОСТИ (РУССКИЙ) ----------

@dp.callback_query(F.data == "spec_ru")
async def spec_ru(callback: CallbackQuery):
    text = (
        "📘 Специальности (2025–2026)\n\n"
        "04110100 — Учет и аудит\n"
        "04120100 — Банковское и страховое дело\n"
        "05320200 — Технология и техника разведки месторождений полезных ископаемых\n"
        "06120100 — Вычислительная техника и информационные сети (по видам)\n"
        "06120200 — Системы информационной безопасности\n"
        "06130100 — Программное обеспечение (по видам)\n"
        "07110100 — Химическая технология и производство (по видам)\n"
        "07110400 — Лабораторная технология\n"
        "07110500 — Технология переработки нефти и газа\n"
        "07130200 — Электроснабжение (по отраслям)\n"
        "07130700 — Техническое обслуживание, ремонт и эксплуатация электромеханического оборудования\n"
        "07140100 — Автоматизация и управление технологическими процессами\n"
        "07140200 — Мехатроника (по отраслям)\n"
        "07140900 — Радиоэлектроника, электроника и телекоммуникации\n"
        "07150500 — Сварочное дело (по видам)\n"
        "07150600 — Слесарное дело (по отраслям и видам)\n"
        "07151100 — Эксплуатация и техническое обслуживание машин и оборудования\n"
        "07220700 — Технология полимерного производства\n"
        "07240700 — Бурение нефтяных и газовых скважин\n"
        "07240900 — Эксплуатация нефтяных и газовых месторождений\n"
        "07320600 — Монтаж магистральных локальных и сетевых трубопроводов\n"
        "10320200 — Защита в чрезвычайных ситуациях (по профилю)\n"
        "10410200 — Организация перевозок и управление движением на железнодорожном транспорте\n\n"
        "Подробнее: https://politcol.kz/applicants/specialties/"
    )
    await callback.message.edit_text(text, reply_markup=back_to_lang_keyboard())
    await callback.answer()


# ---------- СПЕЦИАЛЬНОСТИ (ҚАЗАҚ) ----------

@dp.callback_query(F.data == "spec_kz")
async def spec_kz(callback: CallbackQuery):
    text = (
        "📗 Мамандылықтар (2025–2026)\n\n"
        "04110100 — Есеп және аудит\n"
        "04120100 — Банктік және сақтандыру ісі\n"
        "05320200 — Пайдалы қазбалар кен орындарын барлау технологиясы\n"
        "06120100 — Есептеу техникасы және ақпараттық желілер\n"
        "06120200 — Ақпараттық қауіпсіздік жүйелері\n"
        "06130100 — Бағдарламалық қамтамасыз ету\n"
        "07110100 — Химиялық технология және өндіріс\n"
        "07110400 — Зертханалық технология\n"
        "07110500 — Мұнай мен газды қайта өңдеу технологиясы\n"
        "07130200 — Электрмен жабдықтау\n"
        "07130700 — Электромеханикалық жабдықтарға техникалық қызмет көрсету\n"
        "07140100 — Автоматтандыру және басқару\n"
        "07140200 — Мехатроника\n"
        "07140900 — Радиоэлектроника және телекоммуникация\n"
        "07150500 — Дәнекерлеу ісі\n"
        "07150600 — Слесарлық іс\n"
        "07151100 — Машиналар мен жабдықтарды пайдалану және қызмет көрсету\n"
        "07220700 — Полимер өндірісінің технологиясы\n"
        "07240700 — Мұнай және газ ұңғымаларын бұрғылау\n"
        "07240900 — Мұнай және газ кен орындарын пайдалану\n"
        "07320600 — Құбыр желілерін монтаждау\n"
        "10320200 — Төтенше жағдайларда қорғау\n"
        "10410200 — Теміржол көлігінде тасымалдауды ұйымдастыру\n\n"
        "Толық ақпарат: https://politcol.kz/applicants/specialties/"
    )
    await callback.message.edit_text(text, reply_markup=back_to_lang_keyboard())
    await callback.answer()


# ---------- КОНТАКТЫ ----------

@dp.callback_query(F.data == "contact")
async def contact(callback: CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.button(text="⬅️ Назад в меню", callback_data="main_menu")
    builder.adjust(1)

    await callback.message.edit_text(
        "📞 Контактные телефоны:\n\n"
        "Приемная: +7 7122 365626\n"
        "Приемная комиссия: +7 7122 366299",
        reply_markup=builder.as_markup()
    )
    await callback.answer()


# ---------- АДРЕС ----------

@dp.callback_query(F.data == "address")
async def address(callback: CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.button(
        text="🗺 Открыть в 2GIS",
        url="https://2gis.kz/atyrau/geo/70000001034595909/51.940179,47.134895"
    )
    builder.button(
        text="🗺 Открыть в Google Maps",
        url="https://www.google.com/maps/search/?api=1&query=47.134895,51.940179"
    )
    builder.button(text="⬅️ Назад в меню", callback_data="main_menu")
    builder.adjust(1)

    await callback.message.edit_text(
        "📍 г. Атырау, ул. Габбаса Бергалиева, 45\n\n"
        "Выберите удобный сервис для навигации 👇",
        reply_markup=builder.as_markup()
    )
    await callback.answer()


# ---------- ПРЕПОДАВАТЕЛИ ----------

@dp.callback_query(F.data == "teachers")
async def teachers(callback: CallbackQuery):
    teachers_list = [
        "Абилхан А.С.",
        "Ербатырова М.Т.",
        "Ғалымжан Д.Ж.",
        "Жумагалиева Э.А.",
        "Нәсіпбаева А.Н.",
        "Саханова Б.А.",
        "Сариева А.С."
    ]
    teachers_list.sort()
    text = "👩‍🏫 Преподаватели колледжа:\n\n"
    text += "\n".join(teachers_list)

    await callback.message.edit_text(text, reply_markup=teachers_keyboard())
    await callback.answer()


async def main():
    try:
        me = await bot.get_me()
        print(f"Бот запущен: @{me.username} (id={me.id})")
        await dp.start_polling(bot)
    except TelegramConflictError:
        print("Ошибка: запущено несколько копий бота (409 Conflict).")
        print("Останови второй процесс бота или отключи parallel polling.")
    except TelegramUnauthorizedError:
        print("Ошибка: Telegram отклонил токен (Unauthorized).")
        print("Проверь BOT_TOKEN или выпусти новый у @BotFather.")


if __name__ == "__main__":
    asyncio.run(main())
