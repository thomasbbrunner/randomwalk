
import numpy as np


def random_walk(iterations, ranges, start_coordinates=None, seed=None):
    '''
    Pretty fast random walk algorithm for any number of dimensions

    Arguments:
    iterations: number of iterations to calculate
    ranges: allowed values for each dimension (accepts list of tuples, or tuple of tuples, or in the 1D case a single tuple)
    start_coordinates: None -> origin is starting position
                        (Accepts list or tuple)
                        or 'random' for random

    returns: array with coordinates of points 


    Example:
    to generate 1000 iterations of a random walk in 3 dimensions, with a x, y and z ranges of [-100, 100]
    coords = random_walk(1000, 3*[(-100, 100)])
    coords[0] # coordinates x,y,z of first point
    >>> [[0],
    [0],
    [0]]

    to generate 10000 iterations of a random walk in 2 dimensions, with a x value range of [-10000, 10000] and y range of [-1000, 1000]
    random_walk(10000, [(-10000, 10000), (-1000, 1000)])
    '''

    # configuration
    if seed != None:
        np.random.seed(seed)  # for repeatable results
    _iterations = iterations
    space_size = ranges
    space_dims = len(space_size)

    # checking input sanity

    # array containing coordinate history
    coords = np.zeros((_iterations, space_dims, 1))

    # random starting coordinates
    if start_coordinates != None:
        if start_coordinates == 'random' or start_coordinates == 'rand':
            coords[0] = np.array(
                [[np.random.randint(0, size) for size in space_size]]
            ).T
        else:
            # check if they are inside the given range
            for dim in range(0, space_dims):
                if not space_size[dim][0] <= start_coordinates[dim] <= space_size[dim][1]:
                    raise ValueError(
                        'Start coordinates have to be inside the range')

            # separated indexing accepts tuples as well as lists and other containers
            coords[0] = np.array(
                [[start_coord for start_coord in start_coordinates]]
            ).T

    # new coordinates
    new_coords = np.zeros((space_dims, 2))

    # border matrices in doubled form (eg. xx,yy...)
    # double values are for improving speed of the calculations below
    min_coords = np.zeros((space_dims, 2))
    max_coords = np.zeros((space_dims, 2))
    for dim in range(0, space_dims):
        min_coords[dim] = space_size[dim][0]
        max_coords[dim] = space_size[dim][1]

    # create matrix to create plus and minus steps
    # (first column -1, second column +1)
    step_matrix = np.ones((space_dims, 2)) @ np.array([[-1, 0], [0, 1]])

    # debug

    # iterate through steps
    for iteration in range(0, _iterations-1):

        # possible new coords
        new_coords = coords[iteration] @ np.ones((1, 2)) + step_matrix

        # check if new coords exceed the min and max allowed coords
        allowed_coords = np.logical_and(
            np.not_equal(new_coords, min_coords-1),
            np.not_equal(new_coords, max_coords+1)
        )

        while True:
            i = np.random.randint(0, space_dims)
            j = np.random.randint(0, 2)

            if allowed_coords[i][j]:
                coords[iteration+1] = coords[iteration]
                coords[iteration+1][i] = new_coords[i][j]
                break

    return coords
