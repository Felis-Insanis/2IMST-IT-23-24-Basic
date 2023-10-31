# Jeg vet at jeg bør bruke lister, men det er bare for lett
# å bruke dictionaries på akkurat den slags oppgave, og så skal jeg.

import random

dates = {
    'Monday':    {'Temperature': 0, 'Precipitation': 0, 'Type': '', 'Wind': 0},
    'Tuesday':   {'Temperature': 0, 'Precipitation': 0, 'Type': '', 'Wind': 0},
    'Wednesday': {'Temperature': 0, 'Precipitation': 0, 'Type': '', 'Wind': 0},
    'Thursday':  {'Temperature': 0, 'Precipitation': 0, 'Type': '', 'Wind': 0},
    'Friday':    {'Temperature': 0, 'Precipitation': 0, 'Type': '', 'Wind': 0}
}
typesOfPrecipitation = [
    'snow',
    'sleet',
    'snowy rain',
    'rain',
    'blood',
    'amphibians and small reptiles',
    'ice',
    'Nothing'
]
roughTemp = random.randint(-90, 56)
# Filling out the form:
for day in dates:
    # temperature for the day
    dailyTemp = random.randint(roughTemp-5, roughTemp+5) + round(random.random(), 1)
    dates[day]['Temperature'] = dailyTemp
    roughTemp = round(dailyTemp)
    
    # type of precipitation
    if dailyTemp < -10:
        dates[day]['Type'] = typesOfPrecipitation[random.randint(0, 1)]
    elif -10 <= dailyTemp < 0:
        dates[day]['Type'] = typesOfPrecipitation[random.randint(0, 2)]
    elif 0 <= dailyTemp < 5:
        dates[day]['Type'] = typesOfPrecipitation[random.randint(2, 3)]
    elif 5 <= dailyTemp < 20:
        dates[day]['Type'] = typesOfPrecipitation[random.randint(3, 5)]
    elif 20 <= dailyTemp < 40:
        dates[day]['Type'] = typesOfPrecipitation[random.randint(3, 6)]
    elif 40 <= dailyTemp:
        dates[day]['Type'] = typesOfPrecipitation[7]
    
    # amount of precipitation
    if dates[day]['Type'] in typesOfPrecipitation[0:]:
        dates[day]['Precipitation'] = random.randint(0, 1825) + round(random.random(), 1)
    elif dates[day]['Type'] == 'snow':
        dates[day]['Precipitation'] = random.randint(0, 230) + round(random.random(), 1)
    
    # highest wind speed
    dates[day]['Wind'] = random.randint(0, 516) + round(random.random(), 2)

for day in dates:
    print(f'{day}:')
    print(f'\t- Average temperature: {dates[day]["Temperature"]}')
    if dates[day]['Type'] == 'snow':
        print(f'\t- Precipitation: {dates[day]["Precipitation"]}cm of {dates[day]["Type"]}')
    else:
        print(f'\t-Precipitation: {dates[day]["Precipitation"]}mm of {dates[day]["Type"]}')
    print(f'\t- Highest wind speed: {dates[day]["Wind"]}')