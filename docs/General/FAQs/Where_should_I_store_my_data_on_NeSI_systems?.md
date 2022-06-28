::: {.pm-table-container .sc-jKJlTe .loXQau data-layout="default"}
::: {.pm-table-wrapper}
  --------------------------------------------------------------- ---------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **How often will my team\'s HPC jobs be accessing the data?**   **How often will my team\'s HPC jobs be modifying the data? **   **Recommended option **
  Often                                                           Often (at least once every two months)                           Store in your /nobackup/\<projectcode\> directory (but ensure key result data is copied to the persistent project directory).
  Often                                                           Seldom                                                           Store in your /project/\<projectcode\> directory.
  Seldom                                                          Seldom                                                           Apply for an allocation to use NeSI's [long-term storage service](https://support.nesi.org.nz/hc/en-gb/articles/360001169956-Long-Term-Storage-Service "https://support.nesi.org.nz/hc/en-gb/articles/360001169956-Long-Term-Storage-Service"){.sc-cHGsZl .lirsdj}or store elsewhere (e.g. at your institution).
  --------------------------------------------------------------- ---------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::
:::

 

In general, the **project directory** should be used for reference data,
tools, and job submission and management scripts. The **nobackup
directory** should be used for holding large reference working datasets
(e.g., an extraction of compressed input data) and as a destination for
writing and modifying temporary data. The nobackup directory can also be
used to build and edit code, provided that the code is under version
control and changes are regularly checked into upstream revision control
systems. The **long-term storage service** should be used for larger
datasets that you only access occasionally and do not need to change in
situ. 

 
