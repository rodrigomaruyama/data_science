import pandas as pd

# Change False to True to see what the following block of code does

# Example pandas apply() usage (although this could have been done
# without apply() using vectorized operations)
if True:
    s = pd.Series([1, 2, 3, 4, 5])
    def add_one(x):
        return x + 1
    print s.apply(add_one)

names=pd.Series(['Andre Agassi', 'Barry Bonds', 'Christopher Columbus', 'Daniel Defoe'], index=[0, 1, 2, 3])

# names = pd.Series([
#     'Andre Agassi',
#     'Barry Bonds',
#     'Christopher Columbus',
#     'Daniel Defoe',
#     'Emilio Estevez',
#     'Fred Flintstone',
#     'Greta Garbo',
#     'Humbert Humbert',
#     'Ivan Ilych',
#     'James Joyce',
#     'Keira Knightley',
#     'Lois Lane',
#     'Mike Myers',
#     'Nick Nolte',
#     'Ozzy Osbourne',
#     'Pablo Picasso',
#     'Quirinus Quirrell',
#     'Rachael Ray',
#     'Susan Sarandon',
#     'Tina Turner',
#     'Ugueth Urbina',
#     'Vince Vaughn',
#     'Woodrow Wilson',
#     'Yoji Yamada',
#     'Zinedine Zidane'
# ])

def reverse_name(name):
    splited_name = name.split(' ')
    splited_name[0], splited_name[1] = splited_name[1], splited_name[0]
    return splited_name

def reverse_names(names):
    return names.apply(reverse_name)


print reverse_names(names)
