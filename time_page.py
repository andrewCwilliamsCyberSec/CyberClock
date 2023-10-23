from flask import Flask, render_template_string
import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def index():
    timezones = {
        "UTC": "UTC",
        "India Time": "Asia/Kolkata",
        "Eastern Standard Time": "US/Eastern",
        "Central Standard Time": "US/Central",
        "Pacific Time": "US/Pacific",
        "Salt Lake City Time": "US/Mountain"
    }
    
    times_data = {tz_name: get_times_data_in_timezone(tz_str) for tz_name, tz_str in timezones.items()}
    
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Current Times</title>
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
            <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.2/js/bootstrap.min.js"></script>
            <style>
                body {
                    background-color: #343a40;
                    color: #ffffff;
                    font-family: 'Arial', sans-serif;
                }
                
                .card {
                    background-color: #212529;
                    border-radius: 15px;
                    transition: transform 0.2s;
                }
                
                .card:hover {
                    transform: scale(1.05);
                }

                .card-title {
                    color: #01b4e4;
                }

                .btn {
                    margin: 3px;
                    border-radius: 20px;
                    transition: background-color 0.2s;
                }

                .btn-primary:hover {
                    background-color: #0056b3;
                }

                .btn-info:hover {
                    background-color: #016c9a;
                }
            </style>
            <script>
                function copyToClipboard(text) {
                    const textarea = document.createElement('textarea');
                    textarea.value = text;
                    document.body.appendChild(textarea);
                    textarea.select();
                    document.execCommand('copy');
                    document.body.removeChild(textarea);
                }
            </script>
        </head>
        <body>
            <div class="container mt-5">
                <h1 class="text-center mb-5">Current Times</h1>
                <div class="row">
                    {% for tz_name, data in times_data.items() %}
                        <div class="col-md-4 mb-4">
                            <div class="card shadow">
                                <div class="card-body text-center">
                                    <h5 class="card-title">{{ tz_name }}</h5>
                                    <p><strong>Date:</strong> {{ data['date'] }}</p>
                                    <button class="btn btn-info px-4" onclick="copyToClipboard('{{ data['date'] }}')">Copy Date</button>
                                    <p class="mt-2"><strong>Time:</strong> {{ data['time'] }}</p>
                                    <button class="btn btn-info px-4" onclick="copyToClipboard('{{ data['time'] }}')">Copy Time</button>
                                    <p class="mt-2"><strong>ISO Format:</strong> {{ data['iso'] }}</p>
                                    <button class="btn btn-primary px-4" onclick="copyToClipboard('{{ data['iso'] }}')">Copy ISO</button>
                                </div>
                            </div>
                        </div>
                    {% endfor %}
                </div>
            </div>
        </body>
        </html>
    ''', times_data=times_data)

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
