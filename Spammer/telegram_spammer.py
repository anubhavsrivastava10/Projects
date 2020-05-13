from selenium import webdriver
from time import sleep

# name of your country
name = 'India'

# your phone number
num = '9456623955'

# name of the person you want to send message to
target = 'Saved Messages'

# What do you want to write in the message
string = " _ "

# Number of messages you want to send him
num_of_msg = 10

# install chromedriver / any other web browser driver (I have used chrome change the .Chrome as well)
# and give it's location in the empty string
# activating chromedriver
driver = webdriver.Chrome("C:.............chromedriver.exe")

# calling the whatsapp web url
driver.get("https://web.telegram.org/#/im")

# sleep for 1 minute for the things to load (basically depends your network speed)
sleep(20)

#choosing country
country = driver.find_element_by_xpath('//*[@id="ng-app"]/body/div[1]/div/div[2]/div[2]/form/div[1]/div')
country.click()
sleep(5)

# typing country in search
name_country = driver.find_element_by_xpath('//*[@id="ng-app"]/body/div[5]/div[2]/div/div/div[2]/div[1]/input')
name_country.send_keys(name)
sleep(2)

# selecting the country
if name =='India':
    select = driver.find_element_by_xpath('//*[@id="ng-app"]/body/div[5]/div[2]/div/div/div[2]/div[2]/div/div[1]/ul/li[2]/a')
    select.click()
    sleep(2)
else:
    select = driver.find_element_by_xpath('//*[@id="ng-app"]/body/div[5]/div[2]/div/div/div[2]/div[2]/div/div[1]/ul/li/a')
    select.click()
    sleep(2)

#entering phone number
number = driver.find_element_by_xpath('//*[@id="ng-app"]/body/div[1]/div/div[2]/div[2]/form/div[2]/div[2]/input')
number.send_keys(num)
sleep(3)

# clicking next button
next_button = driver.find_element_by_xpath('//*[@id="ng-app"]/body/div[1]/div/div[2]/div[1]/div/a')
next_button.click()
sleep(10)

# confirming the correct number
ok = driver.find_element_by_xpath('//*[@id="ng-app"]/body/div[5]/div[2]/div/div/div[2]/button[2]/span')
ok.click()
sleep(60)
# increased sleep time here so that user can enter the verification code

# Writing the name in the search button
search = driver.find_element_by_xpath('//*[@id="ng-app"]/body/div[1]/div[2]/div/div[1]/div[1]/div/input')
search.send_keys(target)
sleep(15)

# Clicking the first result shown
name_click = driver.find_element_by_xpath('//*[@id="ng-app"]/body/div[1]/div[2]/div/div[1]/div[2]/div/div[1]/ul/li[1]')
name_click.click()

sleep(5)

# Writitng text feild
message = driver.find_element_by_xpath('//*[@id="ng-app"]/body/div[1]/div[2]/div/div[2]/div[3]/div/div[3]/div[2]/div/div/div/form/div[2]/div[5]')

# send button
# you can also try keys.enter if you want to
send = driver.find_element_by_xpath('//*[@id="ng-app"]/body/div[1]/div[2]/div/div[2]/div[3]/div/div[3]/div[2]/div/div/div/form/div[3]/button')

# sending the message
for i in range(num_of_msg):
    message.send_keys(string)
    sleep(1)
    send.click()
    sleep(1)
    
