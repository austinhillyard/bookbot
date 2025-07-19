def get_word_count(text: str):
    return len(text.split())

def count_unique_characters(text: str):
    text = text.lower()
    chars = list(text)
    counts = {}
    for char in chars:
        if not char.isalpha():
            continue
        counts[char] = counts.get(char, 0) + 1
    return counts

def sort_counts(counts: dict):
    return sorted(counts.items(), reverse=True, key=lambda x:x[1])