# neural_zodiac
A Feed-forward Neural Network trained to predict zodiac love compatibility.

Ignore [onehot](/onehot), this was the original approach before I realised [multihot](/multihot) was a better fitting idea.

A small scraper was made to scape the zodiac love compatibility percetages from [astrology-zodiac-signs.com](https://www.astrology-zodiac-signs.com) ([multihot/scraper](multihot/scraper/scraper.php)) the dataset generated was then used to train a neural network that has a onehot vector input, although I ended up using a "multihot" vector to represent multiple of each category, this fits better with say aries-aries compatibility as you just pass a 2 into the multihot vector at the aries position.

Technically this extrapolates the original dataset to compute polyamorous relationships.

The original dataset is probably nonsense, and the extrapolation is most certainly going to be nonsense++ so take these percetages with a pinch of salt or less.

Or maybe I just understated this network and the source data because honestly, after some testing, it seems to work pretty well if you think the original source data is agreeable. Heading over to the website [astrology-zodiac-signs.com](https://www.astrology-zodiac-signs.com), each compatibility gives a long readout, so it's pretty easy to verify if you agree with the reasoning behind the rating for each compatibility.
