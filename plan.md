# Rencana Pengembangan Landing Page Desa Banyoemas (Produk UMKM Lingkungan 1-11)

## 1. Tujuan
Membuat landing page desa yang modern, responsif (sangat optimal untuk mobile), dan cepat menggunakan HTML, CSS, dan JS native. Desain akan menggunakan referensi screenshot dengan gaya *modern rounded cards* yang besar dan elegan, serta nuansa hijau/alami yang bersih. Fokus utama adalah menampilkan produk dari tiap lingkungan (Lingkungan 1 hingga 11) yang dapat diklik langsung menuju WhatsApp penjual.

## 2. Struktur Direktori
```text
Web-desa/
├── index.html          # File HTML utama
├── css/
│   └── style.css       # File CSS native yang dioptimasi
├── js/
│   └── main.js         # File JS untuk interaksi dasar (seperti lazy loading)
├── attachment/         # Folder gambar yang sudah ada
└── plan.md             # File rencana ini
```

## 3. Desain & Layout (Berdasarkan Referensi Screenshot)
- **Tema Warna**: Menggunakan palet dari referensi (background off-white/sangat cerah, aksen hijau tua `dark green` dan hijau muda cerah `light green`).
- **Tipografi**: Menggunakan font modern sans-serif (misalnya *Inter*, *Outfit*, atau *Plus Jakarta Sans* dari Google Fonts).
- **Layout Mobile-First**:
  - Di layar mobile (HP), kartu produk akan berjejer vertikal, ukurannya besar (memenuhi layar kiri-kanan dengan padding modern), gambar mendominasi agar menarik.
  - Di layar desktop/tablet, menggunakan CSS Grid untuk menampilkan 3-4 kartu per baris.
- **Komponen Kartu Produk (Product Card)**:
  - *Border-radius* besar (misal: `24px` atau `1.5rem`).
  - *Box-shadow* yang sangat halus untuk kesan mengambang dan premium.
  - *Image Thumbnail*: Gambar proporsional di bagian atas kartu. Jika diklik, seluruh area gambar atau sebuah tombol mencolok akan mengarahkan user ke WhatsApp (`https://wa.me/62...`).
  - *Card Body*: Berisi badge Lingkungan, Nama Produk/Penjual, dan ikon WhatsApp.

## 4. Fitur & Optimasi
- **WhatsApp Integration**: Mengubah nomor telepon (misal: 0821...) menjadi format internasional WA (`62821...`) menggunakan API `https://wa.me/`.
- **Performance Optimization**: 
  - *Lazy Loading* pada gambar (`loading="lazy"`).
  - *CSS Variables* untuk konsistensi.
  - Meminimalkan ukuran CSS dan tidak menggunakan library eksternal berukuran besar.
- **Data UMKM**: Menampilkan seluruh 11 lingkungan sesuai permintaan. Untuk data yang belum lengkap (seperti Lingkungan 7 dan 10), akan dibuatkan *placeholder* "Menunggu Data".

## 5. Detail Data yang Akan Diimplementasikan

| Lingkungan | Penjual / Produk | Nomor WA | Format WA | Folder Gambar |
| :--- | :--- | :--- | :--- | :--- |
| Lingkungan 1 | KERIPIK UBI PEDAS MAK KARIN | 0821 6176 1595 | 6282161761595 | `attachment/lingkungan-1/` |
| Lingkungan 2 | CEMAL CEMIL NAILUL MUNA | 0819 4755 4847 | 6281947554847 | `attachment/lingkungan-2/` |
| Lingkungan 3 | Cucur Azizah Salsabilah | 0831 8327 0411 | 6283183270411 | `attachment/lingkungan-3/` |
| Lingkungan 4 | Wajik Bandung Original Mak Zulfanz | 0812 6984 8308 | 6281269848308 | `attachment/lingkungan-4/` |
| Lingkungan 5 | Cemilan & Kerajinan Lin Sundari | 0823 6491 9512 | 6282364919512 | `attachment/lingkungan-5/` |
| Lingkungan 6 | Makanan & Minuman Olahan Nurul A. | 0851 7989 6296 | 6285179896296 | `attachment/lingkungan-6/` |
| Lingkungan 7 | *(Belum ada data)* | - | - | `attachment/lingkungan-7/` |
| Lingkungan 8 | DIMSUM | 0812 6501 5959 | 6281265015959 | `attachment/lingkungan-8/` |
| Lingkungan 9 | Bakery Widayu Astuti | 0822 7519 3889 | 6282275193889 | `attachment/lingkungan-9/` |
| Lingkungan 10 | *(Belum ada data)* | - | - | `attachment/lingkungan-10/` |
| Lingkungan 11 | Mie Ayam Tebet | 0895 3092 4443 | 6289530924443 | `attachment/lingkungan-11/` |

## 6. Langkah Eksekusi (Prompt Instruksi untuk Model)
Untuk agen/model yang akan mengeksekusi kode, ikuti langkah ini:
1. **Buat file `index.html`**:
   - Set tag meta viewport.
   - Buat header/navigasi yang terinspirasi dari referensi (judul desa misal: "Desa Banyoemas" atau disesuaikan).
   - Buat section `grid` berisi 11 kartu (`div.card`).
   - Gunakan format link WA: `<a href="https://wa.me/62..."><img src="..." loading="lazy"></a>`.
   - Gunakan path gambar relatif menunjuk ke folder `attachment/lingkungan-[n]/[namafile]`.
2. **Buat file `css/style.css`**:
   - Definisikan `:root` dengan variabel warna (misal: `--bg-color: #f7f9f6`, `--primary-green: #0a2618`, `--light-green: #e9f5e9`, `--card-radius: 20px`).
   - Styling layout menggunakan Flexbox/Grid.
   - Styling *Card*: `border-radius: var(--card-radius); overflow: hidden; background: #fff; box-shadow: 0 10px 30px rgba(0,0,0,0.05); transition: transform 0.3s;`.
   - Pastikan `@media (max-width: 768px)` memiliki grid 1 kolom, font yang mudah dibaca, dan padding yang cukup agar nyaman digenggam dan di-*scroll*.
3. **Buat file `js/main.js`**:
   - Tambahkan interaksi kecil jika diperlukan, misalnya menambahkan class 'scrolled' pada navigasi saat di-scroll, atau animasi *fade-in* saat kartu mulai terlihat (IntersectionObserver) agar tampilan terasa lebih premium.
4. **Testing UI/UX**:
   - Pastikan hover state jelas (bayangan kartu menebal atau gambar sedikit *zoom* saat dihover).
   - Tombol klik (Area Gambar atau tombol spesifik) memiliki indikasi yang jelas untuk menuju ke WhatsApp.

---
*Silakan jalankan eksekusi pembuatan file HTML, CSS, dan JS berdasarkan rencana di atas.*
