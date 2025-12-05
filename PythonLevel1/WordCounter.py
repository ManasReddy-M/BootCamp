def analyze_sentence(sentence: str) -> dict:
    """
    Analyzes a sentence to count words and characters, 
    and finds the longest and shortest words.
    """
    
    # 1. Prepare the words list 
    # Split the sentence by spaces. This handles multiple spaces gracefully
    # and automatically removes leading/trailing whitespace from the original sentence.
    words = sentence.split()
    
    # Handle the edge case of an empty input string
    if not words:
        return {
            "total_words": 0,
            "total_chars_with_spaces": len(sentence),
            "total_chars_without_spaces": 0,
            "longest_word": None,
            "shortest_word": None
        }

    # --- Calculations ---
    
    # 2. Count total words
    total_words = len(words)
    
    # 3. Count total characters (with and without spaces)
    total_chars_with_spaces = len(sentence)
    total_chars_without_spaces = len("".join(words)) 
    # Or, loop through the original sentence and count non-space characters
    # total_chars_without_spaces = sum(1 for char in sentence if char != ' ')

    # 4. Find the longest and shortest words
    # Initialize with the first word to avoid handling an empty list error
    longest_word = words[0]
    shortest_word = words[0]
    
    # Iterate through the rest of the words starting from the second word
    for word in words[1:]:
        # Find the longest word
        if len(word) > len(longest_word):
            longest_word = word
            
        # Find the shortest word (less than or equal to, to include first word if needed)
        if len(word) < len(shortest_word):
            shortest_word = word

    # 5. Return the results in a dictionary
    return {
        "total_words": total_words,
        "total_chars_with_spaces": total_chars_with_spaces,
        "total_chars_without_spaces": total_chars_without_spaces,
        "longest_word": longest_word,
        "shortest_word": shortest_word
    }

# --- Test ---
test_sentence = "The quick brown fox jumps over the lazy dog"
result = analyze_sentence(test_sentence)
print(f"Input Sentence: '{test_sentence}'")
print("-" * 30)
print(result)