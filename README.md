---
    title: Pikchr Starter Kit
    author: J. Random Author
    date: December 3, 2022
---

This project contains examples of how to:

- render pikchr diagrams into PNG format using inkscape
- make PDFs from markdown documents with internal pikchr diagrams

# Requirements

## With Nix

If you have the Nix package manager installed, just run `./build`. Or run
`nix-shell` and then inside the nix-shell, run `doit`.

## Without Nix

Without Nix, you'll need to have have these tools installed and in your PATH:

- [doit](https://pydoit.org/)
- fossil
- inkscape
- [pandoc](https://pandoc.org/MANUAL.html#pandocs-markdown)
- [pikchr](https://pikchr.org)

Then run `doit`. It will build an example PDF and PNG.

# How It Works

It uses [doit](https://pydoit.org/) as a build tool. Look inside `dodo.py`
to see the pikchr, pandoc, and inkscape commands that are used.

```pikchr
box "doit"
arrow
box "pandoc"
```

# Credits

The 'pikchr.lua` code comes from
[pikchr-filter](https://code.jboy.space/pikchr-filter/doc/trunk/README.md)
