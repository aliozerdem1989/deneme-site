import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

# Veritabanı bağlantısı
def get_db_connection():
    conn = sqlite3.connect('veritabani.db')
    conn.row_factory = sqlite3.Row
    return conn

# Uygulama başladığında tabloyu oluştur (Eğer yoksa)
def init_db():
    conn = get_db_connection()
    conn.execute('''CREATE TABLE IF NOT EXISTS kullanicilar 
                    (id INTEGER PRIMARY KEY, isim TEXT, sifre TEXT)''')
    # Örnek bir kullanıcı ekleyelim (Güvenlik için şifreleri daha sonra hashleyeceğiz)
    conn.execute("INSERT OR IGNORE INTO kullanicilar (id, isim, sifre) VALUES (1, 'admin', '1234')")
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    return render_template('login.html')

if __name__ == '__main__':
    app.run()
