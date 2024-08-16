import nltk
from nltk.tokenize import word_tokenize
from collections import Counter

# Ensure that NLTK resources are downloaded
print("Downloading NLTK resources...")
nltk.download('punkt')  # Download the tokenizer models for NLTK
print("NLTK resources downloaded.")

# Step 1: Read and tokenize the source file
print("Reading and tokenizing source file...")
with open("Nyt.200811.txt", 'r') as in_file:
    text_content = in_file.read()  # Read the entire content of the source file

word_list = word_tokenize(text_content)  # Tokenize the content into words

# Step 2: Save tokens to a file
print("Saving tokens to file...")
with open("file_token.txt", 'w') as tokens:
    for word in word_list:
        tokens.write(word + '\n')  # Write each token to a new line in the file

# Step 3: Create two almost-duplicate files
print("Creating two almost-duplicate files...")
with open("file_token.txt", 'r') as tokens_in:
    all_lines = tokens_in.readlines()  # Read all lines from the token file

# Create two files, each missing one different line
with open("file_token1.txt", 'w') as first_file, open("file_token2.txt", 'w') as second_file:
    for index in range(len(all_lines)):
        if index < len(all_lines) - 1:
            first_file.write(all_lines[index])
            # Write all lines except the last to the first file
        if index > 0:
            second_file.write(all_lines[index])
            # Write all lines except the first to the second file

# Step 4: Create a bigrams file
print("Generating bigrams file...")
with open("file_token1.txt", 'r') as f_input, open("file_token2.txt", 'r') as s_input:
    f_lines = f_input.readlines()
    # Read all lines from the first split file
    s_lines = s_input.readlines()
    # Read all lines from the second split file

# Write bigrams (pairs of words) to a new file
with open("file_bigrams.txt", 'w') as bg_out:
    for line_one, line_two in zip(f_lines, s_lines):
        word_one = line_one.strip()
        # Remove any extra whitespace from the line
        word_two = line_two.strip()
        # Remove any extra whitespace from the line
        bg_out.write(f"{word_one} {word_two}\n")
        # Write the bigram to the file

# Step 5: Find and print the most common bigrams
print("Analyzing bigrams file...")
with open("file_bigrams.txt", 'r') as bg_input:
    bgl = bg_input.readlines()
    # Read all lines from the bigrams file

# Convert each line to a tuple representing a bigram
bg_tup = [tuple(l.strip().split()) for l in bgl]

# Get the 10 most common bigrams and print
print("Top 10 Most Common Bigrams:")
for bg, freq in Counter(bg_tup).most_common(10):
    print(f"{bg}: {freq}")