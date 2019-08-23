class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    if self.current == self.capacity:
      self.storage[0] = item

    self.storage[self.current] = item
    self.current += 1
    return self.storage

  def get(self):
    pass