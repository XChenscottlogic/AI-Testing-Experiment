# Mabl — Research Report

**Summary**  
Mabl is an AI-powered intelligent test automation platform that integrates machine learning, expert systems, and generative AI (GenAI) to streamline the creation, execution, and maintenance of UI and API tests. It continuously learns from each test run, autonomously healing broken tests and providing actionable insights through automated analysis. With advanced features like Visual Find, GenAI Assertions, and Auto Test Failure Analysis (Auto TFA), Mabl represents a major leap toward self-maintaining, adaptive QA automation.

**Link:** [Mabl](https://help.mabl.com/hc/en-us/articles/26881384186004-How-mabl-enhances-your-testing-with-AI)

---

## 1. Capabilities Overview

### I. Features

#### 🔹 AI-Powered Test Creation
- **GenAI Test Creation Agent:** Automatically generates web, mobile and API tests from natural language prompts.
  **To Create UI Tests**
  No human input is required to generate a test from a workflow. For example, Mabl can autonomously decide to navigate to the “News” section of the BBC website and verify the title and content of the first article.
  ![To Create UI Tests](https://github.com/XChenscottlogic/AI-Testing-Experiment/blob/Xin-branch/Mabl/Screenshot%20Generate%20Steps.png)
  **UI Test Generation**
  ![UI Test Generation](https://github.com/XChenscottlogic/AI-Testing-Experiment/blob/Xin-branch/Mabl/Screenshot%20UI%20Test%20Generation%201.png)
  ![UI Test Generation](https://github.com/XChenscottlogic/AI-Testing-Experiment/blob/Xin-branch/Mabl/Screenshot%20UI%20Test%20Generation%202.png)
- **Model-Based Element Recognition:** Builds adaptive models of UI elements rather than relying on static selectors.  
- **Expert System + ML Fusion:** Combines rules-based heuristics with real-time AI decision-making for resilient test automation.  
- **Auto-Healing:** Automatically repairs test scripts when UI or API structures change.  

#### 🔹 API Test Creation
- Define test intent using plain language; GenAI creates structured test steps.  
- Supports OpenAPI, GraphQL, Postman, and custom API schema uploads.  
- Auto-generates tasks, assertions, and data variables.  
- Integrates dynamic parameters and variable substitution.
![Define API Test](https://github.com/XChenscottlogic/AI-Testing-Experiment/blob/Xin-branch/Mabl/Screenshot%20Create%20API%20testing.png)
![API Test Generation](https://github.com/XChenscottlogic/AI-Testing-Experiment/blob/Xin-branch/Mabl/Screenshot%20AI%20Generation%20for%20API%20test.png)
![API Test Assertion](https://github.com/XChenscottlogic/AI-Testing-Experiment/blob/Xin-branch/Mabl/Screenshot%20Generated%20Assertions.png)

#### 🔹 Visual Find (AI-Based Element Detection)
- Uses AI to identify elements visually, rather than relying on selectors or text attributes. Visual find is currently supported only for tap steps in mobile tests. 
- Ideal for elements in **mobile apps**, PDFs, or canvas-based UIs that lack unique identifiers.  
- Automatically generates an AI-driven description of the target element during training.  
- Supports coordinate adjustment for fine-grained control over tap locations.  
- Ensures test accuracy through visual matching on execution.  

#### 🔹 GenAI Assertions
- Validates complex aspects of an application such as **text, visuals, layout, and data relevance** using GenAI.  
- Assertions are written in natural language and can reference dynamic variables.  
- Provides context-aware AI-generated validation criteria that evolve with test updates.  
- Supports both **page-level** and **element-level** assertions.  
- Enables viewport control for accurate rendering during validation.  
- Output can be requested in **non-English languages** by specifying the target language in the prompt.  
- Execution limitations: up to 30 AI assertions per cloud test; not supported for CLI, CI, or performance tests.  

#### 🔹 Auto Test Failure Analysis (Auto TFA)
- Automatically analyses failed tests using a large language model (LLM).  
- Provides AI-generated summaries explaining likely causes of failures.  
- Suggests root causes and failure reasons for browser, mobile, and API tests.  
- Analyzes logs, screenshots, variables, request/response data, and previous passing runs for comparison.  
- Supported for browser, mobile, and API tests; not supported for performance or crawler plan failures.  
![Auto Test Failure Analysis](https://github.com/XChenscottlogic/AI-Testing-Experiment/blob/Xin-branch/Mabl/Screenshot%20Analyse%20Test%20Failure.png)


#### 🔹 AI-Based Reporting & Test Impact Analysis
- Identifies which areas of an application are most affected by recent changes.  
- Generates human-readable reports and failure insights.  
- Enables intelligent regression testing and prioritisation.  

---

## 2. Typical Use Cases

- Accelerating browser and API test creation using AI-generated workflows.  
- Automatically healing tests when UI or API changes break existing selectors.  
- Using **Visual Find** to test apps with dynamic, visual-only UI elements (mobile testing only).  
- Verifying text and visual consistency with **GenAI Assertions**.  
- Reducing test review time through **Auto Test Failure Analysis** summaries.  
- Enhancing continuous integration (CI/CD) pipelines with self-healing and intelligent test prioritization.  
- Scaling QA coverage for fast-moving agile development environments.  

---

## 3. Pros

- **Drastically Reduced Maintenance:** AI healing and adaptive selectors minimize manual updates.  
- **Natural Language Test Authoring:** Allows test generation from simple, human-readable prompts.  
- **Visual + Semantic Testing:** Combines DOM-based, visual, and generative AI models for robust validation.  
- **Rich Failure Insights:** AI failure analysis accelerates root cause detection.  
- **Cross-Platform Support:** Works across browser, API, and mobile environments.  
- **Continuous Learning:** Models update automatically with every test run, improving reliability over time.  
- **Supports Data-Driven Testing:** Dynamic variables and data tables enable flexible validation.  

---

## 4. Cons & Limitations

- **Limited Negative Test Coverage:** GenAI-generated tests require additional human input to design more negative test cases to cover the edge cases.
- **Auth Gaps:** OAuth 1.0 and 2.0 authentication must be configured manually.  
- **Execution Limits:** GenAI Assertions limited to 30 per test in cloud runs.  
- **Local Restrictions:** GenAI Assertions and Auto TFA unavailable in local or CI Runner executions.  
- **Manual Intervention:** Visual Find and GenAI steps may require occasional manual fine-tuning for accuracy.  
- **Complex API Schemas:** Deeply nested or ambiguous schemas can cause incomplete test generation. 
- **English Bias:** GenAI features (Assertions, Test Creation) are primarily optimised for English.  

---

## 5. Pricing Snapshot

Mabl is a commercial tool and it offers a 14-day free trial.


---

## 6. Recommendation

**✅ Recommended For:**  
- QA teams seeking intelligent, low-maintenance automation.  
- Organisations adopting continuous testing or DevOps pipelines.  
- Teams needing visual, language-based, or API-driven validation.  
- Enterprises wanting AI-assisted failure analysis and autonomous test execution.  

**⚠️ Use Caution If:**  
- Your testing relies heavily on localised (non-English) content.  
- You require high control over deeply scripted or authenticated tests.  
- Your organisation’s compliance policies restrict the use of external AI models for test data analysis. 
- Your require minimum efforts to achieve a good test coverage. 
