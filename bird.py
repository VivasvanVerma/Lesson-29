class bird():
    def __init__(self):
        print("Bird is Ready")
    def whoisthis(self):
        print("Bird")
    def swim(self):
        print("Swim faster")

class penguin(bird):
    def __init__(self):
        super().__init__()
        print("Penguin is Ready.")
    def whoisthis(self):
        print("Penguin")
    def run(self):
        print("Run faster")

peggy = penguin()
peggy.whoisthis()
peggy.swim()
peggy.run()