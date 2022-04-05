def read_field_names(file_name: str):
    """
    Reads the fields available in the hycom file (it can be the output or the coordinates)
        file_name: str
            Complete path to the .a or .b hycom output file. It can also be the name of the file without the .a or .b ending
    """
    if file_name.endswith('.a') or file_name.endswith('.b'):
        file_name = file_name[:-2]

    b_file = open(file_name+'.b', 'r')

    # Reading the header file first 4 lines (general info)
    b_file_lines = b_file.readlines()
    all_fields = []
    start_idx = 10
    if file_name.find("regional") != -1:  # For reading coordinates fields also
        start_idx = 3
    for c_line in b_file_lines[start_idx:]:
        c_field = c_line.split()[0].strip()
        if not(c_field in all_fields):
            all_fields.append(c_field)

    return all_fields
