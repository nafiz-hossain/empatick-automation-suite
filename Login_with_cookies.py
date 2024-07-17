from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import pickle

# Path to your Chrome WebDriver executable
webdriver_path = '/Users/Nafiz/Documents/Projects/automate-empatic/chromedriver'

# Path to your custom Chrome profile directory
custom_profile_path = '/Users/Nafiz/Library/Application Support/Google/Chrome/custom_profile'

# Set up Chrome options
options = Options()
options.add_argument(f"user-data-dir={custom_profile_path}")  # Path to your custom profile

# Set up ChromeDriver service
service = Service(webdriver_path)

# Initialize the Chrome driver
driver = webdriver.Chrome(service=service, options=options)

# URL to navigate to
url = "https://portal.dev.empatick.com/dashboard"

# Load cookies from the file
with open("cookies.pkl", "rb") as file:
    cookies = pickle.load(file)

# Navigate to the URL
driver.get(url)

# Add cookies to the browser
for cookie in cookies:
    driver.add_cookie(cookie)

# Refresh the page to apply the cookies
driver.refresh()

# Close the browser session
driver.quit()