# burn-e
Rather crude and simple (but fun) personal diffusion-model playground

`squares.py` takes JPGs in a `data/jpgs` directory and slices them into 400x400 chunks which are then resized to 64x64 and dropped into `data/squares`. Subsequently `go.py` uses the contents of the latter directory as a training set for a diffusion model.

A certain amount of `pip install` will be called for.
