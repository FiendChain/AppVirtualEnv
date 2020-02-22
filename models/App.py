from .InstanceFactoryLoader import InstanceFactoryLoader
from .InstanceFactorySaver import InstanceFactorySaver
from .ObservableList import ObservableList

class App:
    def __init__(self, args):
        self.args = args

        with open(args.apps, "r") as fp:
            loader = InstanceFactoryLoader(fp)
            instance_factories = loader.load()
            instance_factories = list(instance_factories)
            self.instance_factory_list = ObservableList(instance_factories)
        
        self.instance_factory_list.changed.connect(self.on_change)
    
    def on_change(self):
        with open(self.args.apps, "w+") as fp:
            saver = InstanceFactorySaver(fp)
            saver.save(self.instance_factory_list)
        