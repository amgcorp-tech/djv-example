import { defineConfig } from 'vite'
import reactRefresh from "@vitejs/plugin-react-refresh";
import { resolve } from 'path';

// https://vitejs.dev/config/
export default defineConfig({
  base:  "/static/",
  root: "./",
  plugins: [reactRefresh()],
  build: {
    manifest: true,
    outDir: "../static/djv_example",
    emptyOutDir: true,
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'src/main.tsx'),
      },
    },
  },
})
