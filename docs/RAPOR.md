# İŞLEMCİ ZAMANLAMA – PROJE RAPORU

# 1) Amaç
Bu projede 6 farklı CPU zamanlama algoritması iki farklı giriş için (case1 ve case2) çalıştırılmış ve sonuçlar karşılaştırılmıştır.

Algoritmalar:
- FCFS
- SJF (Non-Preemptive)
- SRTF (Preemptive SJF)
- Round Robin (q=4)
- PPS (Preemptive Priority)
- PNP (Non-Preemptive Priority)

# 2) Ölçütler (Başarımlar) [b, c, d, e, f]
- (b) Maksimum / Ortalama Bekleme Süresi (Waiting Time)
- (c) Maksimum / Ortalama Tamamlanma Süresi (Turnaround Time)
- (d) Throughput: T = [50, 100, 150, 200] için tamamlanan iş sayısı
- (e) Ortalama CPU Verimliliği (Context switch süresi = 0.001)
- (f) Toplam Context Switch sayısı

# 3) Zaman Tabloları (Gantt) – ayrı ayrı sunum
Her yöntem kendi sonuç dosyasında zaman tablosu (Gantt) ile birlikte verilmiştir.

# Case1 Gantt dosyaları
- FCFS: case1/case1_FCFS.txt
- SJF:  case1/case1_SJF.txt
- SRTF: case1/case1_SRTF.txt
- RR:   case1/case1_RR_q4.txt
- PPS:  case1/case1_PPS.txt
- PNP:  case1/case1_PNP.txt

# Case2 Gantt dosyaları
- FCFS: case2/case2_FCFS.txt
- SJF:  case2/case2_SJF.txt
- SRTF: case2/case2_SRTF.txt
- RR:   case2/case2_RR_q4.txt
- PPS:  case2/case2_PPS.txt
- PNP:  case2/case2_PNP.txt

> Not: Her dosyada Gantt tablosu en üst bölümde, metrikler (SONUCLAR/THROUGHPUT/CONTEXT SWITCH/CPU VERIMLILIGI) en altta yer almaktadır.


# 4) Case1 – Başarım Tablosu
| Algoritma | Max Waiting | Avg Waiting | Max Turnaround | Avg Turnaround | T=50 | T=100 | T=150 | T=200 | Context Switch | CPU Verimliliği |

| FCFS | 1683 | 813.495 | 1703 | 823.995 | 9 | 13 | 16 | 19 | 200 | 0.9994288978 |
| SJF  | 1863 | 537.425 | 1883 | 547.925 | 11 | 22 | 32 | 42 | 200 | 0.9994288978 |
| SRTF | 1863 | 537.005 | 1883 | 547.505 | 11 | 22 | 32 | 42 | 213 | 0.9994227144 |
| RR(q=4) | 1863 | 1091.7 | 1883 | 1102.2 | 7 | 10 | 12 | 14 | 600 | 0.9992386753 |
| PPS | 1923 | 748.395 | 1943 | 758.895 | 7 | 13 | 20 | 25 | 214 | 0.9994222388 |
| PNP | 1689 | 824.77 | 1707 | 835.27 | 8 | 13 | 16 | 21 | 200 | 0.9994288978 |

# 5) Case1 – Yorum
- Ortalama bekleme ve turnaround açısından en iyi değerler **SJF/SRTF** tarafındadır (Avg Waiting ~537). Bu beklenen bir durumdur çünkü kısa işlerin öne alınması ortalamayı düşürür.
- **SRTF**, SJF’ye çok yakın ortalamalar verir; ancak kesme (preemption) sebebiyle **context switch** sayısı artar (200 → 213). Bu da CPU verimliliğini çok az düşürür.
- **RR(q=4)** adil (fair) bir paylaştırma sağlar; ancak çok sayıda parça oluştuğu için **context switch** çok artar (600). Bu nedenle Avg Waiting ve Avg Turnaround en kötü çıkan yöntem olmuştur.
- **PPS/PNP**, öncelik etkisi nedeniyle bazı süreçleri öne alır. PPS kesmeli olduğu için context switch daha fazladır; PNP kesmesiz olduğu için FCFS’e daha yakındır.
- Throughput açısından T=200’de en yüksek tamamlanan iş sayısı **SJF/SRTF**’dedir.

---

## 6) Case2 – Başarım Tablosu
| Algoritma | Max Waiting | Avg Waiting | Max Turnaround | Avg Turnaround | T=50 | T=100 | T=150 | T=200 | Context Switch | CPU Verimliliği |

| FCFS | 851 | 418.0 | 853 | 428.5 | 5 | 10 | 14 | 18 | 99 | 0.9999057231746722 |
| SJF  | 926 | 268.39 | 946 | 278.89 | 10 | 21 | 30 | 42 | 99 | 0.9999057231746722 |
| SRTF | 926 | 267.86 | 946 | 278.36 | 10 | 21 | 31 | 42 | 110 | 0.9998952490691453 |
| RR(q=4) | 926 | 550.87 | 944 | 561.37 | 3 | 8 | 10 | 11 | 299 | 0.9997153191614959 |
| PPS | 962 | 366.33 | 981 | 376.83 | 6 | 12 | 18 | 25 | 110 | 0.9998952490691453 |
| PNP | 836 | 409.63 | 854 | 420.13 | 5 | 9 | 15 | 19 | 99 | 0.9999057231746722 |

# 7) Case2 – Yorum
- Case2’de ortalama bekleme ve turnaround açısından en iyi yöntem yine **SJF/SRTF**’dir (Avg Waiting ~268). SRTF çok az daha iyi ortalama verir; ancak kesme nedeniyle **context switch** artar (99 → 110) ve verimlilik çok az düşer.
- **FCFS** ve **PNP** değerleri birbirine yakındır. PNP’nin Avg Waiting’i FCFS’den biraz daha düşük/benzer çıkması, öncelik sıralamasının bazı süreçleri öne çekmesinden kaynaklanır.
- **PPS**, önceliği yüksek olanları hızlı bitirmeye çalıştığı için FCFS/PNP’ye göre daha iyi ortalamalar verebilir; ancak kesmeli çalıştığı için context switch sayısı artar.
- **RR(q=4)** Case2’de de en yüksek Avg Waiting/Avg Turnaround değerlerine sahiptir. Bunun ana nedeni, time-slice nedeniyle süreçlerin çok parçalanması ve context switch sayısının yükselmesidir (299).
- Throughput değerlerinde (özellikle T=100 ve T=200) **SJF/SRTF** en yüksek tamamlanan iş sayısına ulaşmıştır.


# 8) Sonuç
İki farklı case üzerinde algoritmalar; bekleme süresi, turnaround süresi, throughput, context switch ve CPU verimliliği metrikleriyle karşılaştırılmıştır.
Genel olarak kısa işleri öne alan yöntemler (SJF/SRTF) ortalama süreleri düşürürken, kesmeli yöntemler ve Round Robin daha fazla context switch üreterek verimliliği azaltabilmektedir.
