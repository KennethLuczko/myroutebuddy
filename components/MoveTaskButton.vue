<template>
  <div class="relative inline-flex">
    <button
      @click.stop="toggleInput"
      class="w-7 h-7 bg-purple-500 text-white hover:bg-purple-600 rounded-full shadow-sm flex items-center justify-center transition-all duration-200 hover:scale-110 hover:ring-2 hover:ring-offset-2 hover:ring-gray-200 ring-2 ring-white ring-inset"
      title="Move to position"
    >
      №
    </button>

    <!-- Popover with fixed positioning -->
    <div v-if="isOpen" class="fixed z-50" :style="popoverStyle">
      <div
        class="bg-white dark:bg-gray-800 rounded-lg shadow-lg border border-gray-200 dark:border-gray-700 p-2"
      >
        <div class="flex gap-2">
          <input
            type="text"
            v-model="inputValue"
            class="w-16 px-2 py-1 border rounded focus:ring-2 focus:ring-purple-500 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:text-gray-200"
            @keydown="handleKeydown"
            @keyup.enter="moveTask"
            ref="input"
          />
          <button
            @click.stop="moveTask"
            class="px-2 py-1 bg-purple-500 text-white rounded hover:bg-purple-600 transition-colors"
          >
            Move
          </button>
        </div>
        <div class="text-xs text-gray-500 dark:text-gray-400 mt-1">
          Enter position (1-{{ maxPosition }})
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MoveTaskButton",
  props: {
    currentPosition: {
      type: Number,
      required: true,
    },
    maxPosition: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      isOpen: false,
      inputValue: "",
      popoverStyle: {
        top: "0px",
        left: "0px",
      },
    };
  },
  methods: {
    toggleInput() {
      this.isOpen = !this.isOpen;
      if (this.isOpen) {
        this.inputValue = this.currentPosition.toString();
        this.$nextTick(() => {
          this.updatePopoverPosition();
          this.$refs.input?.focus();
          this.$refs.input?.select();
        });
      }
    },
    updatePopoverPosition() {
      const button = this.$el.getBoundingClientRect();
      const popoverWidth = 150;
      this.popoverStyle = {
        top: `${button.bottom + 5}px`,
        left: `${button.right - popoverWidth}px`,
      };
    },
    handleKeydown(e) {
      // Only allow numbers and specific keys
      if (
        !/^\d$/.test(e.key) &&
        ![
          "Backspace",
          "Delete",
          "ArrowLeft",
          "ArrowRight",
          "Tab",
          "Enter",
        ].includes(e.key)
      ) {
        e.preventDefault();
      }
    },
    moveTask() {
      const targetPosition = parseInt(this.inputValue) || 0;
      let newIndex;

      if (targetPosition <= 1) {
        newIndex = 0; // Move to start
      } else if (targetPosition >= this.maxPosition) {
        newIndex = this.maxPosition - 1; // Move to end
      } else {
        newIndex = targetPosition - 1;
      }

      this.$emit("move", newIndex);
      this.isOpen = false;
    },
    handleClickOutside(event) {
      if (this.isOpen && !this.$el.contains(event.target)) {
        this.isOpen = false;
      }
    },
  },
  mounted() {
    document.addEventListener("click", this.handleClickOutside);
  },
  beforeUnmount() {
    document.removeEventListener("click", this.handleClickOutside);
  },
};
</script>
