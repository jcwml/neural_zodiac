# neural_zodiac
A Feed-forward Neural Network trained to predict zodiac love compatibility.

Ignore [onehot](/onehot).

A small scraper was made to scape the zodiac love compatibility percetages from astrology-zodiac-signs.com [multihot/scraper](multihot/scraper) the dataset generated was then used to train a neural network that has a onehot vector input, although I ended up using a "multihot" vector to represent multiple of each category, this fits better with say aries-aries compatibility as you just pass a 2 into the multihot vector at the aries position.

Technically this extrapolates the dataset to compute polyamorous relationships.

The original dataset is probably nonsense, and the extrapolation is most certainly going to be nonsense++ so take these percetages with a pinch of salt or less.
