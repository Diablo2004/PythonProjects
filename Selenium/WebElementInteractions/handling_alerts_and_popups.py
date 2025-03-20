from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Setup ChromeDriver
try:
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    wait = WebDriverWait(driver, 10)
    print("Browser launched successfully.")
except Exception as e:
    print(f"Error setting up WebDriver: {e}")
    exit()

def handle_alert(action="accept", text=None):
    """Handles JavaScript alerts with optional text input."""
    try:
        alert = wait.until(EC.alert_is_present())
        if text:
            alert.send_keys(text)  # Send input text if provided
        print(f"Alert Text: {alert.text}")
        if action == "accept":
            alert.accept()
        else:
            alert.dismiss()
    except Exception as e:
        print(f"Error handling alert: {e}")

# Handling a simple alert
try:
    button_alert = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Click for JS Alert']")))
    button_alert.click()
    handle_alert()
except Exception as e:
    print(f"Error handling simple alert: {e}")

# Handling a confirmation alert (OK/Cancel)
try:
    button_confirm = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Click for JS Confirm']")))
    button_confirm.click()
    handle_alert(action="dismiss")  # Click 'Cancel'
except Exception as e:
    print(f"Error handling confirmation alert: {e}")

# Handling a prompt alert (Input required)
try:
    button_prompt = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Click for JS Prompt']")))
    button_prompt.click()
    handle_alert(action="accept", text="Selenium Test")
except Exception as e:
    print(f"Error handling prompt alert: {e}")

# Close browser
try:
    driver.quit()
    print("Browser closed successfully.")
except Exception as e:
    print(f"Error closing browser: {e}")
