from tokenize import Number
from PIL import Image, ImageFilter
import os
import time

"""
I made one big file of all the functions of each feature
At the bottom of the file, there is a running code section with all the functions already written down
Run the function as needed
One thing to note:
    The png folder is empty as there is a function to turn the jpeg files to png. So if you want to view image of the png 
    folder, you will have to convert jpeg to png first and then view png file
"""

# function for user to input what image they want to view
# Jpeg folder
def openImageJpeg():
    jpegList = [] #this while true statement is copied and pasted in every function. very useful honestly
    #i thought of making this section a function to make the code shroter but i assumed that the userOpen variable would not work
    #outside of that function and wouldn't translate over to the function its being called in. not sure if i am wrong but if I
    #am, i just wasted like 50+ lines of code space for no reason
    while True:
        time.sleep(1)
        for i in os.listdir('Password + Image Manipulation\image\jpeg images'):
            print(i)
            jpegList.append(i) # makes a list to the if statement later to make sure user inputs a picture thats in the foler
        time.sleep(1)
        userOpen = input('\nWhich images would you like to open and view?: ').lower()
        if userOpen in (jpegList): #if user input is in the jpegList
            break
        else: 
            print("\nInvalid Input\n")
            continue

    open = Image.open('Password + Image Manipulation\image\jpeg images\{}'.format(userOpen))
    open.show()

    while True:
        continOpen = input("\nWould you like to open another image? (Y/N): ").upper()
        if continOpen == 'Y':
            openImageJpeg()
        if continOpen == 'N':
            print("")
            break
        else:
            print('Invalid Response')
            continue

# Png folder
def openImagePng():
    pngList = [] 
    while True:
        time.sleep(1)
        for i in os.listdir('Password + Image Manipulation\image\png images'):
            print(i)
            pngList.append(i) # makes a list to the if statement later to make sure user inputs a picture thats in the foler
        if len(os.listdir('Password + Image Manipulation\image\png images')) == 0:
            print("The folder is empty!")
            break
        time.sleep(1)
        userOpen = input('\nWhich images would you like to open and view?: ').lower()
        if userOpen in (pngList): #if user input is in the jpegList
            open = Image.open('Password + Image Manipulation\image\png images\{}'.format(userOpen))
            open.show()
            break
        else: 
            print("\nInvalid Input\n")
            continue
   

    while True:
        continOpen = input("\nWould you like to open another image? (Y/N): ").upper()
        if continOpen == 'Y':
            openImagePng()
        if continOpen == 'N':
            print("")
            break
        else:
            print('Invalid Response')
            continue

# functions to save images that ends with .jpeg as .png into the /png images folder
def jpegToPng():
    for i in os.listdir('Password + Image Manipulation\image\jpeg images'):
        if i.endswith('.jpeg'):
            f = Image.open('Password + Image Manipulation\image\jpeg images' "/" + str(i))
            fn, fext = os.path.splitext(i)
            f.save('Password + Image Manipulation\image\png images\{}.png'.format(fn))
    
    print("Saved all images to png folder\n")

# function for thumbnails
def thumbnail():
    jpegList = [] 
    listOfSize = ((200,200), (400,400), (600,600)) # list of sizes of thumbnail 
    while True:
        time.sleep(1)
        for i in os.listdir('Password + Image Manipulation\image\jpeg images'):
            print(i)
            jpegList.append(i) 
        time.sleep(1)
        userOpen = input('\nWhich images would you like to make a thumbnail?: ').lower()
        if userOpen in (jpegList): 
            break
        else: 
            print("\nInvalid Input\n")
            continue
    
    thumbnailImage = Image.open('Password + Image Manipulation\image\jpeg images\{}'.format(userOpen))

    while True: #this while statement should be straightforward i hope
        userSize = input("What size do you want the thumbnail to be? (200, 400 or 600): ")
        if userSize == '200':
            thumbnailImage.thumbnail(listOfSize[0]) # gets index 0 for the list "list of size" which is (200,200)
            thumbnailImage.save('Password + Image Manipulation/image/200/{}'.format("200 " + userOpen))
            print("Saved to folder 200")
            break
        if userSize == '400':
            thumbnailImage.thumbnail(listOfSize[1])
            thumbnailImage.save('Password + Image Manipulation/image/400/{}'.format("400 " + userOpen))
            print("Saved to folder 400")
            break
        if userSize == '600':
            thumbnailImage.thumbnail(listOfSize[2])
            thumbnailImage.save('Password + Image Manipulation/image/600/{}'.format("600 " + userOpen))
            print("Saved to folder 600")
            break
        else:
            print("Invalid Input")
            continue
    
    while True: #asking for repeat
        repeatRequest = input("Would you like to edit again? (Y/N): ").upper()
        if repeatRequest == "Y":
            thumbnail()
            break
        if repeatRequest == "N":
            print("")
            break
        if repeatRequest == "YO": #easter egg i guess lol
            print("Yo how you doin'\n")
            continue
        else:
            print("Invalid Input\n")
            continue

# rotate images, show and save
def rotation():
    jpegList = []
    while True:
        time.sleep(1)
        for i in os.listdir('Password + Image Manipulation\image\jpeg images'):
            print(i)
            jpegList.append(i) 
        time.sleep(1)
        userOpen = input('\nWhich images would you like to rotate?: ').lower()
        if userOpen in (jpegList): 
            break
        else: 
            print("\nInvalid Input\n")
            continue

    selectImage = Image.open('Password + Image Manipulation\image\jpeg images\{}'.format(userOpen))

    while True: #this while true statement should be straightforward
        userDegree = input("By what degree would you like to rotate the image? (90, 180, 270): ")
        if userDegree == '90':
            rotatedImage = selectImage.transpose(Image.ROTATE_90)
            rotatedImage.save('Password + Image Manipulation/image/rotated images/{}'.format('rotated 90 ' + userOpen))
            break
        if userDegree == '180':
            rotatedImage = selectImage.transpose(Image.ROTATE_180)
            rotatedImage.save('Password + Image Manipulation/image/rotated images/{}'.format('rotated 180' + userOpen))
            break
        if userDegree == '270':
            rotatedImage = selectImage.transpose(Image.ROTATE_270)
            rotatedImage.save('Password + Image Manipulation/image/rotated images/{}'.format('rotated 270' + userOpen))
            break
        else: 
            print("Invalid Input") 
            continue
    rotatedImage.show()

    while True: #asking for repeat
        repeatRequest = input("Would you like to edit again? (Y/N): ").upper()
        if repeatRequest == "Y":
            rotation()
            break
        if repeatRequest == "N":
            print("")
            break
        if repeatRequest == "MOO":
            print("Cow\n")
            continue
        else:
            print("Invalid Input\n")
            continue

# black and white
def blackAndWhite():
    jpegList = []
    while True:
        time.sleep(1)
        for i in os.listdir('Password + Image Manipulation\image\jpeg images'):
            print(i)
            jpegList.append(i) 
        time.sleep(1)
        userOpen = input('\nWhich images would you like to change colors?: ').lower()
        if userOpen in (jpegList): 
            break
        else: 
            print("\nInvalid Input\n")
            continue
    
    selectImage = Image.open('Password + Image Manipulation\image\jpeg images\{}'.format(userOpen))
    selectImage = selectImage.convert("L")
    selectImage.save('Password + Image Manipulation/image/black and white/{}'.format('black and white ' + userOpen))
    selectImage.show()

    while True: #asking for repeat 
        repeatRequest = input("Would you like to edit again? (Y/N): ").upper()
        if repeatRequest == "Y":
            blackAndWhite()
            break
        if repeatRequest == "N":
            print("")
            break
        if repeatRequest == "E": #easter egg i guess lol
            for i in range(5):
                print("E")
            continue
        else:
            print("Invalid Input\n")
            continue

# blur images
def blur():
    jpegList = []
    while True:
        time.sleep(1)
        for i in os.listdir('Password + Image Manipulation\image\jpeg images'):
            print(i)
            jpegList.append(i) 
        time.sleep(1)
        userOpen = input('\nWhich images would you like to blur?: ').lower()
        if userOpen in (jpegList): 
            break
        else: 
            print("\nInvalid Input\n")
            continue

    selectImage = Image.open('Password + Image Manipulation\image\jpeg images\{}'.format(userOpen))
    while True:
        try: #try statement very cool, uses error message like an if else value
            userRadius = int(input("By how much do you want the image to be blurred? (1-10): "))
            break
        except ValueError:
            print("Invalid Input")
        #originally was going to make a number list from 0-9 and do a if else statement on if userRadius had at least one value
        #from the number list but that wouldve been a mess and turns out try statement is a thing very cool. i think i tried
        #using it once. dont remember if it worked or not but is still very cool

    blurImage = selectImage.filter(ImageFilter.GaussianBlur(radius = userRadius))
    blurImage.show() 
    blurImage.save('Password + Image Manipulation/image/blur/{}'.format('blurred ' + userOpen))

    while True: #asking for repeat 
        repeatRequest = input("Would you like to edit again? (Y/N): ").upper()
        if repeatRequest == "Y":
            blur()
            break
        if repeatRequest == "N":
            print("")
            break
        if repeatRequest == "A": #easter egg i guess lol
            print("shark")
        else:
            print("Invalid Input\n")
            continue

# * sharpen *
def sharp():
    jpegList = []
    while True:
        time.sleep(1)
        for i in os.listdir('Password + Image Manipulation\image\jpeg images'):
            print(i)
            jpegList.append(i) 
        time.sleep(1)
        userOpen = input('\nWhich images would you like to sharpen?: ').lower()
        if userOpen in (jpegList): 
            break
        else: 
            print("\nInvalid Input\n")
            continue
    selectImage = Image.open('Password + Image Manipulation\image\jpeg images\{}'.format(userOpen))

    sharpImage = selectImage.filter(ImageFilter.SHARPEN) #Sharp once
    for i in range(3): #Sharp three more times >:D
        sharpImage = sharpImage.filter(ImageFilter.SHARPEN)
    sharpImage.show()
    sharpImage.save('Password + Image Manipulation/image/sharp/{}'.format('sharpened ' + userOpen))

    while True: #asking for repeat 
        repeatRequest = input("Would you like to edit again? (Y/N): ").upper()
        if repeatRequest == "Y":
            sharp()
            break
        if repeatRequest == "N":
            print("")
            break
        if repeatRequest == "SHARP": #easter egg i guess lol
            print("SHARP")
            continue
        else:
            print("Invalid Input\n")
            continue


#-------------------------------------------------Running Code---------------------------------------------------

"""
List of Functions:

openImageJpeg() => open images in jpeg folder
jpegToPng() => convert jpeg to png
openImagePng() => open images in png folder
thumbnail() => make thumbnail according to user's requested size
rotation() => rotate an image
blackAndWhite() => turn image black and white
blur() => blur an image
sharp() => sharpen an image
"""
openImageJpeg()
