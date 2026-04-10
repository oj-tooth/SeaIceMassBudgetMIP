# Sea Ice Mass Budget Analysis: Model Intercomparison Project

## **About**

This is a repostitory for the Multi-Model TIPMIP-Tier 1 Sea Ice Mass Balance Analysis project led by Danish Meteorological Institute (DMI) and the National Oceanpgraphy Centre (NOC).

The aim of this project is to use TIPMIP-ESM Tier-1 experiments to disentangle:

* the likelihood of abrupt loss of sea ice in the two poles, in particular in wintertime.
* equilibrium adjustment at constant global warming levels.
* inter-model structural uncertainty.

Here, we seek to quantify the relative contributions to the total sea-ice mass budget following **Keen et al (2021)** to better understand the processes leading to ice loss and growth. 

> Keen, A., Blockley, E., Bailey, D., Debernard, J.B., Bushuk, M., et al. An inter-comparison of the mass budget of the Arctic sea ice in CMIP6 models. The Cryosphere, 2021, 15(2), pp.951-982. [https://doi.org/10.5194/tc-15-951-2021](https://doi.org/10.5194/tc-15-951-2021)

## **Contributing**

We invite contributions from centers producing TIPMIP-ESM simulations.

We have provided a open-source Python tool to perform the Sea Ice Mass Budget Analysis (**SIMBA**) from monthly-mean sea ice outputs.

### **Installation**

Users are recommended to download the latest version of this repository using Git:

```bash
git clone https://github.com/oj-tooth/SeaIceMassBudgetMIP.git
```

Then, install the dependencies in a new conda virtual environment and install **SIMBA** in editable mode:

```bash
# Navigate to cloned GitHub repo:
cd SeaIceMassBudgetMIP

# Activate new Python virtual environment using conda:
conda activate env_simba

# Install SIMBA CLI as a Python package:
pip install -e .
```

Alternatively, install the dependencies in a new Python virtual environment and install **SIMBA** in editable mode:

```bash
# Navigate to cloned GitHub repo:
cd SeaIceMassBudgetMIP

# Create new virtual environment using venv:
python -m venv /path/to/new/env_simba

# Activate new virtual environment:
source activate env_simba/bin/activate

# Install SIMBA as a Python package:
pip install -e .
```

### **Configuring SIMBA**

To perform a Sea Ice Mass Balance Analysis on the outputs of a given model simulation, we must first create a configuration `.toml` file as follows:

1. Create a new directory for your contribution in the `contributions/` directory...
```bash
# Move to contributions directory:
cd contributions/

# Make a new directory for your Earth-System-Model (ESM):
mkdir myESM
```

2. Copy the template configuration `.toml` file to your ESM directory...
```bash
cp template_config.toml myESM/myESM_config.toml
```

3. Modify the configuration `.toml` file:

    * Use the `[inputs]` tables to define the variable names and filepaths to the sea ice mass balance components output by your ESM.
    * Use the `[outputs]` table to specify the directory, filename and date format of the netCDF file output containing time-series of the total sea ice mass and the total sea ice mass changes due to each term in the mass budget.

### **Running SIMBA**

Once you have finished updating your configuration `.toml` file, use the following steps to perform a Sea Ice Mass Balance Analysis pipeline:

1. Activate the Python virtual environment where you installed the **SIMBA** Command-Line Interface using `pip`...

```bash
# Using conda:
conda activate env_simba

# Using venv:
source activate env_simba/bin/activate
```

2. Use the **SIMBA** command-line interface (CLI) to run a Sea Ice Mass Balance Analysis in the current process using your configuration `.toml` file...

```bash
simba run /path/to/config.toml --log /path/to/simba.log
```

where the `--log` argument is used to specify the path to write the `.log` file describing each of the steps of the **SIMBA** pipeline.

**Note:** we can also perform a dry-run, meaning that we do not execute the **SIMBA** pipeline and instead receive a summary of each of the steps that will be undertaken. This is particularly useful for debugging.

## **Contact**

* **Project Lead:** Tian Tian (tian@dmi.dk)
* **Project Developer:** Ollie Tooth (oliver.tooth@noc.ac.uk)