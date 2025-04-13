def defractalize(fractal):
    while fractal in fractal:
        fractal.remove(fractal)


fr = [0]
fr.append(fr)
defractalize(fr)
print(fr)
