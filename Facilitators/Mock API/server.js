import express from "express";

const app = express();
app.use(express.json());

// Endpoint 1: Generate text
app.post("/api/generate_text", (req, res) => {
  const { prompt } = req.body;
  if (Math.random() < 0.1) {
    return res.status(500).json({
      error: "Model Hallucination Detected",
      message: `The model returned inaccurate information, e.g., 'The capital of France is Mars.'`,
      prompt,
    });
  }

  const responseText = `API_RESPONSE: The prompt "${prompt}" generated this text about quantum entanglement.`;
  res.json({
    generated_text: responseText,
    token_count: responseText.length / 5,
    model: "mock-ai-1.0",
    timestamp: new Date().toISOString(),
  });
});

// Endpoint 2: Analyze sentiment
app.post("/api/analyze_sentiment", (req, res) => {
  const { text } = req.body;
  const random = Math.random();
  let label, score;
  if (random < 0.2) {
    label = "NEGATIVE";
    score = (Math.random() * 0.2 + 0.8).toFixed(4);
  } else if (random < 0.6) {
    label = "NEUTRAL";
    score = (Math.random() * 0.4 + 0.3).toFixed(4);
  } else {
    label = "POSITIVE";
    score = (Math.random() * 0.2 + 0.8).toFixed(4);
  }

  res.json({
    input_text: text,
    label,
    confidence_score: parseFloat(score),
    service_version: "v1.1.2",
  });
});

// Endpoint 3: Structured data
app.get("/api/structured_response", (req, res) => {
  res.json({
    catalog_id: "CAT-9001",
    total_items: 3,
    products: [
      { product_id: "P-4321", name: "Quantum Debugger Kit", price: 199.99, in_stock: true },
      { product_id: "P-5500", name: "Synthetic Data Generator", price: 49.5, in_stock: true },
      { product_id: "P-1010", name: "Ethical AI Guideline Handbook", price: 25.0, in_stock: false },
    ],
    last_updated: new Date().toISOString(),
  });
});

app.listen(3000, () => console.log("🚀 Mock API running at http://localhost:3000"));
