import re
from collections import Counter
def find_most_common_words(file_path, n):
    with open(file_path, 'r') as file:
        text = file.read().lower()
        words = re.findall(r'\b\w+\b', text)
        word_counts = Counter(words)
        return word_counts.most_common(n)

print("Las 10 palabras mas utilizadas en el discurso de Obama son:")
for words , number in find_most_common_words("obama_speech.txt", 10):
    print(f"{words}: {number}")
print("Las 10 palabras mas utilizadas en el discurso de Michelle Obama son:")
for words , number in find_most_common_words("michelle_obama_speech.txt", 10):
    print(f"{words}: {number}")
print("Las 10 palabras mas utilizadas en el discurso de Donald Trump son:")
for words , number in find_most_common_words("donald_speech.txt", 10):
    print(f"{words}: {number}")
print("Las 10 palabras mas utilizadas en el discurso de Melina Trump son:")
for words , number in find_most_common_words("melina_trump_speech.txt", 10):
    print(f"{words}: {number}")

"""
Escriba una aplicación de Python que verifique la similitud entre dos textos.
"""


def read_text(source):
    try:
        with open(source, "r", encoding="utf-8") as file:
            return file.read()
    except (OSError, TypeError):
        return source


def clean_text(text):
    text = text.lower()
    return re.sub(r"[^\w\s]", "", text)


def remove_support_words(text, support_words):
    words = text.split()
    support_words = {word.lower() for word in support_words}
    filtered_words = [word for word in words if word not in support_words]
    return ' '.join(filtered_words)


def check_text_similarity(text1, text2):
    words1 = set(text1.split())
    words2 = set(text2.split())
    common_words = words1.intersection(words2)
    largest_text = max(len(words1), len(words2))
    return len(common_words) / largest_text if largest_text else 0


print("La similitud entre los discursos de Michelle y Melina es:")
text1 = clean_text(read_text("michelle_obama_speech.txt"))
text2 = clean_text(read_text("melina_trump_speech.txt"))
support_words = read_text("support_words.txt").splitlines()
text1 = remove_support_words(text1, support_words)
text2 = remove_support_words(text2, support_words)
similarity = check_text_similarity(text1, text2)
print(f"Similitud: {similarity:.2%}")