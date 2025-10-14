import { test, expect } from '@playwright/test';
import { APP_URL } from './config';

test.describe('Test group', () => {
  test('seed', async ({ page }) => {
     await page.goto(APP_URL);
  });
});
