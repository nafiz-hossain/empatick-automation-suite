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

# Navigate to the URL
driver.get(url)

# Wait for 20 seconds to allow manual login
time.sleep(30)

# Get cookies
cookies = driver.get_cookies()
print(cookies)

# Save cookies to a file
with open("cookies.pkl", "wb") as file:
    pickle.dump(cookies, file)

# Close the browser session
driver.quit()