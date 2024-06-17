from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import sys

def check_element_presence(url, element_id):
    try:
        # Set up Chrome options for headless mode
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")  # Applicable only if you have GPU installed
        chrome_options.add_argument("--window-size=1920,1080")  # Optional, can adjust as needed
        # Set up the WebDriver with the correct path to the ChromeDriver executable
        service = Service('chromedriver')  # Specify the correct path
        driver = webdriver.Chrome(service=service, options=chrome_options)
        # Navigate to the web page
        driver.get(url)
        time.sleep(5)  # Wait for the page to load
        # Check if the element with the specified ID is present
        try:
            element = driver.find_element(By.ID, element_id)
            if element:
                print(f"Element with ID '{element_id}' is present on the page.")
                return True
        except Exception as e:
            print(f"Element with ID '{element_id}' is not present on the page.")
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    finally:
        driver.quit()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python web_status_checker.py <url> <element_id>")
        sys.exit(1)

    url = sys.argv[1]
    element_id = sys.argv[2]
    check_interval = 60  # Check every 60 seconds
    previous_state = None

    while True:
        current_state = check_element_presence(url, element_id)
        if current_state != previous_state:
            if current_state:
                print(f"The web app at {url} is running. Element with ID '{element_id}' is present.")
            else:
                print(f"The web app at {url} is not running. Element with ID '{element_id}' is not present.")
            previous_state = current_state
        time.sleep(check_interval)
