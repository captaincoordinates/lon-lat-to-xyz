from math import cos, log, pi, radians, tan, floor
from typing import Tuple


def execute(lon, lat, z) -> Tuple[float, float]:

    def sec(x):
        return 1 / cos(x)

    tile_count = pow(2, z)
    x = (lon + 180) / 360
    y = (1 - log(tan(radians(lat)) + sec(radians(lat))) / pi) / 2
    return (floor(tile_count * x), floor(tile_count * y))


if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument(
        "lon",
        type=float,
        help="Longitude (x)",
    )
    parser.add_argument(
        "lat",
        type=float,
        help="Latitude (y)",
    )
    parser.add_argument(
        "z",
        type=int,
        help="Tile zoom level",
    )
    args = parser.parse_args()
    result = execute(**vars(args))
    print(f"{args.z}/{result[0]}/{result[1]}")
