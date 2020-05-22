import pickle

import netCDF4 as netCDF4
import numpy as np
import matplotlib.pyplot as plt
import argparse


parser = argparse.ArgumentParser(description='Copernicus dataset processor')
parser.add_argument('--dataset_path', type=str, required=True)
parser.add_argument('--out_file', type=str, required=True)

args = parser.parse_args()

					
nc = netCDF4.Dataset(args.dataset_path)

lat = nc.variables['lat'][:]
lon = nc.variables['lon'][:]
times = nc.variables['time']


meshed = np.meshgrid(lat, lon)

time = netCDF4.num2date(times[:] ,times.units)[:]

t2m = nc.variables['ws10m']

numpied = np.array(t2m)


shift_by = (30, 30)

input_size = (10, 10)

formed = np.zeros((t2m.shape[0], input_size[0], input_size[1], 1))

for i in range(input_size[0]):
    for j in range(input_size[1]):
        formed[:, i, j, 0] = numpied[:, i + shift_by[0], j + shift_by[1]]

data = {
    "lat": lat[shift_by[0]:shift_by[0]+ input_size[0]],
    "lon": lon[shift_by[1]:shift_by[1]+input_size[1]],
    "times": np.array(times),
    "data": formed
}

pickle.dump(data, open(args.out_file, "wb"))


