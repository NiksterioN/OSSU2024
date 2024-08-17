 
- Read man ls and write an ls command that lists files in the following manner
    - Includes all files, including hidden files
    - Sizes are listed in human readableformat (e.g. 454M instead of 45279954)
    - Files are ordered by recency
    - Output is colorized

```
ls -lhat --color=auto
```

- Write bash functions marco and polo that do the following. Whenever you execute marco the current working directory should be saved in some manner, then when you execute polo, no matter what directory you are in, polo should cd you back to the directory where you executed marco. For ease of debugging you can write the code in a file marco.sh and (re)load the definitions to your shell by executing source marco.sh.

./marco.sh stores in a variable the present working directory.
./polo.sh reads the variable and changes directory to that directory

See marco.sh and polo.sh


- Say you have a command that fails rarely. In order to debug it you need to capture its output but it can be time consuming to get a failure run. Write a bash script that runs the following script until it fails and captures its standard output and error streams to files and prints everything at the end. Bonus points if you can also report how many runs it took for the script to fail.


Do a while loop to check the status code of the ./some_fun
If the status code does not equal to 1, increment the call counter and call ./some_fun.
Otherwise print the call counter variable.

See ./debug_script.sh and ./some_script.sh

- As we covered in the lecture find’s -exec can be very powerful for performing operations over the files we are searching for. However, what if we want to do something with all the files, like creating a zip file? As you have seen so far commands will take input from both arguments and STDIN. When piping commands, we are connecting STDOUT to STDIN, but some commands like tar take inputs from arguments. To bridge this disconnect there’s the xargs command which will execute a command using STDIN as arguments. For example ls | xargs rm will delete the files in the current directory.

    - Your task is to write a command that recursively finds all HTML files in the folder and makes a zip with them. Note that your command should work even if the files have spaces (hint: check -d flag for xargs).

```
find . -type f -name "*.html" | xargs -d '\n' tar -cvzf html_only.tar.gz 
```

- (Advanced) Write a command or script to recursively find the most recently modified file in a directory. More generally, can you list all files by recency?

```
find . -type f | xargs -d '\n' ls -t | head -n1
```
