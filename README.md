# python
Some random tinkering with Python from tutorials and challenges etc

## dictionary
The user is prompted to enter a word. A json dictionary is searched to see if the word exists in it, and returns the definition if it's there. If it's not there, the first word with a similarity ratio of 0.8 or more is suggested. If the user agrees that this suggestion is, in fact, the correct word, it returns that definition.

For words with multiple definitions in the dictionary, it loops through each one and presents the user with a numbered list of definitions.
