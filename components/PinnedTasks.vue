<template>
  <div class="sticky top-24 z-10">
    <button
      @click="isCollapsed = !isCollapsed"
      class="w-full h-12 px-4 flex items-center justify-between text-gray-700 dark:text-gray-200 bg-gray-50/90 dark:bg-gray-900/90 backdrop-blur-sm hover:bg-gray-100/90 dark:hover:bg-gray-800/90 rounded-lg border border-gray-200 dark:border-gray-700 shadow-sm"
    >
      <div class="flex items-center gap-2">
        <span class="font-medium">Pinned Tasks ({{ pinnedTasks.length }})</span>
      </div>
      <span
        class="transform transition-transform"
        :class="{ 'rotate-180': !isCollapsed }"
        >▼</span
      >
    </button>

    <div
      v-show="!isCollapsed"
      class="absolute top-[calc(100%+0.25rem)] left-0 right-0 bg-gray-50/90 dark:bg-gray-900/90 backdrop-blur-sm border border-gray-200 dark:border-gray-700 rounded-lg shadow-lg"
    >
      <div ref="pinnedList" class="max-h-64 overflow-y-auto">
        <div
          v-for="task in pinnedTasks"
          :key="task.id"
          class="px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-800 flex items-center gap-2 border-b border-gray-200 dark:border-gray-700 last:border-b-0"
        >
          <span class="text-sm font-mono text-gray-500 dark:text-gray-400 w-8">
            #{{ getTaskIndex(task) + 1 }}
          </span>
          <RegionIcon :region="task.region" class="flex-shrink-0" size="4" />
          <a
            :href="`#task-${task.id}`"
            class="flex-grow text-left text-sm text-gray-700 dark:text-gray-200 truncate hover:text-blue-500"
            @click.prevent="scrollToTask(task.id)"
          >
            {{ task.task }}
          </a>
          <button
            @click="$emit('unpin', task)"
            class="flex-shrink-0 text-gray-400 hover:text-gray-600 dark:hover:text-gray-300"
          >
            📌
          </button>
        </div>
        <div
          v-if="pinnedTasks.length === 0"
          class="px-4 py-3 text-sm text-gray-500 dark:text-gray-400 text-center"
        >
          No pinned tasks
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import RegionIcon from "./RegionIcon.vue";

export default {
  name: "PinnedTasks",
  components: {
    RegionIcon,
  },
  props: {
    pinnedTasks: {
      type: Array,
      required: true,
    },
    route: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      isCollapsed: false,
    };
  },
  watch: {
    pinnedTasks(newVal) {
      if (newVal.length > 0) {
        this.$nextTick(() => {
          const listElement = this.$refs.pinnedList;
          if (listElement) {
            listElement.scrollTop = listElement.scrollHeight;
          }
        });
      }
    },
  },
  methods: {
    getTaskIndex(task) {
      return this.route.findIndex((t) => t.id === task.id);
    },
    clearPinnedTasks(e) {
      e.stopPropagation(); // Prevent dropdown toggle
      this.$emit("clear-all-pins", this.pinnedTasks);
    },
    scrollToTask(taskId) {
      const taskElement = document.getElementById(`task-${taskId}`);

      if (taskElement) {
        // Calculate the total height of pinned list when expanded
        const pinnedListHeight = !this.isCollapsed
          ? this.$refs.pinnedList.getBoundingClientRect().height
          : 0;
        // Add extra padding and account for other fixed elements
        const offset = 300 + pinnedListHeight;

        const bodyRect = document.body.getBoundingClientRect();
        const elementRect = taskElement.getBoundingClientRect();
        const scrollPosition = elementRect.top - bodyRect.top - offset;

        window.scrollTo({
          top: scrollPosition,
          behavior: "smooth",
        });

        // Add border pulse animation
        taskElement.classList.remove("task-pulse-border");
        void taskElement.offsetWidth;
        taskElement.classList.add("task-pulse-border");
        setTimeout(() => {
          taskElement.classList.remove("task-pulse-border");
        }, 3000);
      }
    },
  },
};
</script>

<style>
@keyframes task-pulse {
  0% {
    box-shadow: 0 0 0 0 rgba(34, 211, 238, 0.7);
  }
  35% {
    box-shadow: 0 0 0 8px rgba(34, 211, 238, 0.7);
  }
  70% {
    box-shadow: 0 0 0 8px rgba(34, 211, 238, 0);
  }
  100% {
    box-shadow: 0 0 0 0 rgba(34, 211, 238, 0);
  }
}

.task-pulse-border {
  position: relative;
  animation: task-pulse 2.5s cubic-bezier(0.4, 0, 0.6, 1);
  @apply border border-cyan-400;
}

.task-pulse-border::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  border-radius: inherit;
  pointer-events: none;
  animation: task-pulse 2.5s cubic-bezier(0.4, 0, 0.6, 1);
}
</style>
