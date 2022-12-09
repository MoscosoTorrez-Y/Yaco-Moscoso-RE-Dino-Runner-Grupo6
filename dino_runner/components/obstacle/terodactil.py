from dino_runner.components.obstacle.obstacle import Obstalce
import random

class Terodactil(Obstalce):
    def __init__(self, image):
        self.type = random.randint(0, 1)
        super().__init__(image, self.type)
        self.rect.y = 260
