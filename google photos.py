import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
import shutil
import os
import random
from time import sleep
import ctypes
user = os.getlogin()
driver = webdriver.Chrome()
directory = 'C:\\Users\\User\\AppData\\Local\\Temp'         #your path where the picture is saved
prein = str(input("Enter search query"))
inp = prein.replace(" ","+")
url = 'https://www.google.com/search?q='+str(inp)+'&source=lnms&tbm=isch&sa=X&ved=2ahUKEwie44_AnqLpAhUhBWMBHUFGD90Q_AUoAXoECBUQAw&biw=1920&bih=947'
j = random.randint(0, 50)
imagePath = 'C:\\Users\\User\\AppData\\Local\\Temp\\googlepic.jpg'

def save_img(inp,img,i):
    try:
        filename = 'googlepic.jpg'
        response = requests.get(img,stream=True)
        image_path = os.path.join(directory, filename)
        with open(image_path, 'wb') as file:
            shutil.copyfileobj(response.raw, file)
    except Exception:
        pass


def find_urls(inp,url,driver,j):
    driver.get(url)
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    sleep(5)
    imgurl = driver.find_element_by_xpath('//div//div//div//div//div//div//div//div//div//div['+str(j)+']//a[1]//div[1]//img[1]')
    imgurl.click()
    time.sleep(10)
    img = driver.find_element_by_xpath('//body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img').get_attribute("src")
    save_img(inp,img,j)

def delete_file():
    if os.path.exists("\\Users\\User\\AppData\\Local\\Temp\\googlepic.jpg"):        
        os.remove("\\Users\\User\\AppData\\Local\\Temp\\googlepic.jpg")             #delete the previous image if it exist

def changeBG(imagePath):
    find_urls(inp,url,driver,j)
    sleep(5)
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(20, 0, imagePath, 3)
    return;
            
def main():
     delete_file()
     changeBG(imagePath)
     time.sleep(8)
     print("\nHope you like this one! Quitting.")
    
main()