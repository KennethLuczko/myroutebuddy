# My Route Buddy - Leagues 5: Raging Echoes Task Route Planner

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](#contributing)

## Overview

https://myroutebuddy.com

Leagues 5: Raging Echoes Task Route Planner is a web application designed to help players plan and optimize their tasks efficiently. Whether you’re tackling hundreds of pre-made tasks or adding your own custom tasks, this app is built to streamline your experience.

### Features
- **Customizable Task Routes**: Add, reorder, and mark tasks as complete.
- **Region Filtering**: Focus on specific regions with task filtering.
- **Progress Tracking**: Visualize your progress with a dynamic progress bar.
- **Save, Load, Share, and Import Routes**: Save routes locally, share them with others, or import shared routes.
- **Open Source**: Contribute to the project or report issues via GitHub.

## Getting Started

### Prerequisites
To run the app locally, you’ll need:
- **Node.js**: [Download here](https://nodejs.org)
- A web browser.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/KennethLuczko/myroutebuddy.git
   ```
2. Navigate to the project folder:
   ```bash
   cd myroutebuddy
   ```
3. Install dependencies:
   ```bash
   npm install
   ```
4. Run the development server:
   ```bash
   npm run dev
   ```
5. Open the app in your browser at `http://localhost:3000`.

## Usage

1. Select up to 3 regions to filter tasks.
2. Add tasks to your route from the **Available Tasks** section.
3. Reorder or remove tasks in the **Your Route** section.
4. Save, share, or import routes to customize your planning experience.

## Screenshots

Here’s a preview of the app:

![My Route Buddy Screenshot](https://i.imgur.com/ijkxj8o.png)
## Contributing

We welcome contributions from the community! Here’s how you can get involved:
1. **Fork the repository**: Click the "Fork" button on GitHub.
2. **Clone your fork**: 
   ```bash
   git clone https://github.com/your-username/myroutebuddy.git
   ```
3. **Create a new branch**:
   ```bash
   git checkout -b feature-name
   ```
4. Make your changes and commit them:
   ```bash
   git commit -m "Add feature-name"
   ```
5. Push to your fork:
   ```bash
   git push origin feature-name
   ```
6. Submit a pull request to the main repository.

## Reporting Issues
If you encounter bugs or have suggestions, please create an issue on GitHub: [Issues Page](https://github.com/KennethLuczko/myroutebuddy/issues).

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute this project under the terms of the license.

## Acknowledgements

- Inspired by RuneScape's Leagues mechanics.
- Built using [Vue.js](https://vuejs.org/) and [TailwindCSS](https://tailwindcss.com/).

## How to Add Your Own Route to the Default Routes

If you've created an awesome route and want to share it with the community, you can add it to the pre-loaded default routes in this app. There are two options available:

### Option 1: Do It for Me, Please!

If you're not comfortable with Git and the steps involved, you can still share your route:

1. **Create Your Route in the App**
   - Build your custom route using the app's interface.

2. **Export Your Route**
   - Click on the **"Share Route"** button.
   - This copies the JSON representation of your route to your clipboard.

3. **Save the JSON to a Text File**
   - Open a text editor (e.g., Notepad, TextEdit).
   - Paste the JSON data into a new document.
   - Save the file with a descriptive name, such as `my-awesome-route.txt`.

4. **Contact the Maintainer**
   - Send a message to **ke69eth** on Discord.
   - Include:
     - The name of your route.
     - A brief description or any special notes about your route.
     - Attach the `.txt` file containing your route's JSON data.

5. **Wait for Your Route to Be Added**
   - The maintainer will add your route to the default routes in the app.
   - They may contact you if they have any questions or need additional information.

### Option 2: I'm Comfortable with Git

1. **Create Your Route in the App**
   - Use the app to build your custom route, arranging tasks as desired.

2. **Export Your Route**
   - Click on the **"Share Route"** button in the app.
   - This action copies the JSON representation of your route to your clipboard.

3. **Fork the Repository**
   - Visit the [MyRouteBuddy GitHub repository](https://github.com/KennethLuczko/myroutebuddy).
   - Click on the **"Fork"** button in the top-right corner to create a copy of the repository under your GitHub account.

4. **Clone Your Forked Repository**
   - Open your terminal or command prompt.
   - Clone your forked repository to your local machine:

     ```bash
     git clone https://github.com/YourUsername/myroutebuddy.git
     ```

     Replace `YourUsername` with your GitHub username.

5. **Add Your Route File**
   - Navigate to the directory where the routes are stored (e.g., `src/routes/`).
   - Create a new JSON file with a descriptive name for your route, such as `my-awesome-route.json`.
   - Paste the JSON data you copied from the app into this file and save it.

6. **Update the App to Include Your Route**
   - If the app loads default routes from a specific file or configuration, add your route to that list.
   - For example, if there's a `routes.json` file or a configuration array, include an entry for your new route.

7. **Commit and Push Your Changes**
   - Stage your changes:

     ```bash
     git add .
     ```

   - Commit your changes with a meaningful message:

     ```bash
     git commit -m "Add 'My Awesome Route' to default routes"
     ```

   - Push your changes to your forked repository:

     ```bash
     git push origin main
     ```

     Replace `main` with the appropriate branch name if different.

8. **Create a Pull Request**
   - Go to your forked repository on GitHub.
   - Click on the **"Compare & pull request"** button.
   - Provide a clear title and description for your pull request, explaining that you're adding a new default route.
   - Submit the pull request.

9. **Collaborate and Respond to Feedback**
   - The repository maintainer will review your pull request.
   - Be prepared to make any requested changes or provide additional information if needed.

---

**Note:** By submitting your route, you agree to have it included in the app for others to use. Please ensure that your route does not contain any inappropriate content.

**Additional Tips:**

- **Provide a Descriptive Name:** Choose a route name that reflects its purpose or highlights unique aspects.
- **Include a Description:** If possible, provide a brief explanation of your route's strategy or goals.
- **Stay Updated:** After your route is added, check the app to see it in action and share it with others.

---

If you need further assistance or have any questions, feel free to reach out! Your contributions help make the app better for everyone.
