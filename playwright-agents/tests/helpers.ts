import { Page } from '@playwright/test';
import { DEFAULT_TIMEOUT } from './config';

export async function captureConsoleErrors(page: Page, fn: () => Promise<void>) {
  const errors: string[] = [];
  const handler = (msg: any) => { if (msg.type && msg.type() === 'error') errors.push(msg.text()); };
  page.on('console', handler);
  try {
    await fn();
  } finally {
    page.removeListener('console', handler as any);
  }
  return errors;
}

export async function waitForNoDialog(page: Page, action: () => Promise<void>, timeout = 500) {
  const dialogPromise = page.waitForEvent('dialog', { timeout }).then(async (d) => { await d.dismiss(); return true; }).catch(() => false);
  await action();
  return await dialogPromise;
}

export async function assertNativeTypeMismatch(page: Page, selector: string) {
  const el = await page.locator(selector).first();
  return await el.evaluate((e: HTMLInputElement) => e.validity && e.validity.typeMismatch ? true : false);
}
