document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('login-form').addEventListener('submit', function(event) {
        event.preventDefault();
        var password = document.getElementById('password').value;
        if (password === '12345') {
            saveDeviceInfo(); // Panggil fungsi untuk menyimpan informasi perangkat
            window.location.href = '/success';
        } else {
            window.location.href = '/login_failed';
        }
    });
});

function saveDeviceInfo() {
    var deviceInfo = {
        "OS": getOS(),
        "RAM": getRAM(),
        "CPU": getCPU(),
        "IPAddress": getIPAddress()
    };
    localStorage.setItem('deviceInfo', JSON.stringify(deviceInfo));
}

function getOS() {
    return navigator.platform;
}

function getRAM() {
    return navigator.deviceMemory ? navigator.deviceMemory + ' GB' : 'Unknown';
}

function getCPU() {
    return navigator.hardwareConcurrency ? navigator.hardwareConcurrency + ' cores' : 'Unknown';
}

function getIPAddress() {
    // Untuk mendapatkan alamat IP pengguna di sisi klien, dibutuhkan akses ke server atau menggunakan layanan pihak ketiga.
    // Namun, hal ini tidak direkomendasikan karena alamat IP pengguna dapat diakses langsung dari sisi server di sisi belakang.
    // Contoh ini hanya menunjukkan konsep umum penyimpanan lokal di browser.
    return 'Unknown';
                         
