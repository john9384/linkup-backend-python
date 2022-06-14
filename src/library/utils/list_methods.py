def filter_list_none(list_to_filter):
  filtered = filter(lambda item: item != None, list_to_filter)
  return list(filtered)


def list_diff(l1, l2):
  l1.sort()
  l2.sort()
  set_difference = set(l1) - set(l2)
  list_difference = list(set_difference)
  if(list_difference):
    return list_difference
  else:
    return False
