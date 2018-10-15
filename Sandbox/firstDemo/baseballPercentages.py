# Maggi Keddy#####
# October 14 2018#
##################

def main():

    # INPUT AND VARIABLES
    teamName = input("What is the team name? ")
    gamesWon = int(input("Enter how many games did you win? "))
    totalGames = int(input("Enter total number of games. "))


    # PROCESSING
    winningPercentage = gamesWon / totalGames * 100


    # OUTPUT
    print("The winning percentage for {} is: {:.2f}".format(teamName,winningPercentage))



if __name__ == "__main__":
    main()