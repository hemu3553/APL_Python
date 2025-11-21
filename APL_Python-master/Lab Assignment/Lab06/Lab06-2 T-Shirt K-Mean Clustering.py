# ----------------------------------------------------------------------------
#  * Python Programming for Data Scientists and Engineers
#  * LAB #6-2 Simple K-mean Clustering on T-Shirt Size
#  * #11 Chia-Hui Amy Lin
# ----------------------------------------------------------------------------

# Library
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np

# Import data from csv file using panda
dataframe = pd.read_csv("tshirts-H.csv")
dataframe_num = dataframe.drop(["name"], axis=1)
dataframe_num.head()

# K-mean Clustering with cluster size = 4
clustering = KMeans(n_clusters=4, init='k-means++', n_init=10)
clustering.fit(dataframe_num)

x = clustering.fit_predict(dataframe_num)
cluster = pd.Series(x)  # Cluster group series

dataframe_num = dataframe_num.assign(cluster=cluster.values)
print(dataframe_num)

# Split Dataframe into Clusters
first_group = dataframe_num[dataframe_num['cluster'] == 0]
second_group = dataframe_num[dataframe_num['cluster'] == 1]
third_group = dataframe_num[dataframe_num['cluster'] == 2]
fourth_group = dataframe_num[dataframe_num['cluster'] == 3]

# First Group height + weight
first_group_h = first_group['height (inches)'].tolist()
first_group_w = first_group['weight (pounds)'].tolist()
first_group_hMean = np.mean(first_group_h)
first_group_wMean = np.mean(first_group_w)

# Second Group height + weight
second_group_h = second_group['height (inches)'].tolist()
second_group_w = second_group['weight (pounds)'].tolist()
second_group_hMean = np.mean(second_group_h)
second_group_wMean = np.mean(second_group_w)

# Third Group height + weight
third_group_h = third_group['height (inches)'].tolist()
third_group_w = third_group['weight (pounds)'].tolist()
third_group_hMean = np.mean(third_group_h)
third_group_wMean = np.mean(third_group_w)

# Fourth Group height + weight
fourth_group_h = fourth_group['height (inches)'].tolist()
fourth_group_w = fourth_group['weight (pounds)'].tolist()
fourth_group_hMean = np.mean(fourth_group_h)
fourth_group_wMean = np.mean(fourth_group_w)

jet = plt.get_cmap('coolwarm')

# Scatter Plot Graph for 4 Clusters
first = plt.scatter(first_group_w, first_group_h, color='red', s=300, label="First Cluster")
plt.scatter(first_group_wMean, first_group_hMean, color='red', marker='x', s=500)

second = plt.scatter(second_group_w, second_group_h, color='blue', marker='p', s=300, label="Second Cluster")
plt.scatter(second_group_wMean, second_group_hMean, color='blue', marker='x', s=500)

third = plt.scatter(third_group_w, third_group_h, color='green', marker='^', s=300, label="Third Cluster")
plt.scatter(third_group_wMean, third_group_hMean, color='green', marker='x', s=500)

fourth = plt.scatter(fourth_group_w, fourth_group_h, color='orange', marker='*', s=300, label="Fourth Cluster")
plt.scatter(fourth_group_wMean, fourth_group_hMean, color='orange', marker='x', s=500)

# Title, x and y Label, Legend
plt.title("K-Mean on T-Shirt Size", fontsize=40)
plt.xlabel("Weight( lbs )", fontsize=20)
plt.ylabel("Height( inches )", fontsize=20)
plt.legend([first, second, third, fourth], ['First Cluster', 'Second Cluster', 'Third Cluster', 'Fourth Cluster'], fontsize=20)

# Output Graph
plt.show()



