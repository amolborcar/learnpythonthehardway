age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")
# book says this shouldn't work but it appears to...
print "How old are you?", raw_input()

print "So, you're %r years old, %r inches tall, and %r pounds heavy." % (age, height, weight)