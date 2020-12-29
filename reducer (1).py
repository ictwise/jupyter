#example mapreduce job in python

#!/usr/bin/env python
 
import sys
 
last_key = None
running_total = 0
 
for input_line in sys.stdin:

#this gets input, either from the mapper or elsewhere

   input_line = input_line.strip()

#strips out all of the spaces

   this_key, value = input_line.split("\t") # 1 relates to the maximum number of splits. It will become more important later.

#splits the key and the value from the mapper and assigns variables to them both this_key and value

   value = int(value)

   #makes sure that value is an integer not a string

   if last_key == this_key:

#best to look at the else statement first, but basically, if the same key appears more than once...
       running_total += value

       #increase the running total by one

   else:
       if last_key:
           print( "%s\t%d" % (last_key, running_total))

           # if it's the last time the key is referred the is a print out, referencing the above IF statement if it has been used.
           #as the original last_key va, lue was None (null) nothing will be printed, as a null statement can't reference itself
       
       running_total = value

       # the running_total gets assigned to the value before the loop goes round again
       last_key = this_key
       # last_key variable is changed before the loop goes round again
 
if last_key == this_key:
   print( "%s\t%d" % (last_key, running_total))
   

   #this exists to make sure that the last value of the mapper is printed at the end of the loop 
   #i.e the last key from the list provided by the mapper
 
