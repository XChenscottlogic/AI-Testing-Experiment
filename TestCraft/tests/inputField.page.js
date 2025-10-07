// inputField.page.js
class InputFieldPage {
    constructor(page) {
        this.page = page;
        this.inputField = page.locator('#inputUsername');
        this.submitButton = page.locator('.signInBtn');
        this.errorMessage = page.locator('p.error');
    }

    async enterUsername(username) {
        await this.inputField.fill(username);
    }

    async getPlaceholder() {
        return await this.inputField.getAttribute('placeholder');
    }

    async isFocused() {
        return await this.inputField.evaluate((el) => el === document.activeElement);
    }

    async getValue() {
        return await this.inputField.inputValue();
    }

    async clearInput() {
        await this.inputField.fill('');
    }

    async isVisible() {
        return await this.inputField.isVisible();
    }

    async submitForm() {
        await this.submitButton.click();
    }

    async isErrorVisible() {
        return await this.errorMessage.isVisible();
    }

    async getErrorText() {
        return await this.errorMessage.textContent();
    }
}

module.exports = InputFieldPage;
