def main():
    try:
        bilangan = int(input("Masukkan sebuah bilangan: "))

        if bilangan % 2 == 0:
            print(f"{bilangan} adalah bilangan genap.")
        else:
            print(f"{bilangan} adalah bilangan ganjil.")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka bulat.")

if __name__ == "__main__":
    main()
