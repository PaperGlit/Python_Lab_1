import os
from runner import main


if not os.path.exists("history.txt"):
    with open("history.txt", "x"):
        pass
main()