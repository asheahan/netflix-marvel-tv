
from collections import defaultdict
from sklearn.feature_extraction import text
from sklearn.feature_extraction.text import TfidfVectorizer
import json

stop_words = text.ENGLISH_STOP_WORDS.union(['marvel', 'netflix', 'daredevil', 'jessica', 'jones', 'luke', 'cage', 'danny', 'rand', 'iron', 'fist'])
pos_tf = TfidfVectorizer(analyzer='word', ngram_range=(3,5), min_df = 0, stop_words = stop_words)
neg_tf = TfidfVectorizer(analyzer='word', ngram_range=(3,5), min_df = 0, stop_words = stop_words)
# tf = TfidfVectorizer(analyzer='word', ngram_range=(2,4), min_df = 0, stop_words = 'english')
positive_reviews = defaultdict(list)
negative_reviews = defaultdict(list)

with open('data/daredevil/audience-reviews.json', 'r') as handle:
    DD_AUDIENCE_REVIEWS = json.load(handle)

with open('data/jessica-jones/audience-reviews.json', 'r') as handle:
    JJ_AUDIENCE_REVIEWS = json.load(handle)

with open('data/luke-cage/audience-reviews.json', 'r') as handle:
    LC_AUDIENCE_REVIEWS = json.load(handle)

with open('data/iron-fist/audience-reviews.json', 'r') as handle:
    IF_AUDIENCE_REVIEWS = json.load(handle)

AUDIENCE_REVIEWS = DD_AUDIENCE_REVIEWS + JJ_AUDIENCE_REVIEWS + LC_AUDIENCE_REVIEWS + IF_AUDIENCE_REVIEWS

for review in AUDIENCE_REVIEWS:
    if review['rating'] > 3.0:
        positive_reviews[review['show'] + '-' + review['season']].append(review['body'])
    else:
        negative_reviews[review['show'] + '-' + review['season']].append(review['body'])

for show_id, review in positive_reviews.items():
    positive_reviews[show_id] = " ".join(review)

for show_id, review in negative_reviews.items():
    negative_reviews[show_id] = " ".join(review)

pos_corpus = []
neg_corpus = []
for show_id, reviews in sorted(positive_reviews.items(), key=lambda t: t[0]):
    pos_corpus.append(reviews)

for show_id, reviews in sorted(negative_reviews.items(), key=lambda t: t[0]):
    neg_corpus.append(reviews)

pos_tfidf_matrix = pos_tf.fit_transform(pos_corpus)
pos_feature_names = pos_tf.get_feature_names()
pos_dense = pos_tfidf_matrix.todense()

neg_tfidf_matrix = neg_tf.fit_transform(neg_corpus)
neg_feature_names = neg_tf.get_feature_names()
neg_dense = neg_tfidf_matrix.todense()

print('POSITIVE')
for i in range(0, 1):
    season = pos_dense[2].tolist()[0]
    phrase_scores = [pair for pair in zip(range(0, len(season)), season) if pair[1] > 0]

    sorted_phrase_scores = sorted(phrase_scores, key=lambda t: t[1] * -1)
    #with open('data/results/' + str(i) + '-2-3-ngram-tfidf-scores.tsv', 'w') as handle:
    for phrase, score in [(pos_feature_names[word_id], score) for (word_id, score) in sorted_phrase_scores][:20]:
        print('{0: <20} {1}'.format(phrase, score))
            #handle.write('{0: <20}\t{1}\n'.format(phrase, score))

print('NEGATIVE')
for i in range(0, 1):
    season = neg_dense[2].tolist()[0]
    phrase_scores = [pair for pair in zip(range(0, len(season)), season) if pair[1] > 0]

    sorted_phrase_scores = sorted(phrase_scores, key=lambda t: t[1] * -1)
    #with open('data/results/' + str(i) + '-2-3-ngram-tfidf-scores.tsv', 'w') as handle:
    for phrase, score in [(neg_feature_names[word_id], score) for (word_id, score) in sorted_phrase_scores][:20]:
        print('{0: <20} {1}'.format(phrase, score))
            #handle.write('{0: <20}\t{1}\n'.format(phrase, score))
