from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import time
import pickle

# Path to your GeckoDriver executable
geckodriver_path = '/Users/Nafiz/Documents/Projects/automate-empatic/geckodriver'

# Path to your custom Firefox profile directory
custom_profile_path = '/Users/Nafiz/Library/Application Support/Firefox/Profiles/tw7fsjwl.custom_profile'

# Set up Firefox profile
profile = FirefoxProfile(profile_directory=custom_profile_path)

# Set up Firefox options
options = Options()
options.profile = profile
options.add_argument("-private")  # Use private browsing mode

# Set up GeckoDriver service
service = Service(geckodriver_path)

# Initialize the Firefox driver
driver = webdriver.Firefox(service=service, options=options)

# URL to navigate to
url = "https://portal.dev.empatick.com/dashboard"

# Navigate to the URL
driver.get(url)

# Wait for 30 seconds to allow manual login
time.sleep(30)

# Get cookies
cookies = driver.get_cookies()
print(cookies)

# Save cookies to a file
with open("cookies.pkl", "wb") as file:
    pickle.dump(cookies, file)

# Close the browser session
driver.quit()