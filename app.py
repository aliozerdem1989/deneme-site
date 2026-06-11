<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kurumsal Giriş</title>
    <style>
        :root {
            --primary: #1a2a40;
            --accent: #d4af37;
            --bg: #eef2f7;
        }
        body { font-family: 'Segoe UI', Tahoma, sans-serif; background: var(--bg); display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        
        .login-card { 
            background: white; 
            padding: 2.5rem; 
            border-radius: 12px; 
            box-shadow: 0 10px 25px rgba(0,0,0,0.15); 
            width: 100%; 
            max-width: 400px; 
            text-align: center; 
            border-top: 6px solid var(--primary);
            margin: 20px;
        }
        
        h2 { color: var(--primary); margin-bottom: 2rem; letter-spacing: 1px; }
        
        input { 
            width: 100%; 
            padding: 14px; 
            margin: 12px 0; 
            border: 2px solid #ddd; 
            border-radius: 6px; 
            box-sizing: border-box; 
            transition: 0.3s;
        }
        
        input:focus { border-color: var(--primary); outline: none; }
        
        button { 
            width: 100%; 
            padding: 14px; 
            background: var(--primary); 
            color: white; 
            border: none; 
            border-radius: 6px; 
            cursor: pointer; 
            font-size: 16px; 
            font-weight: 600; 
            margin-top: 10px;
            transition: 0.3s;
        }
        
        button:hover { background: #2c4a6e; border-bottom: 3px solid var(--accent); }

        /* Mobil için düzenleme */
        @media (max-width: 480px) {
            .login-card { padding: 1.5rem; }
        }
    </style>
</head>
<body>
    <div class="login-card">
        <h2>SİSTEM GİRİŞİ</h2>
        <form method="post">
            <input type="text" name="username" placeholder="Kullanıcı Adı" required>
            <input type="password" name="password" placeholder="Şifre" required>
            <button type="submit">GİRİŞ YAP</button>
        </form>
    </div>
</body>
</html>
