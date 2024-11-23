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
  
      <!-- Draggable Task List -->
      <Container
        :get-child-payload="getTaskPayload"
        group-name="tasks"
        @drop="onDrop"
      >
        <Draggable
          v-for="(task, index) in filteredTasks"
          :key="task.id"
          :data-id="task.id"
          class="flex justify-between items-center bg-gray-50 hover:bg-gray-100 p-4 rounded-lg shadow border cursor-pointer mb-2"
          @click="selectTask(task)"
        >
          <div class="font-medium text-gray-700">{{ task.task }}</div>
          <div class="text-sm text-gray-500">{{ task.points }} points</div>
        </Draggable>
      </Container>
    </div>
  </template>
  
  
  <script>
  import { Container, Draggable } from 'vue3-smooth-dnd';
  
  export default {
    props: {
      tasks: Array,
    },
    data() {
      return {
        searchQuery: '',
      };
    },
    computed: {
      filteredTasks() {
        const query = this.searchQuery.toLowerCase();
        return this.tasks.filter((task) => task.task.toLowerCase().includes(query));
      },
    },
    methods: {
      getTaskPayload(index) {
        return this.filteredTasks[index];
      },
      onDrop(dropResult) {
        if (dropResult.removedIndex !== null || dropResult.addedIndex !== null) {
          const updatedTasks = [...this.filteredTasks];
  
          // Handle removal
          if (dropResult.removedIndex !== null) {
            updatedTasks.splice(dropResult.removedIndex, 1);
          }
  
          // Handle addition
          if (dropResult.addedIndex !== null) {
            const task = dropResult.payload;
            // Prevent duplicates
            if (!updatedTasks.some((t) => t.id === task.id)) {
              updatedTasks.splice(dropResult.addedIndex, 0, task);
            } else {
              // If moving within the same list, allow reordering
              if (dropResult.removedIndex !== null) {
                updatedTasks.splice(dropResult.addedIndex, 0, task);
              }
            }
          }
  
          // Update the tasks list
          this.$emit('update-tasks', updatedTasks);
        }
      },
      selectTask(task) {
        this.$emit('add-task', task);
      },
    },
    components: {
      Container,
      Draggable,
    },
  };
  </script>
  