import { test, expect } from '@playwright/test';
import { LoginPage } from './pages/loginPage';
import { VALID_EMAIL, VALID_PASSWORD } from './config';
import { waitForNoDialog, assertNativeTypeMismatch } from './helpers';

test.describe('Login Negative Flows', () => {
  test('Invalid credentials shows an error', async ({ page }) => {
    const login = new LoginPage(page);
    await login.goto();
    await login.fillEmail('invalid@user.com');
    await login.fillPassword('wrongpass');
    await login.clickSubmit();

    const alert = await login.bootstrapAlert();
    await expect(alert).toBeVisible({ timeout: 3000 });
    await expect(alert).toContainText('Invalid email id and password');
  });

  test('Empty fields validation shows required errors', async ({ page }) => {
    const login = new LoginPage(page);
    await login.goto();
    await login.clickSubmit();

    const alert = await login.bootstrapAlert();
    await expect(alert).toBeVisible({ timeout: 3000 });
    await expect(alert).toContainText('Email and Password are required');
  });

  test('Whitespace-only inputs are rejected', async ({ page }) => {
    const login = new LoginPage(page);
    await login.goto();
  await login.fillEmail(`   ${VALID_EMAIL}   `);
  await login.fillPassword(`   ${VALID_PASSWORD}   `);
    await login.clickSubmit();

    const alert = await login.bootstrapAlert();
    await expect(alert).toBeVisible({ timeout: 3000 });
    await expect(alert).toContainText('Invalid email id and password');
  });

  test('XSS payloads do not execute and are handled safely', async ({ page }) => {
    const login = new LoginPage(page);
    await login.goto();
    await login.fillEmail("<script>alert('xss')</script>");
    await login.fillPassword('password');

  const isTypeMismatch = await assertNativeTypeMismatch(page, 'input[type="email"]');
  await expect(isTypeMismatch).toBe(true);

  const validationMessage = await login.email().evaluate((el: HTMLInputElement) => el.validationMessage);
  await expect(validationMessage.length).toBeGreaterThan(0);

    const dialogShown = await waitForNoDialog(page, async () => { await login.clickSubmit(); }, 500);
    expect(dialogShown).toBe(false);

    await expect(page.locator('text=<script>')).not.toBeVisible({ timeout: 1000 });

    const err = await login.bootstrapAlert();
    await expect(err).toBeVisible({ timeout: 3000 });
  });

  test('SQL injection payloads are rejected or safely handled', async ({ page }) => {
    const login = new LoginPage(page);
    await login.goto();
    await login.fillEmail("' OR '1'='1");
    await login.fillPassword('anything');
    await login.clickSubmit();

    const alert = await login.bootstrapAlert();
    await expect(alert).toBeVisible({ timeout: 3000 });
  });
});

