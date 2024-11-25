<template>
<<<<<<< HEAD
  <div
    :class="[
      'p-4 bg-white rounded-lg shadow dark:bg-gray-800',
      isFinalView ? 'w-full' : '',
    ]"
  >
    <RouteStats :route="route" />
    <PinnedTasks
      :pinned-tasks="pinnedTasks"
      :route="route"
      @unpin="unpinTask"
      @clear-all-pins="clearAllPins"
    />

    <h2 class="text-xl font-bold m-4 text-gray-800 dark:text-gray-200">
      Your Route
    </h2>

    <input
      type="text"
      v-model="searchQuery"
      placeholder="Search your route..."
      class="w-full border rounded-lg p-2 mb-4 focus:ring-2 focus:ring-blue-500 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:text-gray-200"
    />

    <Container
      :get-child-payload="getTaskPayload"
      group-name="tasks"
      @drop="onDrop"
    >
      <Draggable
        v-for="(task, index) in filteredRoute"
        :key="task.id"
        :id="`task-${task.id}`"
        :class="[
          'p-2 py-3 rounded-lg shadow border transition mb-2 relative cursor-pointer',
          task.completed
            ? 'bg-gray-100 hover:bg-gray-200'
            : getColorClass(task.color),
          !task.completed && (getHoverClass(task.color) || 'hover:bg-gray-100'),
          task.completed
            ? 'border-gray-200'
            : getBorderClass(task.color) ||
              (task.custom ? 'border-blue-600' : 'border-gray-200'),
        ]"
        drag-handler="handle"
=======
    <div
      :class="[
        'p-4 bg-white rounded-lg shadow dark:bg-gray-800',
        isFinalView ? 'w-full' : '',
      ]"
    >
      <RouteStats :route="route" />
  
      <!-- Banner indicating Final View -->
      <div
        v-if="isFinalView"
        class="bg-blue-500 text-white text-center p-2 rounded mb-4"
>>>>>>> upstream/main
      >
        You are in Final View. Click tasks to mark them as complete.
      </div>
  
      <h2 class="text-xl font-bold m-4 text-gray-800 dark:text-gray-200">
        Your Route
      </h2>
  
      <!-- Hide search bar in final view -->
      <input
        v-if="!isFinalView"
        type="text"
        v-model="searchQuery"
        placeholder="Search your route..."
        class="w-full border rounded-lg p-2 mb-4 focus:ring-2 focus:ring-blue-500 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:text-gray-200"
      />
  
      <!-- Task List -->
      <!-- When not in final view -->
      <Container
        v-if="!isFinalView"
        :get-child-payload="getTaskPayload"
        group-name="tasks"
        @drop="onDrop"
      >
        <Draggable
          v-for="(task, index) in filteredRoute"
          :key="task.id"
          :class="[
            'p-2 py-3 rounded-lg shadow border transition mb-2 relative cursor-pointer',
            task.completed
              ? 'bg-gray-100 hover:bg-gray-200 dark:bg-gray-700 dark:hover:bg-gray-600'
              : getColorClass(task.color),
            !task.completed &&
              (getHoverClass(task.color) || 'hover:bg-gray-100 dark:hover:bg-gray-600'),
            task.completed
              ? 'border-gray-200 dark:border-gray-700'
              : getBorderClass(task.color) ||
                (task.custom ? 'border-blue-600 dark:border-blue-500' : 'border-gray-200 dark:border-gray-700'),
          ]"
          drag-handler="handle"
        >
          <!-- Task Content -->
          <TaskContent
            :task="task"
            :index="index"
            :is-final-view="isFinalView"
            @toggle-completion="toggleCompletion"
            @edit-task="editTask"
            @save-edit="saveEdit"
            @cancel-edit="cancelEdit"
            @update-task-color="updateTaskColor"
            @insert-after="insertAfter"
            @remove-task="removeTaskById"
          />
        </Draggable>
      </Container>

      <!-- When in final view -->
      <div v-else>
        <div
          v-for="(task, index) in filteredRoute"
          :key="task.id"
          :class="[
            'p-2 py-3 rounded-lg shadow border transition mb-2 relative',
            task.completed
              ? 'bg-gray-100 hover:bg-gray-200 dark:bg-gray-700 dark:hover:bg-gray-600'
              : getColorClass(task.color),
            !task.completed &&
              (getHoverClass(task.color) || 'hover:bg-gray-100 dark:hover:bg-gray-600'),
            task.completed
              ? 'border-gray-200 dark:border-gray-700'
              : getBorderClass(task.color) ||
                (task.custom ? 'border-blue-600 dark:border-blue-500' : 'border-gray-200 dark:border-gray-700'),
            isFinalView ? 'cursor-pointer' : '',
          ]"
          @click="toggleCompletion(task)"
        >
          <!-- Task Content -->
          <TaskContent
            :task="task"
            :index="index"
            :is-final-view="isFinalView"
            @toggle-completion="toggleCompletion"
          />
<<<<<<< HEAD
          <div class="flex-1">
            <div class="flex flex-col">
              <!-- Editing Mode -->
              <div v-if="task.isEditing">
                <textarea
                  v-model="task.editableTask"
                  class="border p-2 rounded w-full mb-2 focus:outline-none focus:ring-2 focus:ring-blue-500 resize-y max-h-48"
                  rows="2"
                  @mousedown.stop
                  @touchstart.stop
                ></textarea>
                <div class="flex space-x-2">
                  <button
                    @click="saveEdit(task)"
                    class="bg-green-500 text-white px-3 py-1 rounded shadow hover:bg-green-600 transition"
                  >
                    Save
                  </button>
                  <button
                    @click="cancelEdit(task)"
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
                    'font-semibold mt-2 break-words',
                    task.completed
                      ? 'text-gray-600 line-through'
                      : getTextClass(task.color) || 'text-gray-800',
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
                    ? 'text-gray-600'
                    : getMutedTextClass(task.color) || 'text-gray-600',
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
              <div class="flex items-center space-x-2">
                <button
                  v-if="task.custom && !task.isEditing"
                  @click="editTask(task)"
                  class="w-7 h-7 bg-yellow-500 text-white hover:bg-yellow-600 rounded-full shadow-sm flex items-center justify-center transition-all duration-200 hover:scale-110 hover:ring-2 hover:ring-offset-2 hover:ring-gray-200 ring-2 ring-white ring-inset"
                >
                  ✎
                </button>
                <ColorSelect
                  :task="task"
                  @update:task="updateTaskColor($event)"
                />
                <button
                  v-if="!isPinned(task)"
                  @click="pinTask(task)"
                  class="w-7 h-7 bg-gray-500 text-white hover:bg-gray-600 rounded-full shadow-sm flex items-center justify-center transition-all duration-200 hover:scale-110 hover:ring-2 hover:ring-offset-2 hover:ring-gray-200 ring-2 ring-white ring-inset"
                >
                  📌
                </button>
                <button
                  v-else
                  @click="unpinTask(task)"
                  class="w-7 h-7 bg-blue-500 text-white hover:bg-blue-600 rounded-full shadow-sm flex items-center justify-center transition-all duration-200 hover:scale-110 hover:ring-2 hover:ring-offset-2 hover:ring-gray-200 ring-2 ring-white ring-inset"
                >
                  <span class="transform rotate-45">📌</span>
                </button>
                <!-- In the buttons section of your task -->
                <MoveTaskButton
                  :current-position="index + 1"
                  :max-position="route.length"
                  @move="moveTaskToPosition(task, $event)"
                />
                <button
                  v-if="!task.isEditing"
                  @click="insertAfter(task)"
                  class="w-7 h-7 bg-blue-500 text-white hover:bg-blue-600 rounded-full shadow-sm flex items-center justify-center transition-all duration-200 hover:scale-110 hover:ring-2 hover:ring-offset-2 hover:ring-gray-200 ring-2 ring-white ring-inset"
                >
                  ↓
                </button>
                <button
                  @click="removeTaskById(task.id)"
                  class="w-7 h-7 bg-red-500 text-white hover:bg-red-600 rounded-full shadow-sm flex items-center justify-center transition-all duration-200 hover:scale-110 hover:ring-2 hover:ring-offset-2 hover:ring-gray-200 ring-2 ring-white ring-inset"
                >
                  ✕
                </button>
              </div>
            </div>
          </div>
        </div>
      </Draggable>
    </Container>
    <RouteNav :route="route" />
  </div>
</template>

<script>
import { Container, Draggable } from "vue3-smooth-dnd";
import ColorSelect from "./ColorSelect.vue";
import { colorMap } from "./ColorSelect.vue";
import RegionIcon from "./RegionIcon.vue";
import RouteStats from "./RouteStats";
import PinnedTasks from "./PinnedTasks.vue";
import MoveTaskButton from "./MoveTaskButton.vue";
import RouteNav from "./RouteNav.vue";

export default {
  props: {
    route: Array,
    isFinalView: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      searchQuery: "",
    };
  },
  computed: {
    pinnedTasks() {
      return this.route.filter((task) => task.pinned);
    },
    filteredRoute() {
      if (!this.searchQuery) return this.route;
      const query = this.searchQuery.toLowerCase();
      return this.route.filter((task) =>
        task.task.toLowerCase().includes(query)
      );
=======
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import { Container, Draggable } from "vue3-smooth-dnd";
  import ColorSelect from "./ColorSelect.vue";
  import { colorMap } from "./ColorSelect.vue";
  import RegionIcon from "./RegionIcon.vue";
  import RouteStats from "./RouteStats.vue";
  import TaskContent from "./TaskContent.vue";
  
  export default {
    props: {
      route: Array,
      isFinalView: {
        type: Boolean,
        default: false,
      },
    },
    data() {
      return {
        searchQuery: "",
      };
>>>>>>> upstream/main
    },
    computed: {
      filteredRoute() {
        if (!this.searchQuery) return this.route;
        const query = this.searchQuery.toLowerCase();
        return this.route.filter((task) =>
          task.task.toLowerCase().includes(query)
        );
      },
    },
    methods: {
      getColorClass(color) {
        return color && colorMap[color] ? colorMap[color].bg : "bg-gray-50 dark:bg-gray-700";
      },
      getHoverClass(color) {
        return color && colorMap[color] ? colorMap[color].hover : null;
      },
      getBorderClass(color) {
        return color && colorMap[color] ? colorMap[color].border : null;
      },
      getTextClass(color) {
        return color && colorMap[color] ? colorMap[color].text : null;
      },
      getMutedTextClass(color) {
        return color && colorMap[color] ? colorMap[color].mutedText : null;
      },
      getNumberClass(color) {
        return color && colorMap[color] ? colorMap[color].number : null;
      },
      getTaskPayload(index) {
        return this.filteredRoute[index];
      },
      onDrop(dropResult) {
        if (
          dropResult.removedIndex !== null ||
          dropResult.addedIndex !== null
        ) {
          let newRoute = [...this.route];
  
          if (dropResult.removedIndex !== null) {
            newRoute.splice(dropResult.removedIndex, 1);
          }
  
          if (dropResult.addedIndex !== null) {
            const task = dropResult.payload;
  
            if (task.completed === undefined) {
              task.completed = false;
            }
  
            if (!newRoute.some((t) => t.id === task.id)) {
              newRoute.splice(dropResult.addedIndex, 0, task);
            } else {
              if (dropResult.removedIndex !== null) {
                newRoute.splice(dropResult.addedIndex, 0, task);
              } else {
                alert("Task is already in your route.");
              }
            }
          }
  
          this.$emit("update-route", newRoute);
        }
<<<<<<< HEAD

        this.$emit("update-route", newRoute);
      }
    },
    removeTaskById(taskId) {
      const updatedRoute = this.route.filter((task) => task.id !== taskId);
      this.$emit("update-route", updatedRoute);
    },
    toggleCompletion(task) {
      const updatedTask = { ...task, completed: !task.completed };
      if (updatedTask.completed && updatedTask.pinned) {
        updatedTask.pinned = false;
      }
      this.updateTask(updatedTask);
    },
    editTask(task) {
      const updatedTask = { ...task, isEditing: true, editableTask: task.task };
      this.updateTask(updatedTask);
    },
    saveEdit(task) {
      const updatedTask = {
        ...task,
        task: task.editableTask,
        isEditing: false,
      };
      delete updatedTask.editableTask;
      this.updateTask(updatedTask);
    },
    cancelEdit(task) {
      const updatedTask = { ...task, isEditing: false };
      delete updatedTask.editableTask;
      this.updateTask(updatedTask);
    },
    updateTask(updatedTask) {
      const index = this.route.findIndex((t) => t.id === updatedTask.id);
      if (index !== -1) {
=======
      },
      removeTaskById(taskId) {
        const updatedRoute = this.route.filter((task) => task.id !== taskId);
        this.$emit("update-route", updatedRoute);
      },
      toggleCompletion(task) {
        const updatedTask = { ...task, completed: !task.completed };
        this.updateTask(updatedTask);
      },
      editTask(task) {
        const updatedTask = {
          ...task,
          isEditing: true,
          editableTask: task.task,
        };
        this.updateTask(updatedTask);
      },
      saveEdit(task) {
        const updatedTask = {
          ...task,
          task: task.editableTask,
          isEditing: false,
        };
        delete updatedTask.editableTask;
        this.updateTask(updatedTask);
      },
      cancelEdit(task) {
        const updatedTask = { ...task, isEditing: false };
        delete updatedTask.editableTask;
        this.updateTask(updatedTask);
      },
      updateTask(updatedTask) {
        const index = this.route.findIndex((t) => t.id === updatedTask.id);
        if (index !== -1) {
          const newRoute = [...this.route];
          newRoute.splice(index, 1, updatedTask);
          this.$emit("update-route", newRoute);
        }
      },
      insertAfter(task) {
        const index = this.route.findIndex((t) => t.id === task.id);
        const newTask = {
          id: Date.now(),
          task: "",
          points: 0,
          custom: true,
          region: "Global",
          completed: false,
          isEditing: true,
          editableTask: "",
        };
  
>>>>>>> upstream/main
        const newRoute = [...this.route];
        newRoute.splice(index + 1, 0, newTask);
        this.$emit("update-route", newRoute);
      },
      updateTaskColor(updatedTask) {
        this.updateTask(updatedTask);
      },
    },
    components: {
      Container,
      Draggable,
      ColorSelect,
      RegionIcon,
      RouteStats,
      TaskContent,
    },
<<<<<<< HEAD
    updateTaskColor(updatedTask) {
      this.updateTask(updatedTask);
    },
    pinTask(task) {
      const updatedTask = { ...task, pinned: true };
      this.updateTask(updatedTask);
    },

    unpinTask(task) {
      const updatedTask = { ...task, pinned: false };
      this.updateTask(updatedTask);
    },
    clearAllPins(tasksToUnpin) {
      const updatedRoute = this.route.map((task) => {
        if (tasksToUnpin.some((pinnedTask) => pinnedTask.id === task.id)) {
          return { ...task, pinned: false };
        }
        return task;
      });
      this.$emit("update-route", updatedRoute);
    },

    isPinned(task) {
      return task.pinned === true;
    },
    moveTaskToPosition(task, newIndex) {
      const oldIndex = this.route.findIndex((t) => t.id === task.id);
      if (oldIndex !== -1) {
        const newRoute = [...this.route];
        // Remove from old position
        newRoute.splice(oldIndex, 1);
        // Insert at new position
        newRoute.splice(newIndex, 0, task);
        this.$emit("update-route", newRoute);
      }
    },
  },
  created() {
    this.pinnedTasks = this.route.filter((task) => task.pinned);
  },
  components: {
    Container,
    Draggable,
    ColorSelect,
    RegionIcon,
    RouteStats,
    PinnedTasks,
    MoveTaskButton,
    RouteNav,
  },
};
</script>
=======
  };
  </script>
  
>>>>>>> upstream/main
