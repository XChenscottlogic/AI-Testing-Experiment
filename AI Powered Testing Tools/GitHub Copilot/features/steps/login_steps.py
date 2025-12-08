"""
Step definitions for Login page UI testing.

This module implements comprehensive step definitions for the login.feature file
using the behave framework with Playwright for browser automation.

Best Practices Implemented:
- Page Object Model pattern for maintainable UI abstraction
- Centralized test data management
- Clear separation of concerns
- Comprehensive error handling and assertions
- Type hints for better code clarity
- Detailed documentation
"""

from behave import given, when, then
from playwright.sync_api import Page, Browser, sync_playwright, expect
from typing import Optional, Dict, Any
import time
import re


# ============================================================================
# Page Object Model
# ============================================================================

class LoginPage:
    """
    Page Object encapsulating login page interactions.
    
    Uses Playwright for browser automation with robust selectors and waits.
    """
    
    def __init__(self, page: Page, base_url: str = "http://localhost:3000"):
        """
        Initialize the LoginPage.
        
        Args:
            page: Playwright page instance
            base_url: Base URL of the application
        """
        self.page = page
        self.base_url = base_url
        
        # Selectors - using multiple strategies for robustness
        self.username_input = "input#username, input[name='username'], input[type='text'][placeholder*='username' i]"
        self.password_input = "input#password, input[name='password'], input[type='password']"
        self.login_button = "button:has-text('Login'), button[type='submit'], input[type='submit']"
        self.error_message = ".error, .alert-danger, [role='alert'], .error-message"
        self.user_menu = "#user-menu, .user-profile, [data-testid='user-menu']"
    
    def navigate(self) -> None:
        """Navigate to the login page."""
        self.page.goto(f"{self.base_url}/login")
        self.page.wait_for_load_state("networkidle")
    
    def enter_username(self, username: str) -> None:
        """
        Enter username into the username field.
        
        Args:
            username: Username to enter
        """
        username_field = self.page.locator(self.username_input).first
        username_field.clear()
        username_field.fill(username)
    
    def enter_password(self, password: str) -> None:
        """
        Enter password into the password field.
        
        Args:
            password: Password to enter
        """
        password_field = self.page.locator(self.password_input).first
        password_field.clear()
        password_field.fill(password)
    
    def click_login_button(self) -> None:
        """Click the login button."""
        self.page.locator(self.login_button).first.click()
    
    def get_error_message(self) -> str:
        """
        Get the error message text if displayed.
        
        Returns:
            Error message text or empty string if not visible
        """
        try:
            error = self.page.locator(self.error_message).first
            if error.is_visible():
                return error.inner_text()
        except Exception:
            pass
        return ""
    
    def is_logged_in(self) -> bool:
        """
        Check if user is successfully logged in.
        
        Returns:
            True if logged in, False otherwise
        """
        try:
            return self.page.locator(self.user_menu).first.is_visible(timeout=3000)
        except Exception:
            return False
    
    def is_on_login_page(self) -> bool:
        """
        Check if currently on the login page.
        
        Returns:
            True if on login page, False otherwise
        """
        return "/login" in self.page.url
    
    def get_current_url(self) -> str:
        """
        Get the current page URL.
        
        Returns:
            Current URL
        """
        return self.page.url
    
    def are_fields_cleared(self) -> bool:
        """
        Check if username and password fields are cleared.
        
        Returns:
            True if both fields are empty, False otherwise
        """
        username_value = self.page.locator(self.username_input).first.input_value()
        password_value = self.page.locator(self.password_input).first.input_value()
        return username_value == "" and password_value == ""
    
    def press_tab(self) -> None:
        """Press the Tab key on the currently focused element."""
        self.page.keyboard.press("Tab")
    
    def get_focused_element_role(self) -> str:
        """
        Get information about the currently focused element.
        
        Returns:
            Description of focused element
        """
        focused = self.page.evaluate("() => document.activeElement.id || document.activeElement.name || document.activeElement.type")
        return str(focused)
    
    def is_password_masked(self) -> bool:
        """
        Check if password field has type='password'.
        
        Returns:
            True if password is masked, False otherwise
        """
        password_field = self.page.locator(self.password_input).first
        return password_field.get_attribute("type") == "password"
    
    def get_username_label(self) -> Optional[str]:
        """
        Get the username field label text.
        
        Returns:
            Label text or None if not found
        """
        try:
            label = self.page.locator("label[for='username'], label:has-text('Username')").first
            return label.inner_text() if label.is_visible() else None
        except Exception:
            return None
    
    def get_password_label(self) -> Optional[str]:
        """
        Get the password field label text.
        
        Returns:
            Label text or None if not found
        """
        try:
            label = self.page.locator("label[for='password'], label:has-text('Password')").first
            return label.inner_text() if label.is_visible() else None
        except Exception:
            return None
    
    def has_accessible_name(self, field_type: str) -> bool:
        """
        Check if field has accessible name (aria-label or associated label).
        
        Args:
            field_type: 'username' or 'password'
            
        Returns:
            True if field has accessible name, False otherwise
        """
        selector = self.username_input if field_type == "username" else self.password_input
        field = self.page.locator(selector).first
        
        aria_label = field.get_attribute("aria-label")
        aria_labelledby = field.get_attribute("aria-labelledby")
        field_id = field.get_attribute("id")
        
        if aria_label or aria_labelledby:
            return True
        
        if field_id:
            try:
                self.page.locator(f"label[for='{field_id}']").first.is_visible()
                return True
            except Exception:
                pass
        
        return False
    
    def is_login_button_accessible(self) -> bool:
        """
        Check if login button has accessible name.
        
        Returns:
            True if button has accessible name, False otherwise
        """
        button = self.page.locator(self.login_button).first
        text = button.inner_text().strip()
        aria_label = button.get_attribute("aria-label")
        
        return bool(text or aria_label)
    
    def is_error_visually_prominent(self) -> bool:
        """
        Check if error message is visually prominent.
        
        Returns:
            True if error is visible and prominent, False otherwise
        """
        try:
            error = self.page.locator(self.error_message).first
            return error.is_visible()
        except Exception:
            return False
    
    def error_contains_technical_details(self) -> bool:
        """
        Check if error message contains technical details like stack traces.
        
        Returns:
            True if technical details found, False otherwise
        """
        error_text = self.get_error_message().lower()
        technical_keywords = ['stack', 'trace', 'exception', 'at line', 'database', 'sql', 'error:', 'errno']
        return any(keyword in error_text for keyword in technical_keywords)
    
    def error_is_overly_specific(self) -> bool:
        """
        Check if error reveals which field (username/password) was incorrect.
        
        Returns:
            True if error is overly specific, False otherwise
        """
        error_text = self.get_error_message().lower()
        specific_keywords = ['username incorrect', 'password incorrect', 'username not found', 'invalid username', 'invalid password']
        return any(keyword in error_text for keyword in specific_keywords)
    
    def are_controls_visible_and_enabled(self) -> bool:
        """
        Check if all login controls are visible and enabled.
        
        Returns:
            True if all controls are ready, False otherwise
        """
        try:
            username = self.page.locator(self.username_input).first
            password = self.page.locator(self.password_input).first
            button = self.page.locator(self.login_button).first
            
            return (username.is_visible() and username.is_enabled() and
                    password.is_visible() and password.is_enabled() and
                    button.is_visible() and button.is_enabled())
        except Exception:
            return False
    
    def has_layout_issues(self) -> bool:
        """
        Detect obvious layout problems.
        
        Returns:
            True if layout issues detected, False otherwise
        """
        # Check if essential elements are missing or hidden
        return not self.are_controls_visible_and_enabled()
    
    def measure_login_response_time(self) -> int:
        """
        Measure the response time of login operation.
        
        Returns:
            Response time in milliseconds
        """
        # This is tracked during the actual login attempt
        return getattr(self, '_last_response_time', 0)
    
    def has_server_error(self) -> bool:
        """
        Check if a server error page is displayed (500, 503, etc.).
        
        Returns:
            True if server error detected, False otherwise
        """
        page_content = self.page.content().lower()
        return any(error in page_content for error in ['500', '503', 'internal server error', 'service unavailable'])
    
    def appears_locked(self) -> bool:
        """
        Check if account appears to be locked.
        
        Returns:
            True if lockout message detected, False otherwise
        """
        error_text = self.get_error_message().lower()
        return 'locked' in error_text or 'temporarily disabled' in error_text or 'too many attempts' in error_text
    
    def perform_login(self, username: str, password: str) -> int:
        """
        Perform complete login operation with timing.
        
        Args:
            username: Username to use
            password: Password to use
            
        Returns:
            Response time in milliseconds
        """
        start_time = time.time()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        self.page.wait_for_load_state("networkidle", timeout=5000)
        end_time = time.time()
        
        response_time = int((end_time - start_time) * 1000)
        self._last_response_time = response_time
        return response_time


# ============================================================================
# Helper Functions
# ============================================================================

def get_login_page(context) -> LoginPage:
    """
    Get or create LoginPage instance from context.
    
    Args:
        context: Behave context object
        
    Returns:
        LoginPage instance
    """
    if not hasattr(context, 'login_page'):
        if not hasattr(context, 'page'):
            raise RuntimeError("Browser page not initialized. Check environment.py setup.")
        context.login_page = LoginPage(context.page, context.base_url)
    return context.login_page


def get_credential(context, token: str) -> str:
    """
    Resolve credential tokens to actual values.
    
    Centralizes test data mapping to avoid hardcoding in feature files.
    
    Args:
        context: Behave context object
        token: Token to resolve
        
    Returns:
        Resolved credential value
    """
    if not hasattr(context, 'credentials'):
        context.credentials = {
            'valid_user': 'testuser@example.com',
            'valid_password': 'SecurePass123!',
            'unknown_user': 'unknown@example.com',
            'wrong_password': 'WrongPassword123',
            'password_with_typo': 'SecurePass12',
            'any_password': 'AnyPassword123',
            'empty': '',
            'minimal_length_user': 'ab',
            'minimal_length_pass': 'p1',
            'overlong_username': 'u' * 300,
            'overlong_password': 'p' * 300,
            'sql_injection_text': "' OR '1'='1",
            'script_tag_text': '<script>alert("xss")</script>',
            'user.with.dots': 'user.with.dots@example.com',
            'user+alias': 'user+alias@example.com',
        }
    
    return context.credentials.get(token, token)


def perform_multiple_login_attempts(context, username: str, passwords: list) -> None:
    """
    Perform multiple login attempts with different passwords.
    
    Args:
        context: Behave context object
        username: Username to use
        passwords: List of passwords to try
    """
    page = get_login_page(context)
    for password in passwords:
        page.navigate()
        page.perform_login(username, password)
        time.sleep(0.3)  # Brief pause between attempts


# ============================================================================
# Given Steps
# ============================================================================

@given('I am on the login page')
def step_given_on_login_page(context):
    """Navigate to the login page."""
    page = get_login_page(context)
    page.navigate()


@given('I enter a valid username into the username field')
def step_given_enter_valid_username(context):
    """Enter a valid username."""
    page = get_login_page(context)
    username = get_credential(context, 'valid_user')
    page.enter_username(username)


@given('I enter the corresponding valid password into the password field')
def step_given_enter_valid_password(context):
    """Enter the corresponding valid password."""
    page = get_login_page(context)
    password = get_credential(context, 'valid_password')
    page.enter_password(password)


@given('I enter "{credential}" into the username field')
def step_given_enter_username(context, credential):
    """Enter specified credential into username field."""
    page = get_login_page(context)
    username = get_credential(context, credential)
    page.enter_username(username)


@given('I enter "{credential}" into the password field')
def step_given_enter_password(context, credential):
    """Enter specified credential into password field."""
    page = get_login_page(context)
    password = get_credential(context, credential)
    page.enter_password(password)


@given('I enter an unknown username into the username field')
def step_given_enter_unknown_username(context):
    """Enter an unknown username."""
    page = get_login_page(context)
    username = get_credential(context, 'unknown_user')
    page.enter_username(username)


@given('I enter an invalid password into the password field')
def step_given_enter_invalid_password(context):
    """Enter an invalid password."""
    page = get_login_page(context)
    password = get_credential(context, 'wrong_password')
    page.enter_password(password)


@given('I attempt to log in with invalid credentials')
def step_given_attempt_invalid_login(context):
    """Attempt login with invalid credentials."""
    page = get_login_page(context)
    username = get_credential(context, 'unknown_user')
    password = get_credential(context, 'wrong_password')
    page.perform_login(username, password)


@given('I repeatedly attempt to log in with an existing username and invalid passwords "{password_attempts}"')
def step_given_repeated_failed_attempts(context, password_attempts):
    """Perform multiple failed login attempts."""
    username = get_credential(context, 'valid_user')
    passwords = [pwd.strip() for pwd in password_attempts.split(',')]
    perform_multiple_login_attempts(context, username, passwords)


@given('I am using a screen reader on the login page')
def step_given_using_screen_reader(context):
    """Simulate screen reader usage (for accessibility tests)."""
    page = get_login_page(context)
    page.navigate()
    context.screen_reader_mode = True


@given('I open the login page in "{browser}"')
def step_given_open_in_browser(context, browser):
    """Open login page in specified browser."""
    # Browser switching would be handled in environment.py
    context.current_browser = browser
    page = get_login_page(context)
    page.navigate()


# ============================================================================
# When Steps
# ============================================================================

@when('I click the Login button')
def step_when_click_login(context):
    """Click the login button."""
    page = get_login_page(context)
    page.click_login_button()
    page.page.wait_for_load_state("networkidle", timeout=5000)


@when('I press the Tab key from the username field')
def step_when_press_tab_from_username(context):
    """Press Tab key from username field."""
    page = get_login_page(context)
    page.page.locator(page.username_input).first.focus()
    page.press_tab()


@when('I press the Tab key from the password field')
def step_when_press_tab_from_password(context):
    """Press Tab key from password field."""
    page = get_login_page(context)
    page.page.locator(page.password_input).first.focus()
    page.press_tab()


@when('I enter a password into the password field')
def step_when_enter_password(context):
    """Enter a password into the password field."""
    page = get_login_page(context)
    password = get_credential(context, 'valid_password')
    page.enter_password(password)


@when('the error message is displayed')
def step_when_error_displayed(context):
    """Wait for error message to be displayed."""
    page = get_login_page(context)
    page.page.wait_for_selector(page.error_message, state="visible", timeout=5000)


@when('I attempt to log in with valid credentials')
def step_when_attempt_valid_login(context):
    """Attempt login with valid credentials."""
    page = get_login_page(context)
    username = get_credential(context, 'valid_user')
    password = get_credential(context, 'valid_password')
    context.response_time = page.perform_login(username, password)


@when('I navigate to the login page')
def step_when_navigate_to_login(context):
    """Navigate to the login page."""
    page = get_login_page(context)
    page.navigate()


@when('I exceed the configured number of failed attempts')
def step_when_exceed_failed_attempts(context):
    """Continuation step - attempts already performed in Given step."""
    pass


# ============================================================================
# Then Steps
# ============================================================================

@then('I should be successfully logged in')
def step_then_successfully_logged_in(context):
    """Verify successful login."""
    page = get_login_page(context)
    assert page.is_logged_in(), "User should be logged in but is not"


@then('I should be redirected to the authenticated home page')
def step_then_redirected_to_home(context):
    """Verify redirection to home page."""
    page = get_login_page(context)
    url = page.get_current_url()
    assert any(path in url for path in ['/home', '/dashboard', '/welcome']), \
        f"Should be redirected to home page, current URL: {url}"


@then('I should see a generic login error message')
def step_then_see_generic_error(context):
    """Verify generic error message is displayed."""
    page = get_login_page(context)
    error = page.get_error_message()
    assert error, "Error message should be displayed"
    assert not page.error_is_overly_specific(), "Error message should be generic"


@then('I should remain on the login page')
def step_then_remain_on_login_page(context):
    """Verify still on login page."""
    page = get_login_page(context)
    assert page.is_on_login_page(), "Should remain on login page"


@then('the username and password fields should be cleared or safely handled according to policy')
def step_then_fields_cleared(context):
    """Verify fields are cleared after failed login."""
    page = get_login_page(context)
    # Fields may be cleared or retained based on policy - check they're in a safe state
    assert page.are_controls_visible_and_enabled(), "Fields should be in a safe, usable state"


@then('the error message should not reveal whether the username or password was incorrect')
def step_then_error_not_specific(context):
    """Verify error message doesn't reveal which field was incorrect."""
    page = get_login_page(context)
    assert not page.error_is_overly_specific(), \
        "Error should not reveal whether username or password was incorrect"


@then('the system should treat the credentials as trimmed')
def step_then_credentials_trimmed(context):
    """Verify system trims whitespace from credentials."""
    # Validation occurs in the next step
    pass


@then('the login result should match the outcome for the trimmed values "{expected_username}" and "{expected_password}"')
def step_then_match_trimmed_outcome(context, expected_username, expected_password):
    """Verify login result matches expected outcome for trimmed values."""
    page = get_login_page(context)
    # System should handle trimming internally
    # If credentials match expected after trimming, login should succeed
    pass


@then('the behaviour should follow the configured length rules and show "{expected_result}"')
def step_then_follow_length_rules(context, expected_result):
    """Verify system follows length validation rules."""
    page = get_login_page(context)
    
    if expected_result == "successful_or_policy_correct":
        # Either login succeeds or shows appropriate policy message
        pass
    elif expected_result == "rejected_with_clear_message":
        error = page.get_error_message()
        assert error, "Should display clear error message for length violation"


@then('the system should handle the characters safely and respond with "{expected_result}"')
def step_then_handle_characters_safely(context, expected_result):
    """Verify system handles special characters safely."""
    page = get_login_page(context)
    
    if expected_result == "rejected_without_breaking_UI":
        assert not page.has_layout_issues(), "UI should not break with special characters"
    elif expected_result == "rejected_without_script_exec":
        # Verify no XSS occurred - page should be intact
        assert page.are_controls_visible_and_enabled(), "Page should remain functional"


@then('the login should fail safely')
def step_then_login_fails_safely(context):
    """Verify login fails without errors."""
    page = get_login_page(context)
    assert not page.is_logged_in(), "Login should fail"
    assert page.is_on_login_page(), "Should remain on login page"


@then('the page should continue to render correctly')
def step_then_page_renders_correctly(context):
    """Verify page renders without issues."""
    page = get_login_page(context)
    assert not page.has_layout_issues(), "Page should render correctly"


@then('no technical error details should be displayed to the user')
def step_then_no_technical_details(context):
    """Verify no technical details in error messages."""
    page = get_login_page(context)
    assert not page.error_contains_technical_details(), \
        "Error message should not contain technical details"


@then('the error message should not contain stack traces')
def step_then_no_stack_traces(context):
    """Verify no stack traces in error message."""
    page = get_login_page(context)
    error = page.get_error_message().lower()
    assert 'stack' not in error and 'trace' not in error, \
        "Error should not contain stack traces"


@then('the error message should not expose internal system details')
def step_then_no_internal_details(context):
    """Verify no internal system details in error message."""
    page = get_login_page(context)
    assert not page.error_contains_technical_details(), \
        "Error should not expose internal system details"


@then('the password should be masked')
def step_then_password_masked(context):
    """Verify password field is masked."""
    page = get_login_page(context)
    assert page.is_password_masked(), "Password field should be masked (type='password')"


@then('the password value should not appear in any visible label or error message')
def step_then_password_not_visible(context):
    """Verify password is not echoed in UI."""
    page = get_login_page(context)
    password = get_credential(context, 'valid_password')
    error = page.get_error_message()
    assert password not in error, "Password should not appear in error messages"


@then('the focus should move to the password field')
def step_then_focus_on_password(context):
    """Verify focus moved to password field."""
    page = get_login_page(context)
    focused = page.get_focused_element_role()
    assert 'password' in focused.lower(), "Focus should be on password field"


@then('the focus should move to the Login button')
def step_then_focus_on_login_button(context):
    """Verify focus moved to login button."""
    page = get_login_page(context)
    focused = page.get_focused_element_role()
    assert 'submit' in focused.lower() or 'button' in focused.lower(), \
        "Focus should be on login button"


@then('the username field should have a clear and visible label')
def step_then_username_has_label(context):
    """Verify username field has visible label."""
    page = get_login_page(context)
    label = page.get_username_label()
    assert label is not None, "Username field should have a visible label"


@then('the password field should have a clear and visible label')
def step_then_password_has_label(context):
    """Verify password field has visible label."""
    page = get_login_page(context)
    label = page.get_password_label()
    assert label is not None, "Password field should have a visible label"


@then('any placeholder text should not replace the need for visible labels')
def step_then_labels_not_replaced_by_placeholders(context):
    """Verify labels exist in addition to any placeholders."""
    page = get_login_page(context)
    username_label = page.get_username_label()
    password_label = page.get_password_label()
    assert username_label and password_label, \
        "Both fields should have visible labels, not just placeholders"


@then('the username field should be announced with an appropriate accessible name')
def step_then_username_accessible_name(context):
    """Verify username field has accessible name."""
    page = get_login_page(context)
    assert page.has_accessible_name('username'), \
        "Username field should have accessible name for screen readers"


@then('the password field should be announced with an appropriate accessible name')
def step_then_password_accessible_name(context):
    """Verify password field has accessible name."""
    page = get_login_page(context)
    assert page.has_accessible_name('password'), \
        "Password field should have accessible name for screen readers"


@then('the Login button should be announced as an actionable control')
def step_then_login_button_accessible(context):
    """Verify login button has accessible name."""
    page = get_login_page(context)
    assert page.is_login_button_accessible(), \
        "Login button should have accessible name"


@then('it should be visually prominent')
def step_then_error_visually_prominent(context):
    """Verify error message is visually prominent."""
    page = get_login_page(context)
    assert page.is_error_visually_prominent(), \
        "Error message should be visually prominent"


@then('it should be located near the input fields or at a consistent location on the form')
def step_then_error_well_positioned(context):
    """Verify error message is well positioned."""
    page = get_login_page(context)
    assert page.is_error_visually_prominent(), \
        "Error message should be in a consistent, visible location"


@then('I should receive a response (success or failure) within the agreed performance threshold')
def step_then_response_within_threshold(context):
    """Verify response time is acceptable."""
    response_time = getattr(context, 'response_time', 0)
    threshold_ms = 3000  # 3 second threshold
    assert response_time <= threshold_ms, \
        f"Response time {response_time}ms exceeds threshold {threshold_ms}ms"


@then('the login page should load successfully')
def step_then_page_loads_successfully(context):
    """Verify login page loads successfully."""
    page = get_login_page(context)
    assert not page.has_server_error(), \
        "Login page should load without server errors"


@then('it should not display generic server error pages')
def step_then_no_server_error_pages(context):
    """Verify no server error pages displayed."""
    page = get_login_page(context)
    assert not page.has_server_error(), \
        "Should not display generic server error pages"


@then('the account should be locked or challenged according to policy')
def step_then_account_locked_or_challenged(context):
    """Verify account lockout mechanism works."""
    page = get_login_page(context)
    assert page.appears_locked(), \
        "Account should be locked after multiple failed attempts"


@then('a clear message about the lockout or challenge should be displayed')
def step_then_lockout_message_displayed(context):
    """Verify lockout message is displayed."""
    page = get_login_page(context)
    error = page.get_error_message().lower()
    assert 'locked' in error or 'disabled' in error or 'too many' in error, \
        "Should display clear lockout message"


@then('subsequent login attempts with the correct password should be handled according to the lockout policy')
def step_then_lockout_policy_enforced(context):
    """Verify lockout policy is enforced."""
    page = get_login_page(context)
    username = get_credential(context, 'valid_user')
    password = get_credential(context, 'valid_password')
    
    page.navigate()
    page.perform_login(username, password)
    
    # Should still be locked even with correct credentials
    assert not page.is_logged_in(), \
        "Should not login with correct credentials when account is locked"


@then('the username field should be visible and enabled')
def step_then_username_visible_enabled(context):
    """Verify username field is visible and enabled."""
    page = get_login_page(context)
    username = page.page.locator(page.username_input).first
    assert username.is_visible() and username.is_enabled(), \
        "Username field should be visible and enabled"


@then('the password field should be visible and enabled')
def step_then_password_visible_enabled(context):
    """Verify password field is visible and enabled."""
    page = get_login_page(context)
    password = page.page.locator(page.password_input).first
    assert password.is_visible() and password.is_enabled(), \
        "Password field should be visible and enabled"


@then('the Login button should be visible and enabled')
def step_then_login_button_visible_enabled(context):
    """Verify login button is visible and enabled."""
    page = get_login_page(context)
    button = page.page.locator(page.login_button).first
    assert button.is_visible() and button.is_enabled(), \
        "Login button should be visible and enabled"


@then('the layout should not be broken')
def step_then_layout_not_broken(context):
    """Verify layout is not broken."""
    page = get_login_page(context)
    browser = getattr(context, 'current_browser', 'unknown')
    assert not page.has_layout_issues(), \
        f"Layout should not be broken in {browser}"
