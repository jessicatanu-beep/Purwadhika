# Prediksi Customer Lifetime Value (CLV) Menggunakan Regresi

## Pendahuluan Proyek
Proyek ini bertujuan untuk membangun model *machine learning* berbasis **regresi** yang digunakan untuk memprediksi **Customer Lifetime Value (CLV)**. CLV merupakan metrik bisnis penting yang merepresentasikan nilai jangka panjang yang dapat diberikan oleh seorang pelanggan kepada perusahaan. Prediksi CLV yang akurat dapat membantu perusahaan dalam pengambilan keputusan terkait prioritisasi pelanggan, strategi retensi, serta alokasi anggaran pemasaran yang lebih efisien.

## Permasalahan Bisnis
Perusahaan dengan hubungan jangka panjang dengan pelanggan sering menghadapi kesulitan dalam menentukan pelanggan mana yang perlu diprioritaskan untuk program retensi dan loyalitas. Perlakuan yang sama terhadap seluruh pelanggan berpotensi menyebabkan alokasi sumber daya yang tidak efisien serta peningkatan biaya operasional.

## Tujuan Proyek
Tujuan dari proyek ini adalah:
- Membangun model regresi untuk memprediksi Customer Lifetime Value  
- Mengevaluasi dan membandingkan beberapa model regresi  
- Menerjemahkan hasil prediksi model menjadi insight bisnis yang dapat ditindaklanjuti  

## Dataset
Dataset yang digunakan berisi informasi historis pelanggan, yang mencakup:
- Data demografi pelanggan  
- Atribut terkait produk dan polis  
- Indikator keuangan  

Setiap baris data merepresentasikan satu pelanggan, dengan variabel target berupa **Customer Lifetime Value**.

## Metodologi
Proyek ini mengikuti alur kerja *machine learning* secara end-to-end, meliputi:
1. Pemahaman Data dan Exploratory Data Analysis (EDA)  
2. Data Cleaning dan Feature Engineering  
3. Pelatihan Model dan Benchmarking  
4. Evaluasi dan Interpretasi Model  
5. Analisis Nilai Tambah (Prioritisasi Pelanggan & Simulasi Penghematan Biaya)  

## Model
Beberapa model regresi yang dievaluasi dalam proyek ini antara lain:
- Linear Regression  
- Ridge Regression  
- Lasso Regression  
- Random Forest Regression  

**Random Forest Regression** dipilih sebagai model akhir karena menunjukkan performa terbaik berdasarkan metrik MAE, RMSE, dan R².

## Dampak Bisnis
Berdasarkan pendekatan prioritisasi pelanggan berbasis CLV, dilakukan simulasi penghematan biaya pemasaran. Hasil simulasi menunjukkan bahwa dengan memfokuskan kampanye hanya pada pelanggan bernilai tinggi, perusahaan berpotensi menghemat biaya pemasaran hingga sekitar **68%**, dengan asumsi biaya pemasaran per pelanggan bersifat konstan.

## File dalam Repository
- `Customer Lifetime Value Regresi.ipynb` : Jupyter Notebook yang berisi dokumentasi lengkap pengerjaan proyek  
- `clv_random_forest_model.pkl` : Model hasil pelatihan yang disimpan menggunakan Pickle (tersedia pada menu **Releases**)  
- `README.md` : Ringkasan dan dokumentasi proyek  

## Catatan
Model yang dikembangkan dalam proyek ini ditujukan sebagai **alat pendukung pengambilan keputusan (decision-support tool)** dan bukan sebagai estimasi nilai absolut yang presisi untuk setiap individu pelanggan.

## Author
Jessica Tanwijaya
