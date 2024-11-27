from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import json
import os


DEBUG = False
WIKI_REGION_TO_ROUTE_REGION_MAP = {
    'general': 'Global',
    'misthalin': 'Global',
    'karamja': 'Global',
    'asgarnia': 'Asgarnia',
    'desert': 'Desert',
    'fremennik': 'Fremmenik',
    'kandarin': 'Kandarin',
    'kourend': 'Kourend',
    'morytania': 'Morytania',
    'tirannwn': 'Tirannwn',
    'varlamore': 'Varlamore',
    'wilderness': 'Wilderness',
}

# Set up Selenium options (optional, if you don't want the browser window to open)
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run headless (without opening a browser window)

# Set up the webdriver (make sure to provide the path to the ChromeDriver executable for pre-4.6.0 versions)
#driver_path = 'C:\\Users\\Aphro\\Desktop\\chromedriver-win32\\chromedriver.exe'
#service = Service(driver_path)
#driver = webdriver.Chrome(service=service, options=chrome_options)
driver = webdriver.Chrome(options=chrome_options)

# URL of the page
url = "https://oldschool.runescape.wiki/w/Raging_Echoes_League/Tasks"

# Fetch the page content
driver.get(url)

# Allow time for the page to load (you can increase this if needed)
driver.implicitly_wait(10)  # Waits up to 10 seconds for the page to load

# Extract the HTML source
html = driver.page_source

# Save the HTML source to a file if desired
if DEBUG:
    with open('scraping/tasks.html', 'w', encoding="utf-8") as html_file:
        html_file.write(html)

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find the correct table by its class
select = soup.select("table.wikitable.lighttable")

if select:
    task_table = select[0]

    # Initialize an empty list to store the tasks
    tasks = []
    
    # Initialize task id counter
    task_id = 1

    # Loop through the table rows (skip the header row)
    for row in task_table.find_all('tr')[1:]:  # Skip the header row
        columns = row.find_all('td')

        # Ensure the row has the required number of columns (at least 2)
        if len(columns) >= 3:
            wiki_region = row.attrs['data-tbz-area-for-filtering'] if 'data-tbz-area-for-filtering' in row.attrs else ''
            task_region = WIKI_REGION_TO_ROUTE_REGION_MAP[wiki_region] if wiki_region else ''
            task_name = columns[2].text.strip() 
            task_points = columns[4].text.strip()

            # Debugging output for task points
            print(f"Region: {task_region} | Task: {task_name} | Points: {task_points}")

            try:
                # Attempt to convert points to integer
                task_points_int = int(task_points)
                tasks.append({
                    "id": task_id,  # Add incremental ID
                    "region": task_region,
                    "task": task_name,
                    "points": task_points_int
                })
                task_id += 1  # Increment the task ID after adding the task
            except ValueError:
                # If points are not a valid integer, print the task and its points
                print(f"Skipping task with invalid points: {task_name} | Invalid points value: {task_points}")
    
    # GOES TO A TEMP DIRECTORY, MOVE TO public/tasks.json IF VERIFIED THAT ALL LOOKS CORRECT
    output_dir = './temp'
    os.makedirs(output_dir, exist_ok=True)

    # Save the tasks to a JSON file
    with open(os.path.join(output_dir, 'tasks.json'), 'w') as json_file:
        json.dump(tasks, json_file, indent=2)

    print("Tasks have been scraped and saved to temp/tasks.json.")
else:
    print("Table not found. Please check the page structure or class name.")

# Close the driver after scraping
driver.quit()
