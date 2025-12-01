# Playwright Tests — AI-Testing-Experiment

Playwright comes with three **Playwright Agents** out of the box: 🎭 **planner**, 🎭 **generator**, and 🎭 **healer**.

These agents can be used **independently**, **sequentially**, or as **chained calls** in the agentic loop.  
Using them sequentially will produce **test coverage for your product**.

- 🎭 **planner** — explores the app and produces a **Markdown test plan**  
- 🎭 **generator** — transforms the Markdown plan into **Playwright Test files**  
- 🎭 **healer** — executes the test suite and **automatically repairs failing tests**


Quick notes and run commands for Windows PowerShell.

Prerequisites
- Node.js (16+ recommended)
- Playwright installed as a dev dependency (see package.json)

Install

```powershell
npm install
npx playwright install
```

Run tests (default project configuration)

```powershell
# run all tests
npx playwright test

# run a single file
npx playwright test tests\login_happy.spec.ts

# run with headed browser for debugging
npx playwright test --headed

# run only in chromium project
npx playwright test --project=chromium
```

Debug a single test interactively

```powershell
npx playwright test tests\login_happy.spec.ts -g "Login by clicking primary button" --debug
```

Where to change credentials

- `tests/config.ts` contains `VALID_EMAIL` and `VALID_PASSWORD` and `APP_URL`.

Click on [Playwright Agents](https://medium.com/@ismailsobhy/ai-powered-test-automation-part-4-complete-guide-to-playwright-agents-planner-generator-healer-d418166afe34) if you would like to find out more


