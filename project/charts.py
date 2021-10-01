from matplotlib.figure import Figure
import numpy as np
import base64, io

class Charts:
    figure: Figure
    
    def horizontal_bar(self, x: list, y: list, xlabel: str) -> str:
        self.figure = Figure()
        ax = self.figure.subplots()
        y_pos = np.arange(len(x))
        ax.barh(y_pos, y, align = 'center')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(x)
        ax.invert_yaxis()
        ax.set_xlabel(xlabel)

        return self.save_fig()

    def pie_chart(self, labels: list, sizes: list, title: str) -> str:
        self.figure = Figure()
        ax = self.figure.subplots()
        ax.pie(sizes, None, labels = labels, autopct = '%1.1f%%', startangle = 90)
        ax.set(aspect = 'equal', title = title)
        # plt.show()
        return self.save_fig()
        
    def save_fig(self) -> str:
        img = io.BytesIO()
        self.figure.savefig(img, format = 'png')
        plot = base64.b64encode(img.getbuffer()).decode('ascii')
        return f"<img src='data:image/png;base64,{plot}'/>"
        
        

