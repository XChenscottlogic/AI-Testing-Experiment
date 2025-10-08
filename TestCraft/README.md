# TestCraft Research

This repository contains exploratory work and automation examples created as part of my research into **TestCraft**, an AI-assisted testing framework designed to accelerate test creation and analysis.

---

## 🔍 Overview

The focus of this project is to evaluate how **TestCraft** integrates with existing testing practices and tools — particularly **Playwright** for web automation. I have explained in my notes what the Test Craft AI Agent does but haven't yet experimented with it for **API test automation**.

This repo includes:
- AI generated Playwright test suite for form input validation created with TestCraft
- A link to a Miro page detailing key findings and insights

---

## 🧭 Research & Findings

You can view the detailed research notes, comparisons, and findings on my interactive **Miro board**:

👉 [View the Miro board on TestCraft Research & Findings](https://miro.com/app/board/uXjVJ9zIQqc=/?share_link_id=62235004123)

The board includes:
- A breakdown of TestCraft’s automation generation capabilities
- Pros and cons of AI-generated tests     
- Observations on Playwright integration  
- Suggested improvements and test coverage extensions
- Accessibility test results   

---

## ⚙️ Running the Tests

To explore the Playwright-based tests:

```bash
# Clone the repository
git clone https://github.com/XChenscottlogic/AI-Testing-Experiment.git

# Navigate into the project
cd AI-Testing-Experiment/TestCraft

# Install dependencies
npm install

# Run Playwright tests
npx playwright test
