/** @type {import('tailwindcss').Config} */
export default {
  content: [
    './app.vue',           // Includes classes in your main app.vue
    './components/**/*.{vue,js}',  // Includes components
    './layouts/**/*.vue',  // Includes layouts
    './pages/**/*.vue',    // Includes pages
    './plugins/**/*.{js,ts}', // Includes plugins
  ],
  darkMode: 'class', // Enables dark mode using a `class` toggle
  theme: {
    extend: {},
  },
  plugins: [],
};
