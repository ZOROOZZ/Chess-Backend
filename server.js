export default {
  async fetch(request) {
    const url = new URL(request.url);

    // CORS preflight request (OPTIONS)
    if (request.method === "OPTIONS") {
      return new Response(null, {
        headers: {
          "Access-Control-Allow-Origin": "*",   // allow all origins
          "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
          "Access-Control-Allow-Headers": "Content-Type",
        },
      });
    }

    if (url.pathname === "/") {
      return new Response("Backend is running ✅", {
        headers: {
          "Content-Type": "text/plain",
          "Access-Control-Allow-Origin": "*",
        },
      });
    }

    if (url.pathname === "/api/hello") {
      return new Response(
        JSON.stringify({ message: "Hello from Backend 🚀" }),
        {
          headers: {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",  // 👈 important
          },
        }
      );
    }

    return new Response("Not Found", {
      status: 404,
      headers: { "Access-Control-Allow-Origin": "*" },
    });
  },
};
