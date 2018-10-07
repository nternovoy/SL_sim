class Game:
    # general settings 
    genre = ''
    game_name = ''
    player_name = ''
    
    # flags for some "one-time" events
    omnom_summoned = False
    
    # parameters for the main game loop
    is_running = True
    reason_closed = ""
    
    # some valuable stuff
    actions_history = []
    metrics_history = []
    display_metrics_history = []
    
    
    time_total = 0
    time_spent = 0
    iteration_count = 0
    loyalty = 100
    
    def __init__(self, player_name, genre):
        self.player_name = player_name
        self.genre = genre
        self.name = get_game_name(self.genre)
        
        #get all actions
        actionsDF = pd.read_csv('activities.csv')
        self.all_actions = [Action(actionsDF.loc[row]) for row in actionsDF.index]
        
        #get basic metrics
        metricsDF = pd.read_csv('basic_metrics.csv')
        
        self.metrics_history = [Metrics(metricsDF[metricsDF['genre']==genre].d1,
                                       metricsDF[metricsDF['genre']==genre].d7,
                                       metricsDF[metricsDF['genre']==genre].LTV,
                                       metricsDF[metricsDF['genre']==genre].CPI)]
    
    def update(self):
        message = ''

        # loyalty update function
        # logic of increasing and decreasing investor 
        loyalty -= 10
        #update_loyalty
        if (loyalty < 10):
            message += "\nInvestors are about to quit! Do something right now!!"
        elif (loyalty < 25):
            message += "\nBoy oh boy, it looks like you're in a pickle with investors"
        elif (loyalty < 50):
            message += "\nOi mate, it looks like you're in a pickle with investors"

            
    def present_state(self):
        return "Boy oh boy we runnin'"
        
            
    # get all available action based on current progress, metrics, history etc.
    def get_available_actions(self):
        return all_actions
    
    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method)
        if action_method:
            action_method(**kwargs)
    
    # functions that define player actions
    def update_metrics(self, action):
        
        self.metrics_history[:-1].calculate_update_metrics(action.d1,
                                                           action.d7,
                                                           action.LTV,
                                                           action.CPI)
        
        action_history.append(action)
        
        return
    
    def summon_analyst(self):
        return '¯\_(ツ)_/¯'
    
    def improve_LTV(self):
        return
    def add_om_nom(self):
        return
    def choose_random(self):
        return
