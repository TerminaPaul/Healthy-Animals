class Player:
    def __init__(self, name: str = "Pablo", speed: int = 10, inventory_size: int = 3):
        self.name = str(name)
        self.position = [0, 0]
        self.speed = int(speed)
        self.inventory = []
        for length in range(0, int(inventory_size)):
            self.inventory.append("")

    def move(self, dx=0, dy=0):
        self.position[0] += dx
        self.position[1] += dy


if __name__ == '__main__':
    test_player = Player(name="test")
    print(vars(test_player))
