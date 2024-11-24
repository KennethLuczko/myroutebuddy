<template>
  <div class="sticky bottom-4 z-10 max-w-fit mx-auto">
    <div
      class="bg-gray-50/90 dark:bg-gray-900/90 backdrop-blur-sm border border-gray-200 dark:border-gray-700 rounded-lg shadow-lg p-2"
    >
      <div class="flex items-center gap-2">
        <div class="flex-1 flex items-center justify-start">
          <button
            @click="scrollToPosition('start')"
            class="w-8 h-8 bg-blue-500 text-white hover:bg-blue-600 rounded-full shadow-sm flex items-center justify-center transition-all duration-200 hover:scale-110 hover:ring-2 hover:ring-offset-2 hover:ring-gray-200 ring-2 ring-white ring-inset"
            title="Jump to start"
          >
            ↑
          </button>
        </div>

        <div class="flex items-center gap-2">
          <input
            type="text"
            v-model="jumpToNum"
            class="w-16 px-2 py-1 bg-white/50 dark:bg-gray-800/50 border border-gray-200 dark:border-gray-700 rounded focus:ring-2 focus:ring-blue-500 focus:outline-none dark:text-gray-200"
            placeholder="#"
            @keydown="handleKeydown"
            @keyup.enter="jumpToPosition"
          />
          <button
            @click="jumpToPosition"
            class="px-3 py-1 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition-colors text-sm"
          >
            Jump
          </button>
        </div>

        <div class="flex-1 flex items-center justify-end">
          <button
            @click="scrollToPosition('end')"
            class="w-8 h-8 bg-blue-500 text-white hover:bg-blue-600 rounded-full shadow-sm flex items-center justify-center transition-all duration-200 hover:scale-110 hover:ring-2 hover:ring-offset-2 hover:ring-gray-200 ring-2 ring-white ring-inset"
            title="Jump to end"
          >
            ↓
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "RouteNav",
  props: {
    route: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      jumpToNum: "",
    };
  },
  methods: {
    scrollToTaskElement(taskId, position = "center") {
      const taskElement = document.getElementById(`task-${taskId}`);
      if (taskElement) {
        const offset = 300; // Match the offset from pinned tasks

        if (position === "end") {
          // For end position, align to bottom of viewport
          const viewportHeight = window.innerHeight;
          const elementRect = taskElement.getBoundingClientRect();
          const scrollPosition =
            window.pageYOffset +
            elementRect.top -
            (viewportHeight - elementRect.height);

          window.scrollTo({
            top: scrollPosition,
            behavior: "smooth",
          });
        } else {
          // For start/center position, use standard offset
          const elementPosition = taskElement.getBoundingClientRect().top;
          const offsetPosition = elementPosition + window.pageYOffset - offset;

          window.scrollTo({
            top: offsetPosition,
            behavior: "smooth",
          });
        }

        // Add pulse effect
        taskElement.classList.remove("task-pulse-border");
        void taskElement.offsetWidth;
        taskElement.classList.add("task-pulse-border");
        setTimeout(() => {
          taskElement.classList.remove("task-pulse-border");
        }, 2500);
      }
    },

    scrollToPosition(position) {
      if (position === "start" && this.route.length > 0) {
        this.scrollToTaskElement(this.route[0].id, "start");
      } else if (position === "end" && this.route.length > 0) {
        this.scrollToTaskElement(this.route[this.route.length - 1].id, "end");
      }
    },

    jumpToPosition() {
      const num = parseInt(this.jumpToNum);
      if (num && num > 0) {
        const index = Math.min(num - 1, this.route.length - 1);
        this.scrollToTaskElement(this.route[index].id, "center");
        this.jumpToNum = "";
      }
    },
  },
};
</script>
