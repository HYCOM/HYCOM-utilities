import numpy as np
from hycom.info import read_field_names
from hycom.io import read_hycom_fields
import matplotlib.pyplot as plt
import os

# This code can be used as an example when we want to generate images from a preproc folder.
def main():

    file_name = '/data/COAPS_Net/gleam/abozec/HYCOM/TSIS/IASx0.03/forecast/PIES/200906/archv.2009_153_00.a'
    output_folder = 'output'
    fields = ['srfhgt', 'temp']

    # Printing the list of fields
    print(F"The fields available are: {read_field_names(file_name)}")

    # Reading specific field and layers
    hycom_fields = read_hycom_fields(file_name, fields)

    # Making plot of the fields
    for idx, field in enumerate(fields):
        plt.imshow(np.flip(hycom_fields[field][0], axis=0))
        plt.title(field)
        if not (os.path.exists(output_folder)):
            os.makedirs(output_folder)
        plt.savefig(os.path.join(output_folder, F"{field}_{idx}.png"))
        plt.show()


if __name__ == '__main__':
    main()
