// spec: tests/login_ui.spec.ts
// seed: tests/seed.spec.ts

import { test, expect } from '@playwright/test';

// UI and misc scenarios (Scenario 5, 6, 7, 11, 12)
test.describe('Login UI & Interaction', () => {
  test('Remember me checkbox preserves email when used', async ({ page }) => {
    await page.goto('https://testerbud.com/practice-login-form');
    const remember = page.locator('input[type="checkbox"], input[name="remember"]');
    if (await remember.count() === 0) {
      test.skip();
      return;
    }

    const email = page.locator('input[type="email"]').first();
    const pwd = (await page.locator('input[type="password"]').count()) > 0 ? page.locator('input[type="password"]').first() : page.locator('input').nth(1);

    await email.fill('user@premiumbank.com');
    await pwd.fill('Bank@123');
    await remember.check();
    const submit = (await page.locator('button[type="submit"]').count()) > 0 ? page.locator('button[type="submit"]').first() : page.locator('button').first();
    await submit.click();

  // Navigate away and back to assert persistence
  await page.goto('about:blank');
  await page.goto('https://testerbud.com/practice-login-form');
  // Wait for the email input to appear and assert it was actually persisted
  await page.waitForSelector('input[type="email"]', { timeout: 3000 });
  const emailVal = await page.locator('input[type="email"]').first().inputValue();
  // Expect the exact email to be present when 'remember me' is used
  expect(emailVal).toBe('user@premiumbank.com');
  });

  test('Long inputs do not truncate user input and do not produce console errors', async ({ page }) => {
    await page.goto('https://testerbud.com/practice-login-form');

    // Capture console errors during the operation
    const consoleErrors: string[] = [];
    page.on('console', (msg) => {
      if (msg.type() === 'error') consoleErrors.push(msg.text());
    });

    // Construct a long but syntactically valid email (long local-part + @domain)
    const localPart = 'a'.repeat(500);
    const longEmail = `${localPart}@example.com`;
    const longPassword = 'p'.repeat(500);

    const emailLocator = page.locator('input[type="email"]').first();
    const pwd = (await page.locator('input[type="password"]').count()) > 0 ? page.locator('input[type="password"]').first() : page.locator('input').nth(1);

    // Fill inputs with long values
    await emailLocator.fill(longEmail);
    await pwd.fill(longPassword);

    // Ensure the input kept the full value (no client-side truncation)
    const emailVal = await emailLocator.inputValue();
    expect(emailVal).toBe(longEmail);

    // And no console errors should have been emitted while typing or updating the UI
    expect(consoleErrors.length).toBe(0);
  });

  test('Keyboard navigation does not trap focus', async ({ page }) => {
    await page.goto('https://testerbud.com/practice-login-form');
    // Tab through a few elements and ensure focus changes from body
    for (let i = 0; i < 10; i++) await page.keyboard.press('Tab');
    const active = await page.evaluate(() => (document.activeElement && (document.activeElement as Element).tagName) || 'BODY');
    expect(active).not.toBe('BODY');
  });

  test('Key elements are present and visible', async ({ page }) => {
    await page.goto('https://testerbud.com/practice-login-form');
    const email = page.locator('input[type="email"]').first();
    const pwd = (await page.locator('input[type="password"]').count()) > 0 ? page.locator('input[type="password"]').first() : page.locator('input').nth(1);
    const submit = (await page.locator('button:has-text("Login")').count()) > 0 ? page.locator('button:has-text("Login")').first() : page.locator('button').first();
    await expect(email).toBeVisible();
    await expect(pwd).toBeVisible();
    await expect(submit).toBeVisible();
  });
});
