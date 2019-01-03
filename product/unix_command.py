# Unix commands

(1) grep
'''
    It is used to global search for the regular expression.

    Syntax:
    grep [options][pattern][file]
    
'''
import ssh_import_id
from difflib import diff_bytes
grep ^"Grep" file.txt
#it is search "Grep" at the starting of line. if found in file then return.

grep $"output" file.txt
#it is search "output" at the ending of line. if found in file then return.

grep ."s" file.txt

#it is used to find a charater at starting and ending at any position in file.

grep "\m\a" file.txt

#it is used to match all the in file contain string "ma".

grep ['aeiou'] file.txt

#it is used to match vowel in file.

grep [0-9] file.txt
grep [^0-9] file.txt

#it is used to match 0 to 9 in file and [^0-9] is expect it return.


(2) vi

vi file.txt

#It is used to create a file.            

(3) vim

vim file2.txt

#It is used to create a file. exit and save :x 

(3) tar
tar -cvf  new.tgz internship
#it is used to create a filename.tar compress file

(4) find
#It is used to find and locate file by permission,file type,group,date and size.

find . -name file.txt

find /home -name file.txt

find /home -iname FILE.txt

(5) ssh

# it ised to from loging into remote machine.and terminal access,file transfer.

sort file2
#sort file2 

sort file2 > output.txt
sort  -o ouput.txt file2
cat output.txt

#file2 output store in ouput.txt file.

(6) diff

# it is used to get difference between two files.
diff file2 ouput.txt

(7) export

# it is used to Set export attribute for shell variables.

