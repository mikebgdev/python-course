### FIZZ BUZZ

def fizzbuzz():
    for index in range(1, 101):
        if index % 3 == 0 and index % 5 == 0:
            print("fizzbuzz")
        elif index % 3 == 0:
            print("fizz")
        elif index % 5 == 0:
            print("buzz")
        else:
            print(index)


fizzbuzz()


### Anagrama

def is_anagram(word_one, word_two):
    if word_one.lower() == word_two.lower():
        return False
    return sorted(word_one.lower()) == sorted(word_two.lower())


print(is_anagram("amor", "roma"))
print(is_anagram("amor", "loco"))


### Fibonnaci

def fibonacci():
    prev = 0
    next = 1

    for index in range(0, 50):
        print(prev)
        fib = prev + next
        prev = next
        next = fib


fibonacci()


### Primo

def is_prime():
    for number in range(1, 101):
        if number >= 2:

            is_divisible = False

            for index in range(2, number):
                if number % index == 0:
                    is_divisible = True

            if not is_divisible:
                print(number)


is_prime()


### Cadenas

def reverse(text):
    reverse_text = ""
    text_le = len(text)

    for index in range(0, len(text)):
        reverse_text += text[text_le - index - 1]

    return reverse_text


print(reverse("hola mundo"))