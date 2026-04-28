import pprint

class InMemoryKeyStore:

    def __init__(self):
        self.main_map = {}
        self.count_map = {}

    def print_formatted(self, data):
        """Pretty prints the given data."""
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(data)

    def GET(self, key):
        self.print_formatted(f"{'NULL' if self.main_map.get(key) is None else self.main_map.get(key)}")

    def SET(self, key, val):
        if key not in self.main_map:
            # print_formatted(f"Key {key} not in: {self.main_map}")
            self.AddKeyToMap(key, val)
            self.IncrementValueCount(val)
        else:
            # print_formatted(f"Key {key} in: {self.main_map}")
            old_val = self.main_map[key]
            self.DecrementValueCount(old_val)
            self.AddKeyToMap(key, val)
            self.IncrementValueCount(val)

        # print_formatted(f"main_map: {self.main_map}")
        # print_formatted(f"self.count_map: {self.count_map}")

    def COUNT(self, val):
        self.print_formatted(f"{'0' if self.count_map.get(val) is None else self.count_map[val]}")

    def DELETE(self, key):
        #self.print_formatted(f"Running DELETE for {key}")
        if key in self.main_map:
            val = self.main_map[key]
            self.DecrementValueCount(val)
            self.main_map.pop(key)

    # print_formatted(f"self.main_map: {self.main_map}")
    # print_formatted(f"self.count_map: {self.count_map}")

    def IncrementValueCount(self, val):
        self.count_map[val] = self.count_map.get(val, 0) + 1

    def DecrementValueCount(self, val):
        self.count_map[val] = self.count_map.get(val, 0) - 1
        if self.count_map[val] == 0:
            self.count_map.pop(val)

    def AddKeyToMap(self, key, val):
        self.main_map[key] = val

    def UserInterface(self):
        break_loop = False
        while not break_loop:
            try:
                user_commands = input("Enter Key Store Commands:\n").split(" ")

                match user_commands[0].upper():
                    case "SET":
                        self.SET(user_commands[1], user_commands[2])
                    case "GET":
                        self.GET(user_commands[1])
                    case "DELETE":
                        self.DELETE(user_commands[1])
                    case "COUNT":
                        self.COUNT(user_commands[1])
                    case "EXIT":
                        break_loop = True
            except EOFError:
                break

def main():
    db = InMemoryKeyStore()
    db.UserInterface()


if __name__ == "__main__":
    main()