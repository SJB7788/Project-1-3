from PIL import Image
import os
import time


# function for user to input what image they want to view
# Jpeg folder
def openImageJpeg():
    jpegList = [] 
    while True:
        time.sleep(1)
        for i in os.listdir('Password + Image Manipulation\image\jpeg images'):
            print(i)
            jpegList.append(i) # makes a list to the if statement later to make sure user inputs a picture thats in the foler
        time.sleep(1)
        userOpen = input('\nWhich images would you like to open and view?: ')
        if userOpen in (jpegList): #if user input is in the jpegList
            break
        else: 
            print("\nInvalid Input\n")
            continue
    open = Image.open('Password + Image Manipulation\image\jpeg images\{}'.format(userOpen))
    open.show()
# Png folder
def openImagePng():
    pngList = [] 
    while True:
        time.sleep(1)
        for i in os.listdir('Password + Image Manipulation\image\png images'):
            print(i)
            pngList.append(i) # makes a list to the if statement later to make sure user inputs a picture thats in the foler
        time.sleep(1)
        userOpen = input('\nWhich images would you like to open and view?: ')
        if userOpen in (pngList): #if user input is in the jpegList
            break
        else: 
            print("\nInvalid Input\n")
            continue
    open = Image.open('Password + Image Manipulation\image\png images\{}'.format(userOpen))
    open.show()

# functions to save images that ends with .jpeg as .png into the /png images folder
def jpegToPng():
    for i in os.listdir('Password + Image Manipulation\image\jpeg images'):
        if i.endswith('.jpeg'):
            f = Image.open('Password + Image Manipulation\image\jpeg images' "/" + str(i))
            fn, fext = os.path.splitext(i)
            f.save('Password + Image Manipulation\image\png images\{}.png'.format(fn))

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
        userOpen = input('\nWhich images would you like to make a thumbnail?: ')
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

def rotation():
    ()






#----------------------------------------------Running Code-----------------------------------------------
"""
openImageJpeg()
while True:
    continOpen = input("\nWould you like to open another image? (Y/N): ").upper()
    if continOpen == 'Y':
        openImageJpeg()
    if continOpen == 'N':
        break
    else:
        print('Invalid Response')
        continue
"""
"""
openImagePng()
while True:
    continOpen = input("\nWould you like to open another image? (Y/N): ").upper()
    if continOpen == 'Y':
        openImagePng()
    if continOpen == 'N':
        break
    else:
        print('Invalid Response')
        continue
"""   
#jpegToPng()
#thumbnail()
