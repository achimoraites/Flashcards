import argparse
from io import StringIO

from utils import Logger, CardDeck

memory_file = StringIO()

log = Logger(memory_file)

deck = CardDeck(log)

parser = argparse.ArgumentParser()
parser.add_argument("--import_from", type=str)
parser.add_argument("--export_to", type=str)
args = parser.parse_args()

if args.import_from:
    deck.import_card_deck(args.import_from)

while True:
    action = log.input('Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):\n')

    if action == 'add':
        deck.add_card_interactive()

    elif action == 'remove':
        deck.remove_card_interactive()

    elif action == 'import':
        file_name = log.input("File name:\n")
        deck.import_card_deck(file_name)

    elif action == 'export':
        file_name = log.input("File name:\n")
        deck.export_card_deck(file_name)

    elif action == 'ask':
        times_to_ask = int(log.input("How many times to ask?\n"))
        deck.ask(times_to_ask)

    elif action == 'exit':
        print('Bye bye!')
        if args.export_to:
            deck.export_card_deck(args.export_to)
        log.close()
        break

    elif action == 'log':
        file_name = log.input("File name:\n")
        with open(file_name, "w") as log_file:
            log_file.write(memory_file.getvalue())
        log.print("The log has been saved.\n")

    elif action == 'hardest card':
        deck.print_stats()

    elif action == 'reset stats':
        deck.reset_stats()
        log.print("Card statistics have been reset.\n")
