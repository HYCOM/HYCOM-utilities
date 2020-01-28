# HYCOM-utilities
Python, Matlab, IDL routines to handle HYCOM inputs and outputs

## Python
These functions are based on the Matlab implementation
from [Dmitry Dukhovskoy](https://www.coaps.fsu.edu/dmitry-dukhovskoy).

With this library you can:

**Read hycom fields** 
```python
from hycom.info import read_field_names
read_field_names(file_name)
```

**Read hycom output** 

```python
from hycom.io import read_hycom_fields
read_hycom_fields(file_name, fields)
```

