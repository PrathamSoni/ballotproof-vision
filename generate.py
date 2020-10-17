from PIL import Image
import json
from glob import glob
from collections import Counter
import random

ballot1 = Image.open("examples\\SampleBallot-1.png")
json1 = json.load(open("AZ-5-1.json","r+"))
ballot2 = Image.open("examples\\SampleBallot-2.png")
json2 = json.load(open("AZ-5-2.json","r+"))

redFiles = glob("primitives\\*Red*")
accurateFiles = list(Counter(glob("primitives\\accurate*")) - Counter(redFiles))
badFiles = list(Counter(glob("primitives\\*")) - Counter(accurateFiles)-Counter(redFiles))

sections1 = json1["sections"]
sections2 = json2["sections"]

generatedballot1 = ballot1.copy()
for section in sections1:
    bubbles = section["bubbles"]
    max = section["max"]
    if bubbles is not None:
        bubblesToUse = random.sample(bubbles, max)
        for bubble in bubblesToUse:
            shape = Image.open(accurateFiles[random.randint(0, len(accurateFiles)-1)])
            shape_x, shape_y = shape.size
            center_x = bubble["TL_X"] + bubble["BR_X"]
            center_y = bubble["TL_Y"] + bubble["BR_Y"]
            generatedballot1.paste(shape, ((center_x-shape_x)//2, (center_y-shape_y)//2), mask=shape)

generatedballot1.save("test\\generatedballot-1.png")

generatedballot2 = ballot2.copy()
for section in sections2:
    bubbles = section["bubbles"]
    max = section["max"]
    if bubbles is not None:
        bubblesToUse = random.sample(bubbles, max)
        for bubble in bubblesToUse:
            shape = Image.open(accurateFiles[random.randint(0, len(accurateFiles)-1)])
            shape_x, shape_y = shape.size
            center_x = bubble["TL_X"] + bubble["BR_X"]
            center_y = bubble["TL_Y"] + bubble["BR_Y"]
            generatedballot2.paste(shape, ((center_x-shape_x)//2, (center_y-shape_y)//2), mask=shape)

generatedballot2.save("test\\generatedballot-2.png")