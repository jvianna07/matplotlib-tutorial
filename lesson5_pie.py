from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

slices=[60,40]
labels=['Sixty', 'Forty']
colors=['green', 'red']

# plt.pie(slices, labels=labels, colors=colors, explode=[.2,.1],
#         wedgeprops={'edgecolor':'black', 'width': 0.3, 'linewidth':1})
plt.pie(slices, labels=labels, colors=colors, explode=[.02,.01],radius=.5, center=(-3,2), frame=True,
        rotatelabels=False, startangle=90, counterclock=True, autopct='%1.1f%%')
plt.show()