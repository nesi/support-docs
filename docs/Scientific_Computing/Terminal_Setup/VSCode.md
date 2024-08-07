---
created_at: 2024-08-05
description: How to set up Visual Studio Code to access the NeSI cluster
tags: [vscode]
---

'Visual Studio Code' (not to be confused with 'Visual Studio') or 'VSCode', is a popular editor/IDE that with many useful extensions. The 'Remote' extension allows you to connect to a remote computer (like NeSI).

## Setup

!!! prerequisite
    - Mac or Linux users must have first set up an `~/.ssh/config` file as described in
    [Terminal Setup](../Terminal_Setup).
    - Windows users... coming soon.

* Open the 'Extensions' Tab, search `remote` and make sure you have 'Remote - SSH' and 'Remote Explorer' by Microsoft, installed.

![vscode remote extension](../../../assets/images/vscode-remote.png)

## Connecting

Under the 'Remote Explorer' Tab on the left, you should now see the NeSI machines (as well as any other machines configured in your `~/.ssh/config` file)

![vscode explorer](../../../assets/images/vscode-explorer.png)

You will then be prompted for your password and second fator, as per usual.

!!! warning
    As VSCode will continue attempting to reconnect after a failure,
    take care that you do-not get locked out for too many failed login attempts.


## Features

## Environment Setup
