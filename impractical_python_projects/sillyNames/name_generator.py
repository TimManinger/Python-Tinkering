import sys, random

firsts = (
    'Buster', 'Cooter', 'Andy', 'Perigrine', 'Mort', 'Gomer', 'Alistair',
    'John-Jacob-Jingleheimer', 'Dave', 'Gronk', 'Soupcan', 'Johnson and',
    'Burburbur', 'Dick', 'Randolph', 'Jaime', 'Benderick'
)

lasts = (
    'Gubb', 'Fishmonger', 'Krabs', 'Thuul', 'Johnson', 'McGee', 'Bambino',
    'Peebrain', 'the Flatulent', 'CucumberPatch', 'Bumblefuck', 'Dinglebaum',
    'Van-Weinerschnitzel', 'Snifferton', 'Zamboni', 'Bilbilbi'
)

# greet
print("Impractical name generator 3,000,000\n")

# output names
print(random.choice(firsts), random.choice(lasts))
