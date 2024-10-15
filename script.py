import re
import socket
from collections import Counter
import os

# Paths to the text files and output folder inside the container
file2_path = '/home/data/AlwaysRememberUsThisWay.txt'
file1_path = '/home/data/IF.txt'
output_path = '/home/data/output/result.txt'

# Ensure the output directory exists
output_dir = os.path.dirname(output_path)
print(f"Ensuring output directory exists at {output_dir}")
os.makedirs(output_dir, exist_ok=True)

# Read the content of the two text files
with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
    text1 = file1.read()
    text2 = file2.read()

# 1. Count the total number of words in each file
word_count1 = len(text1.split())
word_count2 = len(text2.split())

# 2. Calculate the grand total of words across both files
total_words = word_count1 + word_count2

# 3. Identify the top 3 most frequent words in IF.txt
word_frequencies1 = Counter(text1.split())
top3_if = word_frequencies1.most_common(3)

# 4. Handle contractions and find the top 3 most frequent words in AlwaysRememberUsThisWay.txt
# Replace common contractions
text2 = re.sub(r"n\'t", " not", text2)
text2 = re.sub(r"\'re", " are", text2)
text2 = re.sub(r"\'s", " is", text2)
text2 = re.sub(r"\'ll", " will", text2)
text2 = re.sub(r"\'m", " am", text2)
text2 = re.sub(r"\'d", " would", text2)
text2 = re.sub(r"\'ve", " have", text2)

word_frequencies2 = Counter(text2.split())
top3_arutw = word_frequencies2.most_common(3)

# 5. Determine the IP address of the container's host
ip_address = socket.gethostbyname(socket.gethostname())

# 6. Write all results to /home/data/output/result.txt
print(f"Writing results to {output_path}")
with open(output_path, 'w') as result_file:
    result_file.write(f"Word count IF.txt: {word_count1}\n")
    result_file.write(f"Word count ARUTW.txt: {word_count2}\n")
    result_file.write(f"Grand total of words: {total_words}\n")
    result_file.write(f"Top 3 words in IF.txt: {top3_if}\n")
    result_file.write(f"Top 3 words in AlwaysRememberUsThisWay.txt: {top3_arutw}\n")
    result_file.write(f"IP address: {ip_address}\n")

# 7. Print the contents of result.txt to the console
with open(output_path, 'r') as result_file:
    print(result_file.read())