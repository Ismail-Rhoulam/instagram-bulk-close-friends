# Instagram Bulk Close Friends Adder 🚀📷💻

## Abstract 🎯🔍📱

This document details the development and implementation of an advanced Python-based automation tool designed to facilitate the authentication, retrieval, and categorization of Instagram followers. Leveraging the Selenium framework, the script programmatically interacts with Instagram’s web interface to streamline the collection and organization of follower data while ensuring efficient management of the "Close Friends" list.

## Core Functionalities ⚙️📂✅

- Executes automated authentication on Instagram through secure user input.
- Extracts and archives a comprehensive list of followers in structured text format.
- Implements dynamic scrolling algorithms to traverse and retrieve all follower entries.
- Programmatically adds extracted followers to the "Close Friends" category.
- Logs unsuccessful operations for review and further intervention.

## System Prerequisites 🛠️🖥️📦

- **Python 3.x** installed for script execution.
- **Google Chrome** as the designated web browser.
- **Chrome WebDriver** installed and synchronized with the current browser version.
- **Selenium package** installed for automated browser interaction.

## Installation Protocol ⬇️💾🔧

1. Clone the repository to your local development environment:

   ```bash
   git clone https://github.com/Ismail-Rhoulam/instagram-bulk-close-friends.git
   cd instagram-bulk-close-friends
   ```

2. Install the requisite dependencies:

   ```bash
   pip install selenium
   ```

3. Verify that **Google Chrome** is properly installed and ensure that the corresponding **Chrome WebDriver** matches its version. The latest WebDriver can be obtained from [here](https://sites.google.com/chromium.org/driver/).

## Execution Instructions 🚀📌📝

This script assumes that **Chrome WebDriver is already installed** and available in the system path. If you prefer automatic WebDriver management, you can modify the script to use `webdriver-manager` by installing it and updating the driver instantiation.

1. Initiate script execution:

   ```bash
   python makemclose.py
   ```

2. When prompted, input valid Instagram credentials for authentication.

3. If Instagram requires verification, input the corresponding code.

4. The script will proceed to:

   - Extract follower data systematically.
   - Store the collected information in a directory named after the execution date and username.
   - Attempt to add all retrieved followers to the "Close Friends" list.

5. Any follower who could not be added will be logged in the `failed.txt` file for subsequent manual intervention.

## Output Data Structure 📁📜🗂️

- **`followers.txt`** – A systematically structured list of all extracted followers.
- **`failed.txt`** (if applicable) – A record of followers who could not be processed.

## Considerations and Constraints ⚠️🔄📢

- Instagram enforces security policies that may block or flag automated logins; the use of a proxy may mitigate restrictions.
- Excessive script executions within a short timeframe may lead to temporary account limitations.
- Users are advised to comply with Instagram’s terms of service to avoid account suspension.

## Legal Disclaimer ⚖️📜❗

This tool is developed exclusively for educational and research purposes. Any deployment of this script is undertaken at the user’s discretion and risk.

---

### Author ✍️👤📧

- Ismail RHOULAM
- Contact: [ismail.rhoulam@um5r.ac.ma](mailto\:ismail.rhoulam@um5r.ac.ma)