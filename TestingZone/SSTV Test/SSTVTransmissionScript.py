import winsound
from PIL import Image
from pysstv.color import Robot36
baseImage = Image.open(r'C:\Users\hubba\Documents\GitHub\SSTV-and-Data-Transmission\TestingZone\SSTV Test\maxresdefault.jpg')
baseImage = baseImage.resize((Robot36.WIDTH, Robot36.HEIGHT))
sstv = Robot36(baseImage, 44100, 16)
sstv.write_wav('NASASEES.wav')
filename = 'NASASEES.wav'
winsound.PlaySound(filename, winsound.SND_FILENAME)
