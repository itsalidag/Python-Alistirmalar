import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

kelime = ['baba', 'hayat', 'bilgi', 'an', 'sonuç', 'dış', 'ad', 'süre', 'saat', 'yaş', 'sorun', 'devlet', 'sahip', 'sıra', 'yüzde', 'ay', 
'olay', 'söz', 'sistem', 'kapı', 'kitap', 'gece', 'alan', 'bugün', 'dönem', 'arkadaş', 'ürün', 'aile', 'erkek', 'güç', 'gerçek', 'ilişki', 'çevre', 'yaşam', 'halk', 'sokak', 'bey', 'tarih', 'özellik', 'bölüm', 'akıl', 'anlam', 'banka', 'ayak', 'toplum', 'araç', 'madde', 'tür', 'karar', 'hava', 'sayı', 'grup', 'oda', 'biçim', 'haber', 'Allah', 'soru', 'arka', 'yazı', 'okul', 'dil', 'şirket', 'kaynak', 'program', 'hareket', 'renk', 'hak', 'çalışma', 'açı', 'parça', 'gazete', 'değer', 'yapı', 'doktor', 'gelir', 'görev', 'amaç', 'bölge', 'film', 'müşteri', 'telefon', 'eğitim', 'deniz', 'etki', 'vücut', 'düşünce', 'milyon ', 'temel', 'kültür', 'resim', 'ışık', 'hanım', 'hatun', 'hizmet', 'ihtiyaç', 'nokta', 'yön', 'oyun', 'işlem', 'oran', 'orada', 'dikkat', 'bilgisayar', 'gelecek', 'oğul', 'lira', 'üretim', 'dakika', 'araba', 'ağız', 'duygu', 'örnek', 'derece', 'duvar', 'sanat', 'ana', 'hastalık', 'öğrenci', 'televizyon', 'yöntem', 'masa', 'takım', 'kafa', 'müzik', 'enerji', 'üniversite', 'spor', 'türlü', 'can', 'kısım', 'ölüm', 'sağlık', 'sabah', 'internet', 'teknik', 'dışarı', 'merkez', 'ortam', 'düzey', 'köy', 'yönetim', 'aşağı', 'cevap', 'toprak', 'isim', 'akşam', 'araştırma', 'kan', 'hasta', 'şehir', 'hafta', 'trafik', 'hesap', 'otomobil', 'yabancı', 'davranış', 'mutfak', 'kent', 'fiyat', 'kol', 'cam', 'önem', 'koca', 'varlık', 'ilgi', 'satış', 'içeri', 'acı', 'kat', 'ekonomi', 'fotoğraf', 'hayvan', 'savaş', 'mal', 'saç', 'kalan', 'sayfa', 'teknoloji', 'kurum', 'sektör', 'kağıt', 'koku', 'yüzyıl', 'cadde', 'pazar']
chosen_word = random.choice(kelime)

display = []
for i in range(len(chosen_word)):
    display += "_"

print(display)

end_of_game = False
hearts=6
while not end_of_game:
    guess = input("Guess a word: ")
    if len(guess) > 1:
        print("only one word please. ")
    else:
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == guess:
                print("thats true.")
                display[position] = letter
    print(display)
    
    if guess not in chosen_word:
        hearts-=1
        print("You were wrong. {} hearts remaining".format(hearts))
        print(stages[hearts])
        print(display)
    if hearts ==0:
        print("you lose. Answer was {}".format(chosen_word))
        break
    if "_" not in display:
        print("You Win!")
        end_of_game == True
        break
