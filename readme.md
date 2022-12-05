

# Graph Neural Network for Simulated X-Ray Transient Detection

The present work aims to train a GNN to label a particular sort of X-Ray transient using simulated events overlayed onto real data from XMM-Newton observations. We will experiment with Graph Convolutional Networks (GCNs). We will therefore  have to trandsform our point-cloud data into a "k nearest neighbors"-type graph. Data stored in the `raw` folder at the current working directory is taken from icaro.iusspavia.it `/mnt/data/PPS_ICARO_SIM2`. Observations store data for each photon detected, with no filter applied, in FITS files ending in `EVLI0000.FTZ` for the original observations and `EVLF0000.FTZ` for the observation and simulation combined. We will refer to the former data as "genuine" and to the latter as "faked" for brevity.
