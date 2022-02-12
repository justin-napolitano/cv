# Fish Installation

## Brew Install Fish

:::{code-block} Bash

brew install fish
:::

## Add Fish to the Shell Listings.. Nix systems.

Copy paste the below into your terminal.

:::{code-block} Bash

sudo echo '/usr/local/bin/fish' >> /etc/shells

:::

If your system will not permit the write then manually edit the file at /etc/shells with your preferred editor.  


## Change the Shell to Fish

Copy/paste 

:::{code-block} Bash

chsh -s /usr/local/bin/fish

:::

