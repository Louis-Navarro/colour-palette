# Colour Palette Creator

This is a tool that allows the user to create a colour palette from a source image, using k-means clustering

## How to install

1. Clone the repository using `git clone https://github.com/Louis-Navarro/colour-palette` or download the ZIP file. Then, open a terminal in the directory.

2. Download the required packages by executing `pip install -r requirements` or `python -m pip install -r requirements`.

3. Done! To use the tool, read the documentation below.

## Usage

```
python main.py [-h] [-k K] [-e EPOCHS] [-v] image

positional arguments:
  image                 Name of the image to create a colour palette from (required)

optional arguments:
  -h, --help            show this help message and exit
  -k K                  Number of colour to put in the palette (default: 3)
  -e EPOCHS, --epochs EPOCHS
                        Number of iterations to fit the palette (default: 20)
  -v, --version         show program's version number and exit
```
