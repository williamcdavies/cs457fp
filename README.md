## Build Instructions

1. Build client.

```sh
cd cs457fp/client
python3 -m venv venv
cd ..
source client/venv/bin/activate
pip install -r client/requirements.txt
```

2. Build server.

```sh
cd cs457fp/server
python3 -m venv venv
cd ..
source server/venv/bin/activate
pip install -r server/requirements.txt
```

3. Run Uvicorn

```sh
cd cs456fp
uvicorn server.__main__:app --reload
```

3. Run Application

```sh
cd cs456fp/client
python3 __main__.py
```



## Commands

### `\q`
Quits the application.



### `\get_fire_areas`
Pretty prints a list of `fire_area` objects.

### Parameters
- `offset` starting index of list.
- `limit` length of list.

### `\get_fire_area`
Pretty prints a `fire_area` object.

### Parameters
- `year` partition identifier.
- `id` index of record in partition specified by `year`.



### `\get_hms_fires`
Pretty prints a list of `hms_fire` objects.

### Parameters
- `offset` starting index of list.
- `limit` length of list.

### `\get_hms_fire`
Pretty prints a `hms_fire` object.

### Parameters
- `year` partition identifier.
- `id` index of record in partition specified by `year`.



### `\get_hms_smokes`
Pretty prints a list of `hms_smoke` objects.

### Parameters
- `offset` starting index of list.
- `limit` length of list.

### `\get_hms_smoke`
Pretty prints a `hms_smoke` object.

### Parameters
- `year` partition identifier.
- `id` index of record in partition specified by `year`.



### `\get_lakes_buffers`
Pretty prints a list of `lake_buffer` objects.

### Parameters
- `offset` starting index of list.
- `limit` length of list.

### `\get_lakes_buffer`
Pretty prints a `lake_buffer` object.

### Parameters
- `hylak_id` index of record.



### `\get_lakes_points`
Pretty prints a list of `lake_point` objects.

### Parameters
- `offset` starting index of list.
- `limit` length of list.

### `\get_lakes_point`
Pretty prints a `lake_point` object.

### Parameters
- `hylak_id` index of record.



### `\get_lakes_polys`
Pretty prints a list of `lake_poly` objects.

### Parameters
- `offset` starting index of list.
- `limit` length of list.

### `\get_lakes_poly`
Pretty prints a `lake_poly` object.

### Parameters
- `hylak_id` index of record.



### `\get_lakes`
Pretty prints a list of `lake` objects.

### Parameters
- `offset` starting index of list.
- `limit` length of list.

### `\get_lake`
Pretty prints a `lake` object.

### Parameters
- `hylak_id` index of record.



### `\get_logs`
Pretty prints a list of `log` objects.

### Parameters
- `offset` starting index of list.
- `limit` length of list.

### `\get_log`
Pretty prints a `log` object.

### Parameters
- `id` index of record.



### `\get_populated_places`
Pretty prints a list of `populated_place` objects.

### Parameters
- `offset` starting index of list.
- `limit` length of list.

### `\get_populated_place`
Pretty prints a `populated_place` object.

### Parameters
- `id` index of record.



### `/intersects`
Prints `true` if two geospatial objects intersect, `false` otherwise.

### Parameters

#### Path Parameters 
- `path_a` API path.
- `path_b` API path.

Valid values:
- `fire_areas`
- `hms_fires`
- `hms_smokes`
- `lakes_buffers`
- `lakes_points`
- `lakes_polys`
- `populated_places`

#### Column Parameters
- `col_a` geometry attribute of model associated with `path_a`.
- `col_b` geometry attribute of model associated with `path_b`.

Valid values:
- `geometry` Non-exclusive. Works for all paths excluding `lakes_polys`
- `geometry_4326` Exclusive to `lakes_polys`.
- `geometry_3978` Exclusive to `lakes_polys`.

#### ID Parameters
- `id_a` record index associated with `path_a`.
- `id_b` record index associated with `path_b`.

Valid values:
- `id`Exclusive to `fire_areas`, `hms_fires`, `hms_smokes`, `populated_places`
- `hylak_id` Exclusive to `lakes_buffers`, `lakes_points`, `lakes_polys`,