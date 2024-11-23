<template>
    <div class="p-4 bg-white rounded-lg shadow dark:bg-gray-800">
      <h2 class="text-xl font-bold mb-4 text-gray-800 dark:text-gray-200">Your Route</h2>
      <Container
        :get-child-payload="getTaskPayload"
        group-name="tasks"
        @drop="onDrop"
      >
        <Draggable
          v-for="(task, index) in route"
          :key="task.id"
          :class="[
            'p-4 rounded-lg shadow border hover:bg-gray-100 transition mb-2',
            task.completed ? 'bg-gray-200 line-through text-gray-500' : 'bg-gray-50 text-gray-800'
          ]"
        >
          <div class="flex items-center justify-between">
            <div>
              <h3 class="font-semibold">{{ task.task }}</h3>
              <p class="text-sm text-gray-500">{{ task.points }} pts</p>
            </div>
            <div class="flex items-center space-x-2">
              <!-- Complete Task -->
              <input
                type="checkbox"
                v-model="task.completed"
                @change="updateCompletion"
                class="w-5 h-5 text-blue-500 rounded border-gray-300 focus:ring focus:ring-blue-200 cursor-pointer"
              />
              <!-- Remove -->
              <button
                @click="removeTaskById(task.id)"
                class="w-8 h-8 bg-red-500 text-white hover:bg-red-600 rounded-full shadow-sm"
              >
                ✕
              </button>
            </div>
          </div>
        </Draggable>
      </Container>
    </div>
  </template>
  
  <script>
  import { Container, Draggable } from 'vue-smooth-dnd';
  
  export default {
    props: {
      route: Array,
    },
    methods: {
      getTaskPayload(index) {
        return this.route[index];
      },
      onDrop(dropResult) {
        if (dropResult.removedIndex !== null || dropResult.addedIndex !== null) {
          let newRoute = [...this.route];
          let movedTask = dropResult.payload;
  
          // Check if the task is already in the route
          const taskExists = newRoute.some((task) => task.id === movedTask.id);
          if (taskExists && dropResult.removedIndex === null) {
            alert('Task is already in your route.');
            return;
          }
  
          // Remove from previous position if moving within the same container
          if (dropResult.removedIndex !== null) {
            newRoute.splice(dropResult.removedIndex, 1);
          }
  
          // Add to new position
          if (dropResult.addedIndex !== null) {
            if (movedTask.completed === undefined) {
              movedTask.completed = false;
            }
            newRoute.splice(dropResult.addedIndex, 0, movedTask);
          }
          this.$emit('update-route', newRoute);
        }
      },
      removeTaskById(taskId) {
        const updatedRoute = this.route.filter((task) => task.id !== taskId);
        this.$emit('update-route', updatedRoute);
      },
      updateCompletion() {
        this.$emit('update-route', [...this.route]);
      },
    },
    components: {
      Container,
      Draggable,
    },
  };
  </script>
  