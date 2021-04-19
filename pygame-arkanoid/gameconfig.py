class GameConfig:
    score = 0
    lives = 3
    show_menu = True
    bestScores = []

    @staticmethod
    def save_score(score):
        GameConfig.bestScores.append(score)
        GameConfig.bestScores.sort(reverse=True)
        file = open("bestScores.txt", "w")
        for score in GameConfig.bestScores:
            file.write(str(score) + "\n")
        file.close()
