from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    answers = request.form.getlist('answer')
    color_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
    for answer in answers:
        color_counts[answer] += 1
    dominant_color = max(color_counts, key=color_counts.get)
    return render_template('result.html', color=dominant_color)

if __name__ == '__main__':
    app.run(debug=True)
