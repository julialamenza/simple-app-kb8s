from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def main():
	return jsonify(message='Consegui :D!')

@app.route('/health')
def health():
	return jsonify(message='Tudo certo por aqui')

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0", port="80")