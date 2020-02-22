import os
import json
import subprocess

class InstanceFactory:
    def __init__(self):
        self.name = ""
        self.username = "FiendChain"
        self.exec_path = ""
        self.args = ""
        self.env_name = "Generic"
        self.env_config_path = "E:/GameEnv/scripts/config/default_env.json"
        self.env_parent_dir = "E:/GameEnv/envs/"

    def create_environment(self):
        with open(self.env_config_path, "r") as fp:
            config = json.load(fp)
        params = {
            "root": os.path.join(self.env_parent_dir, self.env_name),
            "username": self.username
        }
        env = create_environment(os.environ, config, params)
        return env

    def create_instance(self):
        exec_path = os.path.abspath(self.exec_path)
        cwd_path = os.path.dirname(exec_path)
        env = self.create_environment()

        process = subprocess.Popen(exec_path, cwd=cwd_path, env=env, start_new_session=True)
        return process


def create_environment(env, config, params):
    environment = {}

    dirs = config.get("directories", {})
    seed_dirs = config.get("seed_directories", [])
    override_variables = config.get("override_variables", {})
    pass_through_variables = config.get("pass_through_variables", [])


    for var, fmt_str in dirs.items():
        directory = fmt_str.format(**params)
        directory = os.path.realpath(directory)
        os.makedirs(directory, exist_ok=True)
        environment[var] = directory
        if var not in env:
            print(f"[warning] {var} not in original env")
    
    for fmt_str in seed_dirs:
        directory = fmt_str.format(**params)
        directory = os.path.realpath(directory)
        os.makedirs(directory, exist_ok=True)
    
    for var, fmt_str in override_variables.items():
        value = fmt_str.format(**params)
        environment[var] = value

    for var in pass_through_variables:
        try:
            environment[var] = env[var]
        except KeyError as ex:
            print(f"{var} is not an existing variable")
    
    return environment