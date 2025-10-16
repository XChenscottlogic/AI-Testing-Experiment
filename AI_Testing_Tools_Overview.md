# AI Testing Tools Overview
A brief summary of a testing tool in test design, automation, environment and execution. </br>
✅Yes ❌No 🚫N/A

## Features ##
| Feature                      |KushoAI  |TestCraft  |Maestro |Postbot   |AI Test Case and Data Generator|NVIDIA NeMo Data Designer  |Testim Copilot Coding Assistant  |Playwright Agents| Mabl  |
|------------------------------|---------|-----------|--------|----------|-------------------------------|---------------------------|---------------------------------|-----------------|-------|
|**Open Source**               |❌       |✅        | ✅     | ❌      |✅                            |❌                         |❌                               |✅              |❌     |
|**Free Plan**                 |✅       |✅        | ✅     |✅       |✅ (10 cases per month)       |❌ (free 90 day in prod)   |❌ ( 30-day trial )              |✅              |❌ ( 14-day trial )|  
|**SUT Type**                  |Traditional App (No AI)    | Traditional App (No AI) |  Traditional App (No AI)       |Traditional App (No AI)     |Traditional App (No AI)| AI-based App & Traditional App (No AI) |  Traditional App (No AI)  |Traditional App (No AI)|Traditional App (No AI)|
|**AI Models**                 |Unclear. Foundational models along with their own pre-trained models  |  GPT-4o-mini by default but other models available         | Defaults: gpt-4o for OpenAI, claude-3-5-sonnet-20240620 for Claude        |OpenAI models         |gpt-4.1-mini but can be changed with openAI API key| Configurable - Any model |OpenAI models         |GPT-5 mini - other models available|Gemini, OpenAI, and Claude  |
|**Primary Focus**             |API/UI Functional Testing         |UI/Accessibility Testing         | Mobile/Browser UI        | API Functional and Performance Testing        |Test Case and Data Generator|Synthetic Data Generation  |UI Testing    |Test Case Generator & Automated UI tests|API/UI/Mobile Testing |
|**Installation Prerequisite** |- Kusho account</br> - Kusho UI Test Recorder as a Chrome extension  | Chrome Extension          | Maestro  Studio and an iOS/Android emulator        |Not required as integrated into Postman UI         |Not required|Docker and Docker Compose, NGC API Key, NGC CLI   |-Testim account</br> - Testim Editor as a Chrome or Edge extension |Install definitions to project| Mabl Desktop App |
|**Supported Languages**       | Java</br> Python</br> C#  |  JS</br> Python</br> C#</br> Java</br> TS         |  Actions written in .yaml file       |JavaScript          |Data generator - JSON, CSV, SQL Insert Statements, XML, HTML Table, BDD Gherkin | Python  | JavaScript| Typescript/Javascript| JavaScript |
|**Supported Platform**        |Playwright</br> Cypress</br> Selenium</br>        |  Playwright</br> Cypress</br> Selenium</br>         | Can be used no matter what framework the team uses        |Postman         |🚫|  NeMo Microservices Python SDK  | 🚫 |Playwright| 🚫 |
|**Officail Link**             | https://docs.kusho.ai/       |  https://home.testcraft.app/         |  https://maestro.dev/       |https://www.postman.com/product/postbot/         |https://www.testingtools.ai/free-tools/ai-test-case-generator/|   https://docs.nvidia.com/nemo/microservices/latest/generate-synthetic-data/index.html|  https://help.testim.io/docs/coding-assistant| https://playwright.dev/docs/test-agents | https://help.mabl.com/hc/en-us/articles/26881384186004-How-mabl-enhances-your-testing-with-AI|
|**Research Report**           | [KushoAI](https://github.com/XChenscottlogic/AI-Testing-Experiment/blob/main/KushoAI/README.md)      |  [TestCraft](https://github.com/XChenscottlogic/AI-Testing-Experiment/blob/main/TestCraft/README.md)        | [Maestro](https://github.com/XChenscottlogic/AI-Testing-Experiment/blob/main/Maestro/README.md)         |[Postbot](https://github.com/XChenscottlogic/AI-Testing-Experiment/blob/main/Postbot/README.md)         |[AI Test Case & Data Generator](https://github.com/XChenscottlogic/AI-Testing-Experiment/tree/main/AI%20Test%20Case%20%26%20Data%20Generator)| [NVIDIA NeMo Data Designer](https://github.com/XChenscottlogic/AI-Testing-Experiment/tree/main/NVIDIA%20NeMo%20Data%20Designer)| [Testim Copilot Coding Assistant](https://github.com/XChenscottlogic/AI-Testing-Experiment/blob/main/Testim/README.md) |[Playwright Agents](https://github.com/XChenscottlogic/AI-Testing-Experiment/blob/main/playwright-agents/README.md) |[Mabl](https://github.com/XChenscottlogic/AI-Testing-Experiment/blob/Xin-branch/Mabl/README.md)|
|**Company Profile**           |Based in San Francisco (United States)</br> Founded in 2023       |    🚫       | 🚫        |Developed by Postman in 2023         |🚫| Formerly Gretel, acquired by Nvidia in 2025.  |Based in San Francisco (United States)</br> Founded in 2014 | Playwright | Based in Boston (United States)</br> Founded in 2016| 

## 	Test Design ##
| Test Design                               | KushoAI | TestCraft | Maestro    | Postbot |AI Test Case and Data Generator|NVIDIA NeMo Data Designer  |Testim Copilot Coding Assistant  | Playwright |Mabl  |
|-------------------------------------------|---------|-----------|------------|---------|-------------------------------|---------------------------|---------------------------------|------------|------|
|**Analyse and Interpret Business Logic**   |❌       |❌        | ❌        |❌       |✅                             |❌                        |❌                               |✅         |❌    |
|**Generate Test Ideas in Plain Language**  |✅       |✅        | ✅        |❌       |✅                             |❌                        |❌                               |✅         |✅    |
|**Generate Test Strategy & Test plan**     |❌       |❌        | ❌        |❌       |❌                             |❌                        |✅*                              |✅         |✅*   |
|**Generate Testing Cases**                 |✅       |✅        | ✅        |✅       |✅                             |❌                        |✅                               |✅         |✅    |
|**Generate End-to-End Testing Scripts**    |✅ (not on free plan)      |❌        | ✅        |❌       |✅           |❌                        |✅*                              |✅         |✅    |
|**Manage Test Suite or Cases**             |✅       |❌        | ❌        |❌       |❌                             |❌                        |✅*                              |✅         |✅*   |
|**Identify Risky Areas**                   |❌       |✅        | ❌        |❌       |✅                             |❌                        |❌                               |✅         |❌    |

## 	Test Automation ##
| Test Automation                           | KushoAI | TestCraft | Maestro | Postbot |AI Test Case and Data Generator|NVIDIA NeMo Data Designer  |Testim Copilot Coding Assistant  |Playwright|Mabl  |
|-------------------------------------------|---------|-----------|---------|---------|-------------------------------|---------------------------|---------------------------------|----------|------|
|**Generate Test Automation Framework**     |❌      |❌         |❌       |❌      |❌                            |❌                         |❌                               |✅       |❌    |
|**Generate API Test Automation Scripts**   |❌      |❌         | ❌      |✅      |❌                            |❌                         |❌                               |✅       |✅    |
|**Generate UI Test Automation Scripts**    |✅      |✅         | ✅      |❌      |❌                            |❌                         |✅                               |✅       |✅    |
|**Refactor Existing Code**                 |❌      |❌         | ❌      |❌      |❌                            |❌                         |❌                               |✅       |✅    |
|**Assist Debugging**                       |❌      |❌         | ❌      |✅      |❌                            |❌                         |✅                               |✅       |✅    |    

## 	Test Environment ##
| Test Environment                          | KushoAI | TestCraft | Maestro | Postbot |AI Test Case and Data Generator|NVIDIA NeMo Data Designer|Testim Copilot Coding Assistant      |Playwright|Mabl  |
|-------------------------------------------|---------|-----------|---------|---------|-------------------------------|-------------------------|-------------------------------------|---------|-------|
|**Generate Synthetic Test Data**           |✅       |❌        |❌       |❌      |✅                             |✅                      |✅*                                  |✅      |❌     |
|**Set Up Test Environment**                |✅       |❌        |❌       |❌      |❌                             |❌                      |✅*                                  |✅      |❌     |
|**Integrate with CI/CD**                   |✅ (not on free plan) |❌     |✅ (not on free plan)|❌      |❌       |❌                      |✅*                                  |✅      |✅*    |

## 	Test Execution ##
| Test Execution                            | KushoAI | TestCraft | Maestro | Postbot |AI Test Case and Data Generator|NVIDIA NeMo Data Designer  |Testim Copilot Coding Assistant      |Playwright|Mabl  |
|-------------------------------------------|---------|-----------|---------|---------|-------------------------------|---------------------------|-------------------------------------|-----------|-----|
|**Execution Environment**                  |KushoAI platform for API testing;</br> UI testing package can be downloaded and run in IDE | 🚫  |  Maestro Studio  |Postman |🚫 | IDE   |Testim Interface |Visual Studio Code - Insiders| Mabl Desktop App     |
|**Support Parallel Test Execution**        |✅      |🚫         |❌       |🚫      |❌                             |🚫                        |✅*                                  |✅       |❌    |
|**Detect defects**                         |❌      |❌         |✅       |❌      |❌                             |❌                        |✅*                                  |✅       |❌    |
|**Generate Test Report**                   |✅      |❌         |✅       |❌      |❌                             |❌                        |✅*                                  |✅       |✅*   |
|**Generate Test Run Dashboard**            |✅      |❌         |✅       |❌      |❌                             |❌                        |✅*                                  |✅       |✅*   |
  
⚠️ \* Supported by the tool’s existing functionality, not AI-powered.
