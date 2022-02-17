#!/bin/bash
#build and deploy script
cname=cv.jnapolitano.io
RED='\033[0;31m'
PINK='\033[38;5;206m'
PURPLE='\033[1;35m'
NC='\033[0m' # No Color
# Define a timestamp function
timestamp() {
  date +"%T-%m-%d-%Y" # current time
}

clean () {
    echo -e ${PINK}cleaning your dirty build onichan
    command make clean > /dev/null
    echo -e ${PURPLE}"Your build is now clean ;)"
}

html () {
    echo -e ${PURPLE}Making your h-h-h-html files.
    command make html &> /dev/null
    echo -e ${PURPLE}I hope the files are to your liking senpai :{}
}
add () {
    echo -e ${PURPLE}Adding changes to git
    command git add . > /dev/null
    echo -e ${PURPLE}Those changes are now added
}

commit () {
    echo -e ${PURPLE}Commiting those changes boss
    command git commit -m "awtocommit on $(timestamp)"
    echo -e ${PURPLE}This branch is up to date!
}

push () {
    echo -e ${PURPLE}Pushing them files sir.  
    command git push 
    echo -e ${PURPLE}pushed them good 4 u 
}

deploy () {
    echo -e ${PURPLE}makey a website now
    command ghp-import -n -p -f -c $cname build/html > /dev/null 
    echo -e ${PURPLE}The site is live at $cname
}

clean && html && add && commit && push && deploy
