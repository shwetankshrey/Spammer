from selenium import webdriver
from random import choice
chromedriver = "C:\chromedriver"
driver = webdriver.Chrome(chromedriver)
f = open('quotes.txt') # txt file with quotes
t = f.read()
lns = t.split('\n.\n')
while True:
  driver.get("https://goo.gl/forms/VLip0H6IN8TkaJBJ3")
  tf = driver.find_element_by_name("entry.925157627")
  tf.send_keys(choice(lns)) # Change this to whatever you want
  bt = driver.find_element_by_class_name("quantumWizButtonPaperbuttonLabel")
  bt.click()