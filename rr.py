import csv

INPUT_FILE = "odev1_case2.txt"
BOSTA = "BOSTA"
SWITCH_SURESI = 0.001
Q = 4

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

cikti = open(f"RR_sonuc_q{Q}.txt", "w", encoding="utf-8")
print(f"ROUND ROBIN (q={Q}) GANTT:", file=cikti)

segmentler = []
def seg_ekle(start, end, label):
    if start == end:
        return
    if len(segmentler) > 0 and segmentler[-1][2] == label and segmentler[-1][1] == start:
        segmentler[-1][1] = end
    else:
        segmentler.append([start, end, label])

t = 0
ready = []
next_i = 0
completion = {}

toplam_burst = 0
for p in processler:
    toplam_burst += p[2]

def arrivals_ekle(t_zamani):
    global next_i
    while next_i < n and processler[next_i][1] <= t_zamani:
        ready.append(next_i)
        next_i += 1

arrivals_ekle(t)

while len(completion) < n:
    if len(ready) == 0:
        if next_i < n and t < processler[next_i][1]:
            yeni_t = processler[next_i][1]
            seg_ekle(t, yeni_t, BOSTA)
            t = yeni_t
        arrivals_ekle(t)
        continue

    idx = ready.pop(0)
    pid, arrival, burst, remaining = processler[idx]

    calisma = remaining if remaining < Q else Q

    baslangic = t
    bitis = t + calisma
    seg_ekle(baslangic, bitis, pid)

    t = bitis
    remaining -= calisma
    processler[idx][3] = remaining

    arrivals_ekle(t)

    if remaining == 0:
        completion[pid] = t
    else:
        ready.append(idx)

for s, e, lab in segmentler:
    print(f"[ {s} ] - - {lab} - - [ {e} ]", file=cikti)

beklemeler = []
tamamlanmalar = []
bitis_zamanlari = []

for pid, arrival, burst, remaining in processler:
    c = completion[pid]
    turnaround = c - arrival
    waiting = turnaround - burst
    beklemeler.append(waiting)
    tamamlanmalar.append(turnaround)
    bitis_zamanlari.append(c)

print("\n--- RR SONUCLAR ---", file=cikti)
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

parca_sayisi = len(segmentler)
context_switch = parca_sayisi - 1 if parca_sayisi > 0 else 0

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

