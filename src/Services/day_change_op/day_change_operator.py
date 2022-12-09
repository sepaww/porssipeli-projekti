def summary(stocks, finance, owned):
    """a function to count the networth of player
    Args:
        stocks (matrix): a matrix with each days stocks
        finance (Finance object): Players finance info
        owned (list): the indexes of owned
        stocks and the amount of owned

    Returns:
        int: players networth
    """
    curstock = stocks[-1]
    length = len(curstock)
    sumofmoney = 0
    for i in range(length):
        if owned.owned[i] > 0:
            sumofmoney += curstock[i][1]*owned.owned[i]
    sumofmoney += finance.money

    return sumofmoney


def finance_update(finance, timer):
    """updates the amount of expenses for each day

    Args:
        finance (Finance object): players finance info
        timer (Timer object): timer object containing the
        current day, which is used to determine the
        raise of expenses
    """

    finance.money -= finance.exp
    finance.money += finance.inc
    if timer.day > len(finance.explist)-1:
        finance.exp += finance.standard_exp_increase
        finance.exp += timer.day*2
    else:
        finance.exp += finance.explist[timer.day]