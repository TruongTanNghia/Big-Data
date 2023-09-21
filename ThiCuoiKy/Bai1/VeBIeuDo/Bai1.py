import re
import matplotlib.pyplot as plt

# Read the file and extract words and counts
words = []
counts = []
with open('data', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        match = re.match(r"b'(.+?)'\s+(\d+)", line)
        if match:
            word, count = match.groups()
            words.append(word)
            counts.append(int(count))

# Create the chart
plt.bar(words, counts)

# Add labels and title

plt.xlabel('Word')
plt.ylabel('Frequency')
plt.title('Most Common Words')
# Show the chart
plt.show()
