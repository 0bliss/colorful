import os
import sys

class Colorfuls:

        reset = ""
        red = ""
        green = ""
        yellow = ""
        blue = ""
        magenta = ""
        cyan = ""
        white = ""

        def setSystem(self):
                machineOs = ""
                # print(sys.platform)
                if 'linux' in str(sys.platform).lower() or 'os x' in str(sys.platform).lower():
                        self.reset = "\u001b[0m"
                        self.red = "\u001b[31m"
                        self.green = "\u001b[32m"
                        self.yellow = "\u001b[33m"
                        self.blue = "\u001b[34m"
                        self.magenta = "\u001b[35m"
                        self.cyan = "\u001b[36m"
                        self.white = "\u001b[37m"
                elif 'win32' in str(sys.platform).lower() or 'windows' in str(sys.platform).lower():
                        self.reset = "\033[0m"
                        self.red = "\033[31m"
                        self.green = "\033[32m"
                        self.yellow = "\033[33m"
                        self.blue = "\033[34m"
                        self.magenta = "\033[34m"
                        self.cyan = "\033[36m"
                        self.white = "\033[37m"
