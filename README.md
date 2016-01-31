# cu-unis

Aim: Generate a better directory for Columbia University, including an API.

Each student has a folder in UNIX where the title is their UNI.

./
../u
../1 through 11
.../a through z
..../unis beginning with that letter
...../unique folder each student SSHs into

By going into one of the numbered folders (e.g. /u/10), you can use a bash script to get all of the unis. Ex:

find . -maxdepth 2 -type d > ../[number folder your uni is in]/[first letter of your uni]/[your uni]/[text file]