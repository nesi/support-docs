On Thursday afternoon there was a change to the University ANSYS
licences, you may find that your jobs fail with a licence error.

The following command should resolve the issue (where `-revn 202` is
replaced with the version you use).

    module load ANSYS/2020R2
    ansysli_util -revn 202 -deleteuserprefs

It is yet to be determined the effect this will have on all of the ANSYS
products, so please open a [support ticket](mailto:support.nesi.org.nz)
if you encounter problems.
