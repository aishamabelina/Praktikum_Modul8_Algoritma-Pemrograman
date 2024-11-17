print("Ini merupakan program pemangkatan negatif dan positif, tekan Enter untuk berhenti")

def perpangkatan(x, y):
    if y == 0:
        return 1
    else:
        return x * perpangkatan(x, y - 1)

def program():
    x = input("Masukkan angka awal: ")
    if x == "":  
        print("Program selesai")
        return
    
    y = input("Masukkan pangkatnya: ")
    if y == "":  
        print("Program selesai")
        return
    else:
        x = int(x)
        y = int(y)
        hasil = perpangkatan(x, y)
        print(f"Hasil dari {x} pangkat {y} adalah {hasil}")
        
program()