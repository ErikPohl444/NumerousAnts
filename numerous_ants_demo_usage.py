from numerousantsasynch import NumerousAntsAsynch

answer1 = 'x'
answer2 = 'yes'
answer3 = 'no'


def trial1(answer):
    if not (answer == 'yes' or answer == 'no'):
        return True
    else:
        return False


def trial2(answer):
    if answer not in ('yes', 'no'):
        return True
    else:
        return False


def trial3(answer):
    if answer not in ['yes', 'no']:
        return True
    else:
        return False


def trial4(answer):
    if answer not in {'yes', 'no'}:
        return True
    else:
        return False


def trial5(answer):
    if answer not in {'yes'} and answer not in {'no'}:
        return True
    else:
        return False


def trial6(answer):
    if not {'yes', 'no'}.issuperset({answer}):
        return True
    else:
        return False


def trial7(answer):
    dd = {'yes': 'yes', 'no': 'no'}
    try:
        dd[answer]
        return False
    except KeyError:
        return True


def trial8(answer):
    if {'yes', 'no'}.isdisjoint({answer}):
        return True
    else:
        return False


def trial9(answer):
    if len({'yes', 'no'}.intersection({answer})) == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    algorithms = [
        ('trial1', trial1),
        ('trial2', trial2),
        ('trial3', trial3),
        ('trial4', trial4),
        ('trial5', trial5),
        ('trial6', trial6),
        ('trial7', trial7),
        ('trial8', trial8),
        ('trial9', trial9)
    ]
    inputs = [answer1, answer2, answer3]
    anthill = NumerousAntsAsynch(trial1, algorithms, inputs, 20000000)
    anthill.formicate()
    anthill.resultput()
