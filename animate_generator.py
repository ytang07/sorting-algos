import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

def animate(_list, generator, title, save, save_frames=1000):
    n = len(_list)
    fig, ax = plt.subplots()
    ax.set_title(title)

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
        repeat=False, save_count=save_frames)
    if save:
        writer = PillowWriter(fps=30)
        anim.save(title + ".gif", writer=writer)
    plt.show()