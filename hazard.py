# base class for randonm hazards
# not ready yet --- TODO
from action import Action

class Hazard(Action):
    def __init__(self, **kwargs):
        __super__(kwargs)