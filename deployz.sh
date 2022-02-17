#!/bin/bash
#build and deploy script
pid=$!
cname=cv.jnapolitano.io
RED='\033[0;31m'
PINK='\033[38;5;206m'
PURPLE='\033[1;95m'
JUSTIN='\033[38;5;206;48;5;57m'
UNICORN='\U1F984'
HEART='\xF0\x9F\x92\x9C'
BHEART='\xF0\x9F\x92\x94'
NC='\033[0m' # No Color
KISS='\xF0\x9F\x98\x98'
CWEEN='\xF0\x9F\x98\x8B'
PWEASE='\xF0\x9F\x98\xB3'
HOPE='\xF0\x9F\x98\x85'
HAPPY='\xF0\x9F\x98\x81'
ANGEL='\xF0\x9F\x98\x87'
BOSS='\xF0\x9F\x98\x8E'
KISSY='\xF0\x9F\x98\x99'
DEVIL='\xF0\x9F\x98\x88'
MAKEY='\xF0\x9F\x98\xAE'
MMM='\xF0\x9F\x98\x9B'
TASKS=6

sp[0]="${HEART}"
sp[1]="${BHEART}"


# Define a timestamp function
timestamp() {
  date +"%T-%m-%d-%Y" # current time
}



clean () {
    printf "${PURPLE}Cleaning your dirty build OnIChan $HEART"
    command make clean > /dev/null
    printf "\n  All cween ${CWEEN}"

}

html () {
    printf "\nMaking your h-h-h-tml files... p-p-Wease be pazient wif me ${PWEASE}"
    command make html &> /dev/null
    printf "\n  I hope the files are to your liking senpai ${HOPE}"
}
add () {
    printf "\nAdding changes to git ${happy}"
    command git add . > /dev/null
    printf "\n  git changed"
}

commit () {
    printf "\nCommiting those changes boss ${ANGEL}"
    command git commit -m "awtocommit on $(timestamp)"
    printf "\n  Committed ${BOSS}"
}

push () {
    printf "\nPushing them files sir ${KISSY}"
    command git push  &>/dev/null 
    printf "\n  pushed them good 4 u ${DEVIL}"
}

deploy () {
    printf "\nmakey a website now ${MAKEY}"
    command ghp-import -n -p -f -c $cname build/html &>/dev/null 
    printf "\n  mmm ${MMM} site is live at $cname"
}

progress () {
    i=0
    while kill -0 $pid 
    do
        i=$(( (i+1) %2 ))
        printf "${spin{$i}}"
        sleep .5
    done
}
fakeProgress () {
    i=0
    j=0 
    while [ $j -le 5 ]
    do
        ((j++))
        i=$(( (i+1) %2 ))
        printf "${sp[$i]}"
        
        sleep .5
    done 
}
getpid () {
    pid=$!
}

spin() {
   printf "\b${sp:sc++:1}"
   ((sc==${#sp})) && sc=0
}
endspin() {
   printf "\r%s\n" "$@"
}

clean && html && add && commit && push && deploy

