#NAMA : AISHA MABELINA
#NIM : 065002400026

def jumlah_rekursif(angka):
    if not angka:
        return 0
    return angka[0] + jumlah_rekursif(angka[1:])

jumlah = float(input("Masukkan Jumlah: "))

jumlah = int(jumlah)

angka = []
for i in range(1, jumlah + 1):
    num = float(input(f"Masukkan bilangan ke-{i}: "))
    angka.append(num)

hasil = jumlah_rekursif(angka)
print(f"Hasil dari penjumlahan adalah: {hasil}")


