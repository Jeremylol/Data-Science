import pandas as pd


titanic = 'titanic_data.csv'

# ***** Accurate_heuristic does not calculate the accuracy properly *****
def accurate_heuristic(heuristic):

    titanicFile = pd.read_csv(titanic)
    predictions = heuristic(titanic)

    correct = pd.DataFrame(index=predictions.keys(), data=predictions.values(), columns=['Survived'])
    print('{:.3f}% correct'.format(100 * (correct == titanicFile[['PassengerId', 'Survived']].set_index('PassengerId')).values.sum() / len(correct)))
    return None

def first_heuristic(titanic):
    predictions = {}
    titanicFile = pd.read_csv(titanic)

    for _, passenger in titanicFile.iterrows():
        passenger_id = passenger['PassengerId']

        # assume all [women] survived
        if passenger['Sex'] == 'female':
            predictions[passenger_id] = 1
        else:
            predictions[passenger_id] = 0
    return predictions

print("First heuristic", first_heuristic(titanic))

def second_heuristic(titanic):
    predictions = {}
    titanicFile = pd.read_csv(titanic)
    for _, passenger in titanicFile.iterrows():
        passenger_id = passenger['PassengerId']

        # assume that all [women] and [children in first class] survived
        if passenger['Sex'] == 'female' or (passenger['Age'] < 18 and passenger['Pclass'] == 1):
            predictions[passenger_id] = 1
        else:
            predictions[passenger_id] = 0
    return predictions

print("Second heuristic",second_heuristic(titanic))

def third_heuristic(titanic):
    predictions = {}
    titanicFile = pd.read_csv(titanic)
    for _, passenger in titanicFile.iterrows():
        passenger_id = passenger['PassengerId']

        # assume that all [women] and [children != 3rd class] survived
        if (passenger['Sex'] == 'female' or passenger['Age'] < 15) and passenger['Pclass'] != 3:
            predictions[passenger_id] = 1
        else:
            predictions[passenger_id] = 0
    return predictions

print("Third heuristic",third_heuristic(titanic))