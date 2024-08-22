from PIL import Image, ImageEnhance, ImageFilter
import os

path = "./imgs" # folder for unedited images
pathOut = "./editedImgs" # folder for edited images

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")
    
    edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(-90) # edit the image, for example by applying a filter, converting it to grayscale and rotating it
    
    factor = 1.5 # factor by which the brightness will
    enhancer = ImageEnhance.Brightness(edit) # create an enhancer object
    edit = enhancer.enhance(factor) # enhance the image
    
    clean_name = os.path.splitext(filename)[0] # get the name of the image without the extension

    edit.save(f'{pathOut}/{clean_name}_edited.jpg') # save the edited image in the output folder
    