# WebStatusChecker

**WebStatusChecker** is a Python-based tool that allows you to check the availability and status of any webpage. Using Selenium WebDriver, it verifies the presence of specific elements on the page and either sends notifications or prints messages to the console if the status changes. This tool is ideal for monitoring the health of your websites and ensuring their continuous availability.

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
    pip3 install selenium
    ```
    or

    ```bash
    pip install selenium
    ```

4. **Ensure that chromedriver is installed and available in your system's PATH.** You can download it from [here](https://chromedriver.storage.googleapis.com/index.html).

## Usage

The script checks the presence of a specific element (it doesn't have to be a navbar) on a given website at regular intervals and either sends notifications or prints messages to the console if the status changes.

## Versions

### Notification Version

This version sends desktop notifications when the status of the monitored element changes. It is ideal for **Ubuntu** or any system that supports `notify-send`.

1. **Modify the `url` and `element_id` variables** in the script to match the website and element you want to monitor, or pass them as command-line arguments.

2. **Run the script:**

    ```bash
    python web_status_checker_notify.py <url> <element_id>
    ```

    The script will now check the specified website at regular intervals (default: 60 seconds) and send notifications if the status changes.

### Console Output Version

This version prints messages to the console when the status of the monitored element changes. It is suitable for use on any operating system.

1. **Modify the `url` and `element_id` variables** in the script to match the website and element you want to monitor, or pass them as command-line arguments.

2. **Run the script:**

    ```bash
    python web_status_checker_console.py <url> <element_id>
    ```

    The script will now check the specified website at regular intervals (default: 60 seconds) and print messages to the console if the status changes.

## Example

To check if the element with ID `exampleElement` is present on `https://example.com`, use the following command for the console version:

```bash
python web_status_checker_console.py https://example.com exampleElement
```

You will receive messages about the website's status changes directly in your console or notifications (depends on version).

To use the notification version, download 'script (notification ubuntu)'.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
