import sqlite3
import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service

import time

db = sqlite3.connect('database.db')
cursor = db.cursor()

#  inserir dados no db
def inserir_dados_telefone():

    cursor.execute(f"INSERT INTO bot VALUES ('{contato}')")
    db.commit()

cursor.execute('SELECT * FROM bot')
print(cursor.fetchall())


#  salvando sessão para não precisar carregar novamente
dir_path = os.getcwd()
profile = os.path.join(dir_path, "profile", "wpp")
options = webdriver.ChromeOptions()
options.add_argument(
    r"user-data-dir={}".format(profile))


# abrindo o chrome
driver = webdriver.Chrome("./chromedriver.exe", chrome_options=options)

driver.get('https://web.whatsapp.com/')
time.sleep(8)

while True:

    try:

        #  voltando para o contato padrao contato padrao
        elem = driver.find_element(By.XPATH,
                                   '//*[@id="pane-side"]/div[1]/div/div/div[5]/div/div/div[2]/div[2]/div[2]/span[1]/div')
        elem.click()

        #  capturando notificacao de mensagem
        elem = driver.find_element(By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[4]/div/div/div[2]/div[2]/div[2]/span[1]/div')
        elem.click()  # clickando na notificaçao

        #  pegando nome ou numero de telefone
        elem = driver.find_element(By.CLASS_NAME, '_21nHd')

        contato = elem.text
        print(contato)
        #  inserir_dados_telefone()


        #  pegando ultima msg
        elem = driver.find_elements(By.CLASS_NAME, '_1Gy50')
        #  convertendo as mensagem em texto
        todas_msg_texto = [e.text for e in elem]

        #  respondendo a mensagem


        elem = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
        elem.send_keys('Digite uma opçao:\n'
                       '1 - Boleto\n'
                       '2 - Falar com tecnico\n'
                       '3 - Encerrar')

        elem.send_keys(Keys.RETURN)

        #  pegando ultima msg
        ultima_msg = todas_msg_texto[-1]
        print(ultima_msg)

        if ultima_msg == '1':

            print('abrir boleto')

        else:
            pass


    except:

        time.sleep(5)
        print('Buscando novas msg')




