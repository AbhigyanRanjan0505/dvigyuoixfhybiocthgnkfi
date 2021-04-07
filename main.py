import plotly.figure_factory as figure_factory
import statistics
import random
import pandas

df = pandas.read_csv("data.csv")
data = df["reading_time"].tolist()

population_mean = statistics.mean(data)
print("Population mean :", population_mean)


def show_fig(mean_list):
    df = mean_list
    fig = figure_factory.create_distplot(
        [df], ["reading_time"], show_hist=False)
    fig.show()


def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data))
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean


def setup():
    mean_list = []
    for i in range(0, 100):
        set_of_means = random_set_of_mean(30)
        mean_list.append(set_of_means)

    show_fig(mean_list)

    mean = statistics.mean(mean_list)
    print("Sampling mean :", mean)


setup()
