from flask import Flask, render_template
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/servicios')
def service():
    return render_template("servicios.html")

@app.route('/nosotros')
def about_us():
    return render_template("nosotros.html")

@app.route('/contacto')
def contact():
    return render_template("contacto.html")
if __name__=='__main__':
    app.run(debug=True)