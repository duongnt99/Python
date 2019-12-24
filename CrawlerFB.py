import time
import urllib
import urllib.request
import calendar
import os
import platform
import sys

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



def new_window(driver):
    	
	#To switch to a new window in order to save state on present window ( required to avoid stale element reference exception)
	WebDriverWait(driver, 10)
	time.sleep(7)

def old_window(driver):
    
	# To switch back to previous state
	driver.switch_to_window(driver.window_handles[0])
	time.sleep(10)


def scroll_all(driver, scrolls = 1000):
    
    SCROLL_PAUSE_TIME = 5
    count = 0
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        count+=1
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if(new_height == last_height):
            break
        if count == scrolls:
            break
        last_height = new_height

def images(driver):
    	
	loc="C:/Users/Admin/Pictures/DowloadIm"
	
	print
	print ("---------------Getting images of Friends--------------------")
	
	driver.get("https://www.facebook.com/profile.php?id=100010448595370")
	time.sleep(7)

	friend_image = driver.find_elements_by_tag_name("img")
	for image in friend_image:
		if image.get_attribute("class") == "_11kf img":
			image_link = image.get_attribute("src")
			break

	friend_name = driver.find_elements_by_tag_name("a")
	for friend in friend_name:
		if friend.get_attribute("class") == "_2nlw _2nlv":
			image_name = friend.get_attribute("text")
			break

	image_name = "/" + image_name +".jpg"
	image_loc = loc + image_name

	urllib.request.urlretrieve(image_link,image_loc)    

def timeline_images(driver):
    	
	# loc = place to store downloaded images (specify this)
	loc="C:/Users/Admin/Pictures/DowloadIm"
	
	print
	print ("---------------Downloading timeline images of user--------------------")
	cnt = 1

	scroll_all(driver,3)
	all_anchor = driver.find_elements_by_tag_name("a")
	for anchor in all_anchor:

		link = anchor.get_attribute("href")

		if link == None:
			continue

		rel_atr = anchor.get_attribute("rel")

		if rel_atr == "theater":
			new_window(driver)
			driver.get(link)
			time.sleep(7)
			wall_image = driver.find_elements_by_tag_name("img")

			for image in wall_image:
				image_class = image.get_attribute("class")

				if image_class == "spotlight":
					src = image.get_attribute("src")
					image_loc = loc+"/"+ str(cnt) +".png"
					#print link
					urllib.request.urlretrieve(src,image_loc)
					cnt += 1

			old_window(driver)
			break
			time.sleep(7)

def Allimages(driver,idlink):
    	
	loc="C:/Users/Admin/Pictures/DowloadIm"
	
	print
	print ("---------------Getting images of Friends--------------------")
	
	driver.get("https://www.facebook.com"+idlink+"photos")
	time.sleep(7)
	driver.find_element

	friend_image = driver.find_elements_by_tag_name("img")
	for image in friend_image:
		if image.get_attribute("class") == "_11kf img":
			image_link = image.get_attribute("src")
			break

	friend_name = driver.find_elements_by_tag_name("a")
	for friend in friend_name:
		if friend.get_attribute("class") == "_2nlw _2nlv":
			image_name = friend.get_attribute("text")
			break

	image_name = "/" + image_name +".jpg"
	image_loc = loc + image_name

	urllib.request.urlretrieve(image_link,image_loc)






def login():
    
    driver = webdriver.Chrome("C:/Users/Admin/Desktop/New folder (2)/chromedriver.exe")
    driver.maximize_window()
    driver.get('http://fb.com')
    driver.maximize_window()
    """Email = input("Enter your Facebook email: ")
    PassWord = input("Enter your Password: ")"""

    inputElement = driver.find_element_by_id("email")
    inputElement.send_keys("thaiduong101999@gmail.com")
    inputElement = driver.find_element_by_id("pass")
    inputElement.send_keys("3010197")
    driver.find_element_by_id("u_0_b").click()

	time.sleep(10)
    driver.get
    
    #driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div[1]/div[1]/div[2]/div[1]/a[1]/span[1]").click()	
	
    
    #images(driver)
    #timeline_images(driver)
   
    
login()

