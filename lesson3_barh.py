import csv
from matplotlib import pyplot as plt
import numpy as np
from collections import Counter

plt.style.use("fivethirtyeight")
data='datas/data.csv'

with open(data) as csv_file:
    csv_reader = csv.DictReader(csv_file)

    language_counter = Counter()

    for row in csv_reader:
        language_counter.update(row['LanguagesWorkedWith'].split(';'))

language=[]
popularity=[]
for item in language_counter.most_common(15):
    language.append(item[0])
    popularity.append(item[1])


# print(language)
# print(popularity)

language.reverse()
popularity.reverse()

plt.barh(language, popularity)
plt.title("Most popular programming languages")
# plt.ylabel("Programming language")
plt.xlabel("Number of people who use")
# plt.legend()
plt.tight_layout()
plt.show()