<template>
  <div class="min-h-screen flex bg-gray-50 dark:bg-gray-900">
    <!-- Sidebar -->
    <div :class="{'lg:fixed lg:inset-y-0 lg:z-50 flex flex-col transition-all duration-300 ': true, 'lg:w-0 md:w-0': isCollapsed, 'lg:w-2/6 md:w-full': !isCollapsed, 'absolute  top-0 left-0 z-40': true,
      }">
      <!-- Moved button toggle to parent div for UX, started untoggled  -->
      <div class="flex items-center justify-center p-2 bg-blue-600 rounded-lg cursor-pointer " @click="toggleSidebar" type="button" aria-label="Toggle progress sidebar"> 
          <span class="text-lg text-white">
            <span v-if="isCollapsed">&gt;</span> <!-- Right arrow when collapsed -->
            <span v-else>&lt;</span> <!-- Left arrow when expanded -->
          </span>
      </div>
      <div v-show="!isCollapsed" class="flex grow flex-col gap-y-5 overflow-y-auto scrollbar-hide lg:border-r lg:border-r-gray-700 border-b-2 border-b-gray-700 lg:border-b-0  bg-white px-6 pb-4 dark:bg-gray-800 " >
        <!-- Progress Section -->
        <div class="mt-4">
          <h3 class="text-lg font-semibold text-gray-700 mb-4 dark:text-gray-200">Progress</h3>
          <div class="w-full bg-gray-200 rounded-full h-6">
            <div
              class="bg-blue-500 h-6 rounded-full transition-all"
              :style="{ width: progressPercentage + '%' }"
            ></div>
          </div>
          <p class="text-md text-gray-500 mt-2 dark:text-gray-400">
            {{ completedPoints }} of {{ totalPoints }} points completed
          </p>
        </div>

        <!-- Time Until Launch -->
        <div class="mt-4">
          <h3 class="text-lg font-semibold text-gray-700 dark:text-gray-200">Time Until Launch</h3>
          <p class="text-md text-gray-500 dark:text-gray-400">{{ timeUntilLaunch }}</p>
        </div>

        <!-- Region Selection -->
        <div class="mt-8">
          <RegionFilter
            :regions="regions"
            :selectedRegions="selectedRegions"
            @update-regions="updateRegions"
          />
        </div>

          <!-- New Section for Displaying Combined Region Information
          <div v-if="selectedRegions.length > 0" class="mt-4 text-white">
          <h3 class="text-lg font-semibold">Combined Region Information</h3>
          <div class="mt-2 text-gray-700 dark:text-gray-200">
            <p>
              <strong>Notable Settlements:</strong>
              {{ combinedRegionInfo.settlements.join(', ') }}
            </p>
            <br />
            <p>
              <strong>Restricted Travel:</strong>
              {{ combinedRegionInfo.restrictedTravel.join(', ') }}
            </p>
            <br />
            <p>
              <strong>Combat Activities:</strong>
              {{ combinedRegionInfo.combatActivities.join(', ') }}
            </p>
            <br />
            <p>
              <strong>Non-Combat Activities:</strong>
              {{ combinedRegionInfo.nonCombatActivities.join(', ') }}
            </p>
            <br />
            <p>
              <strong>Shops:</strong>
              {{ combinedRegionInfo.shops.join(', ') }}
            </p>
            <br />
            <p>
              <strong>Quests:</strong> {{ combinedRegionInfo.unlocks.quests.join(', ') }}
              <br />
              <br />
              <strong>Achievement Diary Tasks:</strong>
              {{ combinedRegionInfo.unlocks.achievementDiaryTasks.join(', ') }}
            </p>
          </div>
          <div v-if="loading" class="mt-2">Loading...</div>
          <div v-if="error" class="mt-2 text-red-500">{{ error }}</div>
        </div> -->

        <!-- Manage Routes Section -->
        <nav class="flex flex-1 flex-col mt-8">
          <h3 class="text-lg font-semibold text-gray-700 mb-4 dark:text-gray-100">Manage Your Routes</h3>
            <p class="text-sm text-gray-700 dark:text-gray-200 mb-4">
              Have an awesome route and want to share it with everyone? See how you can add it to the pre-loaded default routes.
              <a
                href="https://github.com/KennethLuczko/myroutebuddy?tab=readme-ov-file#how-to-add-your-own-route-to-the-default-routes"
                class="text-blue-500 underline hover:text-blue-700"
                target="_blank"
                rel="noopener noreferrer"
              >
                Learn more.
              </a>
            </p>
          <div class="space-y-3">
            <!-- Save Route -->
            <button
              @click="saveRoute"
              class="w-full bg-blue-500 text-white px-4 py-2 rounded-lg shadow-sm hover:bg-blue-600 transition dark:bg-blue-700 dark:hover:bg-blue-800"
            >
              Save Route
            </button>

            <!-- Load Route -->
            <div class="space-y-2">
              <select
                v-model="selectedRoute"
                class="w-full bg-gray-100 border border-gray-300 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-200"
              >
                <option value="" disabled>Select a Route</option>
                <option
                  v-for="(routeName, index) in Object.keys(savedRoutes)"
                  :key="index"
                  :value="routeName"
                >
                  {{ routeName }}
                </option>
              </select>
              <button
                @click="loadRoute"
                :disabled="!selectedRoute"
                class="w-full bg-gray-300 text-gray-700 py-2 rounded-lg shadow-sm hover:bg-gray-400 transition disabled:opacity-50 dark:bg-gray-700 dark:text-gray-300"
              >
                Load Route
              </button>
            </div>

            <!-- Share Route -->
            <button
              @click="shareRoute"
              class="w-full bg-green-500 text-white px-4 py-2 rounded-lg shadow-sm hover:bg-green-600 transition dark:bg-green-700 dark:hover:bg-green-800"
            >
              Share Route
            </button>

            <!-- Import Route -->
            <div>
              <textarea
                v-model="importedRoute"
                placeholder="Paste shared route JSON here..."
                class="w-full bg-gray-100 border border-gray-300 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-200"
              ></textarea>
              <button
                @click="importRoute"
                :disabled="!importedRoute"
                class="w-full bg-purple-500 text-white py-2 rounded-lg shadow-sm hover:bg-purple-600 transition disabled:opacity-50 dark:bg-purple-700 dark:hover:bg-purple-800"
              >
                Import Route
              </button>
            </div>

            <!-- Reset App -->
            <button
              @click="confirmResetApp"
              class="w-full bg-red-500 text-white px-4 py-2 rounded-lg shadow-sm hover:bg-red-600 transition dark:bg-red-700 dark:hover:bg-red-800"
            >
              Reset
            </button>
          </div>

          <!-- Dark Mode Toggle Section -->
          <div class="mt-6 pt-4 border-t border-gray-200 dark:border-gray-700">
            <h3 class="text-lg font-semibold text-gray-700 dark:text-gray-100 mb-4">Theme</h3>
            <button
              @click="toggleDarkMode"
              class="w-full bg-gray-800 text-white px-4 py-2 rounded-lg shadow-sm hover:bg-gray-700 transition dark:bg-gray-100 dark:text-gray-800 dark:hover:bg-gray-200"
            >
              Toggle Dark Mode
            </button>
          </div>

          <!-- Change Log Section -->
          <div class="mt-6 pt-4 border-t border-gray-200 dark:border-gray-700">
            <h3 class="text-lg font-semibold text-gray-700 dark:text-gray-100">Change Log (latest 3 changes)</h3>
            <a
              href="https://github.com/KennethLuczko/myroutebuddy"
              class="text-blue-500 underline hover:text-blue-700 text-sm"
              target="_blank"
              rel="noopener noreferrer"
            >
              Contribute to this project.
            </a>
            <ul>
              <li
                v-for="(log, index) in changeLog"
                :key="index"
                class="p-4 bg-gray-100 dark:bg-gray-900 rounded-lg mb-2 shadow border dark:border-gray-700"
              >
                <p class="text-sm text-gray-800 dark:text-gray-200">
                  <span class="font-semibold">Date:</span> {{ log.date }}
                </p>
                <p class="text-sm text-gray-800 dark:text-gray-200">
                  <span class="font-semibold">Time:</span> {{ log.time }}
                </p>
                <p class="text-sm text-gray-800 dark:text-gray-200">
                  <span class="font-semibold">Change: </span>
                  <a
                    :href="log.url"
                    class="text-blue-500 underline hover:text-blue-700"
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    {{ log.change }}
                  </a>
                </p>
                <p class="text-sm text-gray-800 dark:text-gray-200">
                  <span class="font-semibold">Contributor:</span> {{ log.contributor }}
                </p>
              </li>
            </ul>
          </div>
        </nav>
      </div>
    </div>
    <!-- Sticky Scroll to Top Button for Mobile UX -->
    <div
      ref="scrollTopButton"
      class="fixed bottom-0 right-0 pb-3 pr-5 transition z-20">
      <button
        class="flex justify-center items-center w-12 h-12 rounded-full bg-white text-black cursor-pointer text-3xl transition transform hover:scale-110 hover:bg-blue-500 hover:text-white hover:shadow-lg"
        @click="scrollToTop"
        role="button"
        aria-label="Scroll to top of the page">
        ↑
      </button>
    </div>

    <!-- Main Content Area -->
    <div :class="{'lg:pl-1/3vw': !isCollapsed, 'flex-1': true}">
      <div class="p-6">
        <h1 class="text-4xl font-bold mb-8 text-gray-800 dark:text-white">My Route Buddy - Leagues 5: Raging Echoes Task Route Planner</h1>
        <h2 class="text-md mb-2 text-gray-800 dark:text-gray-200">
          If you have any issues, want to report a bug, have a suggestion, or want to help develop this web app yourself, please visit
          <a href="https://github.com/KennethLuczko/myroutebuddy" 
            class="text-blue-500 underline hover:text-blue-700" 
            target="_blank" 
            rel="noopener noreferrer">
            this GitHub and contribute.
          </a>
        </h2>
        <h3 class="text-md mb-2 text-gray-800 dark:text-gray-200">
          <span class="text-red-600 font-bold">This app is developed for desktop. Mobile will work, but has bugs and limitations.</span>
        </h3>
        <h4 class="text-md mb-8 text-gray-800 dark:text-gray-200">
          Not sure where to begin? Discover your regions, combat masteries, and more
          <a href="https://docs.google.com/spreadsheets/d/1LJVEIIR9D56FF9PyUzb4nhofaCjpzSWTRGsUNsH7lNw/copy" 
            class="text-blue-500 underline hover:text-blue-700" 
            target="_blank" 
            rel="noopener noreferrer">
            here.
          </a>
        </h4>

        <!-- Final View Toggle Button -->
        <button
          @click="toggleFinalView"
          class="mb-4 bg-gray-800 text-white px-4 py-2 rounded-lg shadow-sm hover:bg-gray-700 transition dark:bg-gray-100 dark:text-gray-800 dark:hover:bg-gray-200"
        >
          {{ isFinalView ? 'Exit Final View (removes available tasks)' : 'Enter Final View (removes available tasks)' }}
        </button>

        <!-- Adjusted Content Based on Final View State -->
        <div>
          <div v-if="!isFinalView" class="grid grid-cols-1 md:grid-cols-2 gap-8">
            <!-- Available Tasks -->
            <TaskList :tasks="filteredTasks" @add-task="addTask" @notify="addNotification" />

            <!-- Your Route -->
            <RouteBuilder :route="route" @update-route="updateRoute" />
          </div>

          <div v-else>
            <!-- Your Route Spanning Full Width -->
            <RouteBuilder :route="route" @update-route="updateRoute" :isFinalView="true" />
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- Include the Notification Component -->
  <Notification :notifications="notifications" @remove-notification="removeNotification" />

  <!-- Include the Confirm Dialog Component -->
  <ConfirmDialog
  :show="showConfirmDialog"
  :message="confirmMessage"
  @confirm="handleConfirm"
  @cancel="handleCancel"
  />
</template>

<script>
import TaskList from './components/TaskList.vue';
import RegionFilter from './components/RegionFilter.vue';
import RouteBuilder from './components/RouteBuilder.vue';
import axios from 'axios';
import { onMounted, onUnmounted, ref } from "vue"; 
import LZString from 'lz-string';
import Notification from './components/Notification.vue';
import ConfirmDialog from './components/ConfirmDialog.vue';

export default {
  components: { TaskList, RegionFilter, RouteBuilder },
  data() {
    return {
      regions: [
      { id: 2, name: 'Asgarnia', api: 'Asgarnia' },
        { id: 3, name: 'Fremennik', api: 'Fremennik_Province' },
        { id: 4, name: 'Kandarin', api: 'Kandarin' },
        { id: 5, name: 'Desert', api: 'Kharidian_Desert' },
        { id: 6, name: 'Morytania', api: 'Morytania' },
        { id: 7, name: 'Tirannwn', api: 'Tirannwn' },
        { id: 8, name: 'Wilderness', api: 'Wilderness' },
        { id: 9, name: 'Kourend', api: 'Kebos_and_Kourend' },
        { id: 10, name: 'Varlamore', api: 'Varlamore' },
      ],
      selectedRegions: [],
      tasks: [],
      route: [],
      savedRoutes: {},
      selectedRoute: '',
      importedRoute: '',
      isFinalView: false,
      changeLog: [],
      launchDate: new Date('2024-11-27T07:00:00-05:00'), // Launch date in EST
      intervalId: null,
      timeUntilLaunch: '', // Countdown string
      isCollapsed: false,
      notifications: [],
      showConfirmDialog: false,
      confirmMessage: '',
      confirmAction: null,
      combinedRegionInfo: {
        settlements: [],
        restrictedTravel: [],
        combatActivities: [],
        nonCombatActivities: [],
        shops: [],
        unlocks: {
          quests: [],
          achievementDiaryTasks: [],
        },
        drops: [],
      },
      loading: false,
      error: null, 
    };
  },
  computed: {
    filteredTasks() {
      return this.tasks.filter((task) => {
        // Always include tasks from the Global region
        const isGlobalTask = task.region === 'Global';

        // Check if the task's region matches one of the selected regions
        const isRegionMatch = this.selectedRegions.includes(task.region);

        // Ensure the task is not already in the route
        const isNotInRoute = !this.route.some((r) => r.id === task.id);

        // Include tasks that are either global or match selected regions, and are not in the route
        return (isGlobalTask || isRegionMatch) && isNotInRoute;
      });
    },
    totalPoints() {
      return this.route.reduce((sum, task) => sum + task.points, 0);
    },
    completedPoints() {
      return this.route.reduce((sum, task) => (task.completed ? sum + task.points : sum), 0);
    },
    progressPercentage() {
      return this.totalPoints ? (this.completedPoints / this.totalPoints) * 100 : 0;
    },
    recentChangeLog() {
      return this.changeLog.slice(-3);
    },
  },
  methods: {
    updateTimeUntilLaunch() {
      const now = new Date();
      const timeDifference = this.launchDate - now;

      if (timeDifference <= 0) {
        clearInterval(this.intervalId);
        this.timeUntilLaunch = 'Launch time has arrived!';
        return;
      }

      const days = Math.floor(timeDifference / (1000 * 60 * 60 * 24));
      const hours = Math.floor((timeDifference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      const minutes = Math.floor((timeDifference % (1000 * 60 * 60)) / (1000 * 60));
      const seconds = Math.floor((timeDifference % (1000 * 60)) / 1000);

      this.timeUntilLaunch = `${days}d ${hours}h ${minutes}m ${seconds}s`;
    },
    updateTasks(updatedTasks) {
      this.tasks = updatedTasks;
      localStorage.setItem('tasks', JSON.stringify(this.tasks));
    },
    updateRegions(regions) {
      this.selectedRegions = regions;
      localStorage.setItem('selectedRegions', JSON.stringify(regions));
    },
    addTask(task) {
    if (!this.route.some((r) => r.id === task.id)) {
      this.route.push({ ...task, completed: false });
      localStorage.setItem('route', JSON.stringify(this.route));
    } else {
      this.addNotification('Task is already in your route.', 'error');
    }
  },
    updateRoute(newRoute) {
      this.route = newRoute;
      localStorage.setItem('route', JSON.stringify(this.route));
    },
    saveRoute() {
      const routeName = prompt('Enter a name for this route:');
      if (routeName) {
        const routeData = this.route.map(({ region, ...task }) => task);
        this.savedRoutes[routeName] = JSON.stringify(routeData);
        localStorage.setItem('savedRoutes', JSON.stringify(this.savedRoutes));
        this.addNotification(`Route "${routeName}" has been saved.`, 'success');
      }
    },
    loadRoute() {
      if (this.selectedRoute && this.savedRoutes[this.selectedRoute]) {
        this.route = JSON.parse(this.savedRoutes[this.selectedRoute]);
        this.addNotification(`Route "${this.selectedRoute}" has been loaded.`, 'success');
      }
    },
    shareRoute() {
      const routeData = this.route.map(({ region, ...task }) => task);
      const routeString = JSON.stringify(routeData, null, 2);

      // const compressedRoute = LZString.compressToEncodedURIComponent(routeString);

      // const shareableURL = `${window.location.origin}${window.location.pathname}?route=${compressedRoute}`;

      // navigator.clipboard.writeText(shareableURL).then(() => {
      //   this.addNotification('Shareable URL copied to clipboard! Share it with others.', 'success');
      // });

      const blob = new Blob([JSON.stringify(routeData, null, 2)], { type: 'application/json' });
      const link = document.createElement('a');
      link.href = URL.createObjectURL(blob);
      link.download = 'route.json';
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);

      // console.log('Shareable Link:', shareableURL);
    },
    importRoute() {
      try {
        const imported = JSON.parse(this.importedRoute);
        const routeName = prompt('Enter a name for the imported route:');
        if (routeName) {
          const cleanedRoute = imported.map(({ region, ...task }) => task);
          this.savedRoutes[routeName] = JSON.stringify(cleanedRoute);
          localStorage.setItem('savedRoutes', JSON.stringify(this.savedRoutes));
          this.addNotification(`Route "${routeName}" has been imported and saved.`, 'success');
          this.importedRoute = '';
        }
      } catch (error) {
        this.addNotification('Invalid route JSON. Please try again.', 'error');
      }
    },
    resetApp() {
      this.route = [];
      this.selectedRegions = [];
      localStorage.removeItem('route');
      localStorage.removeItem('selectedRegions');

      // Clear the route parameter from the URL
      const url = new URL(window.location);
      url.searchParams.delete('route');
      window.history.replaceState({}, document.title, url.toString());

      this.addNotification('App has been reset.', 'success');
    },
    toggleDarkMode() {
      const html = document.documentElement;
      if (html.classList.contains('dark')) {
        html.classList.remove('dark');
        localStorage.setItem('theme', 'light');
      } else {
        html.classList.add('dark');
        localStorage.setItem('theme', 'dark');
      }
    },
    toggleFinalView() {
      this.isFinalView = !this.isFinalView;
    },
    loadTasks() {
      axios
        .get('./tasks.json')
        .then((response) => {
          this.tasks = response.data.map((task) => ({
            ...task,
            task: `${task.task}`,
          }));
          console.log('Tasks loaded:', this.tasks);
        })
        .catch((error) => {
          console.error('Error loading tasks:', error);
        });
    },
    fetchLatestCommits() {
      const cachedData = localStorage.getItem('changeLog');
      const cachedTime = localStorage.getItem('changeLogTime');
      const now = Date.now();

      if (cachedData && cachedTime && now - cachedTime < 15 * 60 * 1000) {
        this.changeLog = JSON.parse(cachedData);
        return;
      }

      const repoOwner = 'KennethLuczko';
      const repoName = 'myroutebuddy';

      axios
        .get(`https://api.github.com/repos/${repoOwner}/${repoName}/commits`, {
          params: { per_page: 3, sort: 'date', direction: 'desc' },
        })
        .then((response) => {
          this.changeLog = response.data.map((commit) => ({
            date: new Date(commit.commit.author.date).toLocaleDateString(),
            time: new Date(commit.commit.author.date).toLocaleTimeString(),
            change: commit.commit.message,
            contributor: commit.author ? commit.author.login : commit.commit.author.name,
            url: commit.html_url,
          }));

          localStorage.setItem('changeLog', JSON.stringify(this.changeLog));
          localStorage.setItem('changeLogTime', now);
        })
        .catch((error) => {
          console.error('Error fetching commits:', error);
        });
    },
    toggleSidebar() {
      this.isCollapsed = !this.isCollapsed;
    },
    // Scroll to Top Button
    scrollTopButton: ref(null),
    handleScroll() {
      if (window.scrollY > 0) {
        this.scrollTopButton.value.classList.remove("invisible");
      } else {
        this.scrollTopButton.value.classList.add("invisible");
      }
    },
    scrollToTop() {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    },
    async fetchRegionInfo(region) {
      this.loading = true;
      this.error = null;
      try {
        const selectedRegion = this.regions.find(r => r.name === region);
        const apiRegion = selectedRegion ? selectedRegion.api : region;

        console.log(`Fetching data for region: ${apiRegion}`);

        const response = await axios.get(
          `https://oldschool.runescape.wiki/api.php?action=query&titles=Raging_Echoes_League/Areas/${apiRegion}&prop=revisions&rvprop=content&format=json`
        );

        console.log('API Response:', response.data);

        const regionData = this.parseRegionInfo(response.data);
        
        this.cleanRegionData(regionData);

        this.combineRegionInfo(regionData);
      } catch (err) {
        console.error('Error fetching region information:', err);
        this.error = 'Failed to load region information. Please try again.';
      } finally {
        this.loading = false;
      }
    },
    parseRegionInfo(data) {
      const page = Object.values(data.query.pages)[0];
      const notableInfo = {
        settlements: [],
        restrictedTravel: [],
        combatActivities: [],
        nonCombatActivities: [],
        shops: [],
        unlocks: {
          quests: [],
          achievementDiaryTasks: [],
        },
        drops: [],
      };

      if (page && page.revisions && page.revisions.length > 0) {
        const content = page.revisions[0]['*'];

        // Extract notable settlements
        notableInfo.settlements = this.extractSection(content, '===Notable settlements===', '===');

        // Extract restricted travel
        notableInfo.restrictedTravel = this.extractSection(content, '===Restricted travel===', '===');

        // Extract combat-related activities
        notableInfo.combatActivities = this.extractSection(
          content,
          '===Notable combat-related activities===',
          '==='
        );

        // Extract non-combat activities
        notableInfo.nonCombatActivities = this.extractSection(
          content,
          '===Notable non-combat activities===',
          '==='
        );

        // Extract shops
        notableInfo.shops = this.extractSection(content, '===Notable shops===', '===');

        // Extract unlocks: quests
        notableInfo.unlocks.quests = this.extractSection(content, '===Quests===', '===');

        // Extract unlocks: achievement diary tasks
        notableInfo.unlocks.achievementDiaryTasks = this.extractSection(
          content,
          '===Achievement diary tasks===',
          '==='
        );

      }

      return notableInfo;
    },
    // Utility function to extract a section from the content
    extractSection(content, startMarker, endMarker) {
      const startIndex = content.indexOf(startMarker);
      if (startIndex === -1) return [];
      const endIndex = content.indexOf(endMarker, startIndex + startMarker.length) || content.length;
      const section = content.slice(startIndex + startMarker.length, endIndex).trim();

      // Split by lines and clean up bullet points
      return section
        .split('\n')
        .filter((line) => line.startsWith('*')) // Lines starting with '*'
        .map((line) => line.replace(/^\*\s*/, '').trim()
        ); // Remove '* ' and trim
    },
    combineRegionInfo(regionData) {
      this.combinedRegionInfo.settlements = [...this.combinedRegionInfo.settlements, ...regionData.settlements];
      this.combinedRegionInfo.restrictedTravel = [...this.combinedRegionInfo.restrictedTravel, ...regionData.restrictedTravel];
      this.combinedRegionInfo.combatActivities = [...this.combinedRegionInfo.combatActivities, ...regionData.combatActivities];
      this.combinedRegionInfo.nonCombatActivities = [...this.combinedRegionInfo.nonCombatActivities, ...regionData.nonCombatActivities];
      this.combinedRegionInfo.shops = [...this.combinedRegionInfo.shops, ...regionData.shops];
      this.combinedRegionInfo.unlocks.quests = [...this.combinedRegionInfo.unlocks.quests, ...regionData.unlocks.quests];
      this.combinedRegionInfo.unlocks.achievementDiaryTasks = [...this.combinedRegionInfo.unlocks.achievementDiaryTasks, ...regionData.unlocks.achievementDiaryTasks];
      this.combinedRegionInfo.drops = [...this.combinedRegionInfo.drops, ...regionData.drops];
    },
    cleanRegionData(regionData) {
      const cleanText = (text) => {
        return text
          .replace(/\[\[([^\]|]+)(?:\|[^\]]+)?\]\]/g, '$1') // Remove wiki links
          .replace(/\*\*|\*|{{REIcon\|[^\}]+}}/g, '') // Remove bold, italic, and REIcon formatting
          .replace(/\s+/g, ' ') // Replace multiple spaces with a single space
          .trim(); // Trim leading and trailing spaces
      };

      regionData.settlements = regionData.settlements.map(cleanText);
      regionData.restrictedTravel = regionData.restrictedTravel.map(cleanText);
      regionData.combatActivities = regionData.combatActivities.map(cleanText);
      regionData.nonCombatActivities = regionData.nonCombatActivities.map(cleanText);
      regionData.shops = regionData.shops.map(cleanText);
      regionData.unlocks.quests = regionData.unlocks.quests.map(cleanText);
      regionData.unlocks.achievementDiaryTasks = regionData.unlocks.achievementDiaryTasks.map(cleanText);
    },
    addNotification(message, type = 'info') {
    const id = Date.now();
    this.notifications.push({ id, message, type });
    setTimeout(() => {
      this.notifications = this.notifications.filter(n => n.id !== id);
    }, 2000); // Notification will disappear after 3 seconds
    },
    removeNotification(id) {
      this.notifications = this.notifications.filter(n => n.id !== id);
    },
    showConfirm(message, action) {
    this.confirmMessage = message;
    this.confirmAction = action;
    this.showConfirmDialog = true;
    },
    handleConfirm() {
      if (this.confirmAction) {
        this.confirmAction();
      }
      this.showConfirmDialog = false;
    },
    handleCancel() {
      this.showConfirmDialog = false;
    },
    confirmResetApp() {
    this.showConfirm('Are you sure you want to reset? This will clear your route and selected regions.', this.resetApp);
  },
},
  mounted() {
    const urlParams = new URLSearchParams(window.location.search);
    const routeParam = urlParams.get('route');

    if (routeParam) {
      try {
        const decompressed = LZString.decompressFromEncodedURIComponent(routeParam);
        const importedRoute = JSON.parse(decompressed);
        this.route = importedRoute;
        this.addNotification('Route imported from URL.', 'success');
      } catch (error) {
        console.error('Error importing route from URL:', error);
      }
    }

    this.updateTimeUntilLaunch();
    this.intervalId = setInterval(this.updateTimeUntilLaunch, 1000);

    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark' || (!savedTheme && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
      document.documentElement.classList.add('dark');
    }

    const savedRegions = localStorage.getItem('selectedRegions');
    if (savedRegions) {
      this.selectedRegions = JSON.parse(savedRegions);
    }

    const savedRoute = localStorage.getItem('route');
      if (savedRoute) {
        this.route = JSON.parse(savedRoute);
      }

    const savedRoutes = localStorage.getItem('savedRoutes');
      if (savedRoutes) {
        this.savedRoutes = JSON.parse(savedRoutes);
      } else {
        this.savedRoutes = {};
      }
    window.addEventListener("scroll", this.handleScroll);
    // Define the default routes
    const defaultRoutes = [
      { name: 'Ken (Updated 11/26 4:05 PM)', file: './ken.json' },
      { name: 'Wizzy (Updated 11/26 3:55 PM)', file: './wizzy.json' },
      { name: 'Mazhar (Updated 11/26 4:04 PM)', file: './mazhar.json' },
      { name: 'Doubleshine (Updated 11/25 10:04 PM)', file: './doubleshine.json' },
      { name: 'Doubleshine Extended Route (150 Tasks, 2500 Points + Overheads, Relic Agnostic)', file: './doubleshine-longer.json' },
      { name: 'Lilratbag (Updated 11/26 8:54 AM)', file: './lilratbag.json' },
      { name: 'Felkrane (Updated 11/27 4:05 AM)', file: './felkrane.json' },
      { name: 'Jergz (Updated 11/27 9:00 AM, +100 Tasks, AFK Friendly and Bottlenecks Labeled)', file: './jergz.json' },
    ];

    // Load each default route if not already present
    defaultRoutes.forEach((route) => {
      if (!this.savedRoutes[route.name]) {
        axios
          .get(route.file)
          .then((response) => {
            this.savedRoutes[route.name] = JSON.stringify(response.data);
            localStorage.setItem('savedRoutes', JSON.stringify(this.savedRoutes));
          })
          .catch((error) => {
            console.error(`Error loading default route (${route.name}):`, error);
          });
      }
    });

    const savedTasks = localStorage.getItem('tasks');
    if (savedTasks) {
      this.tasks = JSON.parse(savedTasks);
    } else {
      this.loadTasks();
    }

    this.fetchLatestCommits();
  },
  beforeDestroy() {
    clearInterval(this.intervalId);
    window.removeEventListener("scroll", this.handleScroll);
  },
  watch: {
    route: {
      handler(newRoute) {
        const routeString = JSON.stringify(newRoute);
        const compressed = LZString.compressToEncodedURIComponent(routeString);
        const url = new URL(window.location);
        url.searchParams.set('route', compressed);
        window.history.replaceState({}, document.title, url.toString());
      },
      deep: true,
    },
  }
};
</script>

<style scoped>
.transition {
  transition: width 0.3s ease;
}
</style>
