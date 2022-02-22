import json
import random


class DataHandler:
  def __init__(self, path: str = './input.json'):
    self.path = path

  def load_data(self) -> dict:
    with open(self.path) as file:
      return json.load(file)

  def generate_training_dataframe(self, goal: int, length: int = 100) -> dict[list[int, list[int]]]:
    data = self.load_data()
    res = []
    for _ in range(length):
      random_number = random.randint(0,9)
      goal_number = 0
      if (random_number == goal):
        goal_number = 1
      res.append([ goal_number, data[str(random_number)] ])
    return res
