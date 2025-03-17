import re
from collections import Counter

def count_unique_words(text):
   
    ignore_list = {"and", "but", "or", "nor", "for", "so", "yet", "a", "an", "the", "of"}
    
   
    words = re.findall(r'\b\w+\b', text)
    
   
    word_counts = Counter(word for word in words if word.lower() not in ignore_list)
    
    
    sorted_words = sorted(word_counts.items(), key=lambda x: (x[0].islower() == False, x[0]))
    
   
    for word, count in sorted_words:
        print(f"{word:<10} - {count}")
    
    print(f"Total words filtered: {sum(word_counts.values())}")


text = input("Enter a string statement:\n")
count_unique_words(text)
