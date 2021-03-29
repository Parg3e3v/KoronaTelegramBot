from covid import Covid
import telebot
from telebot import types
import country_converter as coco
import flag

covid19 = Covid(source="worldometers")

cvd = covid19.get_status_by_country_name("Spain")

print(cvd)