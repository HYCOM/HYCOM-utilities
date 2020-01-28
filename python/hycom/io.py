import numpy as np
from hycom.info import read_field_names

NAN_TH = 2**99  # Nan threshold


def read_hycom_fields(file_name: str, fields: list, layers=[], replace_to_nan=True):
    """
    Reads hycom files (.a and .b) and returns the desired fields in a dictionary.
        file_name: str
            Complete path to the .a or .b hycom output file. It can also be the name of the file without the extension
        fields: list
            List of strings with the fields names to read. If empty, the function reads all the fields
        layers: list
            List of integers that represent the z-index of the layers to read. If empty, all the layers will be read.
        replace_to_nan: boolean
            Indicates if the nan values should be replaced with numpy nan
    """
    # Selecting the proper name
    if file_name.endswith('.a') or file_name.endswith('.b'):
        file_name = file_name[:-2]

    a_file_name = file_name+'.a'
    b_file_name = file_name+'.b'
    b_file = open(b_file_name, 'r')

    # Validate that the field names requested are available in the hycom file
    all_fields = read_field_names(b_file_name)
    if len(fields) == 0:
        fields = all_fields
        # print(F"Reading all the fields in the file: {fields}")
    if not(np.all([field in all_fields for field in fields])):
        print(F"Warning!!!!! Fields {[field for field in fields if not(field in all_fields)]} are not"
              F" in the hycom file {file_name}, removing them from the list.")
        fields = [field for field in fields if field in all_fields ]

    # Reading the header file (first 4 lines, just general info)
    b_file_lines = b_file.readlines()

    hycom_ver = b_file_lines[4].strip().split()[0]
    exp_num = b_file_lines[5].strip().split()[0]
    lon_size = int(b_file_lines[7].strip().split()[0])
    lat_size = int(b_file_lines[8].strip().split()[0])
    layer_size = lon_size*lat_size
    # size of each layer (it seems all the layers have the same size)
    npad = 4096-np.mod(layer_size, 4096)

    # Printing basic information
    print(F"Hycom version: {hycom_ver}, Experiment: {exp_num}")
    for cur_line in range(3):
        print(b_file_lines[cur_line].strip())

    # Looking for the starting locations for each layer and each field
    field_loc = {field: [] for field in fields}
    for line_idx, cur_line in enumerate(b_file_lines[9:]):
        field = cur_line.split()[0].strip()
        if field in field_loc:
            field_loc[field].append(line_idx)

    # Counting the number of layers for each field.
    num_layers = {field: len(field_loc[field]) for field in fields}
    print(F"Dims lon: {lon_size}, lat: {lat_size}")

    # Read layers for each field
    a_file = open(a_file_name, 'rb')

    # Define the layers that are going to be retrieved for each field
    if len(layers) != 0:
        layers_per_field = {field: [layer for layer in layers if layer in range(num_layers[field])] for field in fields}
    else:
        layers_per_field = {field: range(num_layers[field]) for field in fields}

    # Create the dictionary that will contain the np arrays with the fields information
    np_fields = {field: np.zeros((len(layers_per_field[field]), lat_size, lon_size)) for field in fields}

    for field in fields:
        print(F"\tReading layers {layers_per_field[field]} for field {field}. Total layers: {num_layers[field]}")

    # For each field read the proper section for each layer, from the binary file
    for field in fields:
        for cur_layer_idx, cur_layer in enumerate(layers_per_field[field]):
            offset = (field_loc[field][cur_layer]-1) * (layer_size+npad)*4
            a_file.seek(offset)
            cur_layer_data = np.fromfile(file_name+'.a', dtype='>f', count=layer_size, offset=offset)
            if replace_to_nan:
                cur_layer_data[cur_layer_data > NAN_TH] = np.nan
            np_fields[field][cur_layer_idx, :, :] = np.reshape(cur_layer_data, (lat_size, lon_size))

    # Closing both files
    a_file.close()
    b_file.close()

    return np_fields

