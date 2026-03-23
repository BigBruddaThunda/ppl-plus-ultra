import { defineConfig } from "vite";
import { cardApiMiddleware } from "./server/card-api.js";

export default defineConfig({
  server: {
    port: 5173,
  },
  plugins: [
    {
      name: "card-api",
      configureServer(server) {
        server.middlewares.use(cardApiMiddleware());
      },
    },
  ],
  test: {
    globals: true,
    environment: "node",
    include: ["tests/**/*.test.ts"],
  },
});
