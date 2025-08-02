"""Birthday Cake Candles"""

def tallest_candles(candles):
    tallest_candle = candles[0]
    taller_candles = 0
    for i in range(len(candles)):
        if candles[i] > tallest_candle:
            tallest_candle = candles[i]
            taller_candles = 0
        if candles[i] == tallest_candle:
            taller_candles += 1
    return taller_candles

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''