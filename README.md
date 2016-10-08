# Non-ASCII-Nixnote-fixer
Trying to fix non-ASCII characters decoding error in Nixnote2 beta, using Python scripts

I made this simple script and hoping it may be helpful, but there is still no warranty, so, again, use it with your own risk.

Before executing the script, you have to

1.install python 3.X interpreter （I use 3.5; you can find it here: https://www.python.org/downloads/ ）

2.edit this script with a text editor of your choice, and replace the line:

  conn = sqlite3.connect(r'/home/[user name]/.nixnote/db-1/nixnote.db')

with

  conn = sqlite3.connect(r'/your/path/to/nixnote.db')
  
3.Better backup your nixnote.db file and set Nixnote to "Disable upload to server" 

4.execute this script

5.Check the note which was decoded wrong before

6.Enable upload to server if everything goes well locally, and pray for that everything goes well too on the Evernote server

