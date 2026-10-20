# ketahanan.py

import random

random.seed(11)
JAM = 365 * 24

print("== Availability ==")
for a in (0.99, 0.999, 0.9999):
    downtime = (1 - a) * JAM
    print(f"{a * 100:.2f}% -> downtime {downtime:6.1f} jam/tahun")

# Availability sistem berantai: aplikasi, database, jaringan
total = 1.0
for a in (0.999, 0.999, 0.995):
    total *= a

downtime_total = (1 - total) * JAM
print(f"Berantai -> {total * 100:.2f}% | downtime {downtime_total:.1f} jam/tahun")

print()
print("== RPO: 20 transaksi/menit, crash di waktu acak ==")

TRX = 20          # jumlah transaksi per menit
BIAYA = 500       # biaya backup per eksekusi, dalam rupiah

for interval in (1, 15, 60, 1440):
    total_hilang = 0

    for _ in range(2000):
        waktu_crash = random.uniform(0, 1440)
        data_hilang = (waktu_crash % interval) * TRX
        total_hilang += data_hilang

    rata_hilang = total_hilang / 2000
    biaya_harian = (1440 / interval) * BIAYA

    print(
        f"backup tiap {interval:>4} mnt | "
        f"rata-rata hilang {rata_hilang:6.0f} trx | "
        f"biaya {biaya_harian:9,.0f} rp/hari"
    )

print()
print("== Retry: komponen gagal 30% ==")

for retry in range(4):
    jumlah_percobaan = 1 + retry
    sukses = 0

    for _ in range(20000):
        berhasil = any(random.random() > 0.3 for _ in range(jumlah_percobaan))
        if berhasil:
            sukses += 1

    tingkat_sukses = (sukses / 20000) * 100
    print(f"retry {retry}x -> tingkat sukses {tingkat_sukses:.1f}%")