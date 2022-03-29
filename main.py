# Copyright (C) 2022 Louis-Navarro
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import argparse
import os

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def parse_args():
    parser = argparse.ArgumentParser(
        description='Tool to create a colour palette from a given image')
    parser.add_argument('image', type=argparse.FileType(
        'r'), help='Name of the image to create a colour palette from (required)')
    parser.add_argument(
        '-k', type=int, help='Number of colour to put in the palette (default: 3)', default=3)
    parser.add_argument(
        '-e', '--epochs', type=int, help='Number of iterations to fit the palette (default: 20)', default=20)
    parser.add_argument('-v', '--version', action='version', version='1.0.0')

    return parser.parse_args()


def parse_data(file):
    img = Image.open(os.path.basename(file.name))
    img = np.asarray(img) / 255
    img = img.reshape(-1, 3)
    return img


def k_means_clustering(data, k, epochs):

    # Initialize the centroids
    indices = np.random.choice(data.shape[0], k)
    centroids = data[indices, :]

    for i in range(epochs):
        # Assign each point to the closest centroid
        # Store the distance to the closest centroid
        distance = np.full(data.shape[0], np.inf)
        # Store the index of the closest centroid
        closest = np.zeros_like(distance)
        for index, point in enumerate(centroids):
            # Compute the distance to each centroid
            cur_dis = np.sqrt(np.sum((data-point)**2, axis=1))
            condition = cur_dis < distance  # Closer to this centroid
            # Update the index of the closest centroid
            closest[condition] = index
            # Update the distance to the closest centroid
            distance[condition] = cur_dis[condition]
        # Move the centroids
        for index in range(k):
            cluster_points = closest == index  # Points closer to this centroid
            centroids[index] = data[cluster_points].mean(
                axis=0)  # Update centroid using mean of points

    return centroids


def plot(means):
    k = means.shape[0]
    for index, mean in enumerate(means, start=1):
        ax = plt.subplot(1, k, index)
        colour = np.full((50, 50, 3), mean)
        ax.imshow(colour)

    plt.show()


def main():
    args = parse_args()
    data = parse_data(args.image)
    means = k_means_clustering(data, args.k, args.epochs)
    print(means)
    plot(means)
    # import pdb
    # pdb.set_trace()


if __name__ == '__main__':
    main()
