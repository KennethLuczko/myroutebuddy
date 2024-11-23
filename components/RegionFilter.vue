<template>
    <div class="p-4 bg-gray-100 rounded-lg shadow mb-4 border dark:bg-gray-900 border-gray-200 dark:border-gray-700">
      <h2 class="text-xl font-bold mb-4 text-gray-800 dark:text-gray-200 ">Select Regions (Max: 3 Additional)</h2>
      <div class="flex flex-wrap gap-2">
        <!-- Global Region (Always included) -->
        <button
          class="px-4 py-2 rounded border bg-blue-500 text-white font-medium shadow-sm cursor-not-allowed"
          disabled
        >
          Global
        </button>
  
        <!-- Additional Regions -->
        <button
          v-for="region in regions"
          :key="region.name"
          :class="[selectedRegions.includes(region.name) ? 'bg-blue-500 text-white' : 'bg-gray-300 text-gray-800 dark:bg-gray-50', 'px-4 py-2 rounded border font-medium shadow-sm hover:bg-blue-200']"
          @click="toggleRegion(region.name)"
        >
          {{ region.name }}
        </button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      regions: Array,
      selectedRegions: Array,
    },
    methods: {
      toggleRegion(regionName) {
        if (this.selectedRegions.includes(regionName)) {
          this.$emit('update-regions', this.selectedRegions.filter((name) => name !== regionName));
        } else if (this.selectedRegions.length < 3) {
          this.$emit('update-regions', [...this.selectedRegions, regionName]);
        }
      },
    },
  };
  </script>
  