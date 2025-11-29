import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def open_browser():
    # ─────────────────────── CHROME OPTIONS (CRITICAL) ───────────────────────
    options = Options()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    # Optional: run headful (visible) or headless
    # options.add_argument("--headless=new")   # ← uncomment only when ready

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(
            "https://www.browserstack.com/")
        print("Opened browser Stack")

        wait = WebDriverWait(driver, 20)

        # 1. Click "Explore this book" button
        ai_agents_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="primary-menu-container"]/div[1]/div[4]/a/span')
        ))
        time.sleep(1)
        ai_agents_btn.click()
        print("Clicked 'AI Agents btn'")

        # 2. Click "Buy on Amazon" (this opens in new tab!)
        pricing_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="primary-menu-container"]/div[1]/div[5]/a/span')
        ))
        time.sleep(1)

        # Important: This link opens a NEW TAB → we must switch to it
        pricing_btn.click()
        print("Clicked 'Pricing Button'")
        time.sleep(10)

    except Exception as e:
        print("ERROR:", e)
        input("Press Enter to close...")

# ─────────────────────── RUN ───────────────────────
if __name__ == "__main__":
    open_browser()