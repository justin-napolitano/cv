# Schpotify Install and config

[Github](https://github.com/hnarayanan/shpotify)

## Brew Install

Just use brew and make your life easier. 

:::{code-block} Bash

brew install shpotify


## Create an App at the Spotify Developer Dashboard

[Go Here](https://developer.spotify.com/console/)

Create an app and take note of the client id and the client secret. 


## Create .shpotify.cfg

In order for the application to run you will need to create teh .shpotify.cfg file in your home directory. 

:::{code-block} Bash

cd ~ && touch .shpotify.cfg

:::

Add CLIENT_ID AND CLIENT_SECRET to the file. 

:::{code-block} Bash

#vim/nano/vi/emacs/code etc

vim .sphotify.cfg

# enter the values from the spotify application

CLIENT_ID=<your id here>
CLIENT_SECRET=<your secret here>

:::

## Add shpotify to your path.  

If you installed with home brew the shpotify script should be at 

:::{code-block} Bash

/usr/local/Cellar/shpotify/2.1/bin

:::

### Fish Terminal

If you use fish them paste the following:

:::{code-block} Bash

fish_add_path /usr/local/Cellar/shpotify/2.1/bin

:::

### ZSH


:::{code-block} Bash

export "/usr/local/Cellar/shpotify/2.1/bin$PATH" >> ~/.zshrc && source ~/.zshrc

:::

## Run Shpotify

:::{code-block} Bash

spotify play

:::
