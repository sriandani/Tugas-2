import math

def hitung_luas_lingkaran(jari_jari):
    """Menghitung luas lingkaran berdasarkan jari-jari."""
    luas = math.pi * (jari_jari ** 2)
    return luas

def main():
    try:
        jari_jari = float(input("Masukkan jari-jari lingkaran: "))
        luas = hitung_luas_lingkaran(jari_jari)
        print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah {luas:.2f}")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

if __name__ == "__main__":
    main()
