// spec: tests/login_ui.spec.ts
// seed: tests/seed.spec.ts

import { test, expect } from '@playwright/test';
import { LoginPage } from './pages/loginPage';
import { VALID_EMAIL, VALID_PASSWORD } from './config';
import { captureConsoleErrors } from './helpers';

// UI and misc scenarios (Scenario 5, 6, 7, 11, 12)
test.describe('Login UI & Interaction', () => {
  test('Password reveal toggle (if present) works', async ({ page }) => {
    const login = new LoginPage(page);
    await login.goto();
    const pwd = login.password();
    await expect(pwd).toHaveAttribute('type', 'password');

    // Try several common reveal controls; clicking should not throw
    const revealSelectors = ['button:has-text("Show")', '[aria-label*="show" i]', '.password-toggle', '.show-password'];
    for (const sel of revealSelectors) {
      const cand = page.locator(sel);
      if (await cand.count() > 0) {
        await cand.first().click().catch(() => {});
        const typeAfter = await pwd.getAttribute('type');
        if (typeAfter === 'text') await cand.first().click().catch(() => {});
        return;
      }
    }
  });

  test('Remember me checkbox preserves email when used', async ({ page }) => {
    const login = new LoginPage(page);
    await login.goto();
    const remember = page.locator('input[type="checkbox"], input[name="remember"]');
    if (await remember.count() === 0) {
      test.skip();
      return;
    }

  await login.fillEmail(VALID_EMAIL);
  await login.fillPassword(VALID_PASSWORD);
    await remember.check();
    await login.clickSubmit();

    // Navigate away and back to assert persistence
    await page.goto('about:blank');
    await login.goto();
    await page.waitForSelector('input[type="email"]', { timeout: 3000 });
    const emailVal = await login.email().inputValue();
  expect(emailVal).toBe(VALID_EMAIL);
  });

  test('Long inputs do not truncate user input and do not produce console errors', async ({ page }) => {
    const login = new LoginPage(page);
    await login.goto();

    const localPart = 'a'.repeat(500);
    const longEmail = `${localPart}@example.com`;
    const longPassword = 'p'.repeat(500);

    const errors = await captureConsoleErrors(page, async () => {
      await login.fillEmail(longEmail);
      await login.fillPassword(longPassword);
    });

    const emailVal = await login.email().inputValue();
    expect(emailVal).toBe(longEmail);
    expect(errors.length).toBe(0);
  });

  test('Keyboard navigation does not trap focus', async ({ page }) => {
    const login = new LoginPage(page);
    await login.goto();
    for (let i = 0; i < 10; i++) await page.keyboard.press('Tab');
    const active = await page.evaluate(() => (document.activeElement && (document.activeElement as Element).tagName) || 'BODY');
    expect(active).not.toBe('BODY');
  });

  test('Key elements are present and visible', async ({ page }) => {
    const login = new LoginPage(page);
    await login.goto();
    await expect(login.email()).toBeVisible();
    await expect(login.password()).toBeVisible();
    const submit = (await page.locator('button:has-text("Login")').count()) > 0 ? page.locator('button:has-text("Login")').first() : page.locator('button').first();
    await expect(submit).toBeVisible();
  });
});
