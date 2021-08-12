from PIL import Image, ImageSequence

_gif = input("Name of gif file?")
_png = input("Name of png file?")
_output_name = input("What do you want to name your output?")

frames = []
animated_gif = Image.open(_gif)
extend = Image.open(_png)

for frame in ImageSequence.Iterator(animated_gif):
    frame = frame.copy()
    frames.append(frame)

for x in range(50):
    frames.append(extend)

frames[0].save(_output_name, save_all=True, append_images=frames[1:])