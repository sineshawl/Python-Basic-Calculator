def colorPicker(row, column):
    background = ''
    if (row == 1 and column == 1) or (row == 2 and column != 3):
        background = '#11394F'  # for special functions (n!, x^2...)
    elif column == 3 and (row != 6 and row != 1):
        background = '#237099'  # for operators "+,-,*,/"
    elif row == 1 and column == 3:
        background = '#D13763'  # for symbol '<-'
    elif row == 6 and column == 3:
        background = '#3E837D'  # for symbol '='
    elif row == 1 and column == 2:
        background = '#8F0726'  # for symbol 'C'
    else:
        background = '#2F5266'  # for all numbers(0-9,.,+/-)
    return background
