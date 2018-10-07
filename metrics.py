# base class for metrics        
class Metrics:
    def __init__(self):
        self.d1 = 0
        self.ff = 0
        self.LTV = 0
        self.CPI = 0
        
    def __init__(self, d1, ff, LTV, CPI):
        self.d1 = d1
        self.ff = ff
        self.LTV = LTV
        self.CPI = CPI
        
    def calculate_update_metrics(d1_m, ff_m, LTV_m, CPI_m):
        return Metrics(self.d1*d1_m,                           
                        self.ff*ff_m,
                        self.LTV*LTV_m,
                        self.CPI*CPI_m)