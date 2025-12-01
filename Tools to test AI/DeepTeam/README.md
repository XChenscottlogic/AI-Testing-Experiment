# DeepTeam — Research Report

## Summary
DeepTeam is an open-source framework purpose-built for red teaming Large Language Model (LLM) systems. It enables teams to systematically “penetration test” LLM applications by simulating adversarial attacks and evaluating whether the model exhibits unsafe, biased, or harmful behaviours.  

Powered by DeepEval, DeepTeam offers a powerful yet simple way for anyone to red team all sorts of LLM applications for safety risks and security vulnerabilities in just a few lines of code. These LLM apps can be anything such as RAG pipelines, agents, chatbots, or even just the LLM itself, while the vulnerabilities include ones such as bias, toxicity, PII leakage, misinformation.

**Link:** [deepteam](https://www.trydeepteam.com/docs/getting-started)

---

## 1. Capabilities Overview

DeepTeam provides an end-to-end, automated pipeline for evaluating the safety and security of LLM-based systems such as chatbots, agents, RAG pipelines, and foundational models.

**Key capabilities include:**

### 1.1) Security-Focused LLM Penetration Testing
- Designed specifically to “red team” LLM systems
- Detects 40+ categories of vulnerabilities and risks, including:
  - Bias (race, gender, religion, political, etc.)
  - Toxicity and harmful content
  - PII leakage and data exposure
  - Misinformation and factual errors
  - Over-reliance on context
  - Session and database leakage
  - Unsupported claims and hallucinations
  - Policy and safety boundary violations

This enables proactive identification of real-world failure modes before deploying LLMs into production environments.

---

### 1.2) Adversarial Attack Simulation
DeepTeam automatically generates and applies adversarial attack strategies to your model, such as:

- Prompt injection  
- Jailbreaking  
- ROT13 and evasion techniques  
- Data extraction attempts  
- Response manipulation  
- Single-turn and multi-turn probing attacks  

These attacks are not static. They are:
- Dynamically generated
- Matched to your selected vulnerabilities
- Adjustable via weight-based sampling for targeted testing

This allows users to simulate realistic malicious behaviour at scale.

---

### 1.3) Customisable Risk Frameworks
DeepTeam allows assessments to align with established standards, including:

- **OWASP Top 10 for LLMs**
- **NIST AI Risk Management Framework**
- Industry best practices

You can configure:
- Vulnerability lists
- Attack types and weightings
- Number of attacks per vulnerability
- Specific target system purpose (for context-aware evaluation)

This makes DeepTeam suitable for **academic, commercial, and regulatory-aligned AI evaluations**.

---

### 1.4) No Dataset Required (Dynamic Testing)
Unlike traditional evaluation frameworks, DeepTeam:
- Does **not** require a pre-labelled dataset  
- Dynamically generates attacks in real time  
- Adapts based on selected vulnerabilities  

---

### 1.5) Actionable Risk Assessments
DeepTeam outputs structured and reusable results:

- Overall pass/fail rate per vulnerability
- Detailed test cases
- Individual attack + model response analysis
- Binary scoring (0/1) for strict evaluation
- Exportable as:
  - DataFrames (Pandas)
  - Saved local files
  - Structured reports

---

### 1.6) Stateful Red Teaming (Continuous Improvement)
Using the `RedTeamer` class, users can reuse previous attack cases:

- Enables iterative security testing
- Tracks improvement across model versions
- Avoids resimulating identical attacks
- Supports structured “before vs after” comparisons

---

## 2. Typical Use Cases

- A quick safety sweeps
- Red teaming enterprise chatbots
- Evaluating RAG pipeline safety
- Academic research on AI robustness
- Regulatory and compliance checks
- AI governance and safety reporting
- Continuous monitoring of model updates

---

## 3. Pros

✅ Open-source and accessible  
✅ Purpose-built for LLM safety and security  
✅ Supports 40+ vulnerabilities preloaded
✅ Dynamic adversarial attack simulation  
✅ No dataset required  
✅ Customisable and standards-aligned  
✅ Detailed, structured risk reports  
✅ Supports iteration and regression testing  
✅ Works with multiple LLM providers  

---

## 4. Cons & Limitations

⚠️ Requires familiarity with Python  
⚠️ Needs API keys for LLM-based simulation and evaluation  
⚠️ Not suitable if looking for deep customisation
⚠️ May require tuning to avoid rate-limiting issues  
⚠️ Focused on safety, not general response quality (that is DeepEval’s domain)  

---

## 5. Pricing Snapshot

- **DeepTeam:** Open-source (free)
- **DeepEval:** Open-source (free)
- Cost mainly depends on:
  - LLM API usage (OpenAI, Azure, Ollama, custom models)
  - Number of simulated attacks
  - Concurrence settings

---

## 6. Recommendation

✅ **Recommended For:**
- AI engineers building production LLM systems
- Security and safety teams
- AI governance & compliance groups
- Academic researchers in AI robustness
- Organisations deploying chatbots or agents
- Red teams conducting adversarial testing

⚠️ **Use Caution If:**
- You only need standard LLM metrics (correctness, relevancy, etc.) → Use **DeepEval**
- You lack access to LLM APIs
- You do not require adversarial or security-focused evaluation

---

**Note:**  
It is extremely common to use **DeepEval for performance metrics** and **DeepTeam for security testing** together as part of a complete LLM evaluation lifecycle.

