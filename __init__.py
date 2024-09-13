import os
from runner import calculator

if not os.path.exists("history.txt"):
    with open("history.txt", "x"):
        pass
calculator()