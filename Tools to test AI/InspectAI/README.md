# Inspect — Research Report

---

### **Summary**

Inspect is an open-source framework developed by the UK AI Security Institute for evaluating large language models across a wide range of tasks including reasoning, coding, multimodal understanding, agentic behaviour, and tool-assisted workflows. It provides a structured and scalable approach to benchmarking LLM performance using reusable components such as datasets, solvers, scorers, and model providers. Inspect supports both simple evaluation workflows and advanced agent-based testing scenarios, making it suitable for both researchers and teams requiring security-grade evaluation depth.

🔗 **Link:** https://inspect.aisi.org.uk/

---

## 1. Capabilities Overview

Inspect offers a comprehensive evaluation environment for assessing LLM capabilities, robustness, and safety across real-world use cases. Its capabilities go beyond basic prompt scoring and benchmark running, providing infrastructure-level support for structured evaluations at scale.

Key capabilities include:

- **Extensive Evaluation Library:** Over 100 pre-built evaluations covering reasoning, coding, knowledge tasks, agentic tasks, multimodal tasks, and behavioural measurement.
- **Composable Evaluation Architecture:** Evaluations are constructed using reusable components — datasets (inputs), solvers (execution strategies), and scorers (output assessment).
- **Agent & Tool Execution Support:** Built-in support for reasoning agents, external agent frameworks, tool calling (bash, Python, web browsing, text editing), and Model Context Protocol interoperability.
- **Sandbox Execution:** Safe execution environment for untrusted model-generated code using Docker, Kubernetes, Proxmox, or custom execution engines.
- **Multi-Model Compatibility:** Works with models from OpenAI, Anthropic, Google, Grok, Mistral, Azure AI, AWS Bedrock, HuggingFace, TogetherAI, Groq, and locally hosted models (Ollama, llama.cpp, vLLM).
- **Developer Tooling:** VS Code integration, CLI-based execution, log visualisation dashboard (Inspect View), debugging tools, interactive development experience.
- **Scalable Execution & Performance:** Parallel execution, caching, dataset management, batch inference support, structured output enforcement, multimodal evaluation capabilities.
- **Research-Grade Reporting:** Logs, scoring metadata, structured runs, and evaluation viewer suitable for audit, reproducibility, and long-term performance tracking.

---

## 2. Typical Use Cases

- Running standardised AI benchmarks (MMLU, coding tasks, reasoning tests)
- Testing model behaviour across agent frameworks with tool use
- Comparing commercial and open-source LLMs side-by-side
- Evaluating multimodal understanding (text, audio, images, video)
- Security and safety validation using controlled evaluations
- Measuring chain-of-thought or step-by-step reasoning quality
- Running reproducible research workflows or internal LLM assessments
- Performing systematic “Hello World → Research-grade eval” progression

---

## 3. Pros

- Structured evaluation architecture (datasets + solvers + scorers)
- Extensive tooling including UI, CLI, VS Code extension, and logs viewer
- Supports many providers, agents, and execution environments
- Includes >100 ready-to-use benchmark evaluations
- Sandboxed execution protects against untrusted model output
- Highly extensible and flexible for custom evaluation design
- Fully open-source and vendor-neutral

---

## 4. Cons & Limitations

- Requires technical familiarity (Python, CLI, evaluation design principles)
- More complex than lightweight evaluation tools focused only on prompt scoring
- No built-in commercial support or turnkey SaaS interface
- Requires API keys and model access configuration to test multiple providers
- Advanced use (agents, multimodal, custom scorers) has a learning curve

---

## 5. Pricing Snapshot

| Component | Cost Basis | Notes |
|-----------|------------|-------|
| Inspect Framework | **Free (Open Source)** | No licensing fee |
| Model API usage | Variable | Cost depends on provider (OpenAI, Anthropic, etc.) |
| Compute | Optional | Only required for sandbox or local model evaluation |
| Storage & Logging | Variable | Based on local or cloud environment configuration |

> The primary cost driver is the **LLM provider API calls**, not Inspect itself.

---

## 6. Recommendation

### ✅ **Recommended For:**
- Research teams running str
