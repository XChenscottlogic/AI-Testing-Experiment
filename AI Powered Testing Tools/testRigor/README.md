# testRigor

## Summary  
testRigor is an AI-driven test automation platform that lets you write end-to-end functional tests in **plain English**, without traditional coding. It translates natural-language test steps into executable actions, emulating a human (or “human emulator”) interacting with your UI.  

By combining AI, self-healing, and behavior-driven patterns, testRigor helps teams reduce test maintenance, increase coverage, and free up engineering resources.

---

## Capabilities Overview  
- **Plain-English Test Writing**: Write tests like “purchase a Kindle” or “click on menu,” and testRigor interprets and executes it.
- **AI-Based Parsing & LLM Integration**: Uses a large language model (LLM) plus its own command set to turn English instructions into low-level test operations.
- **Self-Healing / AI Object Recognition**: For UI interactions, testRigor will use AI to classify elements (buttons, inputs, texts), even inferring meaning to maintain tests as the UI changes.  
- **Mobile Testing**: Supports Android and iOS (native and hybrid) apps. 
- **Reusable Rules / Functions**: Define subroutines (reusable test steps) to avoid duplication.
- **2FA, Email, SMS, Phone Handling**: Test flows including two-factor authentication, Twilio-based SMS/calls, email attachments, and validation with English commands. 
- **Data-Driven Testing**: Use data sets, global variables or external data to drive tests.
- **AI Security & Privacy Controls**: testRigor’s AI is used with oversight, encrypted data, and role-based access to ensure safety and control.
- **Reporting & Execution Feedback**: Captures screenshots, logs, videos; also supports reviewing AI-generated test flows before execution.
- **CI/CD Integration**: Can be triggered as part of pipelines; built to support continuous testing practices.
- **Cross-Platform**: Supports web, mobile, API, and even desktop (Windows) applications.

---

## Typical Use Cases  
- Manual testers or business testers writing automated tests in plain English, without needing to learn Selenium or code.  
- Teams wanting to automate login flows, complex user journeys, or cross-browser interactions with minimal maintenance.  
- Applications with frequent UI changes: using testRigor’s self-healing to reduce broken tests.  
- End-to-end testing of mobile apps (Android/iOS) including flows with SMS or 2FA.  
- Regression suites where data variation matters: running the same test with different datasets.  
- Security-sensitive environments, where AI usage must be auditable, with oversight and encryption.  
- High-scale testing in CI/CD: testRigor tests can be run as part of build/deploy pipelines.

---

## Pros  
- **Highly accessible**: Because tests are written in English, non-developers (testers, business users) can contribute to automation.
- **Reduced maintenance**: Self-healing AI means less brittle scripts and fewer test failures when UI changes.
- **Behavioral accuracy**: Tests run from a user's perspective, rather than relying on fragile locators, making them more resilient.
- **Flexible for different test types**: Supports web, mobile, API, email, SMS, 2FA, and desktop.
- **Security-first AI**: The platform is designed with data privacy, human oversight, and explainability in mind.
- **Scalable test creation**: Generative AI and LLMs can accelerate building test cases, saving time.
- **Reusable rules**: Modular test steps improve maintainability and make test design more efficient. 

---

## Cons and Limitations  
- **Trust & validation required**: Because AI generates or interprets tests, teams need to validate generated scripts and may want to fine-tune them. 
- **Learning curve**: While English-based, you still need to learn testRigor’s command set and how to phrase descriptions for the best results 
- **Cost**: High usage, large test suites or parallel runs may lead to significant licensing costs (especially in enterprise scenarios).  
- **No code reviews like traditional code**: As tests are described in English, version control or peer review can be less straightforward. (Some users report challenges reviewing test logic.)
- **Cloud dependency**: If using their SaaS platform, network latency or restrictions could impact performance.  
- **Edge case UI handling**: Very unusual or highly dynamic UI elements might confuse AI recognition or require manual intervention.  
- **AI misinterpretation risk**: LLM-based parsing might sometimes generate incorrect steps (requiring human correction).

---

## Pricing Snapshot  
- testRigor offers a **free / trial tier** (public tests) so teams can explore functionality.
- Paid plans available with **private test suites**: enterprise pricing varies based on usage, number of test cases, and parallel execution capacity. 
- As with many AI-driven tools, cost may scale significantly with heavier usage (e.g., many test runs, large test suites) and more advanced needs.

---

## Recommendation  

### Recommended For  
- Teams with **manual testers or non-programmers** who want to contribute to automation directly.  
- Organizations that want to **reduce maintenance burden** of automation through self-healing.  
- Product / QA teams that want to **rapidly generate and run tests** using natural language.  
- Projects where **mobile flows (with SMS, 2FA, or email)** are core to testing.  
- Companies that care about **AI transparency, security, and privacy**. testRigor provides human oversight and data controls.  
- DevOps teams doing **continuous testing** and needing tests that are easy to understand, modify, and execute.

### Use Caution If  
- You need **very complex logic or highly technical test scripts**: plain-English may not always capture edge-case technical behavior.  
- Your team is very code-centric and prefers writing test scripts in code (e.g. Selenium, JS, Python).  
- You require traditional **code review workflows** for test logic and find reviewing English-based steps cumbersome.  
- You operate in a **highly restricted or offline environment** (air-gapped), making cloud dependence problematic.  
- Your UI is extremely dynamic or unconventional, and AI-based element recognition may struggle.

