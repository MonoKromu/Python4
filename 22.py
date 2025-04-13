def fractal_print(fractal):
    print([i for i in fractal])


fr = []
fr += [1, fr, 2, fr, 3]
fractal_print(fr)
