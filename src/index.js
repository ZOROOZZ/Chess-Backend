export class ChessGame {
  constructor(state, env) {
    this.state = state;
    this.env = env;
    this.clients = [];
  }

  async fetch(req) {
    let url = new URL(req.url);

    // Handle WebSocket connections
    if (url.pathname === "/join") {
      const [client, server] = Object.values(new WebSocketPair());

      await this.handleSession(server);
      return new Response(null, { status: 101, webSocket: client });
    }

    return new Response("Chess backend is running!", { status: 200 });
  }

  async handleSession(ws) {
    ws.accept();
    this.clients.push(ws);

    ws.addEventListener("message", (evt) => {
      // Broadcast received move to all players
      for (let client of this.clients) {
        if (client !== ws) {
          client.send(evt.data);
        }
      }
    });

    ws.addEventListener("close", () => {
      this.clients = this.clients.filter((c) => c !== ws);
    });
  }
}

export default {
  async fetch(req, env) {
    return env.ChessGame.fetch(req);
  },
};
