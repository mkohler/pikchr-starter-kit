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

If you have the Nix package manager installed, just run `nix-shell`.

## Without Nix

Without Nix, you'll need doit, fossil, inkscape, pandoc, and pikchr installed.

# How It Works

It uses [doit](https://pydoit.org/) as a build tool.

```pikchr
box "doit"
arrow
box "pandoc"
```

# References

[Pandoc Markdown](https://pandoc.org/MANUAL.html#pandocs-markdown)


