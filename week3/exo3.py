score = float(raw_input("Enter score:"))

# Score grades
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F

# Check range
if score > 1 or score <0:
	print "Score out of range [0 1]"
	exit()

if score >= 0.9:
	print "A"
elif score >= 0.8:
	print "B"
elif score >= 0.7:
	print "C"
elif score >= 0.6:
	print "D"
else:
	print "F"
