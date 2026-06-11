from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == "admin" and request.form['password'] == "1234":
            return "<h1>Giriş Başarılı!</h1>"
        else:
            return "<h1>Hatalı Giriş!</h1>"
    
    return render_template('login.html')

if __name__ == '__main__':
    app.run()
