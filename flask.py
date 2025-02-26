from flask import Flask, request, render_template, jsonify
import google.generativeai as genai

# Configure the API key
genai.configure(api_key="")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    query = request.form['query']
    
    if query:
        # Call the Generative AI API
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        response = model.generate_content([query])
        
        # Extract the generated content
        result = response.get('content', 'No description available')
        return jsonify({'description': result})
    
    return jsonify({'error': 'Invalid request'}), 400

if __name__ == '_main_':
    app.run(debug=True)
