# ⏰ CyberClock: A Timezone Converter Tailored for Cybersecurity Professionals

**CyberClock** 🌍 streamlines time conversions across global time zones, enabling cybersecurity teams to correlate events and respond to incidents swiftly and effectively. One of its standout features is the ability to quickly copy and paste the date, time, or full ISO format for any displayed timezone. Crafted with ❤️ by Andrew Williams, it's an indispensable tool for Security Operations Centers and incident response teams worldwide.

🔗 [LinkedIn Profile of Andrew Williams](https://www.linkedin.com/in/andrew-c-williams/)

![CyberClock Screenshot](https://github.com/andrewCwilliamsCyberSec/CyberClock/raw/main/dashboard_screenshot.png)

## 🛠️ Modifying Timezones

To add or remove time zones from the application:

1. Navigate to the `time_page.py` file.
2. Locate the `timezones` dictionary within the `index()` function:
    ```python
    timezones = {
        "UTC": "UTC",
        "India Time": "Asia/Kolkata",
        ...
    }
    ```

3. To add a new timezone, simply add a new key-value pair to the dictionary:
    ```python
    "Your Timezone Name": "Your_Timezone_String"
    ```

4. To remove a timezone, delete the corresponding key-value pair from the dictionary.

Remember to ensure that the timezone strings are valid according to the [pytz library](https://pythonhosted.org/pytz/#available-time-zones).

## 🚀 Setup

1. 📦 Clone the repository:
   git clone https://github.com/andrewCwilliamsCyberSec/CyberClock.git

2. 🔧 Navigate into the repository directory and install the required packages:
  cd CyberClock
  pip install -r requirements.txt

3. 🖥️ Run the Flask app:
   python time_page.py

🌐 Visit `http://127.0.0.1:5000/` in your browser to see CyberClock in action.


🙌 Pull requests are welcome. For significant changes, please open an issue first to discuss your intentions and proposed modifications.

## 📜 License
[MIT](https://choosealicense.com/licenses/mit/)

