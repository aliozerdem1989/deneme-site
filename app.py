from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Basit bir kullanıcı kontrolü (İleride bunu veritabanıyla yapacağız)
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        kullanici = request.form['username']
        sifre = request.form['password']
        
        # Basit doğrulama
        if kullanici == "admin" and sifre == "1234":
            return "<h1>Hoş geldin! Giriş başarılı.</h1>"
        else:
            return "<h1>Hatalı giriş! <a href='/'>Tekrar dene</a></h1>"
            
    return '''
        <form method="post">
            <input type="text" name="username" placeholder="Kullanıcı Adı" required><br>
            <input type="password" name="password" placeholder="Şifre" required><br>
            <input type="submit" value="Giriş Yap">
        </form>
    '''

if __name__ == '__main__':
    app.run()
