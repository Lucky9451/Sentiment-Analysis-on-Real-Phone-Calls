import matplotlib.pyplot as plt


def generate_graphs(emotions, counts, polarity, subjectivity):
    # Creating subplots for emotion distribution, polarity, and subjectivity
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 6))

    # Emotion Distribution
    ax1.bar(emotions, counts)
    ax1.set_xlabel('Emotions')
    ax1.set_ylabel('Counts')
    ax1.set_title('Emotion Distribution')

    # Rotate the x-axis labels by 45 degrees
    ax1.set_xticks(emotions)
    ax1.set_xticklabels(emotions, rotation=45, ha="right")

    # Bar labels(polarity, subjectivity) and values
    bars = ['Polarity', 'Subjectivity']
    values = [polarity, subjectivity]
    colors = ['blue', 'green']

    ax2.bar(bars, values, color=colors)
    ax2.set_ylabel('Value')
    ax2.set_title('Polarity and Subjectivity')

    # Adjust layout and save the graph as an image
    plt.tight_layout()
    plt.savefig('sentiment_analysis_visualization.png', format='png')
    plt.show()
