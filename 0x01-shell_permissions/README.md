An updated README to give a fuller understanding of what we are doing, for my own benefit as well.
0. Using the su command to change to user betty
1. Using either the whoami command or id -un to print effective userid.
2. Using the groups command to print groups that the current user is a part of.
3. Using the chown command to change owner to betty.
4. Using the touch command to create an empty file called hello. I did not write hello for the file and simply named it 'empty' instead and the code passed.
5. Using the chmod command with the u+x option to add execute permissions to the owner of the specified file.
6. Somewhat more complicated, used the chmod command again, this time with the option ug+x,o+r to allow for reading for the others and execute for group and user.
7. Used the chmod command, this time with a+x to give all users execute permission.
8. Used chmod 007 hello to give only other users any permission.
9. Used chmod 753 hello to give the appropriately outlined permissions based on the written format.
10. Used chmod with the --reference option to copy the permissions from olleh to hello.
11. Used chmod -R a+X . to give all subdirectories execute permissions without affecting regular files. The capital 'X' is key to only influence directories.
12. Used mkdir command along with the specified numerical permission followed by the new directory name to create it with those permissions already allowed.
13. Used the chgrp command to change the group to the specified one with the specified file.
14. Used command chown holberton:betty * to change all files and directories to those groups and owners.
15. Used again the chown command, this time with a -h operator to account for the symlink and followed it instead with the _hello file instead of *.
16. Used the chown command again with the operator --from=guillaume to specify that all files being changed should be from that user only.
17. Made Star Wars play on the console.
18. Created a man page for Holberton based on a given photo to match. 