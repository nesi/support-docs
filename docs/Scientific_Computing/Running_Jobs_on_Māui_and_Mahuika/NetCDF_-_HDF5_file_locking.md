NeSI provides libraries for creating and accessing files in the NetCDF
and HDF5 formats on both Mahuika and Māui.

On Māui, both libraries are part of the Cray Programming Environment and
can be accessed using the modules
\'cray-netcdf\'/\'cray-netcdf-hdf5parallel\', and
\'cray-hdf5\'/\'cray-hdf5-parallel\'.

Recent versions of NetCDF and HDF5 (HDF5 1.10.x and newer) use a file
locking feature. This prevents data corruption in rare cases of
single-writer/multiple-reader and multiple writer access patterns. On
our current XC50 platforms (Māui), file locking is not yet fully
supported by Cray\'s DVS, which allows accessing the parallel file
system GPFS on the XC50 compute nodes.

Due to this missing support, NetCDF (using NetCDF4 format) and HDF5
applications writing data from Māui compute nodes need to disable file
locking by using the following environment variable:

    export HDF5_USE_FILE_LOCKING=FALSE

If file locking is enabled, HDF5/NetCDF4 applications may experience
errors such as

    ncdump: /path/to/file.nc: NetCDF: HDF error

or

    Error in EM_FOPEN: NetCDF: HDF error - /path/to/file.nc 

or

    (-101) // Error at HDF5 layer

or

    HDF5-DIAG: Error detected in HDF5 (1.10.2) thread 0:
    #000: ../../src/H5F.c line 445 in H5Fcreate(): unable to create file
    major: File accessibilty
    minor: Unable to open file
    #001: ../../src/H5Fint.c line 1519 in H5F_open(): unable to lock the file
    major: File accessibilty
    minor: Unable to open file
    #002: ../../src/H5FD.c line 1650 in H5FD_lock(): driver lock request failed
    major: Virtual File Layer
    minor: Can't update object
    #003: ../../src/H5FDsec2.c line 941 in H5FD_sec2_lock(): unable to lock file, errno = 524, error message = 'Unknown error 524'
    major: File accessibilty
    minor: Bad file ID accessed

**Important:** As file locking has to be disabled on the XC50, you need
to take care to avoid concurrent reader/writer access in your
application. Even though most applications should not exhibit such
access patterns, we cannot guarantee that for your case!

For more information see:

-   [Design -File Locking under SWMR in
    HDF5](https://support.hdfgroup.org/HDF5/docNewFeatures/SWMR/Design-HDF5-FileLocking.pdf)
-   [release notes, where mechanism for disabling file locking was
    introduced](https://support.hdfgroup.org/ftp/HDF5/releases/ReleaseFiles/hdf5-1.10.1-RELEASE.txt)
