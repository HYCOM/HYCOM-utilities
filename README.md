# HYCOM-utilities
Python, Matlab, IDL routines to handle HYCOM inputs and outputs

## Python
These functions are based on the Matlab implementation from [Dmitry Dukhovskoy](https://www.coaps.fsu.edu/dmitry-dukhovskoy).

With this library you can:

**Read hycom fields names** 
```python
from hycom.info import read_field_names
read_field_names(file_name)
```

**Read hycom field data** 

```python
from hycom.io import read_hycom_fields
read_hycom_fields(file_name, fields)
```

**Subsample hycom files (just reduce the number of output fields and save with same format)** 

```python
from hycom.io import subset_hycom_field
subset_hycom_field(input_file, output_file, fields, layers)
```
**Read Arakawa-C grid coordinates

```python
from hycom.io import subset_hycom_field
read_hycom_coords(file_name, fields, replace_to_nan, verbose)
```