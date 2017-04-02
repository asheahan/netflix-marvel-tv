
from collections import defaultdict
from sklearn.feature_extraction import text
from sklearn.feature_extraction.text import TfidfVectorizer
import json

stop_words = text.ENGLISH_STOP_WORDS.union(['marvel', 'netflix', 'daredevil', 'jessica', 'jones', 'luke', 'cage', 'danny', 'rand'])
tf = TfidfVectorizer(analyzer='word', ngram_range=(2,3), min_df = 0, stop_words = stop_words)
# tf = TfidfVectorizer(analyzer='word', ngram_range=(2,4), min_df = 0, stop_words = 'english')
shows_and_seasons = defaultdict(list)

with open('data/daredevil/critic-reviews.json', 'r') as handle:
    DD_CRITIC_REVIEWS = json.load(handle)

with open('data/daredevil/audience-reviews.json', 'r') as handle:
    DD_AUDIENCE_REVIEWS = json.load(handle)

with open('data/jessica-jones/critic-reviews.json', 'r') as handle:
    JJ_CRITIC_REVIEWS = json.load(handle)

with open('data/jessica-jones/audience-reviews.json', 'r') as handle:
    JJ_AUDIENCE_REVIEWS = json.load(handle)

with open('data/luke-cage/critic-reviews.json', 'r') as handle:
    LC_CRITIC_REVIEWS = json.load(handle)

with open('data/luke-cage/audience-reviews.json', 'r') as handle:
    LC_AUDIENCE_REVIEWS = json.load(handle)

with open('data/iron-fist/critic-reviews.json', 'r') as handle:
    IF_CRITIC_REVIEWS = json.load(handle)

with open('data/iron-fist/audience-reviews.json', 'r') as handle:
    IF_AUDIENCE_REVIEWS = json.load(handle)

CRITIC_REVIEWS = DD_CRITIC_REVIEWS + JJ_CRITIC_REVIEWS + LC_CRITIC_REVIEWS + IF_CRITIC_REVIEWS
AUDIENCE_REVIEWS = DD_AUDIENCE_REVIEWS + JJ_AUDIENCE_REVIEWS + LC_AUDIENCE_REVIEWS + IF_AUDIENCE_REVIEWS

for review in CRITIC_REVIEWS:
    shows_and_seasons[review['show'] + '-' + review['season']].append(review['body'])

for review in AUDIENCE_REVIEWS:
    shows_and_seasons[review['show'] + '-' + review['season']].append(review['body'])

for show_id, review in shows_and_seasons.items():
    print(show_id)
    shows_and_seasons[show_id] = " ".join(review)

corpus = []
for show_id, reviews in sorted(shows_and_seasons.items(), key=lambda t: t[0]):
    corpus.append(reviews)

tfidf_matrix = tf.fit_transform(corpus)
feature_names = tf.get_feature_names()
dense = tfidf_matrix.todense()

for i in range(0, 5):
    season = dense[i].tolist()[0]
    phrase_scores = [pair for pair in zip(range(0, len(season)), season) if pair[1] > 0]

    sorted_phrase_scores = sorted(phrase_scores, key=lambda t: t[1] * -1)
    with open('data/results/' + str(i) + '-2-3-ngram-tfidf-scores.tsv', 'w') as handle:
        for phrase, score in [(feature_names[word_id], score) for (word_id, score) in sorted_phrase_scores][:20]:
            handle.write('{0: <20}\t{1}\n'.format(phrase, score))
