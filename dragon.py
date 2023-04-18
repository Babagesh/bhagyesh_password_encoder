# Import Cow class
from cow import Cow


# dragon class
class Dragon(Cow):
    # instructor for creating an instance of dragon class
    def __init__(self, name, image):
        self.name = name
        self.image = image
    # Returns True since fire-breathing dragon
    def can_breathe_fire(self):
        return True;
