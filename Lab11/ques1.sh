1.i) after i gave this command, ls -l . newdir 1>presentfiles 2>filesnotpresent the files got redirected to presentfile and since newdir exists and it has no errors so nothing got transferred to filesnotpresent hence filenotpresent remains empty

1.ii) the command ls -l . newdir >listoffiles displays the details of the current directory and newdir, and redirects the output to listoffiles, since both directories exist, their details are stored in listoffiles and there is no error output.
