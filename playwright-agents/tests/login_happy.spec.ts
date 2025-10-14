// spec: tests/login_happy.spec.ts
// seed: tests/seed.spec.ts

import { test, expect, Page, Locator } from '@playwright/test';

// Happy path tests (Scenario 1 & 4)
// Helper: discover input locators (robust fallbacks)
async function findInputs(page: Page): Promise<{ email: Locator; password: Locator }> {
  const email = (await page.locator('input[type="email"]').count()) > 0
    ? page.locator('input[type="email"]').first()
    : page.locator('input').first();
  const password = (await page.locator('input[type="password"]').count()) > 0
    ? page.locator('input[type="password"]').first()
    : page.locator('input').nth(1);
  return { email, password };
}

// Helper: centralize success detection (message OR form hidden OR URL change)
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

test.describe('Login Happy Flows', () => {
  test('Login by clicking primary button should succeed', async ({ page }) => {
    await page.goto('https://testerbud.com/practice-login-form');
    const { email, password } = await findInputs(page);
    await email.fill('user@premiumbank.com');
    await password.fill('Bank@123');

    const submit = (await page.locator('button[type="submit"]').count()) > 0
      ? page.locator('button[type="submit"]').first()
      : (await page.locator('button:has-text("Login")').count()) > 0
        ? page.locator('button:has-text("Login")').first()
        : page.locator('button').first();

    await submit.click();
    await assertLoginSuccess(page);
  });

  test('Login by pressing Enter in password field should succeed', async ({ page }) => {
    await page.goto('https://testerbud.com/practice-login-form');
    const { email, password } = await findInputs(page);
    await email.fill('user@premiumbank.com');
    await password.fill('Bank@123');
    await password.press('Enter');
    await assertLoginSuccess(page);
  });
});
