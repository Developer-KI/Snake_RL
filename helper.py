import matplotlib.pyplot as plt
from IPython import display
from datetime import datetime
import os
import atexit

plt.ion()


def plot(scores, mean_scores):
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()
    plt.title('Training...')
    plt.xlabel('Number of Games')
    plt.ylabel('Score')
    plt.plot(scores)
    plt.plot(mean_scores)
    plt.ylim(ymin=0)
    plt.text(len(scores)-1, scores[-1], str(scores[-1]))
    plt.text(len(mean_scores)-1, mean_scores[-1], str(mean_scores[-1]))
    plt.show(block=False)
    plt.pause(.1)


def exit_handler():
    file_name = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    graph_folder_path = './graph'
    if not os.path.exists(graph_folder_path):
        os.makedirs(graph_folder_path)

    file_name = os.path.join(graph_folder_path, file_name)
    plt.savefig(file_name)


atexit.register(exit_handler)
