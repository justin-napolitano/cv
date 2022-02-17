:::{post}
:tags: python, programming, sphinx
:category: Reference, Tutorials
:author: Justin Napolitano
:location: TX
:language: en
:::



# Getting Started

## Git and Gh CLI

If you have not installed git and gh on your system I would recommend starting [here](gh_install)

## Clone the Repository

Begin by cloning the repository by pasting: 

:::{code-block} bash

git clone https://github.com/justin-napolitano/cv

:::

# Setting up your Development Environment

## Dependencies

### Python

Install Python if you have not already done so.

Reference can be found [here](python_install)

### virtualenv

Ensure virtualenv on your system.  

Reference can be found [here](virtualenv_install)

## Creating Your virtual environment

I would recommend creating a virtualenv directory in you home directory for easy access. 

### CD to the home directory and create the venv dir. 

:::{code-block} Bash

cd ~/ && mkdir venv

:::

### Initialize the venv

Run the virtualenv command from your shell with the system-site-packages to enable the venv to bootstrap into existing packages on your system.  

:::{code-block} Bash

virtualenv --system-site-packages venv/sphinx-cv

:::

### Activate the venv

Depending on your shell environment you will be activating via a script located in the venvs bin directory.  I'll include bash, zsh, and fish directions.  If you are using other shells than you most likely know what to do already.  

#### Cd to the bin and list the files.  

:::{code-block} Bash

cd ~/venv/sphinx-cv/bin && ls

:::

When you run the previous commmands you will see listed before you the files within the bin.  The important ones are titled activate followed by a file extension.  

#### Fish Activation

Within the bin directory of your venv run 

:::{code-block}

source activate.fish

:::


#### Shell and ZSH Activation

Within the bin directory of your venv run 

:::{code-block}

source activate

:::


## Installing the Dependencies

In order to create this site as is you will need to install a number of packages via pip.   You can view them by reading the requirements.txt file in the project directory.

Run the following within the project directory to install all of the needed dependencies.  Be patient this could take a while.  

:::{code-block} Bash

pip install -r requirements.txt

:::

# Building the site

To build the site as is you can simply run `make html` from a terminal window within the project directory.  You may also run the utility scripts included to clean your build directory for updates or build and push to your github repository.  

## Make html

There is already a make file included with this project. In order to build you will only need to run the following.  

:::{code-block}

make clean && make html
:::

This will clean the build directory and make your project.  

## Scripts

I've also included the files below to enable quicker builds and pushes to your github repostory.  In order for them to run you will most likely need to make them executable on your system.  

### Bash Scripts

* doit.sh
    * Cleans the build directory.
    * Makes the html
    * Pushes to github
* pushit.sh
    * Adds changes
    * Pushes to github. 
* chtml.sh
    * Cleans the build 
    * Creates Html
* pullit.sh
    * Pulls changes from Github
    * Cleans the build directory
    * Builds html
* installit.sh
    * Creates a virtualenvironment called sphinx-site
    * activates the environment
    * Installs the requirements
* deploy.sh
    * deploys to gh-pages
# Pushing to Gh Pages
I've included a script that will create a branch named github pages and push it to github to publish.  


Just make it executable by running. 

:::{code-block} Bash

sudo chmod u+x deploy.sh
:::

:::{code-block} Bash

./deploy.sh
:::


Gh Pages workflow support is coming next


I don't know why the build isn't working.  I guess i'll jus write a script for fun.  Python or rust.. Lets try rust for fun.  




