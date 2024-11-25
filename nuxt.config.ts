// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  css: ['~/assets/css/tailwind.css'],

  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  },

  compatibilityDate: '2024-11-22',

  app: {
    head: {
      title: 'My Route Buddy - Task Route Planner',
      meta: [
        // OpenGraph Meta Tags
        { property: 'og:title', content: 'My Route Buddy - Task Route Planner' },
        { property: 'og:type', content: 'website' },
        { property: 'og:url', content: 'https://yourwebsite.com' },
        {
          property: 'og:description',
          content:
            'My Route Buddy is a web application designed to help players plan and optimize their tasks efficiently. Whether you’re tackling hundreds of pre-made tasks or adding your own custom tasks, this app is built to streamline your experience.',
        },
        { property: 'og:site_name', content: 'My Route Buddy' },
        { property: 'og:locale', content: 'en_US' },

        // Twitter Meta Tags
        { name: 'twitter:card', content: 'summary' },
        { name: 'twitter:title', content: 'My Route Buddy - Task Route Planner' },
        {
          name: 'twitter:description',
          content:
            'My Route Buddy is a web application designed to help players plan and optimize their tasks efficiently. Whether you’re tackling hundreds of pre-made tasks or adding your own custom tasks, this app is built to streamline your experience.',
        },
      ],
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      ],
    },
  },
});
