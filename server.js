import express from "express";
const app = express();
const PORT = process.env.PORT || 3000;

// Simple API endpoint
app.get("/api/hello", (req, res) => {
  res.json({ message: "Hello from Backend 🚀" });
});

app.listen(PORT, () => {
  console.log(`Backend running on http://localhost:${PORT}`);
});
