from sentiment_analysis import perform_sentiment_analysis


import string


def text_cleanup():
    # Read the transcribed text
    with open("transcribed_text.txt", "r") as file:
        transcribed_text = file.read()

    # converting to lowercase
    lower_case = transcribed_text.lower()

    # Removing punctuations
    cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

    # Tokenize and remove 'stop' words
    tokenized_words = cleaned_text.split()
    stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
                  "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
                  "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that",
                  "these",
                  "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having",
                  "do",
                  "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
                  "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
                  "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under",
                  "again",
                  "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both",
                  "each",
                  "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so",
                  "than",
                  "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

    # Removing stop words from the tokenized words list
    final_words = []
    for word in tokenized_words:
        if word not in stop_words:
            final_words.append(word)

    print('Set of final words from the audio data:', final_words)
    print()  # For formatting

    # Calling 'perform_sentiment_analysis()' for further processing
    perform_sentiment_analysis(final_words)
