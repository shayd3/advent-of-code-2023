# day 3

## Part 1
This definitely took a bit. Kept getting answers that were too low. Turns out I missed out on an edge case where if the group of numbers came up to an end of a line, it wouldn't be appeneded to the list of num coordinate groups. It would add them to the array but never append them to the main list keeping track of all the groups.

I found this out by taking all of the valid group coordinates and replacing them with "." so that I'm left with all of the invalid groups. I found the one that kept getting missed that should have been considered a valid number group. I then added a check to see if the group was at the end of the line and if so, append it to the list of groups.
