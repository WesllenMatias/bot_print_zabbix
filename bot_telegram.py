import telepot
from selenium import webdriver
from time import sleep
import config
import util

def pegar_print():
    driver = webdriver.Firefox()
    driver.get(config.dash)
    sleep(2)
    campo = driver.find_element_by_name("name")
    campo.send_keys(config.usr)
    sleep(1)
    senha = driver.find_element_by_name("password")
    senha.send_keys(config.pwd)
    logon = driver.find_element_by_name("enter")
    logon.click()
    sleep(1)

    util.fullpage_screenshot(driver,"screenshot.png")
    driver.quit()

def manda_telegram():

    TOKEN = config.tk
    USER = config.alvo
    
    bot = telepot.Bot(TOKEN)
    
    for idtelegram in USER:
        bot.sendPhoto(idtelegram,open('./screenshot.png','rb'),caption=None, parse_mode=None, disable_notification=None, reply_to_message_id=None, reply_markup=None)


pegar_print()
sleep(1)
manda_telegram()