"""Logger Rate Limiter"""
class Logger:
    
    def __init__(self):
        self.messagesTimestamps = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.messagesTimestamps:
            self.messagesTimestamps[message] = timestamp + 10
            return True
        else:
            if timestamp < self.messagesTimestamps[message]:
                return False
            else:
                self.messagesTimestamps[message] = timestamp + 10
                return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)

'''Complexity Analysis:
Time Complexity: O(1)
Space Complexity: O(1)'''