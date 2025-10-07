// inputField.spec.js
const { test, expect } = require('@playwright/test');
const InputFieldPage = require('./inputField.page');

test.describe('Username Input Field Tests', () => {
    let inputFieldPage;

    test.beforeEach(async ({ page }) => {
        inputFieldPage = new InputFieldPage(page);
        await page.goto('https://rahulshettyacademy.com/locatorspractice/');
    });

    test('The Username input field is visible and has correct placeholder text', async () => {
        expect(await inputFieldPage.isVisible()).toBeTruthy();
        expect(await inputFieldPage.getPlaceholder()).toBe('Username');
    });

    test('User can type a valid alphanumeric username', async () => {
        await inputFieldPage.enterUsername('User123');
        expect(await inputFieldPage.getValue()).toBe('User123');
    });

    test('The field can be cleared after typing', async () => {
        await inputFieldPage.enterUsername('TestUser');
        await inputFieldPage.clearInput();
        expect(await inputFieldPage.getValue()).toBe('');
    });

    test('Submitting an empty username shows an error message', async () => {
        await inputFieldPage.clearInput();
        await inputFieldPage.submitForm();
        await expect(inputFieldPage.errorMessage).toBeVisible({ timeout: 5000 });
        expect(await inputFieldPage.isErrorVisible()).toBeTruthy();
        expect(await inputFieldPage.getErrorText()).toContain('* Incorrect username or password ');
    });

    test('Submitting any username with wrong password shows error message (no client validation)', async () => {
        await inputFieldPage.enterUsername('SomeUser');
        await inputFieldPage.submitForm();
        await expect(inputFieldPage.errorMessage).toBeVisible({ timeout: 5000 });
        expect(await inputFieldPage.isErrorVisible()).toBeTruthy();
        expect(await inputFieldPage.getErrorText()).toContain('* Incorrect username or password ');
    });

    test('The Username field accepts special characters (no restrictions applied)', async () => {
        await inputFieldPage.enterUsername('User@123!');
        expect(await inputFieldPage.getValue()).toBe('User@123!');
    });

    test('Check the Username field remains functional on different device viewports', async ({ page }) => {
        const sizes = [
            { width: 375, height: 667 },   // Mobile
            { width: 768, height: 1024 },  // Tablet
            { width: 1920, height: 1080 }  // Desktop
        ];
        for (const size of sizes) {
            await page.setViewportSize(size);
            expect(await inputFieldPage.isVisible()).toBeTruthy();
        }
    });

    test('The Username field is auto-focused on load (expected behavior)', async () => {
        expect(await inputFieldPage.isFocused()).toBeTruthy();
    });

    test('Whitespace is preserved (no trimming behaviour)', async () => {
        await inputFieldPage.enterUsername('   User   ');
        expect(await inputFieldPage.getValue()).toBe('   User   ');
    });
});
