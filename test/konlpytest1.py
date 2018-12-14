from konlpy.tag import Twitter
from collections import Counter

def tag_counting():
    nlpy  = Twitter()
    nouns = nlpy .nouns(u'대학에서 DB, 통계학, 이산수학 등을 배웠지만..., 대학, 대학, DB, DB, 통계학, 배웠지만, DB, Db, 바보, 바보')
    count = Counter(nouns)
    print(nouns)

    tag_count = []
    tags = []

    for n, c in count.most_common(100):
        dics = {'tag': n, 'count': c}
        if len(dics['tag']) >= 2 and len(tags) <= 49:
            tag_count.append(dics)
            tags.append(dics['tag'])

    for tag in tag_count:
        print(" {:<14}".format(tag['tag']), end='\t')
        print("{}".format(tag['count']))
        print("\n---------------------------------")
        print("     명사 총  {}개".format(len(tags)))
        print("---------------------------------\n\n")
        return tags

tag_counting()