# NVIDIA NeMo Data Designer (formerly Gretel) — Research Report

**Summary**  
NVIDIA NeMo Data Designer is a microservice designed to generate high-quality synthetic data using configurable schemas and AI-driven models. It enables organiations to safely create realistic datasets for AI training, testing, and analytics while maintaining data privacy.

**Link:** [NVIDIA NeMo Data Designer Documentation](https://docs.nvidia.com/nemo/microservices/latest/generate-synthetic-data/index.html)

---

## 1. Capabilities Overview

### I. Features

- **Configuration-Driven Workflow:**  
  Define data schemas including column types, constraints, and relationships.

- **AI-Powered Data Generation:**  
  Use specified AI models to generate realistic synthetic data aligned with your configuration. LLMs used on generation can be configued. 

- **Validation and Export:**  
  Automatically validate generated data against schemas and export in multiple formats (CSV, JSON, Parquet).

- **Deployment Flexibility:**  
  Deployed via **Docker Compose** for development and testing; available through **NVIDIA NGC Catalog**.

- **RESTful API:**  
  Full HTTP API for programmatic access, supporting asynchronous batch processing.

- **Scalable Architecture:**  
  Supports horizontal scaling through container orchestration.

- **Model Selection & Aliases:** 
  NeMo Data Designer provides default model aliases for common use cases: 
  - `text`: Text generation tasks  
  - `code`: Code generation  
  - `structured`: Structured data (JSON, schemas)  
  - `judge`: Data quality evaluation  
  - `reasoning`: Logical reasoning and inference  
  Custom model aliases can be defined for specific parameters or endpoints.

- **Comprehensive Column Types:**  
  - **Sampling-based:** Category, Uniform, Gaussian, Poisson, Binomial, DateTime, Person, UUID, etc.  
  - **LLM-based:** Text, Code, Structured JSON, Judge (data scoring).  
  - **Expression-based:** Compute values using Jinja2 expressions and templates.

- **Template Variables & Conditional Parameters:**  
  Define complex relationships or conditional sampling rules between columns.

- **Statistical Distributions:**  
  Supports Uniform, Gaussian, Bernoulli, Poisson, Binomial, and custom SciPy distributions.

- **Data Quality & Privacy Controls:**  
  Schema validation, logical consistency checks, and privacy-preserving synthetic data generation (no direct record copying).

- **Integration & Pipeline Support:**  
  - Data preparation and batch generation via REST API  
  - Result processing and schema validation endpoints  
  - Job tracking, error handling, and dataset download management  

---

## 2. Typical Use Cases

- **Coding Assistants:** Generate synthetic code datasets (e.g., Python, SQL) to improve AI model reasoning and performance.  
- **Conversational AI:** Create realistic domain-specific dialogues for chatbots and virtual assistants.  
- **Synthetic Documents:** Produce structured datasets for document processing and validation tasks.  
- **Evaluation & Benchmarks:** Build datasets to benchmark or enhance model performance (e.g., RAG systems).  


---

## 3. Pros

- Configuration-driven workflow simplifies setup.  
- Highly flexible — supports both statistical and LLM-based data generation.  
- Strong privacy protection — no direct copying of sensitive data.  
- REST API and Docker-based deployment make it easy to integrate and scale.  
- Supports multiple data formats (CSV, JSON, Parquet).  
- Built-in validation ensures consistency and schema compliance.

---

## 4. Cons & Limitations

- **Beta status:** APIs and features subject to change.  
- **Manual integration required** with other NeMo microservices.  
- **Docker Compose dependency:** Standalone deployment only at present.  
- **Local storage requirement** for generated datasets.  
- **Performance variation:** Dependent on model complexity, endpoint latency, and system memory.  
- **Limited concurrency:** Number of jobs constrained by system resources.

---

## 5. Pricing Snapshot

- **Availability:** Currently it is available to download for free or apply for early access.  
- **Licensing:** Use, distribution or deployment of this microservice in production requires an NVIDIA AI Enterprise License. A free 90-day license to try NVIDIA AI Enterprise in production can be applied on its website. 
- **Governing:** The software and materials are governed by the NVIDIA Software License Agreement and the Product-Specific Terms for NVIDIA AI Products.

---

## 6. Recommendation

**✅ Recommended For:**  
- Teams needing **synthetic data generation** for AI/ML training, analytics, or testing.  
- Organisations focused on **data privacy** and **regulatory compliance**.  
- Developers integrating synthetic data generation into **automated pipelines**.

**⚠️ Use Caution If:**  
- You require **production-grade deployment** (as the tool is still in beta).  
- You prefer **fully open-source solutions**.  
- Your infrastructure does not support **Docker Compose or NVIDIA ecosystem dependencies**.

