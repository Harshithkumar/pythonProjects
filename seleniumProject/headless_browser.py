import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def open_browser():
    options = Options()

    # Strictly required for macOS + Jenkins
    options.add_argument("--headless=new")         # 100% REQUIRED in Jenkins
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--window-size=1920,1080")

    # Avoid automation banners
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    # Create driver through webdriver-manager
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    try:
        driver.get("https://www.browserstack.com/")
        print("Opened BrowserStack")

        wait = WebDriverWait(driver, 20)

        ai_agents_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="primary-menu-container"]/div[1]/div[4]/a/span')
        ))
        ai_agents_btn.click()
        print("Clicked 'AI Agents btn'")

        pricing_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="primary-menu-container"]/div[1]/div[5]/a/span')
        ))
        pricing_btn.click()
        print("Clicked 'Pricing Button'")

        time.sleep(5)

    except Exception as e:
        print("ERROR:", e)
    finally:
        driver.quit()


if __name__ == "__main__":
    open_browser()
