import random


# generate spawn locations of side items, ensure they remain on screen
def spawn(img_x, img_y, width, height):
    x = random.randint(img_x, width - img_x)
    y = random.randint(img_y, height - img_y)

    return x, y


# check to see if character has touched an item
def collide(obj1, obj2):
    offset_x = obj2.x_pos - obj1.x_pos
    offset_y = obj2.y_pos - obj1.y_pos
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) is not None


# reward character for finding item
def found_item(found):
    pass



