# neural_zodiac
A Feed-forward Neural Network trained to predict zodiac love compatibility.

Ignore [onehot](/onehot), this was the original approach before I realised [multihot](/multihot) was a better fitting idea. *Technically the term "multi-hot vector" means that you can specify more than one class at a time in the input vector, which is what the onehot approach in this code base allows, so technically the onehot version is a multihot vector and the multihot version is a multi-hot vector that allows a magnitude on each vector element/position.* Jargon!

A small scraper was made to scape the zodiac love compatibility percetages from [astrology-zodiac-signs.com](https://www.astrology-zodiac-signs.com) ([multihot/scraper](multihot/scraper/scraper.php)) the dataset generated was then used to train a neural network that has a onehot vector input, although I ended up using a "multihot" vector to represent multiple of each category, this fits better with say aries-aries compatibility as you just pass a 2 into the multihot vector at the aries position.

Technically this extrapolates the original dataset to compute polyamorous relationships.

The original dataset is probably nonsense, and the extrapolation is most certainly going to be nonsense++ so take these percetages with a pinch of salt or less.

Or maybe I just understated this network and the source data because honestly, after some testing, it seems to work pretty well if you think the original source data is agreeable. Heading over to the website [astrology-zodiac-signs.com](https://www.astrology-zodiac-signs.com), each compatibility gives a long readout, so it's pretty easy to verify if you agree with the reasoning behind the rating for each compatibility.

The only other way to have achieved an algorithm like this is to have manually computed an average, e.g., if I had a vector of 111000000000 that's aries, taurus, and gemini. I would need to write an algorithm to take these percentages from the [CSV](https://github.com/jcwml/neural_zodiac/blob/main/multihot/scraper/zodiacs.csv) and average them together:
```
aries-gemini,  74%
aries-taurus,  63%
taurus-gemini, 23%

(74+63+23) / 3 = 53.33%
```

Compare that to using the neural network:
```
Welcome to the Zodiac Love Compatibility Calculator.

In the relationship please tell me how many of each zodiac will be present.

How many Aries: 1
How many Taurus: 1
How many Gemini: 1
How many Cancer: 
How many Leo: 
How many Virgo: 
How many Libra: 
How many Scorpio: 
How many Sagittarius: 
How many Capricorn: 
How many Aquarius: 
How many Pisces: 

Input Vector: 111000000000

Compatibility: 51.26%
```

<details>
    <summary>A more in-depth example</summary>
    
```
Input Vector: 402010201001

Input Vector Components:
4x Aries
2x Gemini
1x Leo
2x Libra
1x Sagittarius
1x Pisces

---

Relationship Interactions:

aries-gemini, 74%
aries-gemini, 74%
aries-gemini, 74%
aries-gemini, 74%

aries-gemini, 74%
aries-gemini, 74%
aries-gemini, 74%
aries-gemini, 74%

aries-aries, 75%
aries-aries, 75%
aries-aries, 75%

aries-aries, 75%
aries-aries, 75%

aries-aries, 75%

aries-leo, 83%
aries-leo, 83%
aries-leo, 83%
aries-leo, 83%

aries-libra, 62%
aries-libra, 62%
aries-libra, 62%
aries-libra, 62%

aries-libra, 62%
aries-libra, 62%
aries-libra, 62%
aries-libra, 62%

aries-sagittarius, 87%
aries-sagittarius, 87%
aries-sagittarius, 87%
aries-sagittarius, 87%

aries-pisces, 29%
aries-pisces, 29%
aries-pisces, 29%
aries-pisces, 29%
    
gemini-gemini, 83%

gemini-leo, 82%
gemini-leo, 82%

gemini-libra, 78%
gemini-libra, 78%

gemini-libra, 78%
gemini-libra, 78%

gemini-sagittarius, 92%
gemini-sagittarius, 92%

gemini-pisces, 10%
gemini-pisces, 10%

leo-libra, 75%
leo-libra, 75%

leo-sagittarius, 75%

leo-pisces, 14%

libra-libra, 68%

libra-sagittarius, 71%
libra-sagittarius, 71%

sagittarius-pisces, 50%

Averaged Score:
(74*8) + (75*9) + (83*5) + (62*8) + (87*4) + (29*4) + (82*2) + (78*4) + (92*2) + (10*2) + (71*2) + 132 = 3596 
3596 / 53 = 67.84%

---

Neural Zodiac:

Welcome to the Zodiac Love Compatibility Calculator.

In the relationship please tell me how many of each zodiac will be present.

How many Aries: 4
How many Taurus: 
How many Gemini: 2
How many Cancer: 
How many Leo: 1
How many Virgo: 
How many Libra: 2
How many Scorpio: 
How many Sagittarius: 1
How many Capricorn: 
How many Aquarius: 
How many Pisces: 1

Input Vector: 402010201001

Compatibility: 70.45%
```
You can see that even under complex inputs the neural models holds up.

</details>
