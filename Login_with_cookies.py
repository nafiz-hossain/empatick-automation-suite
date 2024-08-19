from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import pickle

# Path to your GeckoDriver executable
geckodriver_path = '/Users/Nafiz/Documents/Projects/automate-empatic/geckodriver'

# Path to your custom Firefox profile directory
custom_profile_path = '/Users/Nafiz/Library/Application Support/Firefox/Profiles/tw7fsjwl.custom_profile'

# Set up Firefox profile
profile = FirefoxProfile(custom_profile_path)

# Set up Firefox options
options = Options()
options.profile = profile
options.add_argument("-private")  # Use private browsing mode

# Set up GeckoDriver service
service = Service(geckodriver_path)

# Initialize the Firefox driver
driver = webdriver.Firefox(service=service, options=options)

# URL to navigate to (same domain as the cookies)
url = "https://portal.dev.empatick.com/dashboard"

# Navigate to the correct domain
driver.get(url)

# Load cookies from the file
with open("cookies.pkl", "rb") as file:
    cookies = pickle.load(file)

# Add cookies to the browser
for cookie in cookies:
    try:
        driver.add_cookie(cookie)
    except Exception as e:
        print(f"Error adding cookie: {cookie}. Error: {e}")

# Refresh the page to apply the cookies
driver.refresh()

# Close the browser session
driver.quit()