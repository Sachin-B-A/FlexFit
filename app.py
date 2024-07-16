import os
from flask import Flask, request, jsonify
import openai
from flask import Flask, request, jsonify, render_template

app = Flask(__name__, static_url_path='/static')

# Configure OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/analyze', methods=['POST'])
def analyze():
    try:
        data = request.json
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": (
                f"Here are the user's details: Name: {data['name']}, Age: {data['age']}, Gender: {data['gender']}, "
                f"Height: {data['height']} cm, Weight: {data['weight']} kg, BMI: {data['bmi']}, Lifestyle: {data['lifestyle']}, "
                f"Diet: {data['diet']}. Provide an analysis of their current health and suggest a nutrition diet and physical exercise regimen."
            )}
        ]

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=500
        )

        return jsonify(response.choices[0].message['content'].strip()), 200
    except Exception as e:
        app.logger.error(f"Error: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=int(os.getenv('PORT', 5000)))
