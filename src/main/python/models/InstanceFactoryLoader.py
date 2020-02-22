import os
import json
from .InstanceFactory import InstanceFactory

class InstanceFactoryLoader:
    def __init__(self, fp):
        self.fp = fp
        self.json = json.load(self.fp)

    def load(self):
        apps = self.json.get("apps", [])

        for data in apps:
            instance = InstanceFactory()
            instance.name = data.get("name", "")
            instance.username = data.get("username", "")
            instance.exec_path = data.get("exec_path", "")
            instance.args = data.get("args", "")
            instance.env_name = data.get("env_name", "default")
            instance.env_config_path = data.get("env_config_path", "config/default_config.json")
            instance.env_parent_dir = data.get("env_parent_dir", "E:/GameEnv/envs/")

            yield instance