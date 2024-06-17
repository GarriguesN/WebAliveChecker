# WebStatusChecker

**WebStatusChecker** is a Python-based tool that allows you to check the availability and status of any webpage. Using Selenium WebDriver, it verifies the presence of specific elements on the page and sends notifications if the status changes. This tool is ideal for monitoring the health of your websites and ensuring their continuous availability.

## Features

- **Efficient and Fast:** Quickly checks the status of URLs.
- **Detailed Reports:** Provides response time and HTTP status codes.
- **Error Handling:** Notifies of inactive sites and handles errors gracefully.
- **Easy Integration:** Simple to use and integrate into existing projects.

## Requirements

- Python 3.x
- Google Chrome
- ChromeDriver
- Libraries: selenium

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/WebStatusChecker.git
    ```

2. **Navigate to the repository directory:**

    ```bash
    cd WebStatusChecker
    ```

3. **Install the required Python libraries:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Ensure that chromedriver is installed and available in your system's PATH.** You can download it from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).

## Usage

The script checks the presence of a specific navbar (you can choose another item) on a given website at regular intervals and sends Ubuntu notifications if the status changes.

## Running the Script

1. **Modify the `url` and `navbar_id` variables** in the script to match the website and element you want to monitor.

2. **Run the script:**

    ```bash
    python web_status_checker.py
    ```

    The script will now check the specified website at regular intervals (default: 60 seconds) and send Ubuntu notifications if the status changes.

## Example

To check if the navbar with ID `exampleNavbar` is present on `https://example.com`, update the following lines:

```python
url = "https://example.com"
navbar_id = 'exampleNavbar'
```

```bash
python web_status_checker.py
```

You will receive notifications about the website's status changes directly on your Ubuntu desktop.
