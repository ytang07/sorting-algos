import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import random
from time import sleep

def quicksort(array, start, end):
    if start >= end:
        return
    pivot = array[start]
    swap = start
    for i in range(start+1, end+1):
        if array[i] <= pivot:
            swap += 1
            array[swap], array[i] = array[i], array[swap]
        yield array
    array[start], array[swap],  = array[swap], array[start]
    yield array

    yield from quicksort(array, start, swap-1)
    yield from quicksort(array, swap+1, end)

def animate(array):
    n = len(array)
    generator = quicksort(array, 0, n-1)

    fig, ax = plt.subplots()
    bar_rects = ax.bar(range(n), array, align="edge")

    ax.set_title("Quicksort")

    text = ax.text(0.01, 0.95, "", transform = ax.transAxes)
    iteration = [0]
    def animate(array, rects, iteration):
        for rect, val in zip(rects, array):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text(f"iterations: {iteration[0]}")
    
    anim = FuncAnimation(fig, func=animate,
        fargs=(bar_rects, iteration), frames=generator, interval=10, 
        repeat=False, save_count=1000)
    # writer = PillowWriter(fps=30)
    # anim.save("quicksort.gif", writer=writer)
    plt.show()

array = [i for i in range(100)]
random.shuffle(array)
animate(array)