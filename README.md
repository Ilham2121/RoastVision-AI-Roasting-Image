# RoastVision 🔥

RoastVision adalah aplikasi AI yang dapat memberikan kritik humoris ("roast") pada gambar yang diunggah oleh pengguna

## Fitur

- Upload gambar langsung dari perangkat
- Analisis gambar menggunakan Google Gemini Pro Vision API
- Menghasilkan roasting yang lucu dan sarkastik tentang gambar

## Teknologi

- Python
- Streamlit
- Google Gemini API
- PIL (Python Imaging Library)
- Requests

## Cara Menjalankan

1. Pastikan Anda memiliki Python versi 3.8 atau lebih baru
2. Clone repositori ini
3. Install dependensi:
   ```
   pip install streamlit google-generativeai python-dotenv Pillow requests
   ```
4. Siapkan file `.env` dengan API key Google Gemini:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```
5. Jalankan aplikasi:
   ```
   streamlit run app.py
   ```


### Streamlit

1. Buat akun di [Streamlit Cloud](https://streamlit.io/cloud)
2. Hubungkan repositori GitHub Anda
3. Tambahkan API key ke secrets di dashboard Streamlit


## Disclaimer

Aplikasi ini dibuat untuk hiburan dan tidak bermaksud menyinggung siapapun. Gunakan dengan bijak ya. 