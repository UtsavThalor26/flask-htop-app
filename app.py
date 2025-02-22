from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

def get_top_output():
    try:
        top_output = subprocess.check_output("top -b -n 1", shell=True, text=True)
        return top_output
    except Exception as e:
        return str(e)

@app.route('/htop')
def htop():
    name = "Your Full Name"  # Replace with your actual name
    username = os.getenv("USER", "codespace")  # Get system username
    server_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    top_output = get_top_output().replace("\n", "<br>")  # Formatting for HTML

    response = f"""
    <h1>Name: {name}</h1>
    <h2>Username: {username}</h2>
    <h3>Server Time (IST): {server_time}</h3>
    <h4>TOP output:</h4>
    <pre>{top_output}</pre>
    """
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
