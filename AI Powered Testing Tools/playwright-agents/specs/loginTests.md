# Login & Interaction Test Plan — locatorspractice

## Executive summary

This document is a comprehensive test plan for the page: https://rahulshettyacademy.com/locatorspractice/

Goal: produce clear, reproducible test scenarios suitable for manual QA and for converting into Playwright automated tests. The plan assumes a fresh browser state for every scenario (no prior cookies or localStorage). The file `tests/seed.spec.ts` in this repository is the provided seed and contains a minimal navigator that already visits the URL; use it as the starting point for automation.


## Application overview

The page under test is a practice lab containing a small login-like form and many common HTML controls used to teach locator strategies. Key interactive areas:
- Email / Username and Password inputs and a "Sign In" button
- Checkbox(s) such as "Remember me"
- Links and small helper text (for example demo links or navigation)
- Other interactive elements used on the page (radio buttons, dropdowns, buttons, dynamic content)

Primary test focus for this plan: form behavior (validation, submission, error handling), input edge cases, keyboard accessibility, and interaction stability.


## Test environment & assumptions

- Assume a clean/fresh browser profile at the start of each scenario (clear cookies, localStorage, sessionStorage). This avoids bleed between tests.
- Tests should run in Playwright (seed file: `tests/seed.spec.ts`) but scenarios are framework-agnostic.
- If the application requires real credentials, use a test account provided by product or a stubbed/mocked auth endpoint. This plan uses descriptive placeholders like `VALID_USER` and `VALID_PASS`. Confirm credentials with the product owner or configure a test account.
- Run tests in both headed and headless browsers when possible for visual verification.
- Expected timeout behavior: default Playwright timeouts unless otherwise specified.


## Primary user flows (high level)

1. Navigate to the page and inspect visible fields and controls.
2. Enter credentials and submit (via Click and Enter key).
3. Observe success or error flows (messages, UI state changes).
4. Use keyboard navigation and accessibility-related flows.
5. Interact with ancillary controls (checkboxes, links, dropdowns) and ensure correct behavior.


## How to use this plan

- Each scenario is independent and can be run in any order.
- For automation, start with `tests/seed.spec.ts` which currently contains a `page.goto('https://rahulshettyacademy.com/locatorspractice/')` call. Extend that seed into additional tests or create new spec files per scenario group.
- Map scenario titles to spec filenames (example mapping provided below).


## Scenario index (quick list)

1. Happy path: Valid sign in
2. Invalid credentials
3. Empty fields validation
4. Submit using Enter key
5. Password masking and reveal
6. "Remember me" persistence
7. Long input / max length
8. Whitespace-only and trimming
9. Special characters / XSS attempt
10. Keyboard navigation & focus order
11. UI elements presence & visibility
12. Responsive / mobile viewport behavior
13. Error message behaviour and timing
14. Accessibility checks (labels, roles)


---

## Detailed scenarios

### Scenario 1 — Happy path: Valid sign in

Assumptions:
- Fresh browser state
- Test account exists: VALID_USER / VALID_PASS (confirm with product owner)

Steps:
1. Navigate to the page.
2. Locate the username/email input and type `VALID_USER`.
3. Locate the password input and type `VALID_PASS`.
4. Click the "Sign In" button.

Expected results:
- The page transitions to the post-login state (success banner, redirect, or specific text indicating success).
- No visible validation error is shown.
- Optional: a specific element that only appears on success is present (define the selector before automation).

Success criteria:
- Verified by presence of the expected success element or redirect URL within the expected timeout.

Failure conditions:
- Any visible error message about invalid credentials.
- No page change within timeout.


### Scenario 2 — Invalid credentials

Assumptions: fresh browser state

Steps:
1. Navigate to the page.
2. Enter `INVALID_USER` into username and `INVALID_PASS` into password.
3. Click "Sign In".

Expected results:
- An error/validation message is displayed (e.g., "Incorrect username or password").
- The form remains on the page; username and password fields may be cleared or left as-is per UI behavior.

Success criteria:
- Error message visible and matches expected text or contains the expected keywords.

Failure conditions:
- No error message shown and no redirect.
- Unexpected crash or 500-level errors.


### Scenario 3 — Empty fields validation

Assumptions: fresh browser state

Steps:
1. Navigate to the page.
2. Leave username and password empty.
3. Click "Sign In".

Expected results:
- Client-side validation triggers; show required field messages for username and/or password.
- No network call should be made in strict client-side validation modes (verify via network stubbing if automation can do so).

Success criteria:
- Proper field-level validation messages are visible.

Failure conditions:
- Form submits and server returns an error without client-side validation.


### Scenario 4 — Submit using Enter key

Assumptions: fresh browser state

Steps:
1. Navigate to the page.
2. Enter `VALID_USER` and `VALID_PASS` into the respective inputs.
3. Focus the password field and press Enter (keyboard Enter key press).

Expected results:
- Form is submitted and behaves identically to clicking "Sign In".

Success criteria:
- Success state is reached (redirect or success message) as in Scenario 1.

Failure conditions:
- Enter key does nothing or triggers an unexpected action.


### Scenario 5 — Password masking and reveal

Assumptions: UI provides a toggle (eye icon) to unmask password. If not present, mark test as N/A.

Steps:
1. Navigate to the page.
2. Type `S3cr3tPass!` into password field.
3. Confirm by inspecting the input `type` attribute is `password` (masked).
4. Click the show/reveal control (if present).
5. Confirm input `type` changes to `text` and displayed value is the same.
6. Click again to re-mask.

Expected results:
- Masking/unmasking toggles correctly, value preserved throughout.

Success criteria:
- Toggling changes the `type` attribute and visible characters accordingly.

Failure conditions:
- Toggle not present or reveals a different value; input is corrupted.


### Scenario 6 — "Remember me" persistence

Assumptions: a "Remember me" or similar checkbox exists and toggles persistence.

Steps:
1. Navigate to the page.
2. Enter valid credentials.
3. Check the "Remember me" checkbox.
4. Sign in successfully.
5. Close the browser context (or clear only session storage but keep persistent storage) and re-open/visit the page.

Expected results:
- Depending on intended behavior: either (A) user still appears logged-in, or (B) username field is pre-populated. Define exact expected behavior with product owner.

Success criteria:
- The observed behavior matches the intended persistence spec.

Failure conditions:
- Data not persisted when it should be, or persisted when it should not be.


### Scenario 7 — Long input / max length

Assumptions: inputs may enforce max-length

Steps:
1. Navigate to the page.
2. Enter an extremely long string (e.g., 5000 characters) into the username field.
3. Enter a long string into the password field.
4. Attempt to submit.

Expected results:
- The UI either truncates input at the defined maxlength or accepts and safely sends input to server (server should handle without error).
- No client-side crash, layout break, or unhandled exceptions.

Success criteria:
- Page remains functional and returns an expected validation error if defined.

Failure conditions:
- Crash, layout break, or server error (5xx) caused by input size.


### Scenario 8 — Whitespace-only and trimming

Assumptions: expected behavior is that fields are trimmed before validation.

Steps:
1. Navigate to the page.
2. Enter `   VALID_USER   ` (leading/trailing spaces) and `   VALID_PASS   `.
3. Submit.

Expected results:
- The application trims whitespace and authenticates (if credentials are correct when trimmed), or shows explicit validation error if whitespace-only is disallowed.

Success criteria:
- Behavior conforms to product spec (trims vs rejects).

Failure conditions:
- Unexpected rejection or acceptance of whitespace-only credentials if spec says otherwise.


### Scenario 9 — Special characters / XSS attempt

Assumptions: application must handle special characters safely

Steps:
1. Navigate to the page.
2. Enter payloads such as `<script>alert(1)</script>` and other special characters into inputs.
3. Submit.

Expected results:
- Input is escaped and not executed. No injected script should run. Any error messages should be normal strings, not HTML.

Success criteria:
- No popups created by injected scripts. App returns safe responses.

Failure conditions:
- Execution of injected script or display of unescaped HTML.


### Scenario 10 — Keyboard navigation & focus order

Assumptions: accessibility standards followed; logical tab order exists.

Steps:
1. Navigate to page.
2. Press Tab repeatedly from the top of page.
3. Observe focus order across interactive elements (should hit username -> password -> remember checkbox -> sign in -> other controls).
4. Use Shift+Tab to navigate backward.

Expected results:
- Focus order is logical, visible focus ring is present on each interactive control, and keyboard operations (Enter, Space for checkbox) work.

Success criteria:
- Keyboard-only navigation can operate the full sign-in flow.

Failure conditions:
- Focus is lost, skip links, or controls not reachable via keyboard.


### Scenario 11 — UI elements presence & visibility

Assumptions: All critical controls have stable locators and are visible on page load.

Steps:
1. Navigate to page.
2. Verify presence and visibility of:
   - Username/email input
   - Password input
   - Sign In button
   - Any checkboxes or helper links used by further scenarios

Expected results:
- Each control is visible, not off-screen, and has accessible labels.

Success criteria:
- Elements found with stable selectors and match product's design.

Failure conditions:
- Missing elements or unexpected layout issues.


### Scenario 12 — Responsive / mobile viewport behavior

Assumptions: Page should be usable at smaller viewports (mobile/tablet)

Steps:
1. Launch the page at a mobile viewport (example: 375x812)
2. Verify inputs and button are visible without requiring horizontal scroll.
3. Attempt a sign-in happy-path with valid credentials.

Expected results:
- Inputs scale/stack properly and functionality remains intact.

Success criteria:
- No layout break and interactive elements remain reachable and usable.

Failure conditions:
- Overflows, hidden controls, or truncated text that prevents action.


### Scenario 13 — Error message behaviour and timing

Assumptions: Error messages display and disappear deterministically.

Steps:
1. Trigger an error (invalid credentials or client validation) and note the message.
2. Correct the input and submit again.

Expected results:
- Error message is removed or replaced by success message when problem fixed.
- Error messages have ARIA roles if appropriate (e.g., role="alert").

Success criteria:
- Messages behave predictably and are announced by screen readers when applicable.

Failure conditions:
- Stale error messages remain after correction; duplicate messages appear.


### Scenario 14 — Accessibility checks (labels, ARIA, contrast)

Assumptions: The page aims for basic accessibility compliance.

Steps:
1. Inspect form controls for <label> association or aria-label attributes.
2. Verify roles for error messages (role="alert") and presence of accessible names.
3. Check color contrast for input placeholders and button text.
4. Run a quick automated accessibility check (axe or Playwright a11y snapshot) as part of CI.

Expected results:
- Inputs have accessible names and error messages are announced.
- No critical accessibility violations are present.

Success criteria:
- Zero critical/serious violations from an automated scanner.

Failure conditions:
- Missing labels, unreadable contrast, or inaccessible error announcements.


---

## Mapping to automated Playwright tests (suggested file names)

- specs/login_happy.spec.ts — Scenario 1 & 4
- specs/login_negative.spec.ts — Scenarios 2, 3, 8, 9
- specs/login_ui.spec.ts — Scenarios 5, 6, 7, 11
- specs/login_accessibility.spec.ts — Scenarios 10, 13, 14

Note: the provided seed `tests/seed.spec.ts` already contains the navigation call. Use it as a template for `page.goto(...)`, then add scenario-specific steps and assertions.


## Test data examples

- VALID_USER / VALID_PASS — request from product owner or use a stubbed auth endpoint.
- INVALID_USER / INVALID_PASS — any non-existing combination.
- LONG_STRING — generate programmatically (e.g., 'a'.repeat(5000)).
- XSS_PAYLOAD — `<script>alert('xss')</script>` and other encoded forms.


## Run instructions (Playwright)

From the repository root, run tests with Playwright test runner. Example commands for PowerShell:

```powershell
# run all tests
npx playwright test

# run a single file
npx playwright test specs\login_happy.spec.ts

# run with headed browser for visual debugging
npx playwright test --headed
```


## Notes & next steps

- Confirm expected success criteria for the happy path (what indicates a real successful login on this demo page).
- If real auth is unavailable, consider stubbing network responses for predictable automated tests.
- Convert each scenario into Playwright spec files and add simple test-data fixtures.


---

Generated using `tests/seed.spec.ts` as the seed (which currently navigates to the target URL). Each scenario is independent and written for clarity for both manual testers and automation engineers.

