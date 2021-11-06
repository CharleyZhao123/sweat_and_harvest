class CQueue:

    def __init__(self):
        self.val = []


    def appendTail(self, value: int) -> None:
        self.val.append(value)


    def deleteHead(self) -> int:
        if not self.val:
            return -1
        else:
            return self.val.pop(0)



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()