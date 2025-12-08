# language: en
# Feature file: Login UI Test Coverage
#
# Assumptions (kept minimal to avoid over-specification):
# - The login page contains only:
#     - a username text field
#     - a password text field
#     - a "Login" button
#     - a generic error message area for failed logins
# - There exists at least one valid username/password pair that can be used for testing.
# - The page communicates with a backend authentication service to validate credentials.
# - Where policies (e.g. lockout, password rules) are referenced, they are assumed to be
#   configured in the system; this feature verifies that the UI behaves correctly with them.


Feature: Login page UI for username and password
  In order to access the application securely
  As a user of the system
  I want the login page to correctly handle username/password input and provide clear feedback

  # --------------------------------------------------------------------------
  # 1. Basic successful and unsuccessful login flows (functional)
  # --------------------------------------------------------------------------

  @smoke @functional
  Scenario: Successful login with valid username and password
    Given I am on the login page
    And I enter a valid username into the username field
    And I enter the corresponding valid password into the password field
    When I click the Login button
    Then I should be successfully logged in
    And I should be redirected to the authenticated home page

  @functional
  Scenario Outline: Invalid login attempts with various incorrect credentials
    Given I am on the login page
    And I enter "<username>" into the username field
    And I enter "<password>" into the password field
    When I click the Login button
    Then I should see a generic login error message
    And I should remain on the login page
    And the username and password fields should be cleared or safely handled according to policy

    Examples:
      | username            | password             |
      | valid_user          | wrong_password       |
      | unknown_user        | any_password         |
      | valid_user          | empty                |
      | empty               | valid_password       |
      | empty               | empty                |
      | valid_user          | password_with_typo   |

  @functional
  Scenario: Error message is not overly specific to avoid information leakage
    Given I am on the login page
    And I enter an unknown username into the username field
    And I enter an invalid password into the password field
    When I click the Login button
    Then I should see a generic login error message
    And the error message should not reveal whether the username or password was incorrect

  # --------------------------------------------------------------------------
  # 2. Input validation and boundary conditions (functional)
  # --------------------------------------------------------------------------

  @functional
  Scenario Outline: Leading and trailing whitespace handling in credentials
    Given I am on the login page
    And I enter "<username_input>" into the username field
    And I enter "<password_input>" into the password field
    When I click the Login button
    Then the system should treat the credentials as trimmed
    And the login result should match the outcome for the trimmed values "<expected_username>" and "<expected_password>"

    Examples:
      | username_input    | password_input      | expected_username | expected_password  |
      | " valid_user"     | "valid_password"    | valid_user        | valid_password     |
      | "valid_user "     | "valid_password"    | valid_user        | valid_password     |
      | "  valid_user  "  | "  valid_password"  | valid_user        | valid_password     |

  @functional
  Scenario Outline: Username and password length boundaries
    Given I am on the login page
    And I enter "<username>" into the username field
    And I enter "<password>" into the password field
    When I click the Login button
    Then the behaviour should follow the configured length rules and show "<expected_result>"

    Examples:
      | username              | password              | expected_result                |
      | minimal_length_user   | minimal_length_pass   | successful_or_policy_correct   |
      | overlong_username     | valid_password        | rejected_with_clear_message    |
      | valid_user            | overlong_password     | rejected_with_clear_message    |

  @functional
  Scenario Outline: Special characters and allowed character sets
    Given I am on the login page
    And I enter "<username>" into the username field
    And I enter "<password>" into the password field
    When I click the Login button
    Then the system should handle the characters safely and respond with "<expected_result>"

    Examples:
      | username           | password               | expected_result              |
      | user.with.dots     | ValidPa55!            | login_allowed_if_configured  |
      | user+alias         | Valid_Pass-123        | login_allowed_if_configured  |
      | sql_injection_text | any_password          | rejected_without_breaking_UI |
      | script_tag_text    | any_password          | rejected_without_script_exec |

  # --------------------------------------------------------------------------
  # 3. Security and robustness (functional + non-functional)
  # --------------------------------------------------------------------------

  @security @functional
  Scenario Outline: Resilience against obvious injection strings
    Given I am on the login page
    And I enter "<username_input>" into the username field
    And I enter "<password_input>" into the password field
    When I click the Login button
    Then the login should fail safely
    And the page should continue to render correctly
    And no technical error details should be displayed to the user

    Examples:
      | username_input            | password_input         |
      | "' OR '1'='1"             | "anything"             |
      | "admin'--"                | "anything"             |
      | "<script>alert(1)</script>" | "<script>alert(2)</script>" |

  @security @functional
  Scenario: No sensitive information in error messages
    Given I am on the login page
    And I attempt to log in with invalid credentials
    When I click the Login button
    Then I should see a generic error message
    And the error message should not contain stack traces
    And the error message should not expose internal system details

  @security @functional
  Scenario: No credential echo in the UI
    Given I am on the login page
    When I enter a password into the password field
    Then the password should be masked
    And the password value should not appear in any visible label or error message

  # --------------------------------------------------------------------------
  # 4. Usability and accessibility (non-functional but UI-focused)
  # --------------------------------------------------------------------------

  @usability @nonfunctional
  Scenario: Tab order between fields and Login button
    Given I am on the login page
    When I press the Tab key from the username field
    Then the focus should move to the password field
    When I press the Tab key from the password field
    Then the focus should move to the Login button

  @usability @nonfunctional
  Scenario: Labels clearly describe the input fields
    Given I am on the login page
    Then the username field should have a clear and visible label
    And the password field should have a clear and visible label
    And any placeholder text should not replace the need for visible labels

  @accessibility @nonfunctional
  Scenario: Screen reader support for login controls
    Given I am using a screen reader on the login page
    Then the username field should be announced with an appropriate accessible name
    And the password field should be announced with an appropriate accessible name
    And the Login button should be announced as an actionable control

  @usability @nonfunctional
  Scenario: Clear and visible error message placement
    Given I am on the login page
    And I attempt to log in with invalid credentials
    When the error message is displayed
    Then it should be visually prominent
    And it should be located near the input fields or at a consistent location on the form

  # --------------------------------------------------------------------------
  # 5. Performance and reliability characteristics (non-functional)
  # --------------------------------------------------------------------------

  @performance @nonfunctional
  Scenario: Login response time within acceptable threshold
    Given I am on the login page
    When I attempt to log in with valid credentials
    Then I should receive a response (success or failure) within the agreed performance threshold

  @reliability @nonfunctional
  Scenario: Login page is available when requested
    When I navigate to the login page
    Then the login page should load successfully
    And it should not display generic server error pages

  # --------------------------------------------------------------------------
  # 6. Account lockout and repeated failure behaviour (functional + non-functional)
  # --------------------------------------------------------------------------
  # Assumption: The system implements an account lockout policy after multiple failed attempts.

  @security @functional
  Scenario Outline: Multiple failed login attempts leading to lockout
    Given I am on the login page
    And I repeatedly attempt to log in with an existing username and invalid passwords "<password_attempts>"
    When I exceed the configured number of failed attempts
    Then the account should be locked or challenged according to policy
    And a clear message about the lockout or challenge should be displayed
    And subsequent login attempts with the correct password should be handled according to the lockout policy

    Examples:
      | password_attempts         |
      | wrong1, wrong2, wrong3   |

  # --------------------------------------------------------------------------
  # 7. Cross-browser / layout sanity (non-functional, high-level)
  # --------------------------------------------------------------------------

  @compatibility @nonfunctional
  Scenario Outline: Basic layout and control visibility across supported browsers
    Given I open the login page in "<browser>"
    Then the username field should be visible and enabled
    And the password field should be visible and enabled
    And the Login button should be visible and enabled
    And the layout should not be broken

    Examples:
      | browser   |
      | Chrome    |
      | Firefox   |
      | Edge      |

