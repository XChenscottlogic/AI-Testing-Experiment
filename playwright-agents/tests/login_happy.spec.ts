// spec: tests/login_happy.spec.ts
// seed: tests/seed.spec.ts

import { test, expect } from '@playwright/test';
import { LoginPage } from './pages/loginPage';
import { VALID_EMAIL, VALID_PASSWORD } from './config';

// Happy path tests (Scenario 1 & 4)

test.describe('Login Happy Flows', () => {
  test('Login by clicking primary button should succeed', async ({ page }) => {
    const login = new LoginPage(page);
    await login.goto();
  await login.fillEmail(VALID_EMAIL);
  await login.fillPassword(VALID_PASSWORD);
    await login.clickSubmit();
    await login.assertLoginSuccess();
  });

  test('Login by pressing Enter in password field should succeed', async ({ page }) => {
    const login = new LoginPage(page);
    await login.goto();
  await login.fillEmail(VALID_EMAIL);
  await login.fillPassword(VALID_PASSWORD);
    await login.submitByEnter();
    await login.assertLoginSuccess();
  });
});
