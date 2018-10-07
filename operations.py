from random import shuffle, random


####
# Данный фрагмент кода был использован для генерации колоды(card_deck)
# cards = ['6 ', '7 ', '8 ', '9 ', '10 ', 'J ', 'Q ', 'K ', 'A ']
# card_suits = ['diamonds', 'clubs', 'hearts', 'spades']
# card_deck = list()
# for card in cards:
#     for suit in card_suits:
#         card_deck.append(card + suit)
# print(card_deck)
####


def gamefunc(player_amount):
    if 1 < player_amount < 7:
        players = {'player' + str(i): 0 for i in range(1, player_amount + 1)} # игроки, им будет присвоен суммарный прииоритет их карт
        card_deck = ['6 diamonds', '6 clubs', '6 hearts', '6 spades',   # колода карт
                     '7 diamonds', '7 clubs', '7 hearts', '7 spades',
                     '8 diamonds', '8 clubs', '8 hearts', '8 spades',
                     '9 diamonds', '9 clubs', '9 hearts', '9 spades',
                     '10 diamonds', '10 clubs', '10 hearts', '10 spades',
                     'J diamonds', 'J clubs', 'J hearts', 'J spades',
                     'Q diamonds', 'Q clubs', 'Q hearts', 'Q spades',
                     'K diamonds', 'K clubs', 'K hearts', 'K spades',
                     'A diamonds', 'A clubs', 'A hearts', 'A spades']
        card_priority = {'6': 1, '7': 2, '8': 3, '9': 4, '10': 5, 'J': 6, 'Q': 7, 'K': 8, 'A': 9}  # приоритет карт
        shuffle(card_deck)  # тасуем карты в колоде
        trump_suit = ['diamonds', 'clubs', 'hearts', 'spades'][int(random() * 4)]  # генерация козырной масти
        player_cards = dict()   # словарь с наборами карт игроков
        for player in players:
            player_cards[player] = list()
            for card in card_deck[:6]:
                player_cards[player].append(card)
            del card_deck[:6]   # после передачи карт игроку - стираем их из колоды
        for player in players:
            for card in player_cards[player]:
                for k, v in card_priority.items():
                    if k in card:
                        players[
                            player] += v + 9 if trump_suit in card else v  # если карта козырная - приоритет выше на 9
                        break
        strongest_sets = [sorted(players.items(), key=lambda x: x[1], reverse=True)[0]]  # "сильнейший" набор
        for player in sorted(players.items(), key=lambda x: x[1], reverse=True)[1:]:
            if player[1] == strongest_sets[0][1]:
                strongest_sets.append(player)
            else:
                break
        print('{:-^30}'.format('TRUMP SUIT'), '\n')
        print('Trump suit:', trump_suit.upper(), '\n')
        print('------------------------------')
        print('{:-^30}'.format('PLAYER CARDS'))
        for k, v in player_cards.items():
            print('------------------------------')
            print(k.upper(), ':', sep='')
            print(*v, sep='\n')
            print('------------------------------')
        print('{:-^30}'.format('THE STRONGEST SETS'), '\n')
        for name, card_score in strongest_sets:
            print(' - ' + name, '\n')
        print('------------------------------')
        input('Press the Enter to close..')