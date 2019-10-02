import sys
import json
import os
import argparse

def default_parameters():
    return {
        'Group_1':
        { 
            'String' : 'Strung',
            'Integer' : 50,
            'List' : [1, 2, 3, 4],
            'Bool' : True
        }, 
        'Group_2':
        {
            'Subgroups' :
            {
                'Food' : 'Banana',
                'Drink' : 'Sprite'
            }
        },
        'Group_3':
        {
            'Subgroup_With_Subgroups' :
            {
                'Elements' : 
                {
                    'Hydrogen' : 'H',
                    'Helium' : 'He',
                    'Carbon' : 'C',
                    'Iron' : 'Fe'
                },
                'Operators' : 
                {
                    'Add' : '+',
                    'Subtract' : '-',
                    'Multiply' : 'x',
                    'Divide' : '/'
                }
            }
        }
    }

def output_json(): 
    print(json.dumps(default_parameters(), indent = 4))

def find_missing(defaults, user_parameters, missing_parameters = {}, updated_parameters = {}):
    for key in defaults.keys():
        if key not in user_parameters.keys():
            missing_parameters[key] = 'MISSING'
            updated_parameters[key] = defaults[key]
        else:
            if type(defaults[key]) == dict:
                if type(user_parameters[key]) == dict:
                    missing_parameters[key], updated_parameters[key] = find_missing(defaults[key], user_parameters[key], user_parameters[key], defaults[key])
                else:
                    updated_parameters[key] = defaults[key]
                    missing_parameters[key] = 'MISSING'
            else:
                updated_parameters[key] = defaults[key]
                missing_parameters[key] = 'PRESENT'
    return missing_parameters, updated_parameters


def get_complete_json(): #Checks parameters.json for errors, prints errors, returns corrected list of params
    path = 'parameters.json'
    defaults = default_parameters()
    try:
        data = json.load(open(path))
    except:
        print('Invalid JSON file format.',) 
        return default_parameters()

    print('JSON file format valid\nChecking parameters...')    

    missing_parameters, updated_parameters = find_missing(defaults, data)
    print('missing_parameters:')
    #print(missing_parameters)
    print(json.dumps(missing_parameters, indent = 4))
    print('updated_parameters:')
    #print(updated_parameters)
    print(json.dumps(updated_parameters, indent = 4))
    return data

def main():
    parser = argparse.ArgumentParser(description = 'Checks parameters.json for validitiy')
    exclusive = parser.add_mutually_exclusive_group(required = True)
    exclusive.add_argument('-f', '--jsonformat', action='store_true', help='Show valid json format and exit')
    exclusive.add_argument('-j', '--jsoncheck', action='store_true', help='Check if json file is valid and exit') 
    args = parser.parse_args()
    if args.jsoncheck:              
        get_complete_json()
        sys.exit(0)
    elif args.jsonformat:
        output_json()
        sys.exit(0)

if __name__ == '__main__':
    main()