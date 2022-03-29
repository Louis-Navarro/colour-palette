# Colour Palette Creator

This is a tool that allows the user to create a colour palette from a source image, using k-means clustering

## How to install

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
