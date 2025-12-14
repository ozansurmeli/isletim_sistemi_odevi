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
        processler.append([pid, arrival, burst, prio])

processler.sort(key=lambda p: (p[1], p[0]))
n = len(processler)
bitti_mi = [False] * n

cikti = open("PNP_sonuc.txt", "w", encoding="utf-8")
print("PNP (Non-Preemptive Priority) GANTT:", file=cikti)

t = 0
parca_sayisi = 0

beklemeler = []
tamamlanmalar = []
bitis_zamanlari = []

toplam_burst = 0
for p in processler:
    toplam_burst += p[2]

tamamlanan = 0

while tamamlanan < n:
    ready = []
    for i in range(n):
        pid, arrival, burst, prio = processler[i]
        if (not bitti_mi[i]) and (arrival <= t):
            ready.append(i)

    if len(ready) == 0:
        sonraki_gelis = None
        for i in range(n):
            if not bitti_mi[i]:
                sonraki_gelis = processler[i][1]
                break
        for i in range(n):
            if not bitti_mi[i] and processler[i][1] < sonraki_gelis:
                sonraki_gelis = processler[i][1]

        if t < sonraki_gelis:
            print(f"[ {t} ] - - {BOSTA} - - [ {sonraki_gelis} ]", file=cikti)
            parca_sayisi += 1
            t = sonraki_gelis
        continue

    sec = ready[0]
    for i in ready[1:]:
        a = processler[i]
        b = processler[sec]
        if (a[3], a[1], a[0]) < (b[3], b[1], b[0]):
            sec = i

    pid, arrival, burst, prio = processler[sec]

    baslangic = t
    bitis = t + burst
    print(f"[ {baslangic} ] - - {pid} - - [ {bitis} ]", file=cikti)
    parca_sayisi += 1

    t = bitis
    bitti_mi[sec] = True
    tamamlanan += 1

    completion = bitis
    turnaround = completion - arrival
    waiting = turnaround - burst

    bitis_zamanlari.append(completion)
    tamamlanmalar.append(turnaround)
    beklemeler.append(waiting)

print("\n--- PNP SONUCLAR ---", file=cikti)
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

