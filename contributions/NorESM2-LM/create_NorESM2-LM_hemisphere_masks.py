"""
create_NorESM2-LM_hemisphere_masks.py

Description: Script to define Northern & Southern Hemisphere masks for NorESM2-LM.

Created By: Ollie Tooth (oliver.tooth@noc.ac.uk)
Modified by: Tomas Torsvik (tomas.torsvik@uib.no)
"""
# -- Import dependencies -- #
import xarray as xr

# -- Create NEMODataTree -- #
# Define path to domain_cfg:
fpath = "/nird/datalake/NS2980K/projects/TipESM/cice_Ofx/areacello_CICE_Ofx_NorESM2-LM_esm-piControl_r1i1p1f1_gn.nc"
ds_domain = xr.open_dataset(fpath)

# Define Northern Hemisphere ocean mask [latitude > 0N]:
mask_NH = (ds_domain['latitude'] > 0)
mask_NH = mask_NH.assign_attrs({"long_name": "Northern Hemisphere ocean mask",
                                "comment": "Northern Hemisphere is defined as the region where latitude > 0N for all ocean scalar grid points in the NorESM2-LM domain."
                                })
# Convert to xarray.Dataset:
ds_out = mask_NH.to_dataset(name="mask_NH")

# Define Southern Hemisphere ocean mask [latitude < 0N]:
mask_SH = (ds_domain['latitude'] < 0)
mask_SH = mask_SH.assign_attrs({"long_name": "Southern Hemisphere ocean mask",
                                "comment": "Southern Hemisphere is defined as the region where latitude < 0N for all ocean scalar grid points in the NorESM2-LM domain."
                                })
# Add to xarray.Dataset:
ds_out["mask_SH"] = mask_SH

# Update coordinate dimensions:
ds_out = ds_out.squeeze()
ds_out = ds_out.assign_coords({"latitude": ds_domain["latitude"],
                               "longitude": ds_domain["longitude"],
                               }
                              )
outfilepath = "/nird/datalake/NS2980K/projects/TipESM/cice_Ofx/hemisphere_masks_CICE_Ofx_NorESM2-LM.nc"
ds_out.to_netcdf(outfilepath)
print(f"Completed: Saved Northern & Southern Hemisphere masks to netCDF file -> {outfilepath}")
