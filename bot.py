from flask import Flask, render_template, request, redirect
import json
import os
import platform
import psutil

app = Flask(__name__)

# Fungsi untuk memeriksa apakah password benar
def check_password(password):
    return password == "12345"

# Fungsi untuk menyimpan informasi perangkat ke file JSON
def save_device_info(device_info):
    if not os.path.exists('user.json'):
        with open('user.json', 'w') as f:
            json.dump([], f)
    with open('user.json', 'r+') as f:
        data = json.load(f)
        data.append(device_info)
        f.seek(0)
        json.dump(data, f, indent=4)

# Fungsi untuk mendapatkan informasi perangkat
def get_device_info():
    cpu_info = " ".join([f"{info}: {value}" for info, value in psutil.cpu_info()[0].items()])
    device_info = {
        "Nama Perangkat": platform.node(),
        "OS": platform.system(),
        "Ram": str(round(os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES') / (1024. ** 3))) + " GB",
        "CPU": cpu_info,
        "Jenis": platform.machine(),
        "IP Address": request.remote_addr  # Mendapatkan alamat IP pengguna
    }
    return device_info

# Halaman utama dengan form input password
@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Login</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background-color: #f0f0f0;
            }
            .login-container {
                background-color: #fff;
                padding: 20px;
                border-radius: 5px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            .login-container h2 {
                margin-bottom: 20px;
            }
            .login-container input {
                width: 100%;
                padding: 10px;
                margin-bottom: 10px;
                border: 1px solid #ccc;
                border-radius: 3px;
            }
            .login-container button {
                width: 100%;
                padding: 10px;
                background-color: #007bff;
                border: none;
                border-radius: 3px;
                color: #fff;
                cursor: pointer;
            }
            .login-container button:hover {
                background-color: #0056b3;
            }
        </style>
    </head>
    <body>
        <div class="login-container">
            <h2>Login</h2>
            <form action="/login" method="post">
                <input type="password" name="password" placeholder="Password" required>
                <button type="submit">Login</button>
            </form>
        </div>
    </body>
    </html>
    '''

# Route untuk memproses form input password
@app.route('/login', methods=['POST'])
def login():
    password = request.form['password']
    if check_password(password):
        return redirect('/success')
    else:
        return '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Login</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    background-color: #f0f0f0;
                }
                .login-container {
                    background-color: #fff;
                    padding: 20px;
                    border-radius: 5px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                }
                .login-container h2 {
                    margin-bottom: 20px;
                }
                .login-container input {
                    width: 100%;
                    padding: 10px;
                    margin-bottom: 10px;
                    border: 1px solid #ccc;
                    border-radius: 3px;
                }
                .login-container button {
                    width: 100%;
                    padding: 10px;
                    background-color: #007bff;
                    border: none;
                    border-radius: 3px;
                    color: #fff;
                    cursor: pointer;
                }
                .login-container button:hover {
                    background-color: #0056b3;
                }
            </style>
        </head>
        <body>
            <div class="login-container">
                <h2>Login</h2>
                <p style="color: red;">Password salah</p>
                <form action="/login" method="post">
                    <input type="password" name="password" placeholder="Password" required>
                    <button type="submit">Login</button>
                </form>
            </div>
        </body>
        </html>
        '''

# Halaman sukses setelah password benar
@app.route('/success')
def success():
    device_info = get_device_info()
    save_device_info(device_info)
    return "Informasi perangkat telah disimpan."

if __name__ == '__main__':
    app.run(port=8080)
