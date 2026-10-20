\# Identifikasi Undercurrents pada pipeline\_mini.py



| Undercurrent | Bukti penerapan di kode | Kekurangan | Usulan perbaikan |

|---|---|---|---|

| Security | Kredensial dibaca dari `.env` melalui `load\_dotenv()` | Pipeline memakai user `de\_user` yang memiliki hak penuh | Buat user khusus pipeline dengan hak terbatas |

| Data management | `check\_quality()` memeriksa duplikasi, total negatif, dan kanal kosong | Belum memeriksa format tanggal, nilai anomali, dan kelengkapan data | Tambahkan validasi tanggal, rentang nilai, dan data hilang |

| DataOps | Pipeline menggunakan logging dengan `logging.info()` | Belum ada pengujian otomatis, monitoring, dan alerting | Tambahkan unit test, monitoring, dan notifikasi kegagalan |

| Data architecture | Data mentah disimpan di `data/raw/transaksi.csv`, hasil olahan disimpan di `mart\_omzet\_harian` | Pemisahan raw dan serving masih sederhana serta memakai CSV lokal | Gunakan object storage seperti MinIO dan format Parquet |

| Orchestration | Fungsi `main()` menjalankan ingestion, storage, quality check, transformation, dan serving | Pipeline masih dijalankan manual dan belum dijadwalkan | Gunakan scheduler atau orchestrator seperti Airflow |

| Software engineering | Kode dipisah menjadi fungsi sesuai tahap lifecycle | Belum ada unit test dan dokumentasi kode yang lengkap | Tambahkan docstring, unit test, dan code review |



\## Jawaban Pertanyaan Sesi 2



\### 1. Mengapa `mart\_omzet\_harian` tetap aman saat data rusak masuk?



Karena pemeriksaan kualitas dilakukan sebelum tahap transformasi dan serving. Jika data gagal validasi, pipeline berhenti sehingga tabel `mart\_omzet\_harian` tidak ditulis ulang dengan data yang salah.



\### 2. Apakah `data/raw/transaksi.csv` tetap diperbarui walaupun data rusak itu masalah atau berguna?



Justru berguna sebagai jejak data mentah untuk audit dan investigasi. Namun, file perlu diberi penanda status atau tanggal agar data rusak tidak tertukar dengan data yang sudah lolos pemeriksaan.

