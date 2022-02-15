# Oh My Fish Installation


:::{code-block} Bash

curl -L http://get.oh-my.fish | fish

:::

This will add the config files to the .config directroy in your home folder.  

# Adding Plugins

## Tab

similar to zsh term, allows u to open new tab with current directory

:::{code-block} Bash

omf install tab

:::
## Brew

Add all brew paths to fish $PATH

:::{code-block} Bash
omf install brew
:::

## SSH 

`https://github.com/oh-my-fish/plugin-ssh`

:::{code-block} Bash

omf install ssh
:::

## SSH Term Helper

used to make ssh term colors consistent

`https://github.com/oh-my-fish/plugin-ssh`

:::{code-block} Bash

omg install ssh-term-helper

:::


# Further Customization

## Powerline 
 

Install Powerline if you are using a theme that requires it.  

Review the installation instructions `HERE <https://powerline.readthedocs.io/en/latest/installation/osx.html>` for more information.

:::{code-block} Bash

pip install --user powerline-status

:::

### Powerline Fonts

Install the powerline fonts

:::{code-block} Bash

git clone https://github.com/powerline/fonts.git && sudo ./fonts/install.sh

:::


