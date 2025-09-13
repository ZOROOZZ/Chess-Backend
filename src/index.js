export default {
  async fetch(request, env) {
    let url = new URL(request.url);

    if (url.pathname === "/join") {
      let id = env.CHESSGAME.idFromName(url.searchParams.get("gameId"));
      let obj = env.CHESSGAME.get(id);
      return obj.fetch(request);
    }

    return new Response("Not Found", { status: 404 });
  },
};

export class ChessGame {
  constructor(state, env) {
    this.state = state;
    this.env = env;
    this.sessions = [];
  }

  async fetch(request) {
    if (request.headers.get("Upgrade") === "websocket") {
      let [client, server] = Object.values(new WebSocketPair());
      this.sessions.push(server);
      server.accept();

      server.addEventListener("message", (event) => {
        // Broadcast move to all players
        for (let s of this.sessions) {
          if (s !== server) {
            s.send(event.data);
          }
        }
      });

      return new Response(null, { status: 101, webSocket: client });
    }

    return new Response("OK");
  }
}
