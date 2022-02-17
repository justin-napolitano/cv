(header_target)=brew_install
# Brew Install

## Installing Command Line Tools for Mac.

:::{code-block} bash

xcode-select --install

:::

## Run the Install Script

:::{code-block} bash

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"

:::

## Add Brew to you path 

:::{code-block} Bash 

#First Command
echo ‘eval “$(/opt/homebrew/bin/brew shellenv)”’ >> /Users/cpo/.zprofile

#Seccond Command
eval “$(/opt/homebrew/bin/brew shellenv)”

:::

