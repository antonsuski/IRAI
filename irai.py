# Import neccessary libs
from PIL import Image
import numpy as np
import matplotlib.pyplot as mat_pyplot
import time
from collections import Counter

def threshold(image_buffer):
    from statistics import mean
    balanceAr = []
    newAr = image_buffer

    for eachRow in image_buffer:
        for eachPix in eachRow:
            avgNum = mean(eachPix[:3])
            balanceAr.append(avgNum) 

    balance = mean(balanceAr)
    for eachRow in newAr:
        for eachPix in eachRow:
            if mean(eachPix[:3]) > balance:
                eachPix[0] = 255
                eachPix[1] = 255
                eachPix[2] = 255
                eachPix[3] = 255
            else:
                eachPix[0] = 0
                eachPix[1] = 0
                eachPix[2] = 0
                eachPix[3] = 255
    return newAr

def createExamples():
    numberArrayExamples = open('numArEx.txt','a')
    numbersWeHave = range(1,10)
    for eachNum in numbersWeHave:
        #print eachNum
        for furtherNum in numbersWeHave:
            # you could also literally add it *.1 and have it create
            # an actual float, but, since in the end we are going
            # to use it as a string, this way will work.
            print(str(eachNum)+'.'+str(furtherNum))
            imgFilePath = 'images/numbers/'+str(eachNum)+'.'+str(furtherNum)+'.png'
            ei = Image.open(imgFilePath)
            eiar = np.array(ei)
            eiarl = str(eiar.tolist())

            print(eiarl)
            lineToWrite = str(eachNum)+'::'+eiarl+'\n'
            numberArrayExamples.write(lineToWrite)

def whatNumIsThis(filePath):
    matchedAr = []
    loadExamps = open('numArEx.txt','r').read()
    loadExamps = loadExamps.split('\n')
    
    i = Image.open(filePath)
    iar = np.array(i)
    iarl = iar.tolist()
    inQuestion = str(iarl)
    for eachExample in loadExamps:
        try:
            splitEx = eachExample.split('::')
            currentNum = splitEx[0]
            currentAr = splitEx[1]
            
            eachPixEx = currentAr.split('],')
            eachPixInQ = inQuestion.split('],')
            x = 0
            while x < len(eachPixEx):
                if eachPixEx[x] == eachPixInQ[x]:
                    matchedAr.append(int(currentNum))
                x+=1
        except Exception as e:
            print(str(e))

    print(matchedAr)
    x = Counter(matchedAr)
    print(x)
    graphX = []
    graphY = []

    ylimi = 0

    for eachThing in x:
        graphX.append(eachThing)
        graphY.append(x[eachThing])
        ylimi = x[eachThing]



    fig = mat_pyplot.figure()
    ax1 = mat_pyplot.subplot2grid((4,4),(0,0), rowspan=1, colspan=4)
    ax2 = mat_pyplot.subplot2grid((4,4),(1,0), rowspan=3,colspan=4)
    
    ax1.imshow(iar)
    ax2.bar(graphX,graphY,align='center')
    mat_pyplot.ylim(400)
    
    xloc = mat_pyplot.MaxNLocator(12)
    ax2.xaxis.set_major_locator(xloc)

    mat_pyplot.show()
# image_1 = Image.open("images/numbers/0.1.png")
# image_2 = Image.open("images/numbers/y0.4.png")
# image_3 = Image.open("images/numbers/y0.5.png")
# image_4 = Image.open("images/sentdex.png")

# # Save as buffer of RGBA(RED, GREEN, BLUE, ALPHA) bytes
# im_buffer_1 = np.array(image_1)
# im_buffer_2 = np.array(image_2)
# im_buffer_3 = np.array(image_3)
# im_buffer_4 = np.array(image_4)

# # Processing image
# im_buffer_2 = threshold(im_buffer_2)
# im_buffer_3 = threshold(im_buffer_3)
# im_buffer_4 = threshold(im_buffer_4)

# # Set up mat_pyplot grid
# fig = mat_pyplot.figure()
# ax1 = mat_pyplot.subplot2grid((8,6),(0,0), rowspan=4, colspan=3)
# ax2 = mat_pyplot.subplot2grid((8,6),(4,0), rowspan=4, colspan=3)
# ax3 = mat_pyplot.subplot2grid((8,6),(0,3), rowspan=4, colspan=3)
# ax4 = mat_pyplot.subplot2grid((8,6),(4,3), rowspan=4, colspan=3)

# # Prepare image for showing
# ax1.imshow(im_buffer_1)
# ax2.imshow(im_buffer_2)
# ax3.imshow(im_buffer_3)
# ax4.imshow(im_buffer_4)

# # Print image buffer
# #print(im_buffer_1)

# # Show image
# mat_pyplot.show()

# createExamples()

whatNumIsThis('images/test.png')
