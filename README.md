# lon-lat-to-xyz
Small utility to convert a longitude, latitude, and zoom level to a tile identifier in the XYZ tile system

```sh
docker build -t local/util-lon-lat-to-xyz .
docker run --rm local/util-lon-lat-to-xyz python -m lon_lat_to_xyz -87.15 30.99 14
# 14/4225/6707 [zoom level, x column, y column]
```

# xyz-to-bbox
Small utility to convert a z,x,y tile identifier to a lon/lat bounding box

```sh
docker build -t local/util-lon-lat-to-xyz .
docker run --rm local/util-lon-lat-to-xyz python -m xyz_to_lon_lat_bbox 4225 6708 14
# 
```