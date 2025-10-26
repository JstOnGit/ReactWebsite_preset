import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    port: 4173,
    proxy: {
      '/api': {
        target: 'http://localhost:4269',
        changeOrigin: true,
        secure: false,
      },
    },
  },
});
