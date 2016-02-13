# Name: Nancy Gomez
# Date: February 8, 2016
# Project: Images (Making a Man Dissapear)


#make a for loop that increments 9 times
#and stores all the pics in an array
pictures = []
for i in range(0,9):
  file = pickAFile()
  pic = makePicture(file)
  pictures.append(pic)

#obtain the height and width of the 1st picture in the array
height = getHeight(pictures[0])
width = getWidth(pictures[0])

#make an empty array for each color
redValues = []
greenValues = []
blueValues = []

#make an empty picture that will represent the end result
newPicture = makeEmptyPicture(width, height)

#making a function that will find the median of an unsorted array
def findMedian(unsortedArray):
  sortedArray = sorted(unsortedArray)
  lengthOfList = len(sortedArray)
  halfwayPoint = ((lengthOfList+1)/2)
  return sortedArray[halfwayPoint]

#increment through every pixel in the picture--
#for every picture in the list
for x in range(0,width):
  for y in range(0,height):
    for pic in range(0,9):
      pixel = getPixel(pictures[pic], x, y)
      
      #obtain the color values at each pixel
      redPixel = getRed(pixel)
      greenPixel = getGreen(pixel)
      bluePixel = getBlue(pixel)
      
      #add the values to the color arrays
      redValues.append(redPixel)
      greenValues.append(greenPixel)
      blueValues.append(bluePixel)
    
    #calculate median (my own function)
    redMedian = findMedian(redValues)
    greenMedian = findMedian(greenValues)
    blueMedian = findMedian(blueValues)
    
    #set the median values to the output image
    newPicPixel = getPixel(newPicture,x,y)
    
    setRed(newPicPixel, redMedian)
    setGreen(newPicPixel, greenMedian)
    setBlue(newPicPixel, blueMedian)
    
    #reset the arrays
    redValues = []
    greenValues = []
    blueValues = []
    

show(newPicture)
