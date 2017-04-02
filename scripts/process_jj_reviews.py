
import json
import string
import nltk
from nltk.corpus import stopwords

'''
critic_review_sample = {
    'show': 'Jessica Jones',
    'season': '1',
    'user_id': 'critic_name_id',
    'user_name': 'critic_name',
    'source': 'publication',
    'date': 'November 2, 2015',
    'body': 'review'
}

audience_review_sample = {
    'show': 'Jessica Jones',
    'season': '2',
    'rating': 3.5,
    'user_id': '134819431',
    'user_name': 'user_name',
    'date': 'November 2, 2015',
    'body': 'review'
}
'''

with open('data/jessica-jones/critic-reviews.json', 'r') as handle:
    CRITIC_REVIEWS = json.load(handle)

with open('data/jessica-jones/audience-reviews.json', 'r') as handle:
    AUDIENCE_REVIEWS = json.load(handle)

## -- Most Common Words -- ##
for season in range(1, 2):
    print(str(season))
    critic_tokens = []
    audience_tokens = []
    for review in CRITIC_REVIEWS:
        if review['season'] == str(season):
            lowers = review['body'].lower()
            no_punctuation = lowers.translate(str.maketrans('', '', string.punctuation))
            critic_tokens.extend(nltk.word_tokenize(no_punctuation))
    critic_filtered = [w for w in critic_tokens if not w in stopwords.words('english')]
    critic_word_list = nltk.FreqDist(critic_filtered)
    with open('data/jessica-jones/results/season-' + str(season) \
        + '-critic-most-common-words.tsv', 'w') as handle:
        for word, frequency in critic_word_list.most_common(50):
            handle.write('{}\t{}\n'.format(word, frequency))
    for review in AUDIENCE_REVIEWS:
        if review['season'] == str(season):
            lowers = review['body'].lower()
            no_punctuation = lowers.translate(str.maketrans('', '', string.punctuation))
            audience_tokens.extend(nltk.word_tokenize(no_punctuation))
    audience_filtered = [w for w in audience_tokens if not w in stopwords.words('english')]
    audience_word_list = nltk.FreqDist(audience_filtered)
    with open('data/jessica-jones/results/season-' + str(season) \
        + '-audience-most-common-words.tsv', 'w') as handle:
        for word, frequency in audience_word_list.most_common(50):
            handle.write('{}\t{}\n'.format(word, frequency))
