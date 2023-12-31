# ⏰ CyberClock: A Timezone Converter for Cybersecurity Reporting

CyberClock streamlines time conversions across global time zones, which is crucial for precise cybersecurity report writing. Enabling teams to correlate events and respond to incidents with pinpoint temporal accuracy ensures the integrity and reliability of time-sensitive security documents. One of its standout features is quickly copying and pasting the date, time, or full ISO format for any displayed timezone. Crafted by Andrew Williams, this tool has become indispensable for Security Operations Centers and incident response teams worldwide.

🔗 [LinkedIn Profile of Andrew Williams](https://www.linkedin.com/in/andrew-c-williams/)

![CyberClock Screenshot](https://github.com/andrewCwilliamsCyberSec/CyberClock/blob/main/dashboard_screenshot.PNG)


## 📦 Dependencies

This application uses the following Python packages:

- Flask: A lightweight web framework.
- pytz: World timezone definitions, modern and historical.

To install these dependencies, use the following command:

```bash
pip install Flask pytz
```

🛠️ Modifying Timezones
1. To add or remove time zones from the application:
2. Navigate to the time_page.py file.

Locate the timezones dictionary within the index() function:
```python
Copy code
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

To remove a timezone, delete the corresponding key-value pair from the dictionary.
Please remember to make sure that the timezone strings are valid according to the pytz library.


🚀 Setup

📦 Clone the repository:
```bash
git clone https://github.com/andrewCwilliamsCyberSec/CyberClock.git
```

🔧 Navigate into the repository directory and install the required packages:
```bash
cd CyberClock
pip install -r requirements.txt
```

🖥️ Run the Flask app:
```bash
python time_page.py
```

🌐 Visit http://127.0.0.1:5000/ in your browser to see CyberClock in action.

🙌 Pull requests are welcome.
For significant changes, please open an issue first to discuss your intentions and proposed modifications.

📜 License
MIT
