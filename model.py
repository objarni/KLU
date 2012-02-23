class Model:
    def __init__(self, units, ask_threshold, todo):
        self.knowledge = [5]
        self.odd = False
    
    def add_developer(self, name, knowledge):
        pass
        
    def step(self, steps):
        for i in xrange(steps):
            self.step_once()

    def step_once(self):
        self.odd = not self.odd
        if self.odd:
            self.knowledge[0] += 1
        if self.knowledge[0] > 9:
            self.knowledge[0] = 9
        
    def get_knowledge(self, developer):
        return self.knowledge
        
    def get_doing(self, developer):
        return "working on unit " + ('1' if self.odd else '0')

''' ungefärlig algoritm (behöver verifieras mot Tors flödesschema i boken)
jobbar någon med uppgiften?
 ja - har denne tillräckligt med kunskap för att jobba själv?
   ja - minska insatserna på uppgiften med utvecklarens kunskapsnivå.
        är antalet insatser <= 0?
           ja - utvecklaren markeras som "ledig" i (början av) nästa runda
           nej - gå till nästa uppgift
   nej - finns det någon att fråga?
 nej - finns det någon ledig utvecklare?
   ja - tillsätt den utvecklare som har högst kunskap uppgiften
         (vid flera med samma nivå gå efter hackordning)
   nej - gå till nästa runda
'''
