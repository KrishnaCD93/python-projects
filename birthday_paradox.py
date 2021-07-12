# Run a monte-carlo simulation to find the number of people with similar
# birthdays in a group. 
import datetime, random

def getBirthday(numOfBirthdays):
    # Returns a list of number random date objects for birthdays
    birthdays = []
    for i in range(numOfBirthdays):
        startOfYear = datetime.date(2001, 1, 1)
        randomNumOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumOfDays
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    # matches birthdays in the birthdays list
    if len(birthdays) == len(set(birthdays)):
        return None # all birthdays are unique
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a+1 :]):
            if birthdayA == birthdayB:
                return birthdayA

# display intro
print('''The birthday paradox shows that in a group of N people, 
the odds that two of them have matching birthdays is surprisingly large.
This program runs a monte-carlo simulation to explore this concept.''')

months = ('Jan', 'Feb', 'Mar','Apr','May','Jun', 'Jul',
            'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
while True:
    print('How many birthdays shall I generate? (Max 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break
print()
print('Here are ', numBDays, 'birthdays:')
birthdays = getBirthday(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(', ', end='') # add a comma at the end of each birthday after the first
    monthName = months[birthday.month - 1]
    dateText = f'{monthName} {birthday.day}'
    print(dateText, end='')
print()
print()

match = getMatch(birthdays)
print('In this simulation, ', end='')
if match != None:
    monthName = months[match.month - 1]
    dateText = f'{monthName} {birthday.month}'
    print('Multiple people have a birthday on ', dateText)
else:
    print('There are no matching birthdays.')
print()

print('Generating', numBDays, ' random birthdays 100,000 times...')
input('Press ENTER to begin...')

print('Let\' run another 100,000 simulations')
simMatch = 0
for i in range(100_000):
    if i % 10_000 == 0:
        print(i, 'simulations run')
    birthdays = getBirthday(numBDays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1
print('100,000 simulations run.')

probability = round(simMatch / 100_000 * 100, 2)
print('Out of 100,000 simulations of', numBDays, 'people, there was a')
print('matching birthday in that group', simMatch, 'times. This means')
print('that', numBDays, 'people have a', probability, '% chance of')
print('having a matching birthday in their group.')
print('That\'s probably more than you would think!')