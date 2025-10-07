# 🧠 Mock AI Testing API

A simple **mock API** for experimenting with API testing tools such as **KushoAI**, **Postman**, or **Insomnia**.  
This project simulates realistic AI-like endpoints — including latency, random errors, and structured JSON — to help you test automation, validation, and error handling logic.

---

## 🚀 Features

✅ **3 Mock Endpoints**
- `/api/generate_text` – Simulates an AI text-generation API (with 10% chance of “hallucination” errors).  
- `/api/analyze_sentiment` – Returns random sentiment analysis results and occasionally malformed data.  
- `/api/structured_response` – Returns structured JSON data for schema validation.

✅ **Realistic API Behavior**
- Random response delays (latency simulation)  
- Intentional data errors for schema testing  
- JSON-based input and output  
- Easy to extend for more endpoints  

✅ **Front-end + Node.js support**
- Run the **HTML version** to interact in your browser, or  
- Use the **Node.js version** to expose real HTTP endpoints for testing tools.

---

## 🧩 Project Structure

mock-api/
├── mock_api.html # Front-end UI simulation (browser only)
├── server.js # Node.js Express backend version
├── package.json # NPM project file
└── README.md # Documentation

---

## ⚙️ Setup (Node.js API)

### 1️⃣ Prerequisites
- [Node.js](Company portal) v20+ installed  
- npm available in terminal (`npm -v`)

### 2️⃣ Install dependencies
```bash
npm install

3️⃣ Start the server
node server.js

4️⃣ Verify
Once running, visit:

http://localhost:3000
or test endpoints directly via Postman

🧠 API Endpoints
1. POST /api/generate_text
Description: Simulates an AI text generation response.
Request:

{
  "prompt": "Explain quantum entanglement."
}

Success Response:

{
  "generated_text": "API_RESPONSE: The prompt 'Explain quantum entanglement'...",
  "token_count": 72,
  "model": "mock-ai-1.0",
  "timestamp": "2025-10-07T12:34:56.000Z"
}

Error (10% chance):

{
  "error": "Model Hallucination Detected",
  "message": "The model returned inaccurate information.",
  "prompt": "Explain quantum entanglement."
}

2. POST /api/analyze_sentiment
Description: Returns a random sentiment label with confidence score.
Request:

{
  "text": "I love testing tools!"
}

Response Example:

{
  "input_text": "I love testing tools!",
  "label": "POSITIVE",
  "confidence_score": 0.9231,
  "service_version": "v1.1.2"
}

Occasional malformed output for schema testing.

3. GET /api/structured_response
Description: Returns structured catalog data for schema validation.
Response:

{
  "catalog_id": "CAT-9001",
  "total_items": 3,
  "products": [
    {
      "product_id": "P-4321",
      "name": "Quantum Debugger Kit",
      "category": "Tools",
      "price": 199.99,
      "in_stock": true
    },
    ...
  ],
  "last_updated": "2025-10-07T12:45:00.000Z"
}


🧪 Example Testing with cURL

curl -X POST http://localhost:3000/api/generate_text \
  -H "Content-Type: application/json" \
  -d '{"prompt": "What is machine learning?"}'

curl -X POST http://localhost:3000/api/analyze_sentiment \
  -H "Content-Type: application/json" \
  -d '{"text": "This tool is amazing!"}'

curl http://localhost:3000/api/structured_response

🧰 Use Cases
Practice API test automation
Validate OpenAPI spec compliance
Simulate AI model behaviors (latency, errors, JSON schema)
Train/test QA tools such as Postman, or Cypress

🧩 Optional: Browser Sandbox
If you just want a visual mock API playground, open mock_api.html in your browser.
It includes Tailwind CSS styling and lets you test endpoints with no setup.

