import os
import sys

class Colors:

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
                        self.reset = "Esc[0m"
                        self.red = "Esc[31m"
                        self.green = "Esc[92m"
                        self.yellow = "Esc[93m"
                        self.blue = "Esc[34m"
                        self.magenta = "Esc[35m"
                        self.cyan = "Esc[96m"
                        self.white = "Esc[97m"
