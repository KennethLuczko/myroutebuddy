<!-- TaskContent.vue -->
<template>
  <div>
    <span
      :class="[
        'absolute top-1 left-1.5 text-xs font-mono',
        task.completed
          ? 'text-gray-600 dark:text-gray-400'
          : task.color
          ? getNumberClass(task.color)
          : 'text-gray-600 dark:text-gray-400',
      ]"
    >
      {{ index + 1 }}
    </span>

    <div class="flex items-center space-x-2">
      <!-- Checkbox (only shown when not in final view) -->
      <input
        v-if="!isFinalView"
        type="checkbox"
        :checked="task.completed"
        @change.stop="toggleCompletion(task)"
        class="flex-shrink-0 w-5 h-5 text-blue-500 rounded border-gray-300 dark:border-gray-600 focus:ring focus:ring-blue-200 cursor-pointer mr-1"
      />

      <div class="flex-1">
        <div class="flex flex-col">
          <!-- Editing Mode -->
          <div v-if="task.isEditing">
            <textarea
              v-model="task.editableTask"
              class="border dark:border-gray-600 p-2 rounded w-full mb-2 focus:outline-none focus:ring-2 focus:ring-blue-500 resize-y max-h-48 dark:bg-gray-700 dark:text-gray-200"
              rows="2"
              @mousedown.stop
              @touchstart.stop
            ></textarea>
            <div class="flex space-x-2">
              <button
                @click.stop="saveEdit(task)"
                class="bg-green-500 text-white px-3 py-1 rounded shadow hover:bg-green-600 transition"
              >
                Save
              </button>
              <button
                @click.stop="cancelEdit(task)"
                class="bg-gray-500 text-white px-3 py-1 rounded shadow hover:bg-gray-600 transition"
              >
                Cancel
              </button>
            </div>
          </div>
          <!-- Display Mode -->
          <div v-else>
            <h3
              :class="[
                'font-semibold mt-2 break-words whitespace-pre-wrap ',
                task.completed
                  ? 'text-gray-600 dark:text-gray-400 line-through'
                  : getTextClass(task.color) || 'text-gray-800 dark:text-gray-200',
              ]"
            >
              {{ task.task }}
            </h3>
          </div>
        </div>
        <div class="flex items-center space-x-2 w-full pt-0.5">
          <p
            :class="[
              'text-sm mr-auto flex justify-center',
              task.completed
                ? 'text-gray-600 dark:text-gray-400'
                : getMutedTextClass(task.color) || 'text-gray-600 dark:text-gray-400',
            ]"
          >
            <RegionIcon
              v-if="task.custom"
              :region="task.region"
              :is-custom="true"
              class="mr-2"
            />
            <RegionIcon v-else :region="task.region" class="mr-2" />
            {{
              task.custom ? "Custom Task / Note" : `${task.points} points`
            }}
          </p>
          <!-- Action Buttons (only shown when not in final view) -->
          <div class="flex items-center space-x-2">
            <button
              v-if="!isFinalView && task.custom && !task.isEditing"
              @click.stop="editTask(task)"
              class="w-7 h-7 bg-yellow-500 text-white hover:bg-yellow-600 rounded-full shadow-sm flex items-center justify-center transition-all duration-200 hover:scale-110 hover:ring-2 hover:ring-offset-2 hover:ring-gray-200 dark:hover:ring-gray-700 ring-2 ring-white dark:ring-gray-800 ring-inset"
            >
              ✎
            </button>
            <ColorSelect
              v-if="!isFinalView"
              :task="task"
              @update:task="updateTaskColor($event)"
            />
            <button
              v-if="!isFinalView && !task.isEditing"
              @click.stop="insertAfter(task)"
              class="w-7 h-7 bg-blue-500 text-white hover:bg-blue-600 rounded-full shadow-sm flex items-center justify-center transition-all duration-200 hover:scale-110 hover:ring-2 hover:ring-offset-2 hover:ring-gray-200 dark:hover:ring-gray-700 ring-2 ring-white dark:ring-gray-800 ring-inset"
            >
              ↓
            </button>
            <button
              v-if="!isFinalView"
              @click.stop="removeTaskById(task.id)"
              class="w-7 h-7 bg-red-500 text-white hover:bg-red-600 rounded-full shadow-sm flex items-center justify-center transition-all duration-200 hover:scale-110 hover:ring-2 hover:ring-offset-2 hover:ring-gray-200 dark:hover:ring-gray-700 ring-2 ring-white dark:ring-gray-800 ring-inset"
            >
              ✕
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
  
  <script>
  import RegionIcon from "./RegionIcon.vue";
  import ColorSelect from "./ColorSelect.vue";
  import { colorMap } from "./ColorSelect.vue";
  
  export default {
    props: {
      task: Object,
      index: Number,
      isFinalView: Boolean,
    },
    methods: {
      getTextClass(color) {
        return color && colorMap[color] ? colorMap[color].text : null;
      },
      getMutedTextClass(color) {
        return color && colorMap[color] ? colorMap[color].mutedText : null;
      },
      getNumberClass(color) {
        return color && colorMap[color] ? colorMap[color].number : null;
      },
      toggleCompletion(task) {
        this.$emit("toggle-completion", task);
      },
      editTask(task) {
        this.$emit("edit-task", task);
      },
      saveEdit(task) {
        this.$emit("save-edit", task);
      },
      cancelEdit(task) {
        this.$emit("cancel-edit", task);
      },
      updateTaskColor(updatedTask) {
        this.$emit("update-task-color", updatedTask);
      },
      insertAfter(task) {
        this.$emit("insert-after", task);
      },
      removeTaskById(taskId) {
        this.$emit("remove-task", taskId);
      },
    },
    components: {
      RegionIcon,
      ColorSelect,
    },
  };
  </script>
  