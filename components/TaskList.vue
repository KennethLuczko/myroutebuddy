<template>
    <div class="p-4 bg-white rounded-lg shadow mb-4 dark:bg-gray-800">
      <h2 class="text-xl font-bold mb-4 text-gray-800 dark:text-gray-200">Available Tasks</h2>
      
      <!-- Search Bar -->
      <input
        type="text"
        v-model="searchQuery"
        placeholder="Search tasks..."
        class="w-full border rounded-lg p-2 mb-4 focus:ring-2 focus:ring-blue-500 focus:outline-none"
      />
  
      <ul class="space-y-2">
        <li
          v-for="task in filteredTasks"
          :key="task.id"
          class="flex justify-between items-center bg-gray-50 hover:bg-gray-100 p-4 rounded-lg shadow border cursor-pointer"
          @click="selectTask(task)"
        >
          <span class="font-medium text-gray-700">{{ task.task }}</span>
          <span class="text-sm text-gray-500">{{ task.points }} pts</span>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import { Container, Draggable } from 'vue-smooth-dnd';
  export default {
    components: {
        Container,
        Draggable,
    },
    props: {
      tasks: Array,
    },
    data() {
      return {
        searchQuery: '', // Bind to the search bar
      };
    },
    computed: {
      filteredTasks() {
        // Filter tasks based on the search query (case insensitive)
        const query = this.searchQuery.toLowerCase();
        return this.tasks.filter(
          (task) => task.task.toLowerCase().includes(query)
        );
      },
    },
    methods: {
      selectTask(task) {
        this.$emit('add-task', task);
      },
    },
  };
  </script>
  