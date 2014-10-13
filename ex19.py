def cheese_and_crackers(cheese_count, boxes_of_crackers):
  print "You have %d cheeses!" % cheese_count
  print "You have %d boxes of crackers!" % boxes_of_crackers
  print "That's enough for a party!"
  print "Get a blanket. \n"

print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"

cheese_and_crackers(10 + 20, 10 + 40)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 10, amount_of_crackers + 50)