import numpy as np
from hycom.info import read_field_names
from hycom.io import read_hycom_fields, subset_hycom_field
import matplotlib.pyplot as plt
from os.path import join, exists
import os

# This code can be used as an example when we want to generate images from a preproc folder.
def main():

    # ------------------ Example to read HYCOM fields ------------------
    # input_folder = '/data/COAPS_Net/gleam/abozec/HYCOM/TSIS/IASx0.03/forecast/PIES/200906/'
    input_folder = join('..','test_data')
    output_folder = 'output'
    file_name = 'archv.2009_153_00.a'
    input_file = join(input_folder, file_name)
    fields = ['srfhgt', 'temp', 'u-vel.']
    layers = [0,1,2,3]

    # Printing the fields available in the file
    print(F"The fields available are: {read_field_names(input_file)}")

    # Reading specific field and layers
    hycom_fields = read_hycom_fields(input_file, fields, layers)

    # Making plot of the fields
    for idx, field in enumerate(fields):
        layers = hycom_fields[field].shape[0]
        for layer in range(layers):
            plt.imshow(np.flip(hycom_fields[field][layer], axis=0))
            plt.title(F"{field} z-axis:{layer}")
            if not (exists(output_folder)):
                os.makedirs(output_folder)
            plt.savefig(join(output_folder, F"{field}_{idx}_{layer}.png"))
            plt.show()

    # ------------------ Example to susample HYCOM files (by number of fields and layers) ------------------
    output_folder = 'output'
    file_name = 'archv.2009_153_00.a'
    input_file = join(input_folder, file_name)
    fields = ['temp']
    layers = [0]

    output_file = join(output_folder, F"subsampled_{file_name}")
    subset_hycom_field(input_file, output_file, fields, layers)


if __name__ == '__main__':
    main()
