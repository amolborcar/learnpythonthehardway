
def loop_while(final_num, incr):
  i = 0
  numbers = []

  while i < final_num:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + incr
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i

  print "The numbers: "

  for num in numbers:
    print num

loop_while(10, 2)