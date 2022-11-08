# Compute the number of seconds in a given number of hours, minutes, and seconds.

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

# Test 1 - Select the following lines and use ctrl+shift+k to uncomment.
#hours = 7
#minutes = 21
#seconds = 37


# Test 2 - Select the following lines and use ctrl+shift+k to uncomment.
#hours = 10
#minutes = 1
#seconds = 7


# Test 3 - Select the following lines and use ctrl+shift+k to uncomment.
#hours = 1
#minutes = 0
#seconds = 1


###################################################
# Hours, minutes, and seconds to seconds conversion formula
# Student should enter formula on the next line.



###################################################
# Test output
# Student should not change this code.

hours1 = 7
minutes1 = 21
seconds1 = 37
total_seconds1 = (hours1 * 60 + minutes1) * 60 + seconds1

hours2 = 10
minutes2 = 1
seconds2 = 7
total_seconds2 = (hours2 * 60 + minutes2) * 60 + seconds2

hours3 = 1
minutes3 = 0
seconds3 = 1
total_seconds3 = (hours3 * 60 + minutes3) * 60 + seconds3


print ("Test1 " + str(hours1) + " hours, " + str(minutes1) + " minutes, and")
print (str(seconds1) + " seconds totals to " + str(total_seconds1) + " seconds.\n")

print ("Test2 " + str(hours2) + " hours, " + str(minutes2) + " minutes, and")
print (str(seconds2) + " seconds totals to " + str(total_seconds2) + " seconds.\n")

print ("Test3 " + str(hours3) + " hours, " + str(minutes3) + " minutes, and")
print (str(seconds3) + " seconds totals to " + str(total_seconds3) + " seconds.\n")



###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
# Test 1 output:
#7 hours, 21 minutes, and 37 seconds totals to 26497 seconds.

# Test 2 output:
#10 hours, 1 minutes, and 7 seconds totals to 36067 seconds.

# Test 3 output:
#1 hours, 0 minutes, and 1 seconds totals to 3601 seconds.