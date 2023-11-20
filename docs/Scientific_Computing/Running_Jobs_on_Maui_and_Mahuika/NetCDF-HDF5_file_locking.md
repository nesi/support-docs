---
created_at: '2019-04-12T02:21:25Z'
hidden: false
position: 17
tags: []
title: NetCDF / HDF5 file locking
vote_count: 2
vote_sum: 2
zendesk_article_id: 360000902955
zendesk_section_id: 360000030876
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! warning
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

NeSI provides libraries for creating and accessing files in the NetCDF
and HDF5 formats on both Mahuika and Māui.

On Māui, both libraries are part of the Cray Programming Environment and
can be accessed using the modules
'cray-netcdf'/'cray-netcdf-hdf5parallel', and
'cray-hdf5'/'cray-hdf5-parallel'.

Recent versions of NetCDF and HDF5 (HDF5 1.10.x and newer) use a file
locking feature. This prevents data corruption in rare cases of
single-writer/multiple-reader and multiple writer access patterns.

On our current XC50 platform (Māui), **file locking is not yet fully
supported** by Cray's DVS. (DVS allows accessing the parallel file
system GPFS on the XC50 compute nodes).

Accordingly, NetCDF-4 and HDF5 applications that write data from Māui
compute nodes need to disable file locking with:

``` sl
export HDF5_USE_FILE_LOCKING=FALSE
```

If file locking is enabled, HDF5/NetCDF4 applications may experience
errors such as

``` sl
ncdump: /path/to/file.nc: NetCDF: HDF error
```

or

``` sl
Error in EM_FOPEN: NetCDF: HDF error - /path/to/file.nc 
```

or

``` sl
(-101) // Error at HDF5 layer
```

or

``` sl
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
```

**Important:** As file locking has to be disabled on the XC50, care
should be taken to avoid concurrent reader/writer access in your
application.

For more information see:

-   [Design -File Locking under SWMR in
    HDF5](https://support.hdfgroup.org/HDF5/docNewFeatures/SWMR/Design-HDF5-FileLocking.pdf)
-   [release notes, where mechanism for disabling file locking was
    introduced](https://support.hdfgroup.org/ftp/HDF5/releases/ReleaseFiles/hdf5-1.10.1-RELEASE.txt)