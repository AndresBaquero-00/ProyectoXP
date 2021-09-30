import matplotlib.pyplot as plt
import numpy as np

class Charts:
    def horizontal_bar(self, x: list, y: list, xlabel: str):
        fig, ax = plt.subplots()

        y_pos = np.arange(len(x))

        ax.barh(y_pos, y, align = 'center')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(x)
        ax.invert_yaxis()
        ax.set_xlabel(xlabel)

        plt.show()

    def pie_chart(self, labels: list, sizes: list, title: str):
        fig, ax = plt.subplots()
        ax.pie(sizes, None, labels = labels, autopct = '%1.1f%%', startangle = 90)
        ax.set(aspect = 'equal', title = title)

        plt.show()

