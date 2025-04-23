kamus = {"pisang": "buah berwarna kuning",
        "apel": "buah berwarna merah atau hijau",
        "jeruk": "buah berwarna oranye",
        "mangga": "buah tropis yang manis",
        "anggur": "buah kecil yang tumbuh berkelompok"}
    
kata = input("Masukkan kata yang ingin dicari artinya: ").lower()

    
if kata in kamus:
        print(f"Arti dari {kata} adalah {kamus[kata]}")
else:
        print(f"Maaf, arti dari {kata} tidak ditemukan dalam kamus.")