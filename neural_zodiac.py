# github.com/jcwml
import os
from tensorflow import keras

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

def getFloat():
    i = input()
    if i == '':
        return 0.0
    return float(i)

def istr(i):
    return str(int(i))

print("Welcome to the Zodiac Love Compatibility Calculator.\n\nIn the relationship please tell me how many of each zodiac will be present.\n")

print("How many Aries: ", end='')
aries = getFloat()
print("How many Taurus: ", end='')
taurus = getFloat()
print("How many Gemini: ", end='')
gemini = getFloat()
print("How many Cancer: ", end='')
cancer = getFloat()
print("How many Leo: ", end='')
leo = getFloat()
print("How many Virgo: ", end='')
virgo = getFloat()
print("How many Libra: ", end='')
libra = getFloat()
print("How many Scorpio: ", end='')
scorpio = getFloat()
print("How many Sagittarius: ", end='')
sagittarius = getFloat()
print("How many Capricorn: ", end='')
capricorn = getFloat()
print("How many Aquarius: ", end='')
aquarius = getFloat()
print("How many Pisces: ", end='')
pisces = getFloat()

model = keras.models.load_model("/home/v/Desktop/neural_zodiac/multihot/models/model_tanh_adam_6_32_24_12500_a0.000001/tanh_adam_6_32_24_12500_a0.000001/")
r = model.predict([[aries, taurus, gemini, cancer, leo, virgo, libra, scorpio, sagittarius, capricorn, aquarius, pisces]], verbose=0)
print("\nInput Vector: " + istr(aries) + istr(taurus) + istr(gemini) + istr(cancer) + istr(leo) + istr(virgo) + istr(libra) + istr(scorpio) + istr(sagittarius) + istr(capricorn) + istr(aquarius) + istr(pisces))
print("\nCompatibility: " + "{:.2f}".format(r.flatten()[0]) + '%' + "\n")
