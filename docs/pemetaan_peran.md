\# Pemetaan Peran Batik Kinanthi



| No | Kebutuhan | Peran utama | Alasan singkat | Tahap lifecycle |

|---|---|---|---|---|

| 1 | Data penjualan dari toko, web, dan marketplace dikumpulkan ke satu tempat setiap malam | Data Engineer | Memindahkan dan menyatukan data dari banyak sumber secara otomatis | Ingestion |

| 2 | Dashboard omzet harian per kanal | Data Analyst | Membuat visualisasi dan laporan dari data yang sudah siap | Serving |

| 3 | Prediksi kebutuhan stok kain bulan depan | Data Scientist | Membangun model prediksi berdasarkan data historis | Serving |

| 4 | Tabel pelanggan tidak boleh berisi data ganda | Data Engineer | Membersihkan dan menjamin kualitas data pelanggan | Transformation |

| 5 | Laporan motif terlaris per kota untuk rapat bulanan | Data Analyst | Menganalisis dan menyajikan pola penjualan | Serving |

| 6 | Rekomendasi produk untuk pelanggan di situs web | Data Scientist | Membuat model rekomendasi berbasis perilaku pelanggan | Serving |

| 7 | Data transaksi lama tetap tersimpan aman dan hemat biaya | Data Engineer | Merancang penyimpanan dan arsip data | Storage |

| 8 | Analisis penyebab penurunan penjualan marketplace bulan lalu | Data Analyst | Mencari penyebab penurunan dari data transaksi | Serving |



\## Jawaban Pertanyaan



\### a. Mengapa kebutuhan 3 dan 6 tidak bisa dikerjakan sebelum kebutuhan 1 dan 4 selesai?



Karena prediksi stok dan rekomendasi produk membutuhkan data yang sudah terkumpul dari semua kanal penjualan serta data pelanggan yang bersih dan tidak duplikat. Jika data belum terintegrasi atau masih ganda, hasil prediksi dan rekomendasi bisa tidak akurat.



\### b. Risiko satu orang merangkap tiga peran di UMKM



Risikonya adalah beban kerja tinggi, sulit memisahkan pekerjaan teknis dan analisis, rawan kesalahan data, serta kualitas pipeline dan analisis sulit dijaga. Bagian yang sebaiknya diotomatisasi lebih dulu adalah pengumpulan data harian, pembersihan data, dan pembuatan laporan omzet karena dilakukan berulang setiap hari.

