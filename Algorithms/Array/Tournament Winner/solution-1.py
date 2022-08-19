def tournamentWinner(competitions, results):
    # Write your code here.
    teams = {}
    winning_team_val = 0
    winning_team_name = ""
    for comp in competitions:
        if comp[0] not in teams:
            teams[comp[0]] = 0
        if comp[1] not in teams:
            teams[comp[1]] = 0
    for team, result in zip(competitions, results):
        if result == 1:
            teams[team[0]] += 3
            temp_team_name = team[0]
            temp_team_val = teams[team[0]]
        else:
            teams[team[1]] += 3
            temp_team_name = team[1]
            temp_team_val = teams[team[1]]

        if temp_team_val > winning_team_val:
            winning_team_val = temp_team_val
            winning_team_name = temp_team_name

    return winning_team_name
