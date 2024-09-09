from PIL import Image, ImageEnhance, ImageFilter

with Image.open("Images/sample-1.png") as picture:
    # picture.show()
    
    black_white = picture.convert("L")
    black_white.save("Images/black-white.png")
    
    mirror = picture.transpose(Image.FLIP_LEFT_RIGHT)
    mirror.save("Images/mirror.png")
    
    blur = picture.filter(ImageFilter.BLUR)
    blur.save("Images/blur.png")
    
    #Image Enhance
    contrast = ImageEnhance.Contrast(picture)
    picture = contrast.enhance(2.5)
    picture.save("Images/contrast.png")
    
    color = ImageEnhance.Color(picture).enhance(2.5)
    color.save("Images/color.png")
    
    #image filter
    filter = picture.filter(ImageFilter.EDGE_ENHANCE)
    filter.save("Images/filter.png")
    
    