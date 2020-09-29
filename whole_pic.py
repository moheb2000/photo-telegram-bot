from PIL import Image # import Image from pillow module for rendering pictures
from os import scandir, remove # import some method from os module


# Create main function for rendering whole_photo
def create_whole_pic():

    # photo x, y size
    x = 3000
    y = 1500

    # Create a list from all pictures in download directory
    imgList = ['./download/' + n.name for n in scandir('./download/')]

    # count = number of all pictures
    count = len(imgList)

    # number of rows and columns in final whole_pic
    row = 1
    col = 2

    # Create rows and columns numbers
    while True:
        if count < row * col:
            break
        row += 1
        col = 2 ** row

    # side of an indivitual image
    side = y // row

    # open base pic
    pic = Image.open('test.jpg')

    # open mask image
    mycover = Image.open('mycover.png')

    index = 0

    # loops for rendering final pic
    for i in range(row):
        for j in range(col):
            myimg = Image.open(imgList[index])
            index += 1
            if index >= len(imgList):
                index = 0
            myimg.thumbnail((side, side))
            pic.paste(myimg, (j * side, i * side))

    # save pic without mask
    pic.save('new_test.jpg', 'JPEG')

    # mask for final pic
    pic = Image.open('test.jpg')
    newImage = Image.open('new_test.jpg')
    pic.paste(newImage, (0, 0), mycover)
    pic.save('whole_pic.jpg', 'JPEG')

    # remove new_test.jpg that have not mask
    remove('./new_test.jpg')
