import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use("ggplot")

import sklearn
from sklearn.decomposition import TruncatedSVD

ratings = pd.read_csv('ds.csv')
ratings = ratings.dropna()
# print(ratings.shape)

popular_products = pd.DataFrame(ratings.groupby('ProductId')['Rating'].count())
most_popular = popular_products.sort_values('Rating', ascending=False)
# print(most_popular.head(30))
most_popular.head(30).plot(kind='bar')
# plt.show()

ratings2 = ratings.head(10000)
ratings_utility_matrix = ratings2.pivot_table(values='Rating', index='UserId', columns='ProductId', fill_value=0)
X = ratings_utility_matrix.T
# print(X.shape) # 886 user x 9697 items


SVD = TruncatedSVD(n_components=10) #Decomposizione ai valori singolari
decomposed_matrix = SVD.fit_transform(X)
# print(decomposed_matrix)
correlation_matrix = np.corrcoef(decomposed_matrix)

# plt.matshow(correlation_matrix)

f = plt.figure(figsize=(19, 15))
plt.matshow(correlation_matrix, fignum=f.number)
cb = plt.colorbar()
cb.ax.tick_params(labelsize=14)
plt.title('Correlation Matrix', fontsize=16)
plt.show()







i = X.index[99] #id dello user 99

product_names = list(X.index)
product_ID = product_names.index(i)
correlation_product_ID = correlation_matrix[product_ID]
Recommend = list(X.index[correlation_product_ID > 0.90])
# Removes the item already bought by the customer
Recommend.remove(i)
print(Recommend[0:9])