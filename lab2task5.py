def isTriangle(a, b, c):
  mx = max(a, b, c)
  return (mx < a+b+c-mx)
