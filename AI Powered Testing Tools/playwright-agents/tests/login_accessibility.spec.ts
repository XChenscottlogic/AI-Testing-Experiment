// spec: tests/login_accessibility.spec.ts
// seed: tests/seed.spec.ts

import { test, expect } from '@playwright/test';
import { LoginPage } from './pages/loginPage';
import { VALID_EMAIL, VALID_PASSWORD } from './config';

test.describe('Login Accessibility & Responsive', () => {
  test('Mobile viewport: key controls visible and actionable', async ({ page }) => {
    const login = new LoginPage(page);
    await login.setMobileViewport();
    await login.goto();

    await expect(login.email()).toBeVisible();
    await expect(login.password()).toBeVisible();
    const submit = (await page.locator('button[type="submit"]').count()) > 0
      ? page.locator('button[type="submit"]').first()
      : (await page.locator('button:has-text("Login")').count()) > 0
        ? page.locator('button:has-text("Login")').first()
        : page.locator('button').first();
    await expect(submit).toBeVisible();
  });

  test('Error message timing and correction flow', async ({ page }) => {
    const login = new LoginPage(page);
    await login.goto();
  await login.fillEmail('invalid@user.com');
  await login.fillPassword('wrongpass');
    await login.clickSubmit();

    const alert = await login.bootstrapAlert();
    await expect(alert).toBeVisible({ timeout: 3000 });

  await login.fillEmail(VALID_EMAIL);
  await login.fillPassword(VALID_PASSWORD);
    await login.clickSubmit();
    await login.assertLoginSuccess();
  });

  test('Basic accessibility label checks', async ({ page }) => {
    const login = new LoginPage(page);
    await login.goto();
    const email = login.email();
    const hasAccessibleName = await email.evaluate((el: HTMLInputElement) => {
      try {
        if ((el as any).labels && (el as any).labels.length > 0) return true;
      } catch (e) {}
      if (el.getAttribute('aria-label')) return true;
      if (el.getAttribute('aria-labelledby')) return true;
      if (el.getAttribute('placeholder')) return true;
      if (el.getAttribute('title')) return true;
      return false;
    });
    await expect(hasAccessibleName).toBe(true);
  });
});
