from . import *
from .templates import *


def erosion_geodesic(marker: np.ndarray, condition: np.ndarray):
    e = morph.grey_erosion(marker, 3)
    return np.maximum(condition, e)


def dilation_geodesic(marker: np.ndarray, condition: np.ndarray):
    d = morph.grey_dilation(marker, 3)
    return np.minimum(condition, d)


def greyscale_hit_or_miss(input_image: np.ndarray,
                          str_el_in: np.ndarray,
                          str_el_out: np.ndarray
                          ) -> np.ndarray:
    str_el_dil = np.flip(str_el_out, axis=[0, 1])
    e = morph.grey_erosion(input_image, footprint=str_el_in)
    d = morph.grey_dilation(input_image, footprint=str_el_dil)
    d[np.isinf(d)] = np.min(d[np.logical_not(np.isinf(d))])

    output = input_image - d
    is_simple = np.logical_and(np.greater_equal(e, input_image), np.greater(input_image, d))
    output[np.logical_not(is_simple)] = 0

    return output


def elementary_greyscale_sequential_thinning(x: np.ndarray, direction: str = 'a'):
    if direction == 'h':
        x_simple = greyscale_hit_or_miss(x, C_E, D_E)
        x_thin = x - x_simple

        x_simple = greyscale_hit_or_miss(x_thin, C_W, D_W)
        x_thin = x_thin - x_simple

        x_simple = greyscale_hit_or_miss(x_thin, C_NW, D_NW)
        x_thin = x_thin - x_simple

        x_simple = greyscale_hit_or_miss(x_thin, C_SE, D_SE)
        x_thin = x_thin - x_simple

        x_simple = greyscale_hit_or_miss(x_thin, C_NE, D_NE)
        x_thin = x_thin - x_simple

        x_simple = greyscale_hit_or_miss(x_thin, C_SW, D_SW)
        x_thin = x_thin - x_simple

        return x_thin

    elif direction == 'v':
        x_simple = greyscale_hit_or_miss(x, C_N, D_N)
        x_thin = x - x_simple

        x_simple = greyscale_hit_or_miss(x_thin, C_S, D_S)
        x_thin = x_thin - x_simple

        x_simple = greyscale_hit_or_miss(x_thin, C_NE, D_NE)
        x_thin = x_thin - x_simple

        x_simple = greyscale_hit_or_miss(x_thin, C_SW, D_SW)
        x_thin = x_thin - x_simple

        x_simple = greyscale_hit_or_miss(x_thin, C_NW, D_NW)
        x_thin = x_thin - x_simple

        x_simple = greyscale_hit_or_miss(x_thin, C_SE, D_SE)
        x_thin = x_thin - x_simple

        return x_thin
    else:
        raise ValueError("Parameter 'direction' must be 'h' or 'v'")


def greyscale_thinning(input_image: np.ndarray, iterations: Optional[int] = None, direction: str = 'a',
                       verbose=False, verbose_it_step=10):
    x_thin = np.copy(input_image)
    count = 0
    while True:
        x_out = elementary_greyscale_sequential_thinning(x_thin, direction)

        if np.all(np.equal(x_out, x_thin)):
            break
        else:
            x_thin = x_out
        count += 1

        if verbose:
            if count % verbose_it_step == 0:
                print("it:", count)

        if count == iterations:
            break

    if verbose:
        if iterations is None:
            print("Iterations needed for stability:", count)
        else:
            print("Iterations performed:", iterations)

    return x_thin


def elementary_greyscale_trimming(x: np.ndarray, direction: str = 'a'):
    if direction == 'h':
        x_simple = greyscale_hit_or_miss(x, C, D_E)
        x_trim = x - x_simple

        x_simple = greyscale_hit_or_miss(x_trim, C, D_W)
        x_trim = x_trim - x_simple

        return x_trim

    elif direction == 'v':
        x_simple = greyscale_hit_or_miss(x, C, D_N)
        x_trim = x - x_simple

        x_simple = greyscale_hit_or_miss(x_trim, C, D_S)
        x_trim = x_trim - x_simple

        return x_trim
    else:
        raise ValueError("Parameter 'direction' must be 'h' or 'v'")


def greyscale_trimming(input_image: np.ndarray, iterations: Optional[int] = None, direction: str = 'a',
                       verbose=False, verbose_it_step=10):
    x_thin = np.copy(input_image)
    count = 0
    while True:
        x_out = elementary_greyscale_trimming(x_thin, direction)

        if np.all(np.equal(x_out, x_thin)):
            break
        else:
            x_thin = x_out
        count += 1

        if verbose:
            if count % verbose_it_step == 0:
                print("it:", count)

        if count == iterations:
            break

    return x_thin


def binary_thinning(image_input: np.ndarray, iterations: Optional[int] = None, direction: str = 'h',
                    verbose=False, verbose_it_step=10):
    x_thin = np.copy(image_input)
    count = 0
    while True:
        x_out = elementary_binary_thinning(x_thin, direction)
        if np.all(np.equal(x_out, x_thin)):
            break
        else:
            x_thin = x_out
        count += 1

        if verbose:
            if count % verbose_it_step == 0:
                print("it:", count)

        if count == iterations:
            break

    return x_thin


def elementary_binary_thinning(x: np.ndarray, direction: str = 'h'):
    if direction == 'h':
        x_simple = morph.binary_hit_or_miss(x, C_E, D_E)
        x_thin = np.logical_and(x, np.logical_not(x_simple))

        x_simple = morph.binary_hit_or_miss(x_thin, C_W, D_W)
        x_thin = np.logical_and(x_thin, np.logical_not(x_simple))

        x_simple = morph.binary_hit_or_miss(x_thin, C_NW, D_NW)
        x_thin = np.logical_and(x_thin, np.logical_not(x_simple))

        x_simple = morph.binary_hit_or_miss(x_thin, C_SE, D_SE)
        x_thin = np.logical_and(x_thin, np.logical_not(x_simple))

        x_simple = morph.binary_hit_or_miss(x_thin, C_NE, D_NE)
        x_thin = np.logical_and(x_thin, np.logical_not(x_simple))

        x_simple = morph.binary_hit_or_miss(x_thin, C_SW, D_SW)
        x_thin = np.logical_and(x_thin, np.logical_not(x_simple))

        return x_thin
    elif direction == 'v':
        x_simple = morph.binary_hit_or_miss(x, C_N, D_N)
        x_thin = np.logical_and(x, np.logical_not(x_simple))

        x_simple = morph.binary_hit_or_miss(x_thin, C_S, D_S)
        x_thin = np.logical_and(x_thin, np.logical_not(x_simple))

        x_simple = morph.binary_hit_or_miss(x_thin, C_NE, D_NE)
        x_thin = np.logical_and(x_thin, np.logical_not(x_simple))

        x_simple = morph.binary_hit_or_miss(x_thin, C_SW, D_SW)
        x_thin = np.logical_and(x_thin, np.logical_not(x_simple))

        x_simple = morph.binary_hit_or_miss(x_thin, C_NW, D_NW)
        x_thin = np.logical_and(x_thin, np.logical_not(x_simple))

        x_simple = morph.binary_hit_or_miss(x_thin, C_SE, D_SE)
        x_thin = np.logical_and(x_thin, np.logical_not(x_simple))

        return x_thin
    else:
        raise ValueError("Parameter 'direction' must be 'h' or 'v'")


def skeleton(image_input, shape=(3, 3), n_max=None):
    str_el = np.ones(shape, dtype=np.bool).astype(image_input.device)

    result = np.zeros_like(image_input)
    tmp = np.copy(image_input)

    n = 1
    while np.any(tmp):
        opening = morph.binary_opening(tmp, str_el)
        top_hat = np.logical_and(tmp, np.logical_not(opening))
        result = np.logical_or(result, top_hat)

        tmp = morph.binary_erosion(tmp, str_el)

        n += 1
        if n_max is not None:
            if n > n_max:
                break

    return result


def remove_isolated_greyscale(input_image: np.ndarray):
    d = morph.grey_dilation(input_image, structure=np.zeros_like(B_O), footprint=B_O)
    e = morph.grey_erosion(input_image, structure=np.zeros_like(B_O), footprint=B_O)
    is_plateau = np.equal(d, e)
    is_bigger = np.greater(input_image, d)

    is_isolated = np.logical_and(is_plateau, is_bigger)

    input_image[is_isolated] = d[is_isolated]
