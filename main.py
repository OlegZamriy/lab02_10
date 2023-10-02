user_text = input("Введіть текст: ")

sentences = user_text.split(".") or user_text.split("!") or user_text.split("?")

sentences = [sentence.strip() for sentence in sentences if sentence.strip()]

sentence_count = len(sentences)

print("Кількість речень в тексті:", sentence_count)