<template>
  <div class="relative color-select">
    <button
      @click="toggleDropdown"
      ref="colorButton"
      :class="[
        'w-7 h-7 rounded-full shadow-sm flex items-center justify-center transition-all duration-200 hover:scale-110',
        getColorClass(),
        'hover:ring-2 hover:ring-offset-2 hover:ring-gray-200',
        task.color === 'yellow'
          ? 'ring-2 ring-yellow-600 ring-inset'
          : 'ring-2 ring-white ring-inset',
      ]"
    >
      <span class="text-white"></span>
    </button>

    <Teleport to="body">
      <div
        v-if="isOpen"
        :style="dropdownStyle"
        class="fixed flex flex-row gap-2 p-2 bg-white rounded-lg shadow-lg border z-50"
        @click.stop
      >
        <button
          v-for="color in colors"
          :key="color.name"
          @click="selectColor(color.name)"
          :class="[
            'w-7 h-7 rounded-full transition-all duration-200 hover:scale-110',
            getColorClass(color.name),
            'hover:ring-2 hover:ring-offset-2',
            getColorRing(color.name),
            'ring-2 ring-white ring-inset',
          ]"
        ></button>
        <button
          @click="removeColor"
          class="w-7 h-7 bg-gray-100 rounded-full transition-all duration-200 hover:scale-110 hover:ring-2 hover:ring-offset-2 hover:ring-gray-200 ring-2 ring-gray-300 ring-inset flex items-center justify-center"
        >
          ✕
        </button>
      </div>
    </Teleport>
  </div>
</template>

<script>
const colorMap = {
  red: {
    bg: "bg-red-500 dark:bg-red-600",
    text: "text-white dark:text-white",
    mutedText: "text-red-200 dark:text-red-300",
    border: "border-red-600 dark:border-red-500",
    hover: "hover:bg-red-400 dark:hover:bg-red-500",
    number: "text-red-300 dark:text-red-400",
    ring: "hover:ring-red-200 dark:hover:ring-red-300",
  },
  orange: {
    bg: "bg-orange-500 dark:bg-orange-600",
    text: "text-white dark:text-white",
    mutedText: "text-orange-200 dark:text-orange-300",
    border: "border-orange-600 dark:border-orange-500",
    hover: "hover:bg-orange-400 dark:hover:bg-orange-500",
    number: "text-orange-300 dark:text-orange-400",
    ring: "hover:ring-orange-200 dark:hover:ring-orange-300",
  },
  yellow: {
    bg: "bg-yellow-400 dark:bg-yellow-500",
    text: "text-gray-900 dark:text-gray-900",
    mutedText: "text-yellow-700 dark:text-yellow-800",
    border: "border-yellow-500 dark:border-yellow-600",
    hover: "hover:bg-yellow-300 dark:hover:bg-yellow-400",
    number: "text-yellow-600 dark:text-yellow-700",
    ring: "hover:ring-yellow-600 dark:hover:ring-yellow-700",
  },
  green: {
    bg: "bg-green-500 dark:bg-green-600",
    text: "text-white dark:text-white",
    mutedText: "text-green-200 dark:text-green-300",
    border: "border-green-600 dark:border-green-500",
    hover: "hover:bg-green-400 dark:hover:bg-green-500",
    number: "text-green-300 dark:text-green-400",
    ring: "hover:ring-green-200 dark:hover:ring-green-300",
  },
  blue: {
    bg: "bg-blue-500 dark:bg-blue-600",
    text: "text-white dark:text-white",
    mutedText: "text-blue-200 dark:text-blue-300",
    border: "border-blue-600 dark:border-blue-500",
    hover: "hover:bg-blue-400 dark:hover:bg-blue-500",
    number: "text-blue-300 dark:text-blue-400",
    ring: "hover:ring-blue-200 dark:hover:ring-blue-300",
  },
  purple: {
    bg: "bg-purple-500 dark:bg-purple-600",
    text: "text-white dark:text-white",
    mutedText: "text-purple-200 dark:text-purple-300",
    border: "border-purple-600 dark:border-purple-500",
    hover: "hover:bg-purple-400 dark:hover:bg-purple-500",
    number: "text-purple-300 dark:text-purple-400",
    ring: "hover:ring-purple-200 dark:hover:ring-purple-300",
  },
};

export default {
  props: {
    task: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      isOpen: false,
      dropdownStyle: {
        top: "0px",
        left: "0px",
      },
      colors: [
        { name: "red" },
        { name: "orange" },
        { name: "yellow" },
        { name: "green" },
        { name: "blue" },
        { name: "purple" },
      ],
    };
  },
  mounted() {
    document.addEventListener("click", this.closeDropdown);
    window.addEventListener("resize", this.updateDropdownPosition);
    window.addEventListener("scroll", this.updateDropdownPosition, true);
  },
  beforeUnmount() {
    document.removeEventListener("click", this.closeDropdown);
    window.removeEventListener("resize", this.updateDropdownPosition);
    window.removeEventListener("scroll", this.updateDropdownPosition, true);
  },
  methods: {
    getColorClass(colorName = this.task?.color) {
      return colorName && colorMap[colorName]
        ? colorMap[colorName].bg
        : "bg-gray-500";
    },
    getColorRing(colorName) {
      return colorName && colorMap[colorName]
        ? colorMap[colorName].ring
        : "hover:ring-gray-200";
    },
    toggleDropdown() {
      this.isOpen = !this.isOpen;
      if (this.isOpen) {
        this.$nextTick(this.updateDropdownPosition);
      }
    },
    updateDropdownPosition() {
      const button = this.$refs.colorButton;
      if (!this.isOpen || !button) return;

      const buttonRect = button.getBoundingClientRect();
      const dropdownWidth = 244;

      this.dropdownStyle = {
        top: `${buttonRect.top + buttonRect.height / 2}px`,
        left: `${buttonRect.left - dropdownWidth - 24}px`,
        transform: "translateY(-50%)",
      };
    },
    selectColor(colorName) {
      this.$emit("update:task", {
        ...this.task,
        color: colorName,
      });
      this.isOpen = false;
    },
    removeColor() {
      this.$emit("update:task", {
        ...this.task,
        color: null,
      });
      this.isOpen = false;
    },
    closeDropdown(e) {
      if (
        e &&
        e.target.closest(".color-select") &&
        e.target.tagName === "BUTTON"
      ) {
        return;
      }
      this.isOpen = false;
    },
  },
};

export { colorMap };
</script>
