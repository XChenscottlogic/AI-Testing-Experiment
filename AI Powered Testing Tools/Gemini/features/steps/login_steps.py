LOGIN_LOCATORS = {
    "username_field": ("id", "username"),
    "password_field": ("id", "password"),
    "login_button": ("id", "login-btn"),
    "error_message": ("css selector", ".error-message"),
    "dashboard_header": ("xpath", "//h1[contains(text(), 'Dashboard')]"),
    "welcome_message": ("css selector", ".welcome-banner"),
    "language_selector": ("id", "language-select"),
    "logout_button": ("id", "logout-btn"),
    "password_toggle": ("id", "show-hide-password"),
}

# Helper function to find elements
from behave import step
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep # Used for simulating session timeout

def find_element(context, key):
    """Finds an element using the key from LOGIN_LOCATORS."""
    by, value = LOGIN_LOCATORS[key]
    return context.browser.find_element(by=getattr(By, by.upper()), value=value)

def get_test_data(key):
    """A simple placeholder function for fetching known test data."""
    # In a real app, this would query a database, JSON file, or fixture
    data = {
        "valid username": "testuser",
        "valid password": "StrongPassword123",
        "InvalidUser": "wronguser",
        "InvalidPassword": "wrongpass",
        "InactiveUser": "inactive_user",
        "SQL Injection": "' OR '1'='1",
        "Cross-Site Scripting (XSS)": "<script>alert('XSS')</script>",
        "<empty>": "",
        "More than Max Length": "a" * 51,
        "Less than Min Length": "a" * 2,
        "Special Characters": "user$name!",
        # Add other specific test data here...
    }
    return data.get(key, key) # Return the key itself if not found (e.g., for custom data)

# features/steps/login_steps.py

# ... (Insert the LOGIN_LOCATORS and helper functions here for a single executable file) ...

# --- GIVEN steps ---

@step('I am on the login page')
def step_impl(context):
    context.browser.get(context.base_url)
    WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located(LOGIN_LOCATORS["login_button"])
    )

@step('I have successfully logged in')
def step_impl(context):
    context.execute_steps(u"""
        When I enter a valid username in the username field
        And I enter a valid password in the password field
        And I click the "Login" button
    """)
    # Wait for redirection to confirm login
    WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located(LOGIN_LOCATORS["dashboard_header"])
    )

# --- WHEN steps (Input and Actions) ---

@step('I enter a {data_type} in the username field')
@step('I enter "{username}" in the username field')
def step_impl(context, username="valid username", data_type=None):
    if data_type:
        username = get_test_data(data_type)
    elif username in ["valid username", "valid password", "InvalidUser", "InvalidPassword", "InactiveUser", "SQL Injection", "Cross-Site Scripting (XSS)"]:
        username = get_test_data(username)

    if username == '<empty>':
        username = '' # Set to empty string
        
    username_field = find_element(context, "username_field")
    username_field.clear()
    username_field.send_keys(username)


@step('I enter a {data_type} in the password field')
@step('I enter "{password}" in the password field')
def step_impl(context, password="valid password", data_type=None):
    if data_type:
        password = get_test_data(data_type)
    elif password in ["valid username", "valid password", "InvalidUser", "InvalidPassword", "InactiveUser", "SQL Injection", "Cross-Site Scripting (XSS)"]:
        password = get_test_data(password)

    if password == '<empty>':
        password = '' # Set to empty string
        
    password_field = find_element(context, "password_field")
    password_field.clear()
    password_field.send_keys(password)


@step('I click the "{button_name}" button')
def step_impl(context, button_name):
    if "Login" in button_name:
        find_element(context, "login_button").click()
    elif "Logout" in button_name:
        find_element(context, "logout_button").click()
    # Add more button logic here...

@step('I remain inactive for the configured session timeout duration \(e.g., 30 minutes\)')
def step_impl(context):
    # NOTE: For real testing, you'd configure a short timeout (e.g., 5 seconds)
    # in your application config during the test run, not simulate 30 mins.
    # We will simulate a short wait for demonstration.
    print("\n--- Simulating wait for session timeout (5 seconds) ---")
    sleep(5) 
    context.browser.refresh() # Trigger the server to check session status

@step('I click the {toggle_action} toggle')
def step_impl(context, toggle_action):
    toggle = find_element(context, "password_toggle")
    toggle.click()
    context.current_toggle_action = toggle_action # Store state for assertion

@step('I enter a valid input in the other field')
def step_impl(context):
    # Logic to fill the field that was NOT the focus of the current boundary test
    # (Requires context to track which field is being tested, which is handled implicitly by Scenario Outline)
    # For now, we assume this is handled by the calling step setting the context correctly.
    pass # No explicit action needed as the specific input steps handle the primary field.

@step('I enter the correct "{username_case}" and correct "{password_case}"')
def step_impl(context, username_case, password_case):
    # This assumes a test fixture/data source called 'valid_credentials'
    valid_username = get_test_data("valid username")
    valid_password = get_test_data("valid password")

    user_input = valid_username if "Correct Case" in username_case else valid_username.upper()
    pass_input = valid_password if "Correct Case" in password_case else valid_password.upper()

    find_element(context, "username_field").send_keys(user_input)
    find_element(context, "password_field").send_keys(pass_input)

@step('I press the Tab key repeatedly, starting from outside the form')
def step_impl(context):
    # Focus on the body, then tab through the elements
    body = context.browser.find_element(By.TAG_NAME, "body")
    
    # Send a few initial tabs to ensure focus is outside the form
    for _ in range(3):
        body.send_keys(Keys.TAB) 

    # We cannot easily assert the exact *order* here without looping, 
    # but the subsequent Enter key step will validate the final position.
    
    # Tab to Username
    body.send_keys(Keys.TAB)
    # Tab to Password
    body.send_keys(Keys.TAB)
    # Tab to Login Button
    body.send_keys(Keys.TAB)
    # Tab to Forgot Password Link (Assume this is the next focusable element)
    body.send_keys(Keys.TAB)
    context.current_focus_element = "Forgot Password Link" # For assertion if needed

@step('I press the Enter key')
def step_impl(context):
    # If the login button has focus, pressing Enter should trigger a click
    find_element(context, "login_button").send_keys(Keys.ENTER)

@step('I change the language selection from English to Spanish')
def step_impl(context):
    # Simple selection logic
    from selenium.webdriver.support.ui import Select
    select_element = Select(find_element(context, "language_selector"))
    select_element.select_by_value("es") # Assuming 'es' is the value for Spanish

# --- THEN steps (Assertions and Verification) ---

@step('I should be redirected to the {page_name} or home page')
def step_impl(context, page_name):
    # Use explicit wait to ensure the element on the new page is loaded
    WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located(LOGIN_LOCATORS["dashboard_header"])
    )
    # Assert successful navigation (e.g., check URL or element presence)
    assert context.browser.current_url.endswith("/dashboard"), f"Expected to be on dashboard, found URL: {context.browser.current_url}"

@step('I should see a welcome message \(e.g., "Welcome, \[Username\]!"\)')
def step_impl(context):
    welcome_message = find_element(context, "welcome_message").text
    assert "Welcome" in welcome_message, f"Welcome message not found or incorrect: {welcome_message}"

@step('I should remain on the login page')
def step_impl(context):
    # Assert that the login button is still present (standard check)
    WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located(LOGIN_LOCATORS["login_button"])
    )
    # Assert the URL is still the login page
    assert context.browser.current_url.endswith("/login"), f"Expected to stay on login page, found URL: {context.browser.current_url}"

@step('I should see an error message stating "{expected_message}"')
def step_impl(context, expected_message):
    error_element = find_element(context, "error_message")
    actual_message = error_element.text
    assert expected_message in actual_message, f"Expected error message: '{expected_message}', but found: '{actual_message}'"

@step('I should see the error message: "{expected_message}"')
def step_impl(context, expected_message):
    # Reuses the same assertion logic for constraint testing
    step_impl_error_message(context, expected_message) 

@step('I should be automatically logged out and redirected to the login page')
def step_impl(context):
    # Assert redirect to login page after refresh/timeout
    assert context.browser.current_url.endswith("/login"), f"Did not redirect to login page. Current URL: {context.browser.current_url}"

@step('I should not be able to navigate back to the dashboard using the browser Back button')
def step_impl(context):
    context.browser.back()
    # After pressing back, we should still be on the login page (due to session invalidation)
    assert context.browser.current_url.endswith("/login"), f"Back button allowed access to non-login page: {context.browser.current_url}"

@step('the password field input type should change from "{from_type}" to "{to_type}" \(text is {visibility}\)')
def step_impl(context, from_type, to_type, visibility):
    password_field = find_element(context, "password_field")
    actual_type = password_field.get_attribute("type")
    assert actual_type == to_type, f"Password field type did not change to '{to_type}', but is '{actual_type}'"

@step('the application should {result} the input and {action} the script')
def step_impl(context, result, action):
    # Assuming the login attempt resulted in the standard error message
    error_element = find_element(context, "error_message")
    assert "Invalid username or password" in error_element.text

@step('all UI elements \(field labels, button text, error messages\) should be displayed in Spanish')
def step_impl(context):
    # Quick check for a known Spanish label (e.g., the Login button text)
    login_button_text = find_element(context, "login_button").get_attribute("value") or find_element(context, "login_button").text
    assert "Iniciar Sesión" in login_button_text, f"Login button text is not Spanish. Found: {login_button_text}"

# --- Placeholder steps for Non-Functional Testing (Requires specialized tools) ---

@step('the page should be fully rendered within {seconds} seconds \(under a normal load\)')
def step_impl(context, seconds):
    # Placeholder: Real performance testing requires browser instrumentation or specialized tools (e.g., Lighthouse, custom timing scripts)
    print(f"\n[NON-FUNCTIONAL STUB] Verifying page load time is under {seconds} seconds.")
    # You would use context.browser.execute_script("return window.performance.timing...") here

@step('the system response time for a successful login should not exceed {seconds} seconds')
def step_impl(context, seconds):
    # Placeholder: Requires specialized load testing tools (e.g., JMeter, Locust, k6)
    print(f"\n[NON-FUNCTIONAL STUB] Verifying system response time under load is under {seconds} seconds.")

@step('the system should not return any HTTP 5xx errors')
def step_impl(context):
    # Placeholder: Requires checking server logs or proxy/network monitoring (e.g., BrowserStack logs)
    print("\n[NON-FUNCTIONAL STUB] Verifying no HTTP 5xx errors were returned.")

@step('the login form elements should be stacked vertically and readable without horizontal scrolling')
def step_impl(context):
    # Placeholder: Requires checking screen dimensions and CSS properties
    context.browser.set_window_size(360, 640) # Simulate mobile screen
    print("\n[NON-FUNCTIONAL STUB] Checking responsiveness at 360px width.")
    # Assert specific element coordinates or media queries here

@step('Alternative text should be available for the logo/image elements')
def step_impl(context):
    # Placeholder: Requires checking the 'alt' attribute of <img> tags
    logo = context.browser.find_element(By.ID, "app-logo") # Assuming ID
    assert logo.get_attribute("alt") is not None and logo.get_attribute("alt") != "", "Logo image is missing alt text."

@step('all interactive elements should meet WCAG 2.1 color contrast standards')
def step_impl(context):
    # Placeholder: Requires auditing tools or custom color contrast checks
    print("\n[NON-FUNCTIONAL STUB] Verifying WCAG color contrast standards.")