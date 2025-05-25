import random


NUM_FLIPS = 10000
STREAK_LENGTH = 6

def generate_coin_flips(n):
    return [random.choice(['H', 'T']) for _ in range(n)]

def count_streaks(flips, streak_len):
    num_streaks = 0
    current_streak = 1

    for i in range(1, len(flips)):
        if flips[i] == flips[i - 1]:
            current_streak += 1
            if current_streak == streak_len:
                num_streaks += 1
        else:
            current_streak = 1  # reset streak

    return num_streaks


flips = generate_coin_flips(NUM_FLIPS)
streak_count = count_streaks(flips, STREAK_LENGTH)

print(f"Number of {STREAK_LENGTH}-long streaks in {NUM_FLIPS} coin flips: {streak_count}")
