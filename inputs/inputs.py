
class Inputs:
    staticmethod
    def get_num(msg):
        while True:
            try:
                num = int(input(f"{msg}:").strip())
                if num not in [1,2]:
                    print("only num 1 or 2")
                    continue
                return num
            except ValueError as e:
                print(f"only num 1 or 2")
    staticmethod
    def get_str(msg):
        while True:
            name = input(f"{msg}:").strip()
            if name == "":
                continue
            return name