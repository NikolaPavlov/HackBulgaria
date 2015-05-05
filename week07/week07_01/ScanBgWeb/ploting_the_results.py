from histogram import Histogram
import matplotlib.pyplot as mat_plt

FILENAME = 'results_from_scanner.txt'

histoG = Histogram()
histoG.add_to_histogram_from_file(FILENAME)
the_dict_for_ploting = histoG.get_dict()

keys = list(the_dict_for_ploting.keys())
values = list(the_dict_for_ploting.values())

X = list(range(len(keys)))
mat_plt.bar(X, values, align='center')
mat_plt.xticks(X, keys)
mat_plt.title('Servers')
mat_plt.xlabel('Server')
mat_plt.ylabel('Count')
mat_plt.savefig('histogram.png')
