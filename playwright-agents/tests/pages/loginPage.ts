import { Page, Locator, expect } from '@playwright/test';
import { APP_URL, DEFAULT_TIMEOUT } from '../config';

export class LoginPage {
  readonly page: Page;
  constructor(page: Page) {
    this.page = page;
  }

  async goto() {
    await this.page.goto(APP_URL);
  }

  email(): Locator {
    return this.page.locator('input[type="email"], input[name="email"]').first();
  }

  password(): Locator {
    return this.page.locator('input[type="password"], input[name="password"]').first();
  }

  async fillEmail(value: string) {
    await this.email().fill(value);
  }

  async fillPassword(value: string) {
    await this.password().fill(value);
  }

  async clickSubmit() {
    const submit = (await this.page.locator('button[type="submit"]').count()) > 0
      ? this.page.locator('button[type="submit"]').first()
      : (await this.page.locator('button:has-text("Login")').count()) > 0
        ? this.page.locator('button:has-text("Login")').first()
        : this.page.locator('button').first();
    await submit.click();
  }

  async submitByEnter() {
    await this.password().press('Enter');
  }

  async bootstrapAlert(): Promise<Locator> {
    const bootstrap = this.page.locator("div.fade.alert.alert-danger.show");
    if (await bootstrap.count() > 0) return bootstrap.first();
    return this.page.locator('role=alert');
  }

  async assertLoginSuccess() {
    const successMsg = this.page.locator('text=Login successful');
    if (await successMsg.count() > 0) {
      await expect(successMsg).toBeVisible({ timeout: DEFAULT_TIMEOUT });
      return;
    }
    const loginForm = this.page.locator('form');
    try {
      await expect(loginForm).toBeHidden({ timeout: DEFAULT_TIMEOUT });
      return;
    } catch {
      await expect(this.page).not.toHaveURL(/practice-login-form/, { timeout: DEFAULT_TIMEOUT });
      return;
    }
  }

  async setMobileViewport() {
    await this.page.setViewportSize({ width: 375, height: 812 });
  }
}
