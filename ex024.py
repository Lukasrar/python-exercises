name = str(input('What is your name? ')).strip()

print(f'the letter A appears {name.lower().count("a")} times in your name.')
print(f'the first letter A appears at position {name.lower().find("a") + 1}.')
print(f'the last letter A appears at position {name.lower().rfind("a") + 1}.')

