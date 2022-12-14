from sys import path
path.append('../src')
from database import Database
from image import PartImage
import os

db = Database(os.environ['databaseURL'])

path_images = './drawing/images/A'
part = db.get_part_by_id('1001')

# get all images in the folder
files = os.listdir(path_images)

for file in files:
    if file.endswith('txt'):
        continue

    file = os.path.join(path_images, file)

    triangles_file = file.replace('.png', '.txt')
    triangles = []
    with open(triangles_file, 'r') as f:
        for line in f:
            line = line.strip('\n')
            line = line.split(',')
            x = int(line[0])
            y = int(line[1])
            triangles.append((x, y))

    image = PartImage(file, triangles, part, True)
    image.rotate_part()
    image.draw_quadrants()
    image.show()
    image.get_cropped_holes()

    image.close()
