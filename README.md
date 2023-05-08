latex-fontawesome6
=================

Original project is [Jan-Hendrik Dolling's latex-fontawesome5](https://github.com/JanHendrikDolling/latex-fontawesome5) and [furl's latex-fontawesome](https://github.com/furl/latex-fontawesome). I edited this project to use latest [FontAwesome](https://fontawesome.com/) icons in XeLaTeX.

The current version of FontAwesome icons used is 6.4.0.

How to Use
----------

### Requirements
* You must have the FontAwesome font on your machine (download from [here](https://fontawesome.com/)).
* You must be using XeLaTeX and have the `fontspec` package installed.
* You can use this package with the free fonts.

### Usage
1. Download the `fontawesome6.sty` file and put it in the same directory as the LaTeX file using the icons.
2. Exctract the `.otf` files (`use-on-desktop` directory inside the downloaded zip) into the font directory in the same directory as the LaTeX file using the icons.
3. Include the package as normal (in the preamble of the `.tex` file, add the line `\usepackage{fontawesome6}`).
4. Use an icon by typing `\faicon{address-book}`. Other icons than `address-book` can be found on the [fontawesome](https://fontawesome.com/icons?d=gallery) website.


### Example

Free version
```tex
\usepackage{fontawesome6}

\faicon{font-awesome}
Normal: \faicon{address-book}
Bold: \textbf{\faicon{address-book}}
```

```bash
$ xelatex example-free.tex
```

Make Latest fontawesome.sty
---------------------------

### Requirements
* You need python to create `fontawesome6.sty` from scratch.
* Download FontAwesome from [here](https://fontawesome.com/ and exctact the zip file into `fontawesome` next to the `create_sty.py` file.

### Usage
```bash
$ python create_sty.py
```
This should result in the creation of latest ``fontawesome6.sty``


Contact
-------

You are free to modify it.
If you have any questions, feel free to join me.

Good luck!
