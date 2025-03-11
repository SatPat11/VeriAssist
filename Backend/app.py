from flask import Flask, request, jsonify
from flask_cors import CORS  # Remove if deploying same domain
import os
import requests

app = Flask(__name__)
CORS(app)  # Remove this line if frontend/backend are on same domain

# Get your Hugging Face token from: https://huggingface.co/settings/tokens
API_TOKEN = os.getenv("HF_TOKEN", "your_hf_token_here") 
MODEL_NAME = "your-username/your-model-name"  # Replace with your model

@app.route('/generate', methods=['POST'])
def generate():
    try:
        prompt = request.json.get('prompt', '')
        
        # Call Hugging Face API
        response = requests.post(
            f"https://api-inference.huggingface.co/models/{MODEL_NAME}",
            headers={"Authorization": f"Bearer {API_TOKEN}"},
            json={"inputs": prompt}
        ).json()

        return jsonify({
            'response': response[0]['generated_text']  # Adjust based on your model's response format
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
