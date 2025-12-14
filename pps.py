import csv

INPUT_FILE = "odev1_case2.txt"
BOSTA = "BOSTA"
SWITCH_SURESI = 0.001

prio_map = {"high": 0, "normal": 1, "low": 2}

processler = []
with open(INPUT_FILE, "r", encoding="utf-8-sig") as dosya:
    okuyucu = csv.DictReader(dosya)
    for satir in okuyucu:
        pid = satir["Process_ID"]
        arrival = int(satir["Arrival_Time"])
        burst = int(satir["CPU_Burst_Time"])
        pr = (satir["Priority"] or "").strip().lower()
        prio = prio_map.get(pr, 1)
        processler.append([pid, arrival, burst, burst, prio])

processler.sort(key=lambda p: (p[1], p[0]))
n = len(processler)

cikti = open("PPS_sonuc.txt", "w", encoding="utf-8")
print("PPS (Preemptive Priority) GANTT:", file=cikti)

t = 0
bitti_sayisi = 0
completion = {}

toplam_burst = 0
for p in processler:
    toplam_burst += p[2]

segmentler = []
def seg_ekle(start, end, label):
    if start == end:
        return
    if len(segmentler) > 0 and segmentler[-1][2] == label and segmentler[-1][1] == start:
        segmentler[-1][1] = end
    else:
        segmentler.append([start, end, label])

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
        if sonraki is None:
            break
        seg_ekle(t, sonraki, BOSTA)
        t = sonraki
        continue

    secilen = min(hazir, key=lambda p: (p[4], p[3], p[1], p[0]))
    pid, arrival, burst, remaining, prio = secilen

    seg_ekle(t, t + 1, pid)
    secilen[3] -= 1
    t += 1

    if secilen[3] == 0:
        completion[pid] = t
        bitti_sayisi += 1

for s, e, lab in segmentler:
    print(f"[ {s} ] - - {lab} - - [ {e} ]", file=cikti)

beklemeler = []
tamamlanmalar = []
bitis_zamanlari = []

for pid, arrival, burst, remaining, prio in processler:
    c = completion[pid]
    turnaround = c - arrival
    waiting = turnaround - burst
    tamamlanmalar.append(turnaround)
    beklemeler.append(waiting)
    bitis_zamanlari.append(c)

print("\n--- PPS SONUCLAR ---", file=cikti)
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
