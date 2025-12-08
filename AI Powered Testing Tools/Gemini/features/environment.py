# features/environment.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def before_all(context):
    """Setup the WebDriver instance before all tests."""
    chrome_options = Options()
    # Uncomment the line below if you want to run headlessly (without a visible browser UI)
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Assuming ChromeDriver is in your PATH or specified here
    context.browser = webdriver.Chrome(options=chrome_options)
    context.browser.implicitly_wait(10) # Wait up to 10 seconds for elements to appear
    context.base_url = "http://your-app-domain.com/login" # IMPORTANT: Change this

def after_all(context):
    """Quit the WebDriver instance after all tests."""
    context.browser.quit()

def before_scenario(context, scenario):
    """Set up scenario data or state if needed."""
    context.current_user = None # Placeholder for logged-in user state

def after_scenario(context, scenario):
    """Clear cookies or reset state after each scenario."""
    context.browser.delete_all_cookies()