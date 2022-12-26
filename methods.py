from config import *
from db_functions import *
import requests
import time
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)



def ScrapeItemsMercari(links, tableName):
    options = Options()
    options.headless = True
    driver = uc.Chrome(options=options,use_subprocess=True)
    wait = WebDriverWait(driver, 20)
    for link in links:
        driver.get(link)
        time.sleep(8)
        a_tags = driver.find_elements("tag name", "a")
        data_list = []
        for a_tag in a_tags:
            if "us/item/" in a_tag.get_attribute("href"):
                div_tags = a_tag.find_elements("tag name", "div")
                for div_tag in div_tags:
                    try:
                        if div_tag.text != "":
                            data_list.append(a_tag.get_attribute("href") + "?" + div_tag.text.replace("\n", "+"))
                            break
                    except:pass
        for data in data_list:
            items = data.split("?")
            alreadyexisting_urls = AssignDBContenttoList(dbname,tableName,"url")
            if items[0] in alreadyexisting_urls:
                pass
            else:
                InfoText = items[1].replace("'","").replace('"','')
                QueryToDB(dbname, "INSERT INTO {} (url, Info, Notified) VALUES ('{}','{}','{}')".format(tableName, items[0], InfoText, "0"))
    driver.close()

def NotificationMessageBuilder(table):
    urls = AssignDBContenttoList(dbname, "IphoneOffers", "url")
    Infoes = AssignDBContenttoList(dbname, "IphoneOffers", "Info")

    for k in range(len(urls)):
        urls[k] = urls[k].replace(".","\\.")

    for i in range(len(Infoes)):
        Infoes[i] = Infoes[i].replace("+",",").replace("/","").replace("'","").replace('"','').\
            replace("!","").replace("-","").replace(".","\\.").replace("(","\\(").replace(")","\\)")
    message = ""
    for j in range(len(urls)):
        message = message + urls[j] + Infoes[j] + "\n\n"
    return message

def TelegramNotification(bodytext, bot_token, chatID):
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + \
                chatID + '&parse_mode=MarkdownV2&text=' + bodytext
    response = requests.get(send_text)




