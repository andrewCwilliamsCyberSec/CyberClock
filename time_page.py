from flask import Flask, render_template_string, request, session, redirect, url_for
import datetime
import pytz

app = Flask(__name__)
app.config['SECRET_KEY'] = 'some-secret-key'  # you can change this key

DEFAULT_TIMEZONES = {
    "UTC": "UTC",
    "India Standard Time": "Asia/Kolkata",
    "Eastern Time (US & Canada)": "US/Eastern",
    "Central Time (US & Canada)": "US/Central",
    "Pacific Time (US & Canada)": "US/Pacific",
    "Mountain Time (US & Canada)": "US/Mountain"
}

@app.route('/')
def index():
    timezones = session.get('timezones', DEFAULT_TIMEZONES)
    dark_mode = session.get('dark_mode', True)
    language = session.get('language', 'English')

    times_data = {tz_name: get_times_data_in_timezone(tz_str) for tz_name, tz_str in timezones.items()}

    return render_template_string(open("template.html", encoding='utf-8').read(),
                                  times_data=times_data, 
                                  dark_mode=dark_mode,
                                  language=language,
                                  available_timezones=list(pytz.all_timezones))

@app.route('/toggle_theme', methods=['POST'])
def toggle_theme():
    session['dark_mode'] = not session.get('dark_mode', True)
    return redirect(url_for('index'))

@app.route('/set_language', methods=['POST'])
def set_language():
    session['language'] = request.form.get('language', 'English')
    return redirect(url_for('index'))

@app.route('/add_timezone', methods=['POST'])
def add_timezone():
    tz = request.form.get('timezone')
    if tz and tz not in session.get('timezones', DEFAULT_TIMEZONES):
        session['timezones'] = {**session.get('timezones', DEFAULT_TIMEZONES), tz: tz}
    return redirect(url_for('index'))

@app.route('/remove_timezone', methods=['POST'])
def remove_timezone():
    tz = request.form.get('timezone')
    if tz and tz in session.get('timezones', DEFAULT_TIMEZONES):
        session['timezones'].pop(tz, None)
    return redirect(url_for('index'))

def get_times_data_in_timezone(tz_name):
    """Return the current date, time, and ISO format in the given timezone."""
    local_time = datetime.datetime.now(pytz.timezone(tz_name))
    return {
        'date': local_time.strftime('%Y-%m-%d'),
        'time': local_time.strftime('%H:%M:%S'),
        'iso': local_time.isoformat()
    }

if __name__ == "__main__":
    app.run(debug=True)
