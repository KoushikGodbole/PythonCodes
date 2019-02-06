def electionWinner(votes):
    voters = {}
    for i in range(0,len(votes)):
        if votes[i] in voters:
            voters[votes[i]] += 1
        else:
            voters[votes[i]] = 1
    max = 0
    winner = None
    for key, val in voters.items():
        if max < val:
            max  = val
            winner = key
        elif max == val:
            if winner < key:
                winner = key
    return winner

