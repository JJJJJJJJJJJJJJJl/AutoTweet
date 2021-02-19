from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe" # Setting things up
driver = webdriver.Chrome(PATH)

driver.get("https://twitter.com/login?lang=pt") #Access the twitter login page

username = driver.find_element_by_name("session[username_or_email]") # Finds username text box
username.clear() # Clears text box
username.send_keys("YourUsername") # Writes username

password = driver.find_element_by_name("session[password]") # Finds password text box
password.clear() # Clears text box
password.send_keys("YourPassword") # Writes password
password.send_keys(Keys.RETURN) # Press ENTER after writing the password (instead of clicking in the "Login" button)

driver.get("https://twitter.com/compose/tweet") # Couldve done differently but chose to simply access the link to compose the tweet
driver.implicitly_wait(5) # Wait 5 seconds so the page loads properly and then try to find the text box
tweet = driver.find_element_by_css_selector("div[data-testid='tweetTextarea_0'][role='textbox']") # Finds tweet text box
tweet.send_keys("P#yJm3JeJ3SJJ.ulien8J") # Writes tweet

driver.find_element_by_css_selector("div[data-testid='tweetButton']").click() # Finds tweet button and press it
