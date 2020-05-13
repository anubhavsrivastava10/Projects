from selenium import webdriver
from time import sleep

# name of the person you want to send message to
target = ' _____ ' # remove the underline and write the name as per your contacts

# What do you want to write in the message
string = " ________ " # replace the unerline with your text

# Number of messages you want to send him
num_of_msg = 10 # change the number as per your convinence

# install chromedriver / any other web browser driver (I have used chrome change the .Chrome as well)
# and give it's location in the empty string
# activating chromedriver
driver = webdriver.Chrome("C:/Users/MY HP/Desktop/FSDP2019/DAY 08/chromedriver.exe")

# calling the whatsapp web url
driver.get("https://web.whatsapp.com/")

# sleep for 1 minute for the things to load (basically depends your network speed)
sleep(60)

# Writing the name in the search button
search = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
search.send_keys(target)
sleep(15)

# Clicking the first result shown
name_click = driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[1]')
name_click.click()

sleep(5)

# Writitng text feild
message = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

# send button
# you can also try keys.enter if you want to
send = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]')

# sending the message
for i in range(num_of_msg):
    message.send_keys(string)
    sleep(1)
    send.click()
    sleep(1)
