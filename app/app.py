# Visitor counter

from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__)

# Define the path for the visit count file
DATA_DIR = '../data'
COUNT_FILE = os.path.join(DATA_DIR, 'visitCount.txt')

# Ensure the data directory exists
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Ensure the file exists and is not empty
if not os.path.exists(COUNT_FILE):
    with open(COUNT_FILE, 'w') as f:
        f.write('0')
else:
    # Check if the file is empty
    if os.stat(COUNT_FILE).st_size == 0:
        with open(COUNT_FILE, 'w') as f:
            f.write('0')

# Route to serve the HTML file
@app.route('/')
def index():
    return send_from_directory('../app', 'index.html')  # Adjusted to serve from the app folder

# Route to get the current visit count
@app.route('/visits')
def visits():
    with open(COUNT_FILE, 'r') as f:
        visit_count = int(f.read().strip())
    
    # Increment the visit count
    visit_count += 1
    
    # Write the updated visit count back to the file
    with open(COUNT_FILE, 'w') as f:
        f.write(str(visit_count))
    
    return jsonify({'visitCount': visit_count})

if __name__ == '__main__':
    app.run(debug=True)
