# VSCode via OnDemand


## Introduction

NeSI supports the use of [VS Code](https://code.visualstudio.com/) for interactive computing.
VS Code can be a useful tool for developing code with support for many languages including debugging.


## Accessing VSCode on NeSI


VS Code at NeSI can be accessed via [NeSI OnDemand](https://ondemand.nesi.org.nz/) and launching the VS Code application there.


## VS Code user interface


The VS Code application allows you to access interactive computing with NeSI via [VS Code for Web](https://code.visualstudio.com/docs/setup/vscode-web). This provides a browser based VS Code experience including the use of most extensions and debugging tools.

### filesystems


Your VS Code session will start in your home directory the first time you launch it. On subsequent launches it may remember your previous working directory and start there.

NeSI will auto generate a directory within your home folder called `00_nesi_projects`, you will find symbolic links to projects and nobackup directories of your active projects. We do not recommend that you store files in this initial directory because next time you log into OnDemand the directory will be repopulated based on your user groups, instead switch to your home, project or nobackup directories first.

If you wish to not have this folder recreated upon login then please place the following file in your HOME directory `.00_nesi_projects.stop` and this will stop the folder from being recreated upon login.


### VS Code terminal


## Installing VSCode extensions


VS Code has an extensive library of extensions available to improve language support, debugging and more.


## External documentation
- [VS Code](https://code.visualstudio.com/docs)
- [VS Code for Web](https://code.visualstudio.com/docs/setup/vscode-web)
