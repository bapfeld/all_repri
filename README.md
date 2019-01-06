# all_repri
This extension is meant to take all items in a todo.txt file that have a
priority level and re-prioritize them all at once. Default is to move everything 
up one level, but function takes argument to specify number of levels and
whether shift is up or down in priority.

To move a function down in priority, simply use a negative integer.

If items are already prioritized A, they will maintain the A priority status
if shift is upward. If items are already prioritized Z, they will maintain Z
priority status if shift is downward. Items cannot be prioritized beyond these
bounds (i.e.a 2 level shift for a (B) priority item will only change it one
level to (A) priority.

Items that have no priority will stay unprioritized.

## Installation
Clone this repo into your .todo.actions.d directory

`git clone https://github.com/bapfeld/all_repri`

Alternatively clone it somewhere else and create an symbolic link in your
.todo.actions.d directory to the all_repri binary. If you prefer to type e.g.
`t repri` or `t rp` instead of `t all_repri`, just choose e.g. `repri` / `rp`
as the file name of the symbolic link.

## Usage
`t all_repri 2` shifts all prioritized items up two levels.

`t all_repri -1` shifts all prioritized items down one level.

## Other Notes
`all_repri` is written using python3

Comments and PRs welcome, but this is a low priority task and I cannot promise
to fix any bugs.
