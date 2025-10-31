# VS Code via OnDemand

## Introduction

NeSI supports the use of [VS Code](https://code.visualstudio.com/) for interactive computing.
VS Code can be a useful tool for developing code with support for many languages including debugging.

## Accessing VS Code on NeSI

VS Code at NeSI can be accessed via [NeSI OnDemand](https://ondemand.nesi.org.nz/) and launching the VS Code application there.

## VS Code user interface

The VS Code application allows you to access interactive computing with NeSI via [VS Code for Web](https://code.visualstudio.com/docs/setup/vscode-web). This provides a browser-based VS Code experience including the use of most VS Code extensions and debugging tools.

### VS Code Profiles and Settings

VS Code allows for saving configurations and settings via several methods.

Settings control the user interface and some behaviors and are saved in a `settings.json` file.

Profiles combine Settings with other aspects of VS Code like Extensions, Keyboard Shortcuts, and Snippets. Profiles can be saved and shared as either GitHub gist URLs or `.code-profile` files. Changes to the Settings or Profile made via the VS Code OnDemand app are saved in your NeSI home folder in the `.local/share/code-server` automatically, so new interactive VS Code sessions should retain your preferences.

Please see the VS Code docs for more information on [Settings](https://code.visualstudio.com/docs/configure/settings), [Profiles](https://code.visualstudio.com/docs/configure/profiles) and VS Code customizations.

### VS Code terminal

The VS Code terminal acts like the Shell Access terminal also available via OnDemand. At present, slurm jobs cannot be submitted via the VS Code terminal and you must use Shell Access.

## Installing VS Code extensions

VS Code has an [extensive library of extensions](https://marketplace.visualstudio.com/VSCode) available to improve language support, debugging, and more.

Some extensions do not work in VS Code for Web and will be marked as unavailable in the Extensions view within the OnDemand VS Code app. For more details please see the [VS Code for Web docs](https://code.visualstudio.com/docs/setup/vscode-web#_extensions).

## External documentation

- [VS Code](https://code.visualstudio.com/docs)
- [VS Code for Web](https://code.visualstudio.com/docs/setup/vscode-web)
