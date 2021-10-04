import pandas

class Util:
    def sum(self, gdata) -> pandas.Series:
        return gdata.sum()

    def sort(self, data: pandas.Series, asc:bool=False) -> pandas.Series:
        return data.sort_values(ascending=asc)

    def mean(self, gdata) -> pandas.Series:
        return gdata.mean()

