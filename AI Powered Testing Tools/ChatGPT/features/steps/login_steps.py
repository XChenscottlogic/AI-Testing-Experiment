# steps/login_steps.py
#
# Step definitions for "Login page UI for username and password"
# Framework: behave
#
# Good practices:
# - Use Page Object pattern to encapsulate UI interactions
# - Keep step functions thin and delegate to helper/page methods
# - Reuse generic steps with parameters instead of duplicating logic
# - Centralise test data mapping (e.g., valid/invalid credentials)
#

from behave import given, when, then
from dataclasses import dataclass
from typing import Optional


# ---------------------------
# Page Object (UI abstraction)
# ---------------------------

@dataclass
class LoginPage:
    """Page object representing the login page.

    NOTE:
        Replace all `pass` and pseudo-code with real Selenium/Playwright
        calls and proper locators.
    """

    def open(self):
        """Navigate to the login page."""
        # Example (Selenium):
        # self.driver.get(self.base_url + "/login")
        pass

    def enter_username(self, value: str):
        """Enter text into the username field."""
        # e.g. self.driver.find_element(...).clear(); .send_keys(value)
        pass

    def enter_password(self, value: str):
        """Enter text into the password field."""
        pass

    def click_login(self):
        """Click on the Login button."""
        pass

    def get_error_message_text(self) -> str:
        """Return error message text (if visible)."""
        return ""

    def is_logged_in(self) -> bool:
        """Return True if user is considered logged in."""
        return False

    def is_on_login_page(self) -> bool:
        """Return True if current page is the login page."""
        return True

    def get_current_url(self) -> str:
        """Return current URL for redirection checks."""
        return ""

    def get_focused_element_label(self) -> Optional[str]:
        """Return a description of the currently focused element.

        Used for tab-order and accessibility-style checks.
        """
        return None

    def password_is_masked(self) -> bool:
        """Return True if the password field is masked."""
        return True

    def controls_are_visible_and_enabled(self) -> bool:
        """Return True if username, password and login controls are OK."""
        return True

    def get_browser_name(self) -> str:
        """Return current browser name (for cross-browser tests)."""
        return "Unknown"

    def has_layout_issues(self) -> bool:
        """Return True if layout is obviously broken."""
        return False

    def get_login_response_time_ms(self) -> int:
        """Return measured response time in milliseconds for last login."""
        return 0

    def error_message_reveals_internal_details(self) -> bool:
        """Detect if error reveals stack traces or internal details."""
        return False

    def error_message_is_overly_specific(self) -> bool:
        """Detect if error message reveals which field is wrong."""
        return False

    def is_account_locked(self, username: str) -> bool:
        """Return True if account appears locked."""
        return False

    def has_generic_server_error(self) -> bool:
        """Return True if generic server error page is visible."""
        return False

    def username_label_is_visible(self) -> bool:
        return True

    def password_label_is_visible(self) -> bool:
        return True

    def login_button_has_accessible_name(self) -> bool:
        return True

    def field_has_accessible_name(self, field: str) -> bool:
        return True


# ---------------------------
# Hooks / helpers
# ---------------------------

def _ensure_login_page(context):
    """Lazy-initialize the login page object in context."""
    if not hasattr(context, "login_page"):
        # In real code, you would inject driver/base_url here
        context.login_page = LoginPage()
    return context.login_page


def _resolve_credential_token(context, token: str, field: str) -> str:
    """Resolve special tokens like 'valid_user', 'empty', etc. into real values.

    This avoids hard-coding secrets in the feature file and centralises mapping.
    """
    if not hasattr(context, "test_credentials"):
        context.test_credentials = {
            "valid_user": "valid.user@example.com",
            "valid_password": "CorrectHorseBatteryStaple123!",
            "unknown_user": "unknown.user@example.com",
            "any_password": "somePassword123",
            "password_with_typo": "CorrectHorseBatteryStapl3",
            "sql_injection_text": "' OR '1'='1",
            "script_tag_text": "<script>alert('x')</script>",
            "minimal_length_user": "u1",        # adjust in real project
            "minimal_length_pass": "p1",        # adjust in real project
            "overlong_username": "u" * 300,
            "overlong_password": "p" * 300,
        }

    if token == "empty":
        return ""
    if token in context.test_credentials:
        return context.test_credentials[token]
    # Fallback: treat literal as actual value without quotes
    return token.strip('"')


# ---------------------------
# Step Definitions
# ---------------------------

# 1. Basic navigation and input


@given("I am on the login page")
def step_given_on_login_page(context):
    page = _ensure_login_page(context)
    page.open()
    assert page.is_on_login_page(), "User is not on the login page"


@when('I enter a valid username into the username field')
@given('I enter a valid username into the username field')
def step_enter_valid_username(context):
    page = _ensure_login_page(context)
    username = _resolve_credential_token(context, "valid_user", "username")
    page.enter_username(username)


@when('I enter the corresponding valid password into the password field')
@given('I enter the corresponding valid password into the password field')
def step_enter_valid_password(context):
    page = _ensure_login_page(context)
    password = _resolve_credential_token(context, "valid_password", "password")
    page.enter_password(password)


@when('I enter "{value}" into the username field')
@given('I enter "{value}" into the username field')
def step_enter_username_param(context, value):
    page = _ensure_login_page(context)
    resolved = _resolve_credential_token(context, value, "username")
    page.enter_username(resolved)


@when('I enter "{value}" into the password field')
@given('I enter "{value}" into the password field')
def step_enter_password_param(context, value):
    page = _ensure_login_page(context)
    resolved = _resolve_credential_token(context, value, "password")
    page.enter_password(resolved)


@when("I click the Login button")
def step_click_login_button(context):
    page = _ensure_login_page(context)
    page.click_login()


# 2. Outcomes and assertions


@then("I should be successfully logged in")
def step_should_be_logged_in(context):
    page = _ensure_login_page(context)
    assert page.is_logged_in(), "User is not logged in"


@then("I should be redirected to the authenticated home page")
def step_redirected_to_home(context):
    page = _ensure_login_page(context)
    # Replace with real check (e.g. URL or element)
    url = page.get_current_url()
    assert "home" in url or "dashboard" in url, (
        f"Unexpected post-login URL: {url}"
    )


@then("I should see a generic login error message")
def step_generic_error_message(context):
    page = _ensure_login_page(context)
    msg = page.get_error_message_text()
    assert msg, "No error message was displayed"
    assert not page.error_message_reveals_internal_details(), (
        "Error message reveals internal details"
    )


@then("I should remain on the login page")
def step_should_remain_on_login(context):
    page = _ensure_login_page(context)
    assert page.is_on_login_page(), "User did not remain on login page"


@then("the username and password fields should be cleared or safely handled according to policy")
def step_fields_cleared_or_safe(context):
    # In real code, inspect the field values or security policy.
    # For now, treat as a placeholder assertion.
    pass


@then("the error message should not reveal whether the username or password was incorrect")
def step_error_not_specific(context):
    page = _ensure_login_page(context)
    assert not page.error_message_is_overly_specific(), (
        "Error message is overly specific"
    )


@then("the system should treat the credentials as trimmed")
def step_credentials_trimmed(context):
    # This is a behavioural guarantee; in a real test you would compare
    # behaviour against known good/bad credentials trimmed vs. untrimmed.
    pass


@then('the login result should match the outcome for the trimmed values "{expected_username}" and "{expected_password}"')
def step_login_result_matches_trimmed(context, expected_username, expected_password):
    # Placeholder; in practice you'd validate that trimming does not change
    # outcome relative to the expected credentials.
    pass


@then('the behaviour should follow the configured length rules and show "{expected_result}"')
def step_length_rules(context, expected_result):
    # Implementation depends on specific length rules.
    pass


@then('the system should handle the characters safely and respond with "{expected_result}"')
def step_special_characters(context, expected_result):
    # Check that UI did not break and no security issues surfaced.
    pass


@then("the login should fail safely")
def step_login_fails_safely(context):
    page = _ensure_login_page(context)
    msg = page.get_error_message_text()
    assert msg, "Expected error message for failed login"
    assert not page.has_generic_server_error(), "Got a server error page"


@then("the page should continue to render correctly")
def step_page_renders_correctly(context):
    page = _ensure_login_page(context)
    assert not page.has_layout_issues(), "Layout appears broken after login attempt"


@then("no technical error details should be displayed to the user")
def step_no_technical_details(context):
    page = _ensure_login_page(context)
    assert not page.error_message_reveals_internal_details(), (
        "Technical details are visible to the user"
    )


@then("the password should be masked")
def step_password_masked(context):
    page = _ensure_login_page(context)
    assert page.password_is_masked(), "Password field is not masked"


@then("the password value should not appear in any visible label or error message")
def step_password_not_echoed(context):
    page = _ensure_login_page(context)
    msg = page.get_error_message_text()
    # In real code, you'd compare against the last entered password
    assert "CorrectHorseBatteryStaple" not in msg, (
        "Password appears in error message (example check)"
    )


# 3. Usability & accessibility


@when("I press the Tab key from the username field")
def step_tab_from_username(context):
    # Real implementation would simulate keypress
    pass


@then("the focus should move to the password field")
def step_focus_password(context):
    page = _ensure_login_page(context)
    focused = page.get_focused_element_label()
    assert focused == "password", f"Expected focus on password field, got {focused}"


@when("I press the Tab key from the password field")
def step_tab_from_password(context):
    # Real implementation would simulate keypress
    pass


@then("the focus should move to the Login button")
def step_focus_login_button(context):
    page = _ensure_login_page(context)
    focused = page.get_focused_element_label()
    assert focused == "login_button", f"Expected focus on Login button, got {focused}"


@then("the username field should have a clear and visible label")
def step_username_label_visible(context):
    page = _ensure_login_page(context)
    assert page.username_label_is_visible(), "Username label is not visible"


@then("the password field should have a clear and visible label")
def step_password_label_visible(context):
    page = _ensure_login_page(context)
    assert page.password_label_is_visible(), "Password label is not visible"


@given("I am using a screen reader on the login page")
def step_using_screen_reader(context):
    # This would rely on accessibility tooling; placeholder for now.
    pass


@then("the username field should be announced with an appropriate accessible name")
def step_username_accessible_name(context):
    page = _ensure_login_page(context)
    assert page.field_has_accessible_name("username"), (
        "Username field lacks an accessible name"
    )


@then("the password field should be announced with an appropriate accessible name")
def step_password_accessible_name(context):
    page = _ensure_login_page(context)
    assert page.field_has_accessible_name("password"), (
        "Password field lacks an accessible name"
    )


@then("the Login button should be announced as an actionable control")
def step_login_button_accessible(context):
    page = _ensure_login_page(context)
    assert page.login_button_has_accessible_name(), (
        "Login button lacks an accessible name"
    )


@then("it should be visually prominent")
def step_error_visually_prominent(context):
    # Would require visual/UI checks. Placeholder for now.
    pass


@then("it should be located near the input fields or at a consistent location on the form")
def step_error_location(context):
    # Placeholder: would check DOM structure in a real test.
    pass


# 4. Performance, reliability, availability


@then("I should receive a response (success or failure) within the agreed performance threshold")
def step_response_time_threshold(context):
    page = _ensure_login_page(context)
    ms = page.get_login_response_time_ms()
    # Example threshold: 2 seconds (2000 ms)
    assert ms <= 2000, f"Login response time too slow: {ms} ms"


@when("I navigate to the login page")
def step_navigate_login(context):
    page = _ensure_login_page(context)
    page.open()


@then("the login page should load successfully")
def step_login_page_loads(context):
    page = _ensure_login_page(context)
    assert page.is_on_login_page(), "Login page did not load successfully"


@then("it should not display generic server error pages")
def step_no_server_error_page(context):
    page = _ensure_login_page(context)
    assert not page.has_generic_server_error(), "Generic server error page is displayed"


# 5. Account lockout


@given('I repeatedly attempt to log in with an existing username and invalid passwords "{password_attempts}"')
def step_multiple_failed_attempts(context, password_attempts):
    page = _ensure_login_page(context)
    username = _resolve_credential_token(context, "valid_user", "username")
    attempts = [p.strip() for p in password_attempts.split(",")]
    for pwd_token in attempts:
        page.enter_username(username)
        pwd_value = _resolve_credential_token(context, pwd_token, "password")
        page.enter_password(pwd_value)
        page.click_login()


@then("the account should be locked or challenged according to policy")
def step_account_locked_or_challenged(context):
    page = _ensure_login_page(context)
    username = _resolve_credential_token(context, "valid_user", "username")
    assert page.is_account_locked(username), "Account is not locked or challenged"


@then("a clear message about the lockout or challenge should be displayed")
def step_lockout_message(context):
    page = _ensure_login_page(context)
    msg = page.get_error_message_text()
    assert msg, "No lockout/challenge message is displayed"


@then("subsequent login attempts with the correct password should be handled according to the lockout policy")
def step_subsequent_login_after_lockout(context):
    # In a real test, attempt another login with valid credentials and
    # verify behaviour (still locked, additional challenge, etc.).
    pass


# 6. Cross-browser / layout


@given('I open the login page in "{browser}"')
@when('I open the login page in "{browser}"')
def step_open_login_in_browser(context, browser):
    page = _ensure_login_page(context)
    # In a real implementation, this would start the driver with a given browser.
    # Here we simply call open() as a placeholder.
    page.open()
    # Optionally store the "intended" browser in context for checks:
    context.expected_browser = browser


@then("the username field should be visible and enabled")
def step_username_visible_enabled(context):
    page = _ensure_login_page(context)
    assert page.controls_are_visible_and_enabled(), (
        "Username (or related controls) not visible/enabled"
    )


@then("the password field should be visible and enabled")
def step_password_visible_enabled(context):
    # Covered by the same underlying check in a real implementation
    page = _ensure_login_page(context)
    assert page.controls_are_visible_and_enabled(), (
        "Password (or related controls) not visible/enabled"
    )


@then("the Login button should be visible and enabled")
def step_login_button_visible_enabled(context):
    page = _ensure_login_page(context)
    assert page.controls_are_visible_and_enabled(), (
        "Login button not visible/enabled"
    )


@then("the layout should not be broken")
def step_layout_not_broken(context):
    page = _ensure_login_page(context)
    assert not page.has_layout_issues(), "Layout appears broken"


