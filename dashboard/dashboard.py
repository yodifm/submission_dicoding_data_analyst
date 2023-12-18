import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Menyiapkan data
df_day = pd.read_csv("data/day.csv")
df_hour = pd.read_csv("data/hour.csv")
bike_combine = df_day.merge(df_hour, on='dteday', how='inner', suffixes=('_daily', '_hourly'))

# Mengatur judul dan deskripsi aplikasi
st.title("Bike Sharing Data Analysis Dashboard")
st.write("by Yodi Fakhri")

# Menampilkan pertanyaan bisnis
st.header("Pertanyaan Bisnis:")
st.subheader("1. Apakah cuaca dapat mempengaruhi penyewa sepeda di setiap jam nya?")
st.write("Visualisasi 1: Rata Rata Sewa Sepeda Berdasarkan Cuaca pada setiap jam nya")

# Visualisasi pertanyaan 1
weather_data = bike_combine.groupby('weathersit_hourly')['cnt_hourly'].mean().reset_index()
weather_data['weather_name'] = ['Clear', 'Mist + Clody', 'Light Snow', 'Heavy Rain']
sns.set(style="whitegrid")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='weather_name', y='cnt_hourly', data=weather_data, palette="viridis")
ax.set_title('Pengaruh Cuaca Terhadap Jumlah Sewa Sepeda per Jam')
ax.set_xlabel('Cuaca')
ax.set_ylabel('Rata-rata Jumlah Sewa Per Jam')
st.pyplot(fig)

# Menampilkan pertanyaan bisnis lainnya
st.text("""
        Puncak terjadi pada cuaca terang dan berawan. Meskipun cuaca mendung dengan hujan 
        ringan masih menarik minat, cuaca hujan berat memiliki jumlah penyewa terendah. 
        Bisnis dapat menyesuaikan stok dan pelayanan berdasarkan prakiraan cuaca untuk 
        meningkatkan efisiensi dan kepuasan pelanggan. Rekomendasi meliputi pemasaran intensif 
        saat cuaca baik dan penawaran khusus saat cuaca tidak ideal. Informasi cuaca 
        real-time dan fleksibilitas operasional akan meningkatkan pengalaman pelanggan.
        """)

# Menampilkan pertanyaan bisnis

st.subheader("2. Hubungan musim dengan penyewa sepeda pada setiap jam nya?")
st.write("Visualisasi 2: Rata Rata Sewa Sepeda Berdasarkan Musim pada setiap jam nya")

# Visualisasi pertanyaan 2
season_data = bike_combine.groupby('season_hourly')['cnt_hourly'].mean().reset_index()
season_data['season_name'] = ['Springer','Summer','Fall', 'Winter']
sns.set(style="whitegrid")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='season_name', y='cnt_hourly', data=season_data, palette="viridis")
ax.set_title('Perbandingan penyewa sepeda di setiap musim')
ax.set_xlabel('Musim')
ax.set_ylabel('Rata-rata Jumlah Sewa Per hari di setiap musim')
st.pyplot(fig)



# Menampilkan pertanyaan bisnis lainnya
st.text("""
       
Berdasarkan data puncak penyewaan sepeda terjadi pada musim Fall, diikuti Summer. 
Musim Winter menunjukkan minat tinggi, sementara musim Springer rendah. Strategi 
bisnis difokuskan pada pemasaran intensif di Fall dan Summer, dengan penyesuaian 
stok dan penawaran khusus di Winter. Analisis menyoroti peran cuaca, mendorong 
pemantauan dan penyesuaian operasional. Studi lebih lanjut diperlukan pada musim 
Springer untuk memahami faktor rendahnya minat. Kesimpulan ini memberikan dasar 
untuk merancang strategi yang lebih baik, mengikuti preferensi penyewa sepeda selama 
berbagai musim.
        """)

# Menampilkan visualisasi Pertanyaan 2: Pola berdasarkan bulan dan jam
st.subheader("Pertanyaan 3: Apakah ada kenaikan penyewaan sepeda dalam setiap jamnya pada setiap bulan?")
st.write("Visualisasi 3: Jumlah sewa Sepeda Berdasarkan jam di setiap bulan")

# Visualisasi pertanyaan 2
# Mengatur warna palet
color_palette = sns.color_palette("husl", 12)  # Menggunakan palet warna "husl" dengan 12 warna

sns.set_style("whitegrid")
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(x='hr', y="cnt_hourly", data=bike_combine, hue="mnth_daily", palette=color_palette, linewidth=2)
# legend
ax.legend(title="Bulan", loc="upper left", bbox_to_anchor=(1, 1))

ax.set_title("Jumlah Sewa Sepeda Berdasarkan Jam")
ax.set_xlabel("Jam")
ax.set_ylabel("Jumlah Sewa Sepeda Jam")

ax.grid(axis="y", linestyle="--", alpha=0.7)

# Menyertakan plot ke dalam dashboard Streamlit
st.pyplot(fig)

st.text("""
        Dari visualisasi data penyewaan sepeda, terlihat bahwa puncak aktivitas penyewaan 
        terjadi pada sore hari, khususnya antara jam 5 - 6. Pagi hari, terutama pada rentang 
        jam 6 - 8, juga menunjukkan tingkat minat yang cukup tinggi, mungkin terkait dengan 
        kegiatan rekreasi atau kebutuhan transportasi menuju pekerjaan atau sekolah. 
        Meskipun malam hari, khususnya antara jam 20 - 22, menandakan akhir aktivitas penyewaan, 
        namun masih terdapat minat yang signifikan pada jam-jam tersebut. Strategi operasional 
        dapat difokuskan pada ketersediaan sepeda dan pelayanan optimal pada jam-jam puncak, sambil 
        mengevaluasi kebutuhan stok dan pelayanan pada pagi hari. 
        """)


sns.set_style("whitegrid")
fig, ax = plt.subplots(figsize=(12, 6))
plt.scatter(x='dteday', y="cnt_hourly", data=bike_combine,  alpha=0.7, cmap='viridis')
ax.set_title("Persebaran data penyewa sepeda tahun 2011 dan 2012")
ax.set_xlabel("dteday")
ax.set_ylabel("cnt_hourly")
plt.colorbar(label='Color Intensity')
# ax.legend(title="daily", loc="upper left", bbox_to_anchor=(1, 1))
st.pyplot(fig)



# Menampilkan kesimpulan dari analisis
st.header("Kesimpulan:")
st.write("Berikut adalah kesimpulan dari hasil analisis data.")
st.text("--- Apakah cuaca dapat mempengaruhi penyewa sepeda di setiap jam nya? ---")
st.text('''
       1. Cuaca Terang:
Penyewa sepeda paling banyak terjadi saat cuaca terang.
Cuaca terang sangat mendukung aktivitas luar ruangan, termasuk bersepeda.''')

st.text('''
        2. Cuaca Berawan:
Cuaca berawan juga menjadi kondisi yang disukai oleh penyewa sepeda.
Meskipun tidak sebanyak cuaca terang, cuaca berawan tetap menarik minat penyewa.''')

st.text('''
       3. Cuaca Mendung dengan Hujan Ringan:
Cuaca mendung dengan hujan ringan memiliki jumlah penyewa yang cukup, 
menunjukkan bahwa sebagian penyewa masih tertarik meskipun ada potensi hujan.
''')
st.text('''
      4. Cuaca Hujan Berat:
Cuaca hujan berat menunjukkan jumlah penyewa yang paling rendah.
Ketersediaan sepeda dapat diperkirakan akan lebih banyak yang tersedia karena 
permintaan yang rendah pada kondisi cuaca ini.''')
st.text('''
    - Rekomendasi Bisnis:

Bisnis sepeda dapat menyesuaikan stok dan pelayanan mereka berdasarkan prakiraan 
cuaca untuk memaksimalkan pendapatan.
Pemasaran yang lebih intens dapat dilakukan saat cuaca terang dan berawan, 
sementara penawaran spesial atau promosi dapat diterapkan saat cuaca mendung 
dengan hujan ringan.

- Peluang Peningkatan Layanan:
Menyediakan informasi cuaca secara real-time pada platform penyewaan sepeda dapat 
membantu pelanggan membuat keputusan yang lebih baik berdasarkan kondisi aktual.
    ''')

st.text("--- 2. Hubungan musim dengan penyewa sepeda pada setiap jam nya? ---")
st.text('''
    1. Musim Fall:
Penyewa sepeda paling banyak terjadi selama musim Fall.
Fall mungkin menjadi musim yang sangat diantisipasi oleh penyewa sepeda, mungkin 
karena cuaca yang nyaman dan pemandangan yang menarik.''')

st.text('''
       2. Musim Summer:
Musim Summer menyusul sebagai musim dengan jumlah penyewa sepeda tertinggi setelah Fall.
Cuaca hangat dan kondisi yang mendukung aktivitas luar ruangan membuat Summer menjadi 
pilihan yang populer.''')

st.text('''
       3. Musim Winter:
Musim Winter menunjukkan minat penyewa yang lebih tinggi dibandingkan musim Springer, 
tetapi masih lebih rendah dibandingkan dengan Fall dan Summer.
Peningkatan minat mungkin terkait dengan aktivitas khusus seperti bersepeda salju 
atau kegiatan musim dingin lainnya.
''')
st.text('''
4. Musim Springer:
Musim Springer menunjukkan jumlah penyewa yang paling rendah.
Cuaca yang mungkin belum sepenuhnya stabil atau kurangnya daya tarik khusus pada musim 
ini dapat mempengaruhi minat penyewa.''')
st.text('''
  - Strategi Bisnis Berbasis Musim:

Fokuskan upaya pemasaran dan promosi intensif pada musim Fall dan Summer untuk 
memaksimalkan pendapatan.
Pertimbangkan penyesuaian stok dan strategi penawaran khusus selama musim Winter 
untuk menarik penyewa yang mencari pengalaman musim dingin.

- Analisis Pengaruh Cuaca:

Kesimpulan ini menunjukkan bahwa cuaca dan suhu mungkin memainkan peran penting 
dalam keputusan penyewaan sepeda.
Pemantauan tren cuaca dan penyesuaian strategi operasional dapat menjadi kunci 
untuk mengoptimalkan kinerja bisnis.
    ''')


st.text("--- 3. Apakah ada kenaikan penyewaan sepeda dalam setiap jamnya pada setiap bulan? ---")

st.text('''
    1. Puncak Penyewaan Sore Hari:
Penyewa sepeda paling banyak terjadi pada rentang waktu sore antara jam 5 - 6.
Puncak ini mungkin disebabkan oleh banyaknya orang yang menggunakan sepeda 
setelah bekerja atau sekolah.''')

st.text('''
     2. Pagi Hari (Jam 6 - 8):
Meskipun jumlah penyewa pada pagi hari (jam 6 - 8) tidak sebanyak sore hari, 
tetapi masih menunjukkan minat yang cukup tinggi.
Pagi hari dapat menjadi waktu yang diminati untuk kegiatan rekreasi atau transportasi 
menuju tempat kerja atau sekolah.''')

st.text('''
      3. Malam Hari (Jam 20 - 22):
Meskipun diakhiri oleh malam hari (jam 20 - 22), penyewaan sepeda masih menunjukkan 
tingkat minat yang relatif tinggi di jam-jam tersebut.
Malam hari mungkin digunakan untuk bersepeda setelah jam kerja atau kegiatan malam lainnya.
''')
st.text('''
4. Musim Springer:
Musim Springer menunjukkan jumlah penyewa yang paling rendah.
Cuaca yang mungkin belum sepenuhnya stabil atau kurangnya daya tarik khusus pada 
musim ini dapat mempengaruhi minat penyewa.''')
st.text('''
  - Strategi Operasional:
Fokuskan pada ketersediaan sepeda dan pelayanan pelanggan yang optimal pada jam-jam 
puncak, terutama pada sore hari.
Evaluasi kebutuhan stok dan pelayanan pada pagi hari untuk memastikan kesiapan dalam 
menyambut penyewa yang aktif di waktu tersebut.

- Penyesuaian Penawaran atau Diskon:
Pertimbangkan penawaran khusus atau diskon pada jam-jam tertentu untuk meningkatkan 
minat penyewa di luar jam puncak.
Misalnya, diskon untuk penyewaan di pagi hari atau malam hari untuk merangsang 
aktivitas penyewaan.
    ''')


st.text("--- Dari tahun 2011 sampai 2012, apakah ada kenaikan dalam user menyewa sepeda? ---")

st.text('''
    - Tren Kenaikan Total Penyewa:
Dari analisis data 2011-2012, terlihat tren kenaikan jumlah penyewa sepeda secara keseluruhan.

- Peningkatan Signifikan pada Oktober 2012:
Bulan Oktober 2012 menonjol sebagai periode dengan peningkatan penyewa yang paling signifikan.
Penyebab kenaikan ini perlu dianalisis lebih lanjut, mungkin terkait dengan peristiwa khusus atau strategi pemasaran yang berhasil.''')





