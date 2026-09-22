positive_words = {
    "love",
    "loved",
    "excellent",
    "amazing",
    "good",
    "great",
    "awesome",
    "happy",
    "wonderful",
    "best",
    "fantastic",
    "nice"
}

negative_words = {
    "hate",
    "hated",
    "terrible",
    "bad",
    "poor",
    "worst",
    "awful",
    "horrible",
    "sad",
    "disappointed",
    "slow",
    "problem"
}


def analyze_text(text):
    words = text.lower().split()

    positive_count = 0
    negative_count = 0

    for word in words:
        word = word.strip(".,!?;:")

        if word in positive_words:
            positive_count += 1

        if word in negative_words:
            negative_count += 1

    score = positive_count - negative_count

    if positive_count > 0 and negative_count > 0:
        sentiment = "Mixed"
    elif score > 0:
        sentiment = "Positive"
    elif score < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    if sentiment == "Positive":
        explanation = "The text contains more positive words than negative words."
    elif sentiment == "Negative":
        explanation = "The text contains more negative words than positive words."
    elif sentiment == "Mixed":
        explanation = "The text contains both positive and negative words."
    else:
        explanation = "The text does not contain clear positive or negative words."

    return sentiment, score, explanation

