import time
from operator import itemgetter
from itertools import repeat


class NumerousAnts:

    def __init__(self, control_widget, widgets, inputs, iterations):
        self.control_widget = control_widget
        self.widgets = widgets
        self.iterations = iterations
        self.results = []
        self.inputs = inputs

    def perform(self, fun, *args):
        return fun(*args)

    def formicate(self):
        self.results = []
        for i in self.widgets:
            totaltime = 0
            for k in self.inputs:
                start = time.perf_counter()
                for _ in repeat(None, self.iterations):
                    z = self.perform(i[1], k)
                end = time.perf_counter()
                if z == self.perform(self.control_widget, k):
                    totaltime += end-start
                else:
                    totaltime = -1  # this is a problem
                    break
            self.results.append(totaltime)

    def resultput(self):
        l = [
            (
                self.widgets[i][0], self.results[i], self.results[i]/sum(self.results)*100
            ) for i, j in enumerate(self.results)
        ]
        for j in sorted(l, key=itemgetter(1)):
            print(j)
