# 🔒 Login Page Test Coverage

Feature: User Login Functionality

  As a user,
  I want to be able to log in to the application
  So that I can access my personalized content.

---

## Functional Scenarios

Scenario: Successful Login with Valid Credentials

  Given I am on the login page
  When I enter a valid username in the username field
  And I enter a valid password in the password field
  And I click the "Login" button
  Then I should be redirected to the dashboard or home page
  And I should see a welcome message (e.g., "Welcome, [Username]!")

---

Scenario Outline: Failed Login with Invalid/Empty Credentials

  Given I am on the login page
  When I enter "<Username>" in the username field
  And I enter "<Password>" in the password field
  And I click the "Login" button
  Then I should remain on the login page
  And I should see an error message stating "<Expected Error Message>"

  Examples:
    | Username | Password | Expected Error Message |
    | <empty> | ValidPassword | Please enter your username and password. |
    | ValidUser | <empty> | Please enter your password. |
    | <empty> | <empty> | Please enter your username and password. |
    | InvalidUser | ValidPassword | Invalid username or password. |
    | ValidUser | InvalidPassword | Invalid username or password. |
    | InvalidUser | InvalidPassword | Invalid username or password. |
    | ValidUser | ValidPassword | Your account is locked. | # Locked account
    | InactiveUser | ValidPassword | Your account is inactive. | # Inactive user

---

Scenario Outline: Boundary and Constraint Testing for Input Fields

  Given I am on the login page
  When I enter a "<Data Type>" in the "<Field Name>" field
  And I enter a valid input in the other field
  And I click the "Login" button
  Then I should see the error message: "<Expected Error Message>"

  Examples:
    | Field Name | Data Type | Expected Error Message |
    | username | Less than Min Length (e.g., 2 chars) | Username must be at least 4 characters long. |
    | username | More than Max Length (e.g., 51 chars) | Username cannot exceed 50 characters. |
    | username | Special Characters (e.g., user$name!) | Username contains invalid characters. |
    | password | Less than Min Length (e.g., 5 chars) | Password must be at least 8 characters long. |
    | password | More than Max Length (e.g., 129 chars) | Password cannot exceed 128 characters. |

---

Scenario Outline: Case Sensitivity

  Given I am on the login page
  When I enter the correct "<Username Case>" and correct "<Password Case>"
  And I click the "Login" button
  Then I should "<Expected Result>"

  Examples:
    | Username Case | Password Case | Expected Result |
    | Correct Case | Correct Case | be redirected to the dashboard. |
    | Incorrect Case | Correct Case | remain on the login page and see an error. |
    | Correct Case | Incorrect Case | remain on the login page and see an error. |

---

Scenario: Password Visibility (Show/Hide)

  Given I am on the login page
  When I enter a password in the password field
  And the Show/Hide toggle is present
  And I click the Show toggle
  Then the password field input type should change from "password" to "text" (text is visible)
  When I click the Hide toggle again
  Then the password field input type should change from "text" to "password" (text is masked)

---

Scenario: Focus and Navigation

  Given I am on the login page
  When I press the Tab key repeatedly, starting from outside the form
  Then the focus should move in the correct order: Username Field -> Password Field -> Login Button -> Forgot Password Link
  When the focus is on the "Login" button
  And I press the Enter key
  Then the login attempt should be processed

---

Scenario: Session Management (Logout/Timeout)

  Given I have successfully logged in
  When I click the "Logout" button
  Then I should be redirected to the login page
  And I should not be able to navigate back to the dashboard using the browser Back button.
  Given I have successfully logged in
  When I remain inactive for the configured session timeout duration (e.g., 30 minutes)
  Then I should be automatically logged out and redirected to the login page.

---

## Non-Functional Scenarios

Scenario: Localization/Internationalization

  Given I am on the login page
  When I change the language selection from English to Spanish
  Then all UI elements (field labels, button text, error messages) should be displayed in Spanish.

---

Scenario: Performance - Load Time

  Given I am accessing the login page
  When the page starts to load
  Then the page should be fully rendered within 2 seconds (under a normal load).

---

Scenario: Performance - Concurrent Users

  Given 1000 users are attempting to log in concurrently within a 1-minute window
  When each user submits valid credentials
  Then the system response time for a successful login should not exceed 3 seconds
  And the system should not return any HTTP 5xx errors.

---

Scenario: Security - XSS and SQL Injection

  Given I am on the login page
  When I enter a SQL Injection string (e.g., ' OR '1'='1) in the username field
  And I enter a valid password
  And I click "Login"
  Then the application should not successfully log me in
  And I should see the standard "Invalid username or password" error.
  When I enter a Cross-Site Scripting (XSS) string (e.g., <script>alert('XSS')</script>) in the username field
  And I click "Login"
  Then the application should encode the input and not execute the script.

---

Scenario: Responsiveness and Accessibility

  Given I am viewing the login page on a mobile device screen size (e.g., 360px width)
  When the page loads
  Then the login form elements should be stacked vertically and readable without horizontal scrolling.
  And Alternative text should be available for the logo/image elements.
  And all interactive elements should meet WCAG 2.1 color contrast standards.