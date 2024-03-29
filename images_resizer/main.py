import sys
from PIL import Image

# from https://stackoverflow.com/questions/44370469/python-image-resizing-keep-proportion-add-white-background
def resize(image_pil, width, height):
    '''
    Resize PIL image keeping ratio and using white background.
    '''
    ratio_w = width / image_pil.width
    ratio_h = height / image_pil.height
    if ratio_w < ratio_h:
        # It must be fixed by width
        resize_width = width
        resize_height = round(ratio_w * image_pil.height)
    else:
        # Fixed by height
        resize_width = round(ratio_h * image_pil.width)
        resize_height = height
    image_resize = image_pil.resize((resize_width, resize_height), Image.Resampling.LANCZOS)
    background = Image.new('RGBA', (width, height), (255, 255, 255, 255))
    offset = (round((width - resize_width) / 2), round((height - resize_height) / 2))
    background.paste(image_resize, offset)
    return background.convert('RGB')

def main(argv):
    # Convert images to 512x512 by keeping aspect ratio and adding whitespace
    print('start')
    for i in range(2191):
        ImageFilePath = str(i) + '.jpg'
        image = Image.open(ImageFilePath, 'r')
        image = resize(image, 512, 512)
        outputFilePath = './image512/' + str(i) + '_512.png'
        image.save(outputFilePath, 'PNG')
    print('done')

if __name__ == "__main__":
    main(sys.argv)