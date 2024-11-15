from flask import Flask, jsonify

app = Flask(__name__)

# Health Check route
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})

# Data route
@app.route('/data', methods=['GET'])
def get_data():
    data = [
        {'id': 1, 'name': 'Item 1'},
        {'id': 2, 'name': 'Item 2'},
        {'id': 3, 'name': 'Item 3'}
    ]
    return jsonify(data)

# Kubernetes route (something playful)
@app.route('/docker', methods=['GET'])
def kubernetes_playful():
    message = 'Welcome to the world of Docker!'
    return message

<<<<<<< HEAD
@app.route('/somethings', methods=['GET'])
def kubernetes_playful():
    message = 'somethings are better than nothing!'
=======
@app.route('/something', methods=['GET'])
def something_playful():
    message = 'Something is better than nothing.! LOL! '
>>>>>>> 9d775e6716e44901dc02df6bd2012906686cc7da
    return message

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
