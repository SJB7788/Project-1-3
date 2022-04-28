from PIL import Image
import os

# opens an image
"""
openApple = Image.open(r'Password + Image Manipulation\image\jpeg images\apple jpeg.jpeg')
openApple.show()
"""
# saves images that ends with .jpeg as .png into the /png images folder
"""
for i in os.listdir('Password + Image Manipulation\image\jpeg images'):
    if i.endswith('.jpeg'):
        f = Image.open('Password + Image Manipulation\image\jpeg images' "/" + str(i))
        fn, fext = os.path.splitext(i)
        f.save('Password + Image Manipulation\image\png images\{}.png'.format(fn))
"""
