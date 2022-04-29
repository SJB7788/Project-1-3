from PIL import Image
import os
import time


# function for user to input what image they want to view
def openImage():
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

# functions to save images that ends with .jpeg as .png into the /png images folder
def jpegToPng():
    for i in os.listdir('Password + Image Manipulation\image\jpeg images'):
        if i.endswith('.jpeg'):
            f = Image.open('Password + Image Manipulation\image\jpeg images' "/" + str(i))
            fn, fext = os.path.splitext(i)
            f.save('Password + Image Manipulation\image\png images\{}.png'.format(fn))







#----------------------------------------------Running Code-----------------------------------------------
"""
openImage()
while True:
    continOpen = input("\nWould you like to open another image? (Y/N): ").upper()
    if continOpen == 'Y':
        openImage()
    if continOpen == 'N':
        break
    else:
        print('Invalid Response')
        continue
"""
#jpegToPng()
