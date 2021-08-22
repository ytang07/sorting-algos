import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import random

def insertion_sort(_list):
    for i in range(1, len(_list)):
        j = i-1
        next = _list[i]
        while _list[j] > next and j >= 0:
            _list[j+1] = _list[j]
            j -= 1
        _list[j+1] = next
        yield _list

def animate(_list):
    n = len(_list)
    generator = insertion_sort(_list)
    fig, ax = plt.subplots()
    ax.set_title("insertion sort")

    bar_rects = ax.bar(range(len(_list)), _list, align="edge")  
    ax.set_xlim(0, n)
    ax.set_ylim(0, int(1.1*n))
    text = ax.text(0.01, 0.95, "", transform = ax.transAxes)
    iteration = [0]
    def _animate(array, rects, iteration):
        for rect, val in zip(rects, array):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text(f"iterations: {iteration[0]}")
    
    anim = FuncAnimation(fig, func=_animate,
        fargs=(bar_rects, iteration), frames=generator, interval=10, 
        repeat=False, save_count=150)
    # writer = PillowWriter(fps=30)
    # anim.save("insertionsort.gif", writer=writer)
    plt.show()

array = [i for i in range(100)]
random.shuffle(array)
animate(array)