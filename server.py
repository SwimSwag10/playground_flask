from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html", num=1, color="skyblue")

@app.route('/play')
def play():
  return render_template("index.html", num=3, color="skyblue")

@app.route('/play/<int:box_num>')
def play_num_boxes(box_num):
  return render_template("index.html", num=box_num, color="#333")

@app.route('/play/<int:box_num>/<string:box_color>/')
def play_num_color_boxes(box_num, box_color):
  return render_template("index.html", num=box_num, color=box_color)

if __name__=="__main__":
  app.run(debug=True)