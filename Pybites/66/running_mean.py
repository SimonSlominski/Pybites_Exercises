def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    means = []

    total = 0
    divider = 1

    for i in sequence:
        total += i
        means.append(round(total/divider, 2))
        divider += 1

    return means
