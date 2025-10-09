# Postbot — Research Report

**Summary**  
Postbot is an AI assistant built into Postman that can generate, fix, and explain API test scripts in Javascript through natural language commands. It simplifies Postman scripting and debugging, though it’s limited to the Postman environment.

**Link:** [About Postbot](https://learning.postman.com/docs/getting-started/basics/about-postbot/)

---

## 1. Capabilities Overview

### API Testing

-  **Generate test scripts automatically**  
   Code generation can be done either *inline* or through the *chatbox*. The generated code may include **test scripts** or **pre-request Script**, which can access and modify environment variables, collection variables, or request headers, body, and parameters.  

   - **Inline coding:** A prompt input instructs Postbot to generate a specific test.
    ![Inline coding](https://github.com/XChenscottlogic/AI-Testing-Experiment/blob/Xin-branch/Postbot/Screenshot%20In%20Line%20Coding.png)

   - **Chatbox interface:** You can either prompt Postbot with a request or select from built-in test suggestions, such as:  
     - Data length  
     - Time within acceptable range  
     - Content type  
     - Schema  
     - Against saved value  
     ![Test Generation](https://github.com/XChenscottlogic/AI-Testing-Experiment/blob/Xin-branch/Postbot/Screenshot%20Test%20generations.png)

    **Generated API Tests:** [Test Cases Created by Postbot](https://github.com/XChenscottlogic/AI-Testing-Experiment/blob/Xin-branch/Postbot/test_cases_created_by_postbot.js)

-  **Fix tests automatically**  
   Postbot can automatically debug and fix test scripts by identifying logical or syntax errors in the code.
     ![Fix Tests](https://github.com/XChenscottlogic/AI-Testing-Experiment/blob/Xin-branch/Postbot/Screenshot%20Fix%20Tests.png)

-  **Generate API schema validations**  
   It can automatically validate the response against expected API schema definitions, ensuring field consistency and type safety.
     ![Test for Response Schema](https://github.com/XChenscottlogic/AI-Testing-Experiment/blob/Xin-branch/Postbot/Screenshot%20Test%20for%20response%20schema.png)

-  **Suggest assertions**  
   Postbot suggests appropriate assertions based on API response structure, such as status codes, content types, and field values.

-  **Visualize API responses**  
   Responses can be displayed as tables, line charts, or bar graphs using Postman Visualizer templates for clearer analysis.  
   ![Visualise Response](https://github.com/XChenscottlogic/AI-Testing-Experiment/blob/Xin-branch/Postbot/Screenshot%20Visualise%20the%20response.png)
   
-  **Store fields from responses into variables**  
   A specific field from the API response can be saved into a global variable for later use within scripts.  
   ![Save Field from Response](https://github.com/XChenscottlogic/AI-Testing-Experiment/blob/Xin-branch/Postbot/Screenshot%20Save%20field%20from%20response.png)

-  **Answer general Postman and API-related queries**
   Postbot can explain Postman features, clarify API concepts, or assist with JavaScript scripting questions directly within the app.
   ![Q and A](https://github.com/XChenscottlogic/AI-Testing-Experiment/blob/Xin-branch/Postbot/Screenshot%20Q%20and%20A.png)

---   

## 2. Typical Use Cases

- Generate automated API test scripts using natural language
- Fix and debug existing Postman scripts automatically
- Validate API schema and data integrity
- Store and reuse response data dynamically across test flows
- Visualise API outputs for quick inspection
- Learn Postman scripting and API concepts interactively

---

## 3. Pros

- Integrated into Postman UI — no additional setup required
- Natural language interface makes scripting accessible to non-developers
- Automatic debugging and fixes improve productivity
- Flexible code generation (tests or pre-request scripts)
- Response visualisation enhances data understanding
- Helpful for learning — can answer API and Postman queries

---

## 4. Cons & Limitations

- Limited to Postman environment — cannot be used externally or in CI/CD pipelines
- Requires workspace access — sometimes inconvenient for shared boards
- AI-generated tests may need manual review for complex logic
- Monthly usage is limited to 50 activities per user
- Privacy concerns for sensitive API data

---

## 5. Pricing

Postbot is free to try on all Postman plans. Monthly usage is limited to 50 activities per user. 

---

## 6. Recommendation

**✅ Recommended For:** 
- Postman users who want to speed up test creation and debugging using AI assistance.
- Teams looking for lightweight automation inside Postman.

**⚠️ Use Caution If:** 
- You need CI/CD integration or offline execution.
- Your API involves sensitive or confidential data.
- You require full automation beyond Postman’s ecosystem.   