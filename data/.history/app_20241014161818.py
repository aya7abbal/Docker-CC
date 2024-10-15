import re
import socket
import os
from collections import Counter

# Paths to the text files inside the container
file1_path = './IF.txt'
file2_path = './AlwaysRememberUsThisWay.txt'
output_path = './output/result.txt'

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

# Ensure the output directory exists
output_dir = os.path.dirname(output_path)
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 6. Write all results to ./output/result.txt
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