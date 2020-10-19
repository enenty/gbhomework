import random
from random import randrange


class Card:
    def __init__(self):
        self.player_card = self.create_card
        self.computer_card = self.create_card
        self.pool = random.sample(range(1, 91), 90)

    @property
    def create_card(self):
        unique = random.sample(range(1, 91), 15)
        new_card = [sorted(unique[i:i + 5]) for i in range(0, len(unique), 5)]
        for i in range(1, 5):
            for lst in new_card:
                num = randrange(0, 9)
                lst.insert(num, '[ ]')
        return new_card

    def get_number(self):
        return self.pool.pop()

    def __str__(self, card):
        return '\n'.join(map(str, (' '.join(map(str, el)) for el in card)))

    def replace_number(self, card, turn):
        return [['[-]' if x == turn else x for x in line] for line in card]

    def is_complete(self, card):
        numbers = 0
        for line in card:
            for el in line:
                if el == '[-]':
                    numbers += 1
                    if numbers == 15:
                        return 'empty'

    def game(self):
        while True:
            turn = self.get_number()
            print(f'Новый бочонок: {turn} (осталось {len(self.pool)}) ')
            print('------ Ваша карточка -----')
            print(Card.__str__(self, self.player_card))
            print('-- Карточка компьютера ---')
            print(Card.__str__(self, self.computer_card))
            answer = input(f'Зачеркнуть цифру? (y/n)')
            if answer == 'q':
                return f'Игра остановлена.'
            elif answer == 'y':
                self.player_card = self.replace_number(self.player_card, turn)
                self.computer_card = self.replace_number(self.computer_card, turn)
                if self.is_complete(self.player_card) == 'empty' and self.is_complete(self.computer_card) == 'empty':
                    return f'Ничья.'
                elif self.is_complete(self.player_card) == 'empty':
                    return f'Игрок победил!'
                elif self.is_complete(self.computer_card) == 'empty':
                    return f'Компьютер победил!'

            elif answer == 'n':
                self.computer_card = self.replace_number(self.computer_card, turn)
                if self.is_complete(self.computer_card) == 'empty' and self.is_complete(self.player_card) != 'empty':
                    return 'Компьютер победил'
                continue
            else:
                continue
            print('\n\n')


player = Card()
print(player.game())
