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
    extend: {
      spacing: {
        '1/3vw': '33.33vw', // Adding custom 1/3 of viewport width
      },
    },
  },
  plugins: [
    require('tailwind-scrollbar-hide')
  ],
};
