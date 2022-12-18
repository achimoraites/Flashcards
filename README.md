# Flashcards
Simple Flashcards app that supports import, export, logs and basic statistics


```bash

>python flashcards.py
Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
> add
The Card
> Cat
The definition of the card
> Pet
The pair ("Cat":"Pet") has been added.

Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
> add
The Card
> Dog
The definition of the card
> Pet
The definition "Pet" already exists. Try again:
> woof
The pair ("Dog":"woof") has been added.

Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
> add
The Card
> Paris
The definition of the card
> France
The pair ("Paris":"France") has been added.

Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
> remove
Which card?
> Dog
The card has been removed.

Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
> ask
How many times to ask?
>1
Print the definition of "Cat":
> Italy
Wrong. The right answer is "Pet".
Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
> ask
How many times to ask?
> 2
Print the definition of "Cat":
> France
Wrong. The right answer is "Pet", but your definition is correct for "Paris".
Print the definition of "Paris":
> France
Correct!
Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
>hardest card
The hardest card is "Cat". You have 2 errors answering it
Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
> log
File name:
> test.log
The log has been saved.

Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
> exit
Bye bye!

```