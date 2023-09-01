import os
import platform
from tkinter import NO

class dir:
    def __init__(self):
        self.pwd = os.getcwd()

    @property
    def output(self) -> str:
        dir = f"{self.pwd}/output"
        os.makedirs(f"{self.pwd}/output", exist_ok=True)
        return dir

    @property
    def proccesed(self) -> str:
        dir = f"{self.pwd}/proccessed"
        os.makedirs(f"{self.pwd}/proccessed", exist_ok=True)
        return dir

class Utils:
    
    @classmethod
    def get_os_info(cls):
        os_info = {
            "arch": platform.architecture(),
            "system": platform.system(),
            "machine": platform.machine(),
            "node": platform.node()
        }
        host_os = None

        if 'windows' in os_info['system'].lower():
            host_os = 'windwos'
        elif 'linux' in os_info['system'].lower():
            host_os = 'linux'
        host_arch = os_info['machine'].lower()
        host_system = os_info['system'].lower()
        if ('x86' in host_arch or 'x86' in host_system):
            host_arch = 'x86'
        return host_os, host_arch
