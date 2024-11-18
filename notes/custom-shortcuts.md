# Custom shortcuts

- shortcuts for text editor and jupyter notebooks

## open shortcuts settings

- `cmd + shift + p`
- `>Open Keyboard Shortcuts`
- or `>Open Keyboard Shortcuts (JSON)`

## Change keyboard shortcuts json example

- open the json settings (see above)
- insert the following shortcuts (and change if needed)

```json
// Place your key bindings in this file to override the defaultsauto[]
[
    {
        "key": "cmd+[Semicolon]",
        "command": "workbench.action.terminal.new"
    },
    {
        "key": "cmd+[Backslash]",
        "command": "editor.action.commentLine",
        "when": "editorTextFocus && !editorReadonly"
    },
    {
        "key": "shift+cmd+7",
        "command": "-editor.action.commentLine",
        "when": "editorTextFocus && !editorReadonly"
    },
    {
        "key": "shift+backspace",
        "command": "jupyter.restartkernelandrunallcells",
        "when": "notebookEditorFocused && !inputFocus"
    },
    {
        "key": "shift+d",
        "command": "notebook.cell.executeCellAndBelow",
        "when": "notebookEditorFocused && !inputFocus"
    },
    {
        "key": "ctrl+shift+backspace",
        "command": "notebook.clearAllCellsOutputs",
        "when": "notebookEditorFocused && !inputFocus"
    }
]
```
