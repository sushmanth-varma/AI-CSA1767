class VacuumCleaner:
    def __init__(self, initial_state):
        self.state = initial_state

    def clean(self):
        for i in range(len(self.state)):
            if self.state[i] == 1:
                print(f"Cleaning position {i}")
                self.state[i] = 0
            print(f"Current state: {self.state}")

initial_state = [1, 0, 1, 0, 1]
vacuum = VacuumCleaner(initial_state)
vacuum.clean()
