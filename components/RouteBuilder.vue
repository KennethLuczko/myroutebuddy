<template>
    <div class="p-4 bg-white rounded-lg shadow dark:bg-gray-800">
      <h2 class="text-xl font-bold mb-4 text-gray-800 dark:text-gray-200">Your Route</h2>
      <ul class="space-y-4">
        <li
          v-for="(task, index) in route"
          :key="task.id"
          :class="[
            'p-4 rounded-lg shadow border hover:bg-gray-100 transition',
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
              <!-- Move Up -->
              <button
                @click="moveUp(index)"
                :disabled="index === 0"
                class="w-8 h-8 bg-gray-200 hover:bg-gray-300 rounded-full shadow-sm disabled:opacity-50"
              >
                ↑
              </button>
              <!-- Move Down -->
              <button
                @click="moveDown(index)"
                :disabled="index === route.length - 1"
                class="w-8 h-8 bg-gray-200 hover:bg-gray-300 rounded-full shadow-sm disabled:opacity-50"
              >
                ↓
              </button>
              <!-- Remove -->
              <button
                @click="removeTask(index)"
                class="w-8 h-8 bg-red-500 text-white hover:bg-red-600 rounded-full shadow-sm"
              >
                ✕
              </button>
            </div>
          </div>
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
      route: Array,
    },
    methods: {
      moveUp(index) {
        const updatedRoute = [...this.route];
        const [task] = updatedRoute.splice(index, 1);
        updatedRoute.splice(index - 1, 0, task);
        this.$emit('update-route', updatedRoute);
      },
      moveDown(index) {
        const updatedRoute = [...this.route];
        const [task] = updatedRoute.splice(index, 1);
        updatedRoute.splice(index + 1, 0, task);
        this.$emit('update-route', updatedRoute);
      },
      removeTask(index) {
        const updatedRoute = [...this.route];
        updatedRoute.splice(index, 1);
        this.$emit('update-route', updatedRoute);
      },
      updateCompletion() {
        this.$emit('update-route', [...this.route]);
      },
    },
  };
  </script>
  