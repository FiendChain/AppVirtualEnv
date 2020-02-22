import os
import json

class InstanceFactorySaver:
    def __init__(self, fp):
        self.fp = fp

    def save(self, instances):
        apps = []
        json_data = {"apps": apps}

        for instance in instances:
            data = {} 
            data["name"] = instance.name
            data["username"] = instance.username
            data["exec_path"] = os.path.realpath(instance.exec_path)
            data["args"] = instance.args
            data["env_name"] = instance.env_name
            data["env_config_path"] = os.path.realpath(instance.env_config_path)
            data["env_parent_dir"] = os.path.realpath(instance.env_parent_dir)

            apps.append(data)
        
        json.dump(json_data, self.fp, indent=2)


