from flask import Flask, jsonify
from flask import Flask, render_template

app = Flask(__name__)

data = [
        {
            "id": 1,
            "library": "Pandas",
            "language": "Python"
        },
        {
            "id": 2,
            "library": "requests",
            "language": "Python"
        },
        {
            "id": 3,
            "library": "NumPy",
            "language": "Python"
        }
    ]

@app.route('/')
def hello1():
    return "Hello นางสาววันวิสา เพ้ชรรัตน์ เลขที่ 24 ชั้น ม.4/9"

@app.route('/api', methods=['GET'])
def hello():
    return jsonify(data)

@app.route('/hi')
def hi():
    return "สวัสดี"

if __name__ == "__main__":
    app.run(debug=True)
