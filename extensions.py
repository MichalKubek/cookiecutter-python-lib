import subprocess
from collections import defaultdict

from jinja2.ext import Extension


class GitInfo(Extension):
    DEFAULT_GIT_VALUE = "Value not in git config"
    DEFAULT_NAMESPACE = "default namespace"

    def __init__(self, environment):
        super().__init__(environment)
        data = self.get_git_config()
        environment.globals['git'] = self.get_git_config()
        email = data['user.email']
        namespace = self.DEFAULT_NAMESPACE
        if email != self.DEFAULT_GIT_VALUE and '@' in email:
            namespace = email.split('@', 1)[1].split('.')[0]
        environment.globals['namespace'] = namespace

    def get_git_config(self):
        # hack to know if we don't have value in git config
        git_data = defaultdict(lambda: self.DEFAULT_GIT_VALUE)
        command_data = subprocess.check_output(['git', 'config', '-l'])
        command_data = command_data.strip().decode('UTF-8')
        data = (i.split('=', 1) for i in command_data.split('\n') if '=' in i)
        for k, v in data:
            git_data[k] = v
        return git_data
