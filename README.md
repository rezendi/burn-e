# burn-e
Rather crude and simple (but fun) personal diffusion-model playground

`squares.py` takes JPGs in a `data/jpgs` directory and slices them into 400x400 chunks which go into `data/squares`. Then `go.py` uses the contents of the latter directory as a training set for a diffusion model.

A certain amount of `pip install` will be called for.
