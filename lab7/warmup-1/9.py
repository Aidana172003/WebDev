def front_back(str):
  if len(str) <= 1:
    return str
  new_string = str[1:len(str)-1]
  return str[len(str)-1] + new_string + str[0]