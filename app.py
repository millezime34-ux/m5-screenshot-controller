from flask import Flask, render_template, jsonify, request
import os
from datetime import datetime

app = Flask(__name__)

# Configuration
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Stockage des screenshots
SCREENSHOTS_DIR = 'screenshots'
if not os.path.exists(SCREENSHOTS_DIR):
    os.makedirs(SCREENSHOTS_DIR)

# Variable globale pour tracker les commandes
last_command_time = None
command_count = 0

@app.route('/')
def index():
    """Page web principale"""
    return render_template('index.html')

@app.route('/api/take-screenshot', methods=['POST'])
def take_screenshot():
    """Reçoit la commande de screenshot du M5 Stick"""
    global last_command_time, command_count
    
    try:
        last_command_time = datetime.now()
        command_count += 1
        
        data = request.json or {}
        device_name = data.get('device', 'M5 Stick C Plus 2')
        
        response = {
            'status': 'success',
            'message': f'Screenshot commandée par {device_name}',
            'timestamp': last_command_time.isoformat(),
            'command_count': command_count
        }
        
        print(f"[{{last_command_time.strftime('%H:%M:%S')}}}] Screenshot reçue du M5 Stick!")
        return jsonify(response), 200
        
    except Exception as e:
        print(f"Erreur: {{str(e)}}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/status', methods=['GET'])
def get_status():
    """Retourne le statut du serveur"""
    return jsonify({
        'status': 'online',
        'last_command': last_command_time.isoformat() if last_command_time else None,
        'total_commands': command_count
    }), 200

@app.route('/api/screenshot-history', methods=['GET'])
def get_history():
    """Retourne l'historique des screenshots"""
    return jsonify({
        'total': command_count,
        'last_time': last_command_time.isoformat() if last_command_time else None
    }), 200

if __name__ == '__main__':
    print("🚀 Serveur M5 Screenshot Controller démarré!")
    print("📍 Ouvrez http://localhost:5000 sur votre téléphone")
    print("⚠️  Remplacez 'localhost' par l'IP de votre ordinateur si nécessaire")
    app.run(host='0.0.0.0', port=5000, debug=True)