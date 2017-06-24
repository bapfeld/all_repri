# all_repri
This extension is meant to take all items in a todo.txt file that have a priority level
and reprioritize them all at once. Default is to move everything up one level, but 
user can specify number of levels and whether shift is up or down in priority.

If items are already prioritized A, they will maintain the A priority status if 
shift is upward. If items are already prioritized Z, they will maintain Z priority
status if shift is downward.

Items that have no priority will stay unprioritized.

## Usage
`t all_repri 2` shifts all prioritzied items up two levels.

`t all_repri -1` shifts all prioritized items down one level.
