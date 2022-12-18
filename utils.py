from itertools import cycle, islice


class TermException(Exception):
    pass


class DefinitionException(Exception):
    pass


class Logger:
    def __init__(self, memory_file):
        self.memory_file = memory_file

    def input(self, value=''):
        print(value, file=self.memory_file)
        input_val = input(value)
        print(input_val, file=self.memory_file)
        return input_val

    def print(self, value=''):
        print(value, file=self.memory_file)
        print(value)

    def close(self):
        self.memory_file.close()


class Card:
    def __init__(self, term, definition, mistakes=0):
        self.term = term
        self.definition = definition
        self.mistakes = int(mistakes)

    def check_answer(self, answer):
        if self.definition == answer:
            return True
        self.mistakes += 1
        return False

    def reset_stats(self):
        self.mistakes = 0


class CardDeck:
    def __init__(self, log):
        self.card_deck = dict()
        self.seen_definitions = dict()
        self.log = log

    def get_cards(self):
        return [item[1] for item in self.card_deck.items()]

    def add_card(self, term, definition, mistakes=0):
        self.card_deck.update({term: Card(term, definition, mistakes)})
        self.seen_definitions.update({definition: term})

    def add_card_interactive(self):
        term = self.__read_term()
        definition = self.__read_definition()
        self.add_card(term, definition)
        self.log.print('The pair ("{}":"{}") has been added.\n'.format(term, definition))

    def remove_card(self, card_term):
        definition = self.card_deck.pop(card_term).definition
        self.seen_definitions.pop(definition)

    def remove_card_interactive(self):
        card_term = self.log.input('Which card?\n')
        if self.card_term_exists(card_term):
            self.remove_card(card_term)
            self.log.print('The card has been removed.\n')
        else:
            self.log.print("Can't remove \"{}\": there is no such card.\n".format(card_term))

    def card_term_exists(self, card_term):
        return card_term in self.card_deck

    def reset_stats(self):
        for item in self.get_cards():
            item.reset_stats()

    def print_stats(self):
        cards = sorted(self.get_cards(), key=lambda i: i.mistakes, reverse=True)
        if len(cards):
            mistakes = cards[0].mistakes
            if mistakes > 0:
                results = list(filter(lambda i: i.mistakes == mistakes, cards))
                if len(results) == 1:
                    self.log.print('The hardest card is "{}". You have {} errors answering it'
                                   .format(results[0].term, mistakes))
                else:
                    msg = ', '.join(['"{}"'.format(r.term) for r in results])
                    self.log.print('The hardest cards are {}. You have {} errors answering them'.format(msg, mistakes))
            else:
                self.log.print("There are no cards with errors.\n")
        else:
            self.log.print("There are no cards with errors.\n")

    def ask(self, times_to_ask):
        cards = self.get_cards()

        for card in list(islice(cycle(cards), times_to_ask)):
            self.log.print('Print the definition of "{}":'.format(card.term))
            answer = self.log.input()
            if card.check_answer(answer):
                self.log.print('Correct!')
            else:
                matching_term = self.seen_definitions.get(answer)
                if matching_term:
                    self.log.print('Wrong. The right answer is "{}", but your definition is correct for "{}".'
                                   .format(card.definition, matching_term))
                else:
                    self.log.print('Wrong. The right answer is "{}".'.format(card.definition))

    def export_card_deck(self, file_name):
        cards_number = 0
        with open(file_name, 'w', encoding='utf-8') as file:
            for item in self.card_deck.items():
                card = item[1]
                file.write("{},{},{},\n".format(card.term, card.definition, card.mistakes))
                cards_number += 1
        self.log.print('{} cards have been saved.\n'.format(cards_number))

    def import_card_deck(self, file_name):
        try:
            cards_number = 0
            with open(file_name, 'r', encoding='utf-8') as file:
                for line in file:
                    current_line = line.split(',')
                    term = current_line[0]
                    definition = current_line[1]
                    mistakes = current_line[2]

                    self.add_card(term, definition, mistakes)
                    cards_number += 1
            self.log.print('{} cards have been loaded.\n'.format(cards_number))
        except FileNotFoundError:
            self.log.print("File not found.")

    def __read_term(self):
        term = self.log.input("The Card\n")
        while True:
            try:
                if term in self.card_deck:
                    raise TermException()
                break
            except TermException:
                term = self.log.input('The term "{}" already exists. Try again:\n'.format(term))

        return term

    def __read_definition(self):
        definition = self.log.input("The definition of the card\n")
        while True:
            try:
                if definition in self.seen_definitions:
                    raise DefinitionException()
                break
            except DefinitionException:
                definition = self.log.input('The definition "{}" already exists. Try again:\n'.format(definition))

        return definition
