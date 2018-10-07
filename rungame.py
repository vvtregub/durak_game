from operations import gamefunc

if __name__ == '__main__':
    while True:
        print('{:-^30}'.format('NUMBER OF PLAYERS'), '\n')
        player_amount = int(input('Please, enter the number of players(from 2 to 6): '))
        print()
        print('------------------------------')
        if 1 < player_amount < 7:
            gamefunc(player_amount)
            break



