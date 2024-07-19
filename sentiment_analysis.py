# Sentiment Analysis using Lexicon Based Approach

from visualizations import generate_graphs


def perform_sentiment_analysis(final_words):
    # Read emotions from emotions.txt
    emotions = {}
    with open("emotions.txt", "r") as file:
        for line in file:
            word, emotion = line.replace("\n", '').replace(",", '').replace("'", '').strip().split(':')
            emotions[word] = emotion

    # Perform sentiment analysis
    word_emotions = []
    print('Set of tokens that matched lexicon keys:')
    for word in final_words:
        if word.lower() in emotions:
            print('Word: {}, Emotion: {}'.format(word, emotions[word]))
            word_emotions.append(emotions[word.lower()])

    print()  # For formatting

    # Count the occurrences of each emotion
    emotion_counts = {emotion: word_emotions.count(emotion) for emotion in set(word_emotions)}

    # Output the sentiment analysis results
    print("Emotion counts:", emotion_counts)

    # Calculate polarity and sensitivity
    total_words = len(final_words)
    total_emotions = sum(emotion_counts.values())

    polarity = total_emotions / total_words if total_words > 0 else 0

    unique_emotions = len(set(word_emotions))
    subjectivity = (unique_emotions / total_emotions) if total_emotions > 0 else 0

    # Output the sentiment analysis results
    print("Polarity:", polarity)
    print("Subjectivity:", subjectivity)

    # Extract the emotions and counts for plotting
    emotions = list(emotion_counts.keys())
    counts = list(emotion_counts.values())

    # Pass required data to 'generate_graphs' for visualizations
    generate_graphs(emotions, counts, polarity, subjectivity)
