import pandas as pd
from konlpy.tag import Mecab
from gensim.models.doc2vec import TaggedDocument
from tqdm import tqdm
from gensim.models import doc2vec

df = pd.read_csv('./dataset/merged_output_2.csv',  sep=',')
df = df.dropna()

mecab = Mecab()

tagged_corpus_list = []

for index, row in tqdm(df.iterrows(), total=len(df)):
  isbn13 = row['Isbn13']
  description = row['Description']
  tagged_corpus_list.append(TaggedDocument(tags=[isbn13], words=mecab.morphs(description)))

print('문서의 수 :', len(tagged_corpus_list))

tagged_corpus_list[0]

model = doc2vec.Doc2Vec(vector_size=300, alpha=0.025, min_alpha=0.025, workers=8, window=8)

# Vocabulary 빌드
model.build_vocab(tagged_corpus_list)

# Doc2Vec 학습
model.train(tagged_corpus_list, total_examples=model.corpus_count, epochs=20)

# 모델 저장
model.save('dart.doc2vec')

### test code
similar_doc = model.dv.most_similar(9788969525772)
print(similar_doc)