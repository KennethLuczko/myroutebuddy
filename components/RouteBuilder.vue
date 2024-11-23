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
            task.completed ? 'bg-gray-200 line-through text-gray-500' : 'bg-gray-50 text-gray-800',
            task.custom ? 'bg-blue-200' : ''
          ]"
        >
          <div class="flex items-center justify-between">
            <div>
              <h3 class="font-semibold">{{ task.task }}</h3>
              <p class="text-sm text-gray-500">
                {{ task.custom ? 'Custom Task / Note' : `${task.points} points` }}
              </p>
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
  import { Container, Draggable } from 'vue3-smooth-dnd';
  
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
  
          // Remove the task from the previous position
          if (dropResult.removedIndex !== null) {
            newRoute.splice(dropResult.removedIndex, 1);
          }
  
          // Insert the task at the new position
          if (dropResult.addedIndex !== null) {
            const task = dropResult.payload;
  
            // If the task doesn't have 'completed' property, initialize it
            if (task.completed === undefined) {
              task.completed = false;
            }
  
            // Prevent duplicates
            if (!newRoute.some((t) => t.id === task.id)) {
              newRoute.splice(dropResult.addedIndex, 0, task);
            } else {
              // If moving within the same list, allow reordering
              if (dropResult.removedIndex !== null) {
                newRoute.splice(dropResult.addedIndex, 0, task);
              } else {
                alert('Task is already in your route.');
              }
            }
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
  