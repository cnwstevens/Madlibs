from madlibs import scary, teacher, olympics
import random

if __name__ == "__main__":
  new_madlib = random.choice([teacher, scary, olympics])
  new_madlib.madlib()