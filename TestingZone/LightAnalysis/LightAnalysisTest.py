import math
import PIL
from PIL import Image, ImageStat

#From https://stackoverflow.com/questions/3490727/what-are-some-methods-to-analyze-image-brightness-using-python

def lightAnalysisTest(imageName):
    #Flashlight in front of camera: 247.43088462912542 (Approximately 250 Units)
    #Finger covering camera: 3.6265194813513904 (Approximately 0 Units)
    im = Image.open(imageName)
    stat = ImageStat.Stat(im)
    r,g,b = stat.mean
    Deos = (math.sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2))) * 0.3950913977
    return Deos

result = lightAnalysisTest('BlackTestingImage.jpg')
print("Black Image:",str(result), "Deos")

result = lightAnalysisTest('ThreeFourthsTestingImage.jpg')
print("Dark Grey Image:",str(result), "Deos")

result = lightAnalysisTest('HalfwayTestingImage.jpg')
print("Grey Image:",str(result), "Deos")

result = lightAnalysisTest('FourthTestingImage.jpg')
print("Light Grey Image:",str(result), "Deos")

result = lightAnalysisTest('WhiteTestingImage.jpg')
print("White Image:",str(result), "Deos")