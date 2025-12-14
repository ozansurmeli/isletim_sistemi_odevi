import csv

INPUT_FILE = "odev1_case2.txt"
BOSTA = "BOSTA"
SWITCH_SURESI = 0.001

processler = []
with open(INPUT_FILE, "r", encoding="utf-8-sig") as dosya:
    okuyucu = csv.DictReader(dosya)
    for satir in okuyucu:
        pid = satir["Process_ID"]
        arrival = int(satir["Arrival_Time"])
        burst = int(satir["CPU_Burst_Time"])
        processler.append([pid, arrival, burst, burst]) 

processler.sort(key=lambda p: (p[1], p[0]))
n = len(processler)

cikti = open("SRTF_sonuc.txt", "w", encoding="utf-8")
print("SRTF (Preemptive SJF) GANTT:", file=cikti)

t = 0
bitti_sayisi = 0

beklemeler = []
tamamlanmalar = []
bitis_zamanlari = []

toplam_burst = 0
for p in processler:
    toplam_burst += p[2]

completion = {}  

aktif = None
parca_baslangic = None
parca_sayisi = 0

def segment_degistir(yeni):
    global aktif, parca_baslangic, parca_sayisi, t
    if aktif == yeni:
        return
    if aktif is not None:
        print(f"[ {parca_baslangic} ] - - {aktif} - - [ {t} ]", file=cikti)
        parca_sayisi += 1
    aktif = yeni
    parca_baslangic = t

def segment_kapat():
    global aktif, parca_baslangic, parca_sayisi, t
    if aktif is not None:
        print(f"[ {parca_baslangic} ] - - {aktif} - - [ {t} ]", file=cikti)
        parca_sayisi += 1
        aktif = None
        parca_baslangic = None

while bitti_sayisi < n:
    hazir = []
    for p in processler:
        if p[1] <= t and p[3] > 0:
            hazir.append(p)

    if len(hazir) == 0:
        sonraki = None
        for p in processler:
            if p[3] > 0:
                sonraki = p[1]
                break
        segment_degistir(BOSTA)
        t = sonraki
        continue

    # SRTF
    secilen = min(hazir, key=lambda p: (p[3], p[1], p[0]))
    segment_degistir(secilen[0])

    secilen[3] -= 1
    t += 1

    if secilen[3] == 0:
        completion[secilen[0]] = t
        bitti_sayisi += 1
        segment_kapat()

segment_kapat()

for pid, arrival, burst, _ in processler:
    c = completion[pid]
    ta = c - arrival
    wt = ta - burst
    tamamlanmalar.append(ta)
    beklemeler.append(wt)
    bitis_zamanlari.append(c)

print("\n--- SRTF SONUCLAR ---", file=cikti)
print("Max Waiting:", max(beklemeler), file=cikti)
print("Avg Waiting:", sum(beklemeler) / len(beklemeler), file=cikti)
print("Max Turnaround:", max(tamamlanmalar), file=cikti)
print("Avg Turnaround:", sum(tamamlanmalar) / len(tamamlanmalar), file=cikti)

print("\n--- THROUGHPUT ---", file=cikti)
for T in [50, 100, 150, 200]:
    sayi = 0
    for c in bitis_zamanlari:
        if c <= T:
            sayi += 1
    print(f"T={T}: {sayi}", file=cikti)

context_switch = parca_sayisi - 1
print("\n--- CONTEXT SWITCH ---", file=cikti)
print("Toplam:", context_switch, file=cikti)

cpu_verim = toplam_burst / (t + context_switch * SWITCH_SURESI)
print("\n--- CPU VERIMLILIGI ---", file=cikti)
print("Toplam Burst:", toplam_burst, file=cikti)
print("Makespan:", t, file=cikti)
print("Context Switch:", context_switch, file=cikti)
print("Context Switch Süresi:", context_switch * SWITCH_SURESI, file=cikti)
print("CPU Verimliliği:", cpu_verim, file=cikti)

cikti.close()

