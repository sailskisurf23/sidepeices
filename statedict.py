#userinput = input('Give me a state, I\'ll give you a capital: ')

userinput = 'new york'

state_dictionary = {'Colorado': 'Denver', 'Alaska': 'Juneau',
                    'California': 'Sacramento', 'Georgia': 'Atlanta',
                    'Kansas': 'Topeka', 'Nebraska': 'Lincoln',
                    'Oregon': 'Salem', 'Texas': 'Austin', 'New York': 'Albany'}

try:
    result = state_dictionary[userinput.title()]
    print(result)
except:
    print('Capital unknown')
