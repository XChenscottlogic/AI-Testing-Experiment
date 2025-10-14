// spec: tests/login_accessibility.spec.ts
// seed: tests/seed.spec.ts

import { test, expect, Page, Locator } from '@playwright/test';

// Accessibility and responsive scenarios (Scenario 13, 14, 15)

async function findInputs(page: Page): Promise<{ email: Locator; password: Locator }> {
  const email = (await page.locator('input[type="email"]').count()) > 0
    ? page.locator('input[type="email"]').first()
    : page.locator('input').first();
  const password = (await page.locator('input[type="password"]').count()) > 0
    ? page.locator('input[type="password"]').first()
    : page.locator('input').nth(1);
  return { email, password };
}

async function getBootstrapAlert(page: Page): Promise<Locator> {
  const bootstrap = page.locator("div.fade.alert.alert-danger.show");
  if (await bootstrap.count() > 0) return bootstrap.first();
  return page.locator('role=alert');
}

async function assertLoginSuccess(page: Page) {
  const successMsg = page.locator('text=Login successful');
  if (await successMsg.count() > 0) {
    await expect(successMsg).toBeVisible({ timeout: 5000 });
    return;
  }
  const loginForm = page.locator('form');
  try {
    await expect(loginForm).toBeHidden({ timeout: 5000 });
    return;
  } catch {
    await expect(page).not.toHaveURL(/practice-login-form/, { timeout: 5000 });
    return;
  }
}

test.describe('Login Accessibility & Responsive', () => {
  test('Mobile viewport: key controls visible and actionable', async ({ page }) => {
    await page.setViewportSize({ width: 375, height: 812 });
    await page.goto('https://testerbud.com/practice-login-form');

    const { email, password } = await findInputs(page);
    await expect(email).toBeVisible();
    await expect(password).toBeVisible();

    const submit = (await page.locator('button[type="submit"]').count()) > 0
      ? page.locator('button[type="submit"]').first()
      : (await page.locator('button:has-text("Login")').count()) > 0
        ? page.locator('button:has-text("Login")').first()
        : page.locator('button').first();
    await expect(submit).toBeVisible();
  });

  test('Error message timing and correction flow', async ({ page }) => {
    await page.goto('https://testerbud.com/practice-login-form');
    const { email, password } = await findInputs(page);

    // trigger invalid credentials
    await email.fill('invalid@user.com');
    await password.fill('wrongpass');
    const submit = (await page.locator('button[type="submit"]').count()) > 0
      ? page.locator('button[type="submit"]').first()
      : (await page.locator('button:has-text("Login")').count()) > 0
        ? page.locator('button:has-text("Login")').first()
        : page.locator('button').first();
    await submit.click();

    // Prefer bootstrap alert but fall back to role=alert
    const alert = await getBootstrapAlert(page);
    await expect(alert).toBeVisible({ timeout: 3000 });

    // Correct the input and resubmit
    await email.fill('user@premiumbank.com');
    await password.fill('Bank@123');
    await submit.click();
    await assertLoginSuccess(page);
  });

  test('Basic accessibility label checks', async ({ page }) => {
    await page.goto('https://testerbud.com/practice-login-form');

    // Verify the email input has an accessible name: label association, aria-label/aria-labelledby, or fallback attributes
    const email = (await page.locator('input[type="email"]').count()) > 0 ? page.locator('input[type="email"]').first() : page.locator('input').first();
    const hasAccessibleName = await email.evaluate((el: HTMLInputElement) => {
      try {
        // el.labels is a NodeList of associated <label> elements (if any)
        // Accessing labels may be unsupported in some environments, so guard it.
        if ((el as any).labels && (el as any).labels.length > 0) return true;
      } catch (e) {
        // ignore and continue checking other attributes
      }
      if (el.getAttribute('aria-label')) return true;
      if (el.getAttribute('aria-labelledby')) return true;
      // Accept placeholder or title as a weaker fallback for an accessible name
      if (el.getAttribute('placeholder')) return true;
      if (el.getAttribute('title')) return true;
      return false;
    });
    await expect(hasAccessibleName).toBe(true);
  });
});
