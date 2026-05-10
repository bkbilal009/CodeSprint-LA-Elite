import sys

def SneakyLin():
    try:
        try_string = input()
        if not try_string:
            return 
        total = int(try_string)
    except EOFError:
        return

    for __ in range(total):
        # Yahan bhi input() khali rakha hai
        line1 = input().split()
        if not line1:
            break
        number = int(line1[0])
        K = int(line1[1])

        levels = list(map(int, input().split()))
        total_sneakiness = 0
        negatives = []

        for s in levels:
            if s > 0:
                total_sneakiness += s
            elif s < 0:
                negatives.append(abs(s))

        negatives.sort(reverse=True)

        for f in range(len(negatives)):
            profit = negatives[f]
            penalty = (f + 1) * K

            if profit > penalty:
                total_sneakiness += (profit - penalty)
            else:
                break

        print(total_sneakiness)

if __name__ == "__main__":
    SneakyLin()