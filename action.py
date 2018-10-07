# base class for user actions and how they are affecting user 
class Action:
    def __init__(self, actionsRow):
        self.type = actionsRow.type
        self.stage = actionsRow.stage
        self.activity = actionsRow.activity
        self.max_times = actionsRow.max_times
        self.current_time = 0
        self.cost = actionsRow.cost
        self.d1 = actionsRow.d1
        self.d7 = actionsRow.d7
        self.LTV = actionsRow.LTV
        self.CPI = actionsRow.CPI
        self.available = True
