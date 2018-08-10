##practice from codebat!



def diff21(n):
  if n <= 21:
    return 21 - n
  else:
    return (n - 21) * 2


def shit2(Dominika):
    if Dominika == 22:
        print('tucu this looks like am learning')
        return 22
    else:
        print('I just failed with an error 404')
        return 404


def near_hundred(n):
  return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))



def pos_neg(a, b, negative):
  if negative:
    return (a < 0 and b < 0)
  else:
    return ((a < 0 and b > 0) or (a > 0 and b < 0))



#warmup not_string
def not_string(str):
  if len(str) >= 3 and str[:3] == "not":
    return str
  return "not " + str
  # str[:3] goes from the start of the string up to but not
  # including index 3

