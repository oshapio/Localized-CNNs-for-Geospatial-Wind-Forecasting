# Localized Convolutional Neural Networks for Geospatial Wind Forecasting

Convolutional Neural Networks (CNN) possess many positive qualities when it comes to spatial raster data. Translation invariance enables CNNs to detect features regardless of their position in the scene. But in some domains, like geospatial, not all locations are exactly equal. In this work we propose localized convolutional neural networks that enable convolutional architectures to learn local features in addition to the global ones. We investigate their instantiations in the form of learnable inputs, local weights, and a more general form. They can be added to any convolutional layers, easily end-to-end trained, introduce minimal additional complexity, and let CNNs retain most of their benefits to the extent that they are needed. 

This repository contains the code used in this work. See [1] for details.

## Proposed methods

<p align="center">
  <img src="https://i.imgur.com/YdMjohv.png">
</p>

## Proof of concept: a bouncing ball task

<p align="center"> 
<img src="https://i.imgur.com/SufrfgJ.png">
</p>

### Data
Data of this task can be downloaded [[here]](https://drive.google.com/drive/folders/1vM6lNedCe5dzptYhMjfCiSEOaMVrgm-U?usp=sharing), it contains two files: `bouncing_balls_training_data.dat`, which includes training and first test set data, and `bouncing_balls_testing_data.dat`, a second test set.
### Running 

Easiest way to run the code is through Google Colab [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1L0ggaP15B1MPZ4yQVk8EuQi3ZplW2mKR?usp=sharing). Otherwise, [Localized_CNNs_on_synthetic_data.ipynb](experiments/synthetic/Localized_CNNs_on_synthetic_data.ipynb) can be executed locally by updating the path of the data files. See `requirements.txt` for compatible packages.

## Case studies on real-world data

<p align="center">
  <img src="https://i.imgur.com/tFVm5rd.png">
</p>

Three datasets were used to benchmark proposed methods and their compatibility with leading CNN architectures:
- **Wind Integration National Dataset** (WIND), 10x10 relatively high-resolution data ordered in a grid. The data can be acquired [[here]](https://maps.nrel.gov/wind-prospector/?aL=tNGkbj%255Bv%255D%3Dt&bL=dI6joO&cE=0&lR=0&mC=40.36459630797086%2C-85.13648986816406&zL=11) by using wind resource download tool on the wind toolkit data and selecting 2012 for year, wind speed for attributes, and including leap year and 5 minute interval for download options. This will download a csv for each site, that should be stored in one folder. Also, files that do not fall into the rotated rectangle will be discared. Final processed file can be acquired by running [[form_WINDS_data.py]](https://github.com/oshapio/Localized-CNNs-for-Geospatial-Wind-Forecasting/blob/master/preprocessing/form_WINDS_data.py):

```python
python preprocessing/form_WINDS_data.py --dataset_folder_path path_to_data_folder --out_file WINDS_processed_data.pkl
```

- **Meteorological Terminal Aviation Routine Dataset**, non-orderly data, that we embed into a 8x8 grid: directly and by an optimized embedding. The data file is located [[here]](https://github.com/amirstar/Deep-Forecast/blob/master/MS_winds.dat) (it can be examined visually in [2]). No further processing is required. Permutation file of the optimized embedding is located [[here]](https://github.com/oshapio/Localized-CNNs-for-Geospatial-Wind-Forecasting/blob/master/data/top10perms_GA.pkl).  
- **Copernicus Dataset**, 10x10 low-resolution data ordered in a grid, part of which overlaps with the Atlantic Ocean. The data can be downloaded [[here]](https://cds.climate.copernicus.eu/cdsapp#!/dataset/sis-european-energy-sector?tab=overview), by selecting wind speed variable, 6 hour time aggregation, 10m vertical level and no bias correction boxes. The acquired NetCDF file needs to be further processed by executing [[form_copernicus_data.py]](https://github.com/oshapio/Localized-CNNs-for-Geospatial-Wind-Forecasting/blob/master/preprocessing/form_copernicus_data.py):

```python
python preprocessing/form_copernicus_data.py --dataset_path path_to_NetCDF_file --out_file copernicus_processed_data.pkl
```

### Running

The code can be run in Google Colab [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Zu-MoQLZ04ZgKzvw67JtR0ayXIu4FPCH?usp=sharing) or locally [[in a notebook]](https://github.com/oshapio/Localized-CNNs-for-Geospatial-Wind-Forecasting/blob/master/experiments/real_world/Localized_CNNs_on_real_world_data.ipynb), just update the locations of the data files.



## References

[1] Uselis, Arnas, Mantas Lukoševičius, and Lukas Stasytis. "Localized Convolutional Neural Networks for Geospatial Wind Forecasting". 2020. [[arxiv]](https://arxiv.org/abs/2005.05930v2)

[2] Ghaderi, Amir, Borhan M. Sanandaji, and Faezeh Ghaderi. "Deep forecast: deep learning-based spatio-temporal forecasting". 2017. [[arxiv]](https://arxiv.org/abs/1707.08110)
