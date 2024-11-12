from flask import Flask
import os
from datetime import datetime
import psutil

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Set the username as 'RiteshJadhav-1'
    user_name = 'RiteshJadhav-1'
    
    # Get the server time in IST
    server_time = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S")
    
    # Get top processes
    top_output = '\n'.join(f"{p.info['name']} - {p.info['cpu_percent']}%" for p in psutil.process_iter(['name', 'cpu_percent']))

    return f"""
    <html>
        <head><title>System Info</title></head>
        <body>
            <h1>System Info</h1>
            <p><strong>Name:</strong> Ritesh Jadhav</p>
            <p><strong>Username:</strong> {user_name}</p>
            <p><strong>Server Time (IST):</strong> {server_time}</p>
            <h2>Top Processes:</h2>
            <pre>{top_output}</pre>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
