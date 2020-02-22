def es(num):
  lastNum = num * num
  somma = lastNum
  if (lastNum % 2 == 0):
    x1 = lastNum - (num - 1)
    x2 = x1 - num
    somma = x1 + x2
    lastNum = x2
    num -= 1
  while lastNum > 1:
    for idx in range(4):
      lastNum -= (num - 1)
      somma += lastNum
    num -= 2
  return somma