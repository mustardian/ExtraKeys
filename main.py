from flask import Flask, render_template,jsonify
import keyboard

app = Flask(__name__)

# Simulate key press
def press_key(key):
    keyboard.press_and_release(key)
    print(f"{key} key pressed")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/press_key/<key>', methods=['POST', 'GET'])
def press_key_route(key):
    try:
        press_key(key)
        return jsonify({"success": True, "key": key})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
