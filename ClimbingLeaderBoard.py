def climbingLeaderboard(scores, alice_scores, n, m):
    result_array = []
    for i in range(m):
        scores.append(alice_scores[i])
        scores.sort(reverse=True)
        ranks = CalculateRanks(scores)

        if alice_scores[i] in scores:
            index = scores.index(alice_scores[i])
            result_array.append(ranks[index])
    return result_array


def CalculateRanks(scores):
    rank = [1]*len(scores)

    for i in range(1, len(scores)):
        if scores[i] == scores[i-1]:
            rank[i] = rank[i-1]
        else:
            rank[i] = rank[i-1]+1
    return rank


n = int(input())
scores = list(set(map(int, input().split())))
m = int(input())
alice_scores = list(map(int, input().split()))

result = climbingLeaderboard(scores, alice_scores, n, m)
for i in result:
    print(i)
