# Kullanıcı Kılavuzu

1) Gereksinimler
- Python 3.x
- VS Code (önerilir)

2) Proje Dosyaları
- Girdi dosyaları: odev1_case1.txt, odev1_case2.txt
- Kod dosyaları: fcfs.py, sjf.py, srtf.py, rr.py, pnp.py, pps.py
- Çıktı dosyaları: case1/ ve case2/ klasörleri içinde (her birinde 6 adet txt)

# 3) Çalıştırma
Terminali proje klasöründe açın ve aşağıdaki komutları kullanın.

# Case1 çalıştırma
python fcfs.py
python sjf.py
python srtf.py
python rr.py
python pnp.py
python pps.py

# Case2 çalıştırma
Her algoritma dosyasının en üstündeki şu satırı:
INPUT_FILE = "odev1_case1.txt"
şu şekilde değiştirin:
INPUT_FILE = "odev1_case2.txt"

Sonra tekrar çalıştırın:
python fcfs.py
python sjf.py
python srtf.py
python rr.py
python pnp.py
python pps.py

# 4) RR (Round Robin) Quantum Değiştirme
rr.py dosyasında en üstte bulunan:
Q = 4
değerini değiştirerek quantum ayarlanır.

Örnek:
Q = 2  (daha sık kesme)
Q = 8  (daha az kesme)

# 5) Çıktı Formatı
Her algoritma çıktısı bir txt dosyasına yazdırılır ve şu bölümleri içerir:
- Gantt (Zaman Tablosu)
- Max/Avg Waiting Time
- Max/Avg Turnaround Time
- Throughput (T=50,100,150,200)
- Context Switch Sayısı
- CPU Verimliliği (context switch süresi = 0.001)
