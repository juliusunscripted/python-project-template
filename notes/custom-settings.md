# custom settings

## workspace settings

- see workspace settings in file `.vscode/settings.json`

## user settings

- press `cmd + ,`
- or `>Open User Settings (JSON)`


### a few example settings

```json
{
    // https://gist.github.com/suiluj/5b4480e61ac560549cef3b1a9d469977
    "telemetry.telemetryLevel": "off",
    "workbench.startupEditor": "none",
    "vim.startInInsertMode": true,
    "[python]": {
        "editor.defaultFormatter": "ms-python.black-formatter",
        "editor.formatOnSave": true
    },
    "notebook.formatOnSave.enabled": true,
    "jupyter.interactiveWindow.textEditor.executeSelection": true,
    "gitlens.plusFeatures.enabled": false,
    "gitlens.graph.statusBar.enabled": false,
    "git.enableSmartCommit": true,
    "git.confirmSync": false,
    "git.autofetch": true,
    "files.trimFinalNewlines": true,
    "files.insertFinalNewline": true,
    "jupyter.askForKernelRestart": false,
    "notebook.output.scrolling": true,
    "notebook.markup.fontSize": 14,
    // without vim override copy the cursor goes into command mode after copying text which is annyoing
    "vim.overrideCopy": false,
    // only important for windows
    // "vim.handleKeys": {
    //     "<C-c>": false,
    //     "<C-x>": false,
    //     "<C-w>": false,
    //     "<C-a>": false
    // },

    // do not reload old terminal session on next vscode start
    "terminal.integrated.persistentSessionReviveProcess": "never",
    // paste system clipboard text with p in command mode
    "vim.useSystemClipboard": true
}
```
