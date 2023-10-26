import os
import time
from typing import Any

class TerminalOpener:
    def __init__(self) -> None:
        self.__calls = []
    
    def __call__(self):
        if not os.system('gnome-terminal'):
            self.__calls.append(time.ctime())
        else:
            print('Gnome terminal failed to start!')

    def get_calls(self):
        return self.__calls
    def get_calls_count(self) -> int:
        return len(self.__calls)

opener = TerminalOpener()
        