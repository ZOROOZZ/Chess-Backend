export class ChessGame {
  constructor(state, env) {
    this.state = state;
    this.env = env;
    this.moves = [];
  }

  async fetch(request) {
    let url = new URL(request.url);

    if (url.pathname === "/move") {
      let body = await request.json();
      this.moves.push(body.move);

      return new Response(JSON.stringify({ ok: true, moves: this.moves }), {
        headers: { "Content-Type": "application/json" }
      });
    }

    if (url.pathname === "/state") {
      return new Response(JSON.stringify({ moves: this.moves }), {
        headers: { "Content-Type": "application/json" }
      });
    }

    return new Response("ChessGame Durable Object", { status: 200 });
  }
}

export default {
  async fetch(request, env) {
    let id = env.ChessGame.idFromName("default");
    let obj = env.ChessGame.get(id);
    return obj.fetch(request);
  }
};
