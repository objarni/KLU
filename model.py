class Model:
    def __init__(self, units, ask_threshold, todo):
        self.knowledge = [5]
        pass
    
    def add_developer(self, name, knowledge):
        pass
        
    def step(self, steps):
        odd = False
        for i in xrange(steps):
            odd = not odd
            if odd:
                self.knowledge[0] += 1
            if self.knowledge[0] > 9:
                self.knowledge[0] = 9
        
    def get_knowledge(self, developer):
        return self.knowledge
        
    def get_doing(self, developer):
        return "working on unit 0"