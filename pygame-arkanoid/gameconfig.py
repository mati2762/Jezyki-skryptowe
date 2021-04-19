class GameConfig:
    score = 0
    lives = 3
    show_menu = True
    bestScores = []

    @staticmethod
    def save_score(appScore):
        found = False
        try:
            GameConfig.bestScores.index(appScore)
            found = True
        except:
            found = False

        if (found == False):
            GameConfig.bestScores.append(appScore)
            GameConfig.bestScores.sort(reverse=True)
            file = open("bestScores.txt", "w")
            for score in GameConfig.bestScores:
                file.write(str(score) + "\n")
            file.close()
