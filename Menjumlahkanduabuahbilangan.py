def main():
    try:
        bilangan1 = float(input("Masukkan bilangan pertama: "))
        bilangan2 = float(input("Masukkan bilangan kedua: "))
        hasil = bilangan1 + bilangan2
        
        print(f"Hasil penjumlahan {bilangan1} dan {bilangan2} adalah {hasil}")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

if __name__ == "__main__":
    main()
