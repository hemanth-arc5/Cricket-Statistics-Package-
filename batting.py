def batting_average(runs, innings):
    if innings == 0:
        return 0
    return runs / innings


def strike_rate(runs, balls):
    if balls == 0:
        return 0
    return (runs / balls) * 100


def highest_score(scores):
    return max(scores)