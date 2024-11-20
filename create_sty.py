#!/usr/bin/env python3

import json
import os
from datetime import date

# Download *-desktop.zip from https://github.com/FortAwesome/Font-Awesome/releases
# and extract into fontawesome directory.
SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
INPUT_FILE = os.path.join(SCRIPT_PATH, "fontawesome", "metadata", "icons.json")
OUTPUT_FILE = os.path.join(SCRIPT_PATH, "fontawesome6.sty")

OUTPUT_HEADER = (
    R"""% Identify this package.
\NeedsTeXFormat{LaTeX2e}
\ProvidesPackage{fontawesome6}["""
    + date.today().strftime("%Y/%m/%d")
    + R""" v6.7.0 font awesome icons]

% Requirements to use.
\RequirePackage{fontspec}

% Define shortcut to load the Font Awesome font for brands.
\newfontfamily{\FABrands}{Font Awesome 6 Brands}

% Define shortcut to load the Font Awesome font.
\newfontfamily{\FA}{Font Awesome 6 Free}[
  UprightFont=* Regular,
  BoldFont=* Solid,
]

% Generic command displaying an icon by its name.
\newcommand*{\faicon}[1]{{
  \csname faicon@#1\endcsname
}}

"""
)

OUTPUT_LINE = (
    R'\expandafter\def\csname faicon@%(name)s\endcsname {%(font)s\symbol{"%(symbol)s}}' + "\n"
)


def main():
    with open(INPUT_FILE) as json_data:
        icons = json.load(json_data)
        with open(OUTPUT_FILE, "w") as w:
            w.write(OUTPUT_HEADER)
            for icon_name in sorted(icons.keys()):
                font = R"\FA" if "brands" not in icons[icon_name]["styles"] else R"\FABrands"
                w.write(
                    OUTPUT_LINE
                    % {
                        "name": icon_name,
                        "symbol": icons[icon_name]["unicode"].upper(),
                        "font": font,
                    }
                )
            w.write(r"\endinput")


if __name__ == "__main__":
    main()
