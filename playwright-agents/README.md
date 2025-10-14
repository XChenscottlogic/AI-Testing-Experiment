# Playwright Tests — AI-Testing-Experiment

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

If you need me to run/adjust tests further, run the suite locally and paste failures or traces here.
