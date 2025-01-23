from cs50 import get_string


def main():
    # Get input
    text = get_string("Text: ")

    # Count the number of letters, words, and sentences in the text
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)

    # Compute the Coleman-Liau index
    L = (letters / words) * 100
    S = (sentences / words) * 100
    index = 0.0588 * L - 0.296 * S - 15.8
    grade = round(index)

    # Print the grade level
    if grade >= 16:
        print("Grade 16+")
    elif grade < 1:
        print("Before Grade 1")
    else:
        print(f"Grade {grade}")


def count_letters(text):
    count = 0
    for char in text:
        if char.isalpha():
            count += 1
    return count


def count_words(text):
    # Split the text by spaces to count words
    words = text.split()
    return len(words)


def count_sentences(text):
    count = 0
    for char in text:
        if char in '.!?':
            count += 1
    return count


main()
