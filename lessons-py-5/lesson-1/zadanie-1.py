def count_syllables(word):
    vowels = "aeiouy"
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1
    return count

def check_rhythm(poem):
    words = poem.split()
    syllables_per_word = [count_syllables(word.replace('-', '')) for word in words]
    return "Парам пам-пам" if len(set(syllables_per_word)) == 1 else "Пам парам"

poem = input("Введите стихотворение: ")
print(check_rhythm(poem))
