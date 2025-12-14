import csv

processler = []

with open("odev1_case2.txt", "r", encoding="utf-8-sig") as dosya:
    okuyucu = csv.DictReader(dosya)

    for satir in okuyucu:
        pid = satir["Process_ID"]
        arrival = int(satir["Arrival_Time"])
        burst = int(satir["CPU_Burst_Time"])
        priority = satir["Priority"]

        processler.append([pid, arrival, burst, priority])

# FCFS
processler.sort(key=lambda p: p[1])

t = 0
toplam_burst = 0
bitis_zamanlari = []
beklemeler = []
tamamlanmalar = []

cikti = open("FCFS_sonuc.txt", "w", encoding="utf-8")

print("FCFS GANTT:", file=cikti)

parca_sayisi = 0

for p in processler:
    pid, arrival, burst, priority = p
    toplam_burst += burst

    # CPU boş ise
    if t < arrival:
        print(f"[ {t} ] - - BOSTA - - [ {arrival} ]", file=cikti)
        parca_sayisi += 1
        t = arrival

    # Process
    baslangic = t
    bitis = t + burst
    print(f"[ {baslangic} ] - - {pid} - - [ {bitis} ]", file=cikti)
    parca_sayisi += 1
    t = bitis

    # Süre
    completion = bitis
    bitis_zamanlari.append(completion)
    turnaround = completion - arrival
    waiting = turnaround - burst

    beklemeler.append(waiting)
    tamamlanmalar.append(turnaround)

print("\n--- FCFS SONUCLAR ---", file=cikti)
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

cpu_verim = toplam_burst / (t + context_switch * 0.001)

print("\n--- CPU VERIMLILIGI ---", file=cikti)
print("Toplam Burst:", toplam_burst, file=cikti)
print("Makespan:", t, file=cikti)
print("Context Switch:", context_switch, file=cikti)
print("Context Switch Süresi:", context_switch * 0.001, file=cikti)
print("CPU Verimliliği:", cpu_verim, file=cikti)


cikti.close()



    

    



