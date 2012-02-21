from model import Model

model = Model(ask_threshold = 3, units = 2, todo = [0,1,0,1,1,0,1])
model.add_developer('kalle', [5, 5])
model.add_developer('nisse', [1, 1])

for time in range(10):
    print "*** time " + str(time)
    for dev in ['kalle', 'nisse']:
        print dev + ": " + str(model.get_knowledge(dev)) + ', ' + model.get_doing(dev)
    model.step(1)
