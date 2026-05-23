def economy_rate(runs, overs):
    if overs == 0:
        return 0
    return runs / overs


def bowling_average(runs, wickets):
    if wickets == 0:
        return 0
    return runs / wickets


def best_figures(figures):
    """
    figures format:
    [(wickets, runs), (wickets, runs)]
    Example:
    [(3, 25), (5, 40), (4, 20)]
    """

    best = figures[0]

    for figure in figures:
        if figure[0] > best[0]:
            best = figure
        elif figure[0] == best[0]:
            if figure[1] < best[1]:
                best = figure

    return best