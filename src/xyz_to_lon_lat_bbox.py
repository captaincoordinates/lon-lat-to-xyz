from typing import List, Tuple
from math import pi, atan, sinh, degrees


def execute(x: int, y: int, z: int) -> List[float]:
    def mercatorToLat(mercatorY: int) -> float:
        return degrees(atan(sinh(mercatorY)))

    def y_to_lat_edges(y: int, z: int) -> Tuple[float, float]:
        tile_count = pow(2, z)
        unit = 1 / tile_count
        relative_y1 = y * unit
        relative_y2 = relative_y1 + unit
        lat1 = mercatorToLat(pi * (1 - 2 * relative_y1))
        lat2 = mercatorToLat(pi * (1 - 2 * relative_y2))
        return (lat1, lat2)

    def x_to_lon_edges(x: int, z: int) -> Tuple[float, float]:
        tile_count = pow(2, z)
        unit = 360 / tile_count
        lon1 = -180 + x * unit
        lon2 = lon1 + unit
        return (lon1, lon2)

    def tile_edges(x: int, y: int, z: int) -> List[float]:
        lat1, lat2 = y_to_lat_edges(y, z)
        lon1, lon2 = x_to_lon_edges(x, z)
        return [lon1, lat1, lon2, lat2]

    return tile_edges(x, y, z)

if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument(
        "x",
        type=float,
        help="Tile column (x)",
    )
    parser.add_argument(
        "y",
        type=float,
        help="Tile row (y)",
    )
    parser.add_argument(
        "z",
        type=int,
        help="Tile zoom level",
    )
    args = parser.parse_args()
    result = execute(**vars(args))
    print(f"{result[0]},{result[3]} {result[2]},{result[1]}")
