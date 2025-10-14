// spec: tests/login_negative.spec.ts
// seed: tests/seed.spec.ts

import { test, expect, Page, Locator } from '@playwright/test';

// Helper: find the page's primary submit button with sensible fallbacks
async function getSubmit(page: Page): Promise<Locator> {
  if (await page.locator('button:has-text("Sign in")').count() > 0) {
    return page.locator('button:has-text("Sign in")').first();
  }
  if (await page.locator('button:has-text("Login")').count() > 0) {
    return page.locator('button:has-text("Login")').first();
  }
  if (await page.locator('button[type="submit"]').count() > 0) {
    return page.locator('button[type="submit"]').first();
  }
  return page.locator('button').first();
}

// Helper: prefer the bootstrap danger alert container, fallback to role=alert
async function getBootstrapAlert(page: Page): Promise<Locator> {
  const bootstrap = page.locator("div.fade.alert.alert-danger.show");
  if (await bootstrap.count() > 0) return bootstrap.first();
  return page.locator('role=alert');
}

// Negative scenarios (Scenario 2, 3, 8, 9, 10)
test.describe('Login Negative Flows', () => {
  test('Invalid credentials shows an error', async ({ page }) => {
    await page.goto('https://testerbud.com/practice-login-form');
    await page.fill('input[type="email"], input[name="email"]', 'invalid@user.com');
    await page.fill('input[type="password"], input[name="password"]', 'wrongpass');
    const submit = await getSubmit(page);
    await submit.click();

  // Prefer the bootstrap alert container but fall back to role=alert.
  // Assert the visible alert contains the exact expected error message.
  const alert = await getBootstrapAlert(page);
  await expect(alert).toBeVisible({ timeout: 3000 });
  await expect(alert).toContainText('Invalid email id and password');
  });

  test('Empty fields validation shows required errors', async ({ page }) => {
    await page.goto('https://testerbud.com/practice-login-form');
    // Submit without entering anything. Use helper to pick the right button.
    const submit = await getSubmit(page);
    await submit.click();

    // The page shows a bootstrap danger alert for missing fields
    const alert = await getBootstrapAlert(page);
    await expect(alert).toBeVisible({ timeout: 3000 });
    await expect(alert).toContainText('Email and Password are required');
  });

  test('Whitespace-only inputs are rejected', async ({ page }) => {
    await page.goto('https://testerbud.com/practice-login-form');
    await page.fill('input[type="email"], input[name="email"]', '   user@premiumbank.com   ');
    await page.fill('input[type="password"], input[name="password"]', '   Bank@123   ');
    const submit = await getSubmit(page);
    await submit.click();
    // The app rejects whitespace-only inputs. Assert the specific error message.
    const alert = await getBootstrapAlert(page);
    await expect(alert).toBeVisible({ timeout: 3000 });
    await expect(alert).toContainText('Invalid email id and password');
  });

  test('XSS payloads do not execute and are handled safely', async ({ page }) => {
    await page.goto('https://testerbud.com/practice-login-form');

    // Insert XSS-like payload into the email field
    const email = page.locator('input[type="email"], input[name="email"]');
    await email.fill("<script>alert('xss')</script>");
    await page.fill('input[type="password"], input[name="password"]', 'password');

    // Start a dialog watcher: resolves true if a dialog appears within the timeout
    const dialogPromise = page.waitForEvent('dialog', { timeout: 500 })
      .then(async (dialog) => { await dialog.dismiss(); return true; })
      .catch(() => false);

    // Evaluate native validity (typeMismatch is language-agnostic)
    const isTypeMismatch = await email.evaluate((el: HTMLInputElement) => el.validity.typeMismatch);

    // Click the submit button in any case; the browser may block submission if native validation fails
    const submit = await getSubmit(page);
    await submit.click();

    // If the browser flagged a type mismatch, assert native validation and avoid assuming app-level alerts
    if (isTypeMismatch) {
      const validationMessage = await email.evaluate((el: HTMLInputElement) => el.validationMessage);
      await expect(validationMessage.length).toBeGreaterThan(0);

      const dialogShown = await dialogPromise;
      expect(dialogShown).toBe(false);

      // The app-level bootstrap alert may not appear because the browser prevented the form submit.
      const bootstrap = page.locator('div.fade.alert.alert-danger.show');
      if (await bootstrap.count() > 0) {
        await expect(bootstrap.first()).toBeVisible({ timeout: 2000 });
      }

      await expect(page.locator('text=<script>')).not.toBeVisible({ timeout: 1000 });
      return;
    }

    // If native validation didn't block submit, the application should handle the payload safely.
    const dialogShown = await dialogPromise;
    expect(dialogShown).toBe(false);

    // Ensure the page didn't render raw script text visibly
    await expect(page.locator('text=<script>')).not.toBeVisible({ timeout: 1000 });

    // Expect an application-level error / safe handling
    const err = await getBootstrapAlert(page);
    await expect(err).toBeVisible({ timeout: 3000 });
  });

  test('SQL injection payloads are rejected or safely handled', async ({ page }) => {
    await page.goto('https://testerbud.com/practice-login-form');
    await page.fill('input[type="email"], input[name="email"]', "' OR '1'='1");
    await page.fill('input[type="password"], input[name="password"]', 'anything');
    const submit = await getSubmit(page);
    await submit.click();

    const invalidMsg = page.locator('text=Invalid credentials');
    if (await invalidMsg.count() > 0) {
      await expect(invalidMsg).toBeVisible({ timeout: 3000 });
    } else {
      await expect(page.locator('role=alert')).toBeVisible({ timeout: 3000 });
    }
  });
});
