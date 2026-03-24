# Sea Ice Mass Budget Model Intercomparison Project

## **About**

This is a repostitory for the Multi-Model TIPMIP-Tier 1 Sea Ice Mass Balance Analysis project led by Danish Meteorological Institute (DMI) and the National Oceanpgraphy Centre (NOC).

The aim of this project is to use TIPMIP-ESM Tier-1 experiments to disentangle:

* the likelihood of abrupt loss of sea ice in the two poles, in particular in wintertime.
* equilibrium adjustment at constant global warming levels.
* inter-model structural uncertainty.

Here, we seek to quantify the relative contributions to the total sea-ice mass budget following Keen et al (2021) to better understand the processes leading to ice loss and growth. 

## **Contributing**

We invite contributions from centers producing TIPMIP-ESM simulations.

We have provided a open-source Python tool to perform the Sea Ice Mass Budget Ananlysis (**SIMBA**) from CMORISED monthly-mean sea ice outputs.

### **Installation**

Users are recommended to install the latest version of this repository using Git:
```{bash}
git clone git@github.com:oj-tooth/sea_ice_mass_budget_MIP.git
```

Then, install the dependencies in a new conda virtual environment and install **SIMBA** in editable mode:
```{bash}
# Navigate to cloned GitHub repo:
cd simba_mip

# Create conda virtual environment:
conda env create -f simba_environment.yml

# Activate new virtual environment:
conda activate env_nemo_cookbook

# Install SIMBA as a Python package:
pip install -e .
```

Alternatively, install the dependencies in a new Python virtual environment and install **SIMBA** in editable mode:
```{bash}
# Navigate to cloned GitHub repo:
cd simba_mip

# Create new virtual environment:
python -m venv /path/to/new/env_simba

# Activate new virtual environment:
source activate env_simba/bin/activate

# Install SIMBA as a Python package:
pip install -e .
```

## **Contact**

* **Project Lead:** Tian Tian (tian@dmi.dk)
* **Project Developer:** Ollie Tooth (oliver.tooth@noc.ac.uk)