# Login & Interaction Test Plan — TesterBud practice-login-form

## Executive summary

This document is a comprehensive test plan for the practice login form hosted at:

https://testerbud.com/practice-login-form

Goal: provide clear, reproducible test scenarios suitable for manual QA and for converting into Playwright automated tests. Each scenario assumes a fresh browser state at start (no cookies, no localStorage). The repository already contains a seed spec (`tests/seed.spec.ts`) that navigates to the target URL; use it as the starting point for automation.

Valid test credentials (provided):
- Email: user@premiumbank.com
- Password: Bank@123


## Application overview

The target page is a practice login form used for testing locator strategies and form behaviors. Typical interactive elements include:
- Email (or username) input
- Password input
- Login / Sign In button
- Optional controls such as "Remember me", password reveal, or helper links (assumed — see assumptions below)

Primary test focus for this plan: authentication flow (happy path and negative cases), input validation, keyboard and accessibility behaviors, and robustness against malformed input.


## Assumptions

- Each scenario begins with a cleared browser context (fresh profile).
- The practice page is self-contained and returns deterministic behavior for given inputs.
- The page contains at least: an email input, a password input, and a login button. If other controls (remember checkbox, show password icon) are present the plan includes tests for them; if not, those scenarios can be marked N/A.
- The provided credentials are accepted by the practice page and represent the happy-path login.


## Primary user flows

1. Open the login page.
2. Enter credentials and submit via click or Enter key.
3. Observe success or error behavior (messages, redirects, UI changes).
4. Verify keyboard accessibility and ancillary controls (checkboxes, links).


## How to use this plan

- Each scenario is independent. Run with a fresh browser context per scenario.
- For automation, use `tests/seed.spec.ts` which already navigates to the URL. Extend or create new spec files per scenario.
- Map scenario titles to Playwright spec files (suggestions included later).


## Scenario index

1. Happy path: valid login
2. Invalid credentials
3. Empty fields validation
4. Submit using Enter key
5. Password masking and reveal (if present)
6. "Remember me" persistence (if present)
7. Long input / maxlength behavior
8. Whitespace-only / trimming
9. Special characters / XSS and injection safety
10. SQL injection / backend robustness
11. Keyboard navigation & focus order
12. UI elements presence & visibility
13. Responsive / mobile viewport behavior
14. Error message behavior and timing
15. Accessibility checks (labels, ARIA, contrast)


---

## Detailed scenarios

### Scenario 1 — Happy path: Valid login

Assumptions:
- Fresh browser state
- Provided credentials are valid for this demo page

Steps:
1. Navigate to https://testerbud.com/practice-login-form.
2. Locate the email input and type `user@premiumbank.com`.
3. Locate the password input and type `Bank@123`.
4. Click the Login/Sign In button.

Expected results:
- The page indicates success: either a success message, a redirect to a welcome page, or another distinct UI change.
- No validation error is shown.

Success criteria:
- Presence of a success indicator (message or redirect) within the test timeout.

Failure conditions:
- Error message about invalid credentials, no UI change, or server error.


### Scenario 2 — Invalid credentials

Assumptions: fresh browser state

Steps:
1. Navigate to the page.
2. Enter `invalid@user.com` and `wrongpass`.
3. Click Login.

Expected results:
- A clear error message appears (e.g., "Invalid credentials"), and the user remains on the login form.

Success criteria:
- Error message visible and stable.

Failure conditions:
- Silent failure, redirect to an unexpected page, or a server error.


### Scenario 3 — Empty fields validation

Assumptions: fresh browser state

Steps:
1. Navigate to the page.
2. Leave email and password empty.
3. Click Login.

Expected results:
- Client-side validation shows required-field messages for email and/or password.
- No network request sent if strict client-side validation is present (can be verified via network logs in automation).

Success criteria:
- Field-level validation messages visible.

Failure conditions:
- Form submits without validation and server returns an error.


### Scenario 4 — Submit using Enter key

Assumptions: fresh browser state

Steps:
1. Navigate to the page.
2. Fill in `user@premiumbank.com` and `Bank@123`.
3. Focus the password field and press Enter.

Expected results:
- Form is submitted; behavior matches clicking the Login button.

Success criteria:
- Same success state as Scenario 1.

Failure conditions:
- Enter key does nothing or triggers another unexpected action.


### Scenario 5 — Password masking and reveal

Assumptions: the page may include a show/hide password control. If not present, mark N/A.

Steps:
1. Navigate to the page.
2. Type `Bank@123` into the password field.
3. Confirm the `type` attribute is `password` (masked).
4. If a reveal control exists (eye icon), click it.
5. Confirm `type` becomes `text` and the value is visible; click again to re-mask.

Expected results:
- Toggle preserves the value and only changes masking behavior.

Success criteria:
- Toggle changes the input `type` and visible behavior; value not altered.

Failure conditions:
- No toggle present when expected, or toggle corrupts the value.


### Scenario 6 — "Remember me" persistence

Assumptions: a "Remember me" checkbox exists and is functional. If not, mark N/A.

Steps:
1. Navigate to page.
2. Enter valid credentials, check the "Remember me" box.
3. Login successfully.
4. Close the browser context (but preserve persistent storage) and revisit the page.

Expected results:
- Either the user remains logged in or the email is pre-filled per product spec.

Success criteria:
- Behavior matches the intended persistence specification.

Failure conditions:
- Data not persisted correctly or persisted unexpectedly.


### Scenario 7 — Long input / maxlength

Assumptions: inputs may have maxlength or server-side handling.

Steps:
1. Navigate to page.
2. Enter a very long string (e.g., 5000 characters) into email and password fields.
3. Attempt to submit.

Expected results:
- Inputs are either truncated to maxlength or safely handled by server without crash.
- No layout breaks or uncaught exceptions.

Success criteria:
- Application handles input length safely and returns predictable validation if applicable.

Failure conditions:
- Client or server crash, 5xx errors, or corrupted UI.


### Scenario 8 — Whitespace-only and trimming

Assumptions: fields are trimmed before validation or server-side handles trimming.

Steps:
1. Enter `   user@premiumbank.com   ` and `   Bank@123   `.
2. Submit.

Expected results:
- The application trims whitespace and logs in, or returns a clear validation message if whitespace-only is invalid.

Success criteria:
- Behavior consistent with product expectations.

Failure conditions:
- Unexpected rejection or acceptance contrary to spec.


### Scenario 9 — Special characters / XSS safety

Assumptions: application must escape input and not execute scripts

Steps:
1. Enter `<script>alert('xss')</script>` and other payloads into inputs.
2. Submit.

Expected results:
- No script execution; inputs are escaped or rejected. Any error messages show raw text, not rendered HTML.

Success criteria:
- No JS alert or page injection.

Failure conditions:
- Executed payloads or reflected unescaped HTML in the UI.


### Scenario 10 — SQL injection / backend robustness

Assumptions: backend must be robust to malicious payloads

Steps:
1. Attempt payloads like `' OR '1'='1` or `'; DROP TABLE users; --` in inputs.
2. Submit.

Expected results:
- Backend rejects or safely handles payloads without exposing data or causing errors.

Success criteria:
- No sensitive leak or server error.

Failure conditions:
- Server error, stack trace shown to user, or unexpected success.


### Scenario 11 — Keyboard navigation & focus order

Assumptions: logical tab order and keyboard accessibility

Steps:
1. Load page.
2. Use Tab to navigate all interactive elements.
3. Verify visible focus for each and that keyboard actions (Space, Enter) operate them.

Expected results:
- Logical focus order (email -> password -> optional checkbox -> login button).
- Full sign-in flow reachable using keyboard only.

Success criteria:
- No inaccessible controls and focus visible.

Failure conditions:
- Focus skip, trapped focus, or controls unreachable.


### Scenario 12 — UI elements presence & visibility

Assumptions: critical controls are visible and stable

Steps:
1. Navigate to page.
2. Verify presence and visibility of email input, password input, login button, and any helper links.

Expected results:
- All expected controls present and labeled.

Success criteria:
- Elements findable with stable selectors.

Failure conditions:
- Missing inputs or broken layout.


### Scenario 13 — Responsive / mobile viewport behavior

Assumptions: page should remain usable on mobile viewports

Steps:
1. Emulate a mobile viewport (e.g., 375x812).
2. Verify inputs and button are visible and usable.
3. Perform a happy-path login.

Expected results:
- Inputs stack or scale properly; no horizontal scroll required; login works.

Success criteria:
- No layout break preventing use.

Failure conditions:
- Hidden inputs or unusable controls.


### Scenario 14 — Error message behavior and timing

Assumptions: errors shown/cleared predictably

Steps:
1. Cause an error (invalid credentials).
2. Fix inputs and resubmit.

Expected results:
- Error message removed or replaced by success message upon correction.
- Error messages use ARIA roles where appropriate.

Success criteria:
- Messages behave predictably and are accessible.

Failure conditions:
- Stale errors remain after correction.


### Scenario 15 — Accessibility checks (labels, ARIA, contrast)

Assumptions: the page aims for basic accessibility compliance

Steps:
1. Inspect inputs for label associations or aria-labels.
2. Verify error messages have role="alert" or are reachable by screen readers.
3. Run an automated accessibility scan (axe or Playwright a11y snapshot) during CI.

Expected results:
- Inputs have accessible names and minimal critical accessibility violations.

Success criteria:
- Zero critical violations from automated tooling.

Failure conditions:
- Missing labels, poor contrast, or inaccessible announcements.


---

## Mapping to Playwright specs (suggested)

- specs/login_happy.spec.ts — Scenario 1 & 4
- specs/login_negative.spec.ts — Scenarios 2, 3, 8, 9, 10
- specs/login_ui.spec.ts — Scenarios 5, 6, 7, 11, 12
- specs/login_accessibility.spec.ts — Scenarios 13, 14, 15

Use `tests/seed.spec.ts` as a simple starting template for `page.goto(...)` and adapt each spec to include setup and assertions.


## Test data

- VALID_EMAIL: user@premiumbank.com
- VALID_PASSWORD: Bank@123
- INVALID_EMAIL / INVALID_PASSWORD: any non-matching combo
- LONG_STRING: generate programmatically (e.g., `'a'.repeat(5000)`)
- XSS_PAYLOAD: `<script>alert(1)</script>`
- SQL_INJECTION: `' OR '1'='1` and similar payloads


## Run instructions (Playwright)

From repository root, run Playwright tests. PowerShell examples:

```powershell
# run all tests
npx playwright test

# run a single file
npx playwright test specs\login_happy.spec.ts

# run headed for debugging
npx playwright test --headed

# run a single test by name (example)
npx playwright test -g "Happy path: Valid login"
```


## Notes & next steps

- Confirm the exact success indicator for the practice page (success message text or redirect URL) to harden assertions.
- If the practice page does not accept the provided credentials, consider mocking network responses or using a testing stub.
- I can convert selected scenarios (e.g., Scenario 1 and 2) into Playwright test files and add them to the `tests/` folder—would you like me to implement the happy-path and invalid-credentials specs now?


---

Generated and saved to `specs/loginTests-testerbud.md`. This plan uses `tests/seed.spec.ts` as the seed, which currently navigates to the TesterBud practice-login-form URL.
