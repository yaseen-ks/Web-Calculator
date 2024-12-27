from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    expression = data.get('expression', '')

    try:
        result = str(eval(expression))  # Safely evaluate the expression
        return jsonify({'result': result})
    except:
        return jsonify({'result': 'Error'})

if __name__ == '__main__':
    app.run(debug=True)
