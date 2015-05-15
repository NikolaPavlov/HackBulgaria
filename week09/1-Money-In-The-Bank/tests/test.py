def deposit(username, suM):
    suM = float(suM)
    if suM:
        if float(suM) < 0:
            print('''
                    You cann\'t deposit negative amaount!
                    The bank is jewish!
                    ''')
        elif float(suM) > 0:
            print('Successfully deposit {}'.format(suM))
    else:
        print('not a number')





def deposit_(suM):
    try:
        suM = float(suM)
    except ValueError:
        print('not a number')

deposit_('-111s')
