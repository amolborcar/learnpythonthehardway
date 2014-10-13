x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" % (binary, do_not)

print x
print y

# The %r here shows the single quotes '' in the output.  %r is for the raw variable type
print "I said: %r." % x

# The %s here does not show the quotes, which is why I put them in manuallly
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

# When added, these strings are basically just concatenated
w = "This is the left side of..."
e = "a string with a right side."

print w + e