import re
from collections import Counter
from nltk.corpus import stopwords

# Download NLTK stopwords if not already downloaded
import nltk
nltk.download('stopwords')

# Function to read text from file
def read_text_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    return text

# Function to preprocess text
def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    return text

# Function to remove stopwords
def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    words = text.split()
    filtered_words = [word for word in words if word not in stop_words]
    return filtered_words

# Function to count word frequency
def count_word_frequency(words):
    word_freq = Counter(words)
    return word_freq

# Function to display word frequency
def display_word_frequency(word_freq):
    for word, freq in word_freq.items():
        print(f'{word}: {freq}')

if __name__ == "__main__":
    # Read text from file
    file_path = '/app/random_paragraphs.txt'
    text = read_text_file(file_path)

    # Preprocess text
    processed_text = preprocess_text(text)

    # Remove stopwords
    filtered_words = remove_stopwords(processed_text)

    # Count word frequency
    word_freq = count_word_frequency(filtered_words)

    # Display word frequency
    display_word_frequency(word_freq)
