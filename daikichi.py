import random


class OmikujiResult:
    def __init__(self, result):
        self.result = result

    def __str__(self):
        return f"{self.result}"


class Omikuji:
    def __init__(self):

        self.results = [
            OmikujiResult("大吉"),
            OmikujiResult("中吉"),
            OmikujiResult("小吉"),
            OmikujiResult("吉"),
            OmikujiResult("末吉"),
            OmikujiResult("凶"),
            OmikujiResult("大凶"),
        ]

    def hiku(self):
        # ランダムに結果を選ぶ
        result = random.choice(self.results)
        return result


class daikichi:
    def __init__(self):
        self.daikichi = Omikuji()

    def start(self):
        print("*************************")
        print("おみくじゲームへようこそ！")
        print("*************************")
        while True:
            choice = input("おみくじを引きますか？ (yes/no): ").strip().lower()
            if choice == "yes" or choice == "y":
                result = self.daikichi.hiku()
                print("おみくじの結果は... " + str(result))
            elif choice == "no" or choice == "n":
                print("おみくじゲームを終了します。また遊びに来てくださいね！")
                break
            else:
                print("無効な入力です。「yes」または「no」と入力してください。")


# ここがスタート
if __name__ == "__main__":
    game = daikichi()
    game.start()
