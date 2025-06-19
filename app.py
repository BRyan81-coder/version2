
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.get_json()
        filename = data.get('filename')
        content = data.get('content')

        # Mock logic: detect file type and return summary
        if filename.endswith('.pdf'):
            summary = "PDF detected. Mock summary generated."
        elif filename.endswith('.docx'):
            summary = "Word document detected. Mock summary generated."
        else:
            summary = "Unknown file type."

        return jsonify({"filename": filename, "summary": summary})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
