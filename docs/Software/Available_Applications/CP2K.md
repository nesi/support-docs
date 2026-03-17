---
created_at: '2015-09-08T03:11:50Z'
tags:
- chemistry
- Density Functional Theory
- Molecular Dynamics
- QMMM
- Computational Chemistry
title: CP2K
---

[//]:CP2K.md> (APPS PAGE BOILERPLATE START)
{% set app_name = page.title | trim %}
{% set app = applications[app_name] %}
{% include "partials/app_header.html" %}
[//]:CP2K.md> (APPS PAGE BOILERPLATE END)

## Description

CP2K is a quantum chemistry and solid state physics software package that can perform atomistic simulations of solid state, liquid, molecular, periodic, material, crystal, and biological systems.

CP2K provides a general framework for different modeling methods such as DFT using the mixed Gaussian and plane waves approaches GPW and GAPW. Supported theory levels include DFTB, LDA, GGA, MP2, RPA, semi-empirical methods (AM1, PM3, PM6, RM1, MNDO, …), and classical force fields (AMBER, CHARMM, …). CP2K can do simulations of molecular dynamics, metadynamics, Monte Carlo, Ehrenfest dynamics, vibrational analysis, core level spectroscopy, energy minimization, and transition state optimization using NEB or dimer method.

For more information on what you can do with CP2K see the [official documentation](https://www.cp2k.org/).

## Licensing requirements

CP2K is freely available under the GPL license.

## Example script

```sh
#!/bin/bash -e

#SBATCH --job-name       CP2K_job
#SBATCH --account        nesi99999
#SBATCH --time           01:00:00
#SBATCH --nodes          1
#SBATCH --tasks          8 # This determines the number of MPI processes
#SBATCH --cpus-per-task  8 # This determines the number of OpenMP threads
#SBATCH --mem-per-cpu    2G
#SBATCH --output         NWChem_job.%j.out    # Include the job ID in the names
#SBATCH --error          NWChem_job.%j.err    # of the output and error files

module load CP2K/2025.2-foss-2023a

srun cp2k.psmp -i example.inp -o example.out
```

You can find an example of ```example.inp``` for a water system below for testing at the end of this page:

## Futher Notes

### Using Hybrid Functionals

It is possible to use hybrid functionals in CP2K. However, there is a bug that requires the number of OpenMP threads used to be set to 1 when using hybrid functionals. This requires `--cpus-per-task` to be set to 1. However, if you need extra cores, just set the number of MPI processes (`--tasks`) to your desired value. For example, if you want to use 64 cores, set in your slurm submit script:

```sh
#SBATCH --nodes          1
#SBATCH --tasks          64 # This determines the number of MPI processes
#SBATCH --cpus-per-task  1 # This determines the number of OpenMP threads
```

## Example Input Files

### Example Input file for Pure GGA Functionals

```example.inp``` for a water system using a pure GGA functional:

```example.inp
&GLOBAL
   ! the project name is made part of most output files... useful to keep order 
   PROJECT WATER
   ! various runtypes (energy, geo_opt, etc.) available.
   RUN_TYPE ENERGY
   ! amount of information printed to output
   IOLEVEL  MEDIUM
&END GLOBAL

&FORCE_EVAL
   ! the electronic structure part of CP2K is named Quickstep
   METHOD Quickstep
   &DFT
      ! basis sets and pseudopotential files can be found in cp2k/data
      BASIS_SET_FILE_NAME HFX_BASIS
      POTENTIAL_FILE_NAME GTH_POTENTIALS

      ! Charge and multiplicity
      CHARGE 0
      MULTIPLICITY 1

      &MGRID
         ! PW cutoff ... depends on the element (basis) too small cutoffs lead to the eggbox effect.
         ! certain calculations (e.g. geometry optimization, vibrational frequencies,
         ! NPT and cell optimizations, need higher cutoffs)
         CUTOFF [Ry] 400
      &END

      &QS
         ! use the GPW method (i.e. pseudopotential based calculations with the Gaussian and Plane Waves scheme).
         METHOD GPW
         ! default threshold for numerics ~ roughly numerical accuracy of the total energy per electron,
         ! sets reasonable values for all other thresholds.
         EPS_DEFAULT 1.0E-7
         ! used for MD, the method used to generate the initial guess.
         EXTRAPOLATION ASPC
      &END

      &POISSON
         PERIODIC XYZ ! the default, gas phase systems should have 'NONE' and a wavelet solver
      &END

      &PRINT
         ! at the end of the SCF procedure generate cube files of the density
         &E_DENSITY_CUBE OFF
         &END E_DENSITY_CUBE
         ! compute eigenvalues and homo-lumo gap
         &MO_CUBES
            NLUMO 4
            NHOMO 4
            WRITE_CUBE .FALSE.
            &EACH
               MD 10
            &END
         &END
      &END
      ! use the OT METHOD for robust and efficient SCF, suitable for all non-metallic systems.
      &SCF
         SCF_GUESS ATOMIC ! can be used to RESTART an interrupted calculation
         MAX_SCF 30
         EPS_SCF 1.0E-6 ! accuracy of the SCF procedure, for OT typically 1.0E-6 - 1.0E-7, for diagonalization may have to be smaller
         &OT
            ! an accurate preconditioner suitable also for larger systems
            PRECONDITIONER FULL_SINGLE_INVERSE
            ! the most robust choice (DIIS might sometimes be faster, but not as stable).
            MINIMIZER DIIS
         &END OT
         &OUTER_SCF ! repeat the inner SCF cycle 10 times
            MAX_SCF 10
            EPS_SCF 1.0E-6 ! must match the above
         &END
         ! do not store the wfn during MD
         &PRINT
            &RESTART ON
            &END
         &END
      &END SCF

      ! specify the exchange and correlation treatment
      &XC
         ! use a PBE functional
         &XC_FUNCTIONAL
            &PBE
            &END
         &END XC_FUNCTIONAL
         ! adding Grimme's D3 correction (by default without C9 terms)
         &VDW_POTENTIAL
            POTENTIAL_TYPE PAIR_POTENTIAL
            &PAIR_POTENTIAL
               PARAMETER_FILE_NAME dftd3.dat
               TYPE DFTD3
               REFERENCE_FUNCTIONAL PBE
               R_CUTOFF [angstrom] 16
            &END
         &END VDW_POTENTIAL
      &END XC
   &END DFT
   ! description of the system
   &SUBSYS
      &CELL
         ! unit cells that are orthorhombic are more efficient with CP2K
         ABC [angstrom] 12.42 12.42 12.42
      &END CELL

      ! atom coordinates can be in the &COORD section,
      ! or provided as an external file.
      &TOPOLOGY
         COORD_FILE_NAME water.xyz
         COORD_FILE_FORMAT XYZ
      &END

      ! MOLOPT basis sets are fairly costly,
      ! but in the 'DZVP-MOLOPT-SR-GTH' available for all elements
      ! their contracted nature makes them suitable
      ! for condensed and gas phase systems alike.
      &KIND H
         BASIS_SET DZVP-GTH
         POTENTIAL GTH-PBE-q1
      &END KIND
      &KIND O
         BASIS_SET DZVP-GTH
         POTENTIAL GTH-PBE-q6
      &END KIND
   &END SUBSYS
&END FORCE_EVAL
```

### Example Input file for Hybrid GGA Functionals

```example.inp``` using a water system using a hybrid GGA functional:

```example.inp
&GLOBAL
   ! the project name is made part of most output files... useful to keep order 
   PROJECT WATER
   ! various runtypes (energy, geo_opt, etc.) available.
   RUN_TYPE ENERGY
   ! amount of information printed to output
   IOLEVEL  MEDIUM
&END GLOBAL

&FORCE_EVAL
   ! the electronic structure part of CP2K is named Quickstep
   METHOD Quickstep
   &DFT
      ! basis sets and pseudopotential files can be found in cp2k/data
      BASIS_SET_FILE_NAME HFX_BASIS
      POTENTIAL_FILE_NAME GTH_POTENTIALS

      ! Charge and multiplicity
      CHARGE 0
      MULTIPLICITY 1

      &MGRID
         ! PW cutoff ... depends on the element (basis) too small cutoffs lead to the eggbox effect.
         ! certain calculations (e.g. geometry optimization, vibrational frequencies,
         ! NPT and cell optimizations, need higher cutoffs)
         CUTOFF [Ry] 400
      &END

      &QS
         ! use the GPW method (i.e. pseudopotential based calculations with the Gaussian and Plane Waves scheme).
         METHOD GPW
         ! default threshold for numerics ~ roughly numerical accuracy of the total energy per electron,
         ! sets reasonable values for all other thresholds.
         EPS_DEFAULT 1.0E-7
         ! used for MD, the method used to generate the initial guess.
         EXTRAPOLATION ASPC
      &END

      &POISSON
         PERIODIC XYZ ! the default, gas phase systems should have 'NONE' and a wavelet solver
      &END

      &PRINT
         ! at the end of the SCF procedure generate cube files of the density
         &E_DENSITY_CUBE OFF
         &END E_DENSITY_CUBE
         ! compute eigenvalues and homo-lumo gap
         &MO_CUBES
            NLUMO 4
            NHOMO 4
            WRITE_CUBE .FALSE.
            &EACH
               MD 10
            &END
         &END
      &END
      ! use the OT METHOD for robust and efficient SCF, suitable for all non-metallic systems.
      &SCF
         SCF_GUESS ATOMIC ! can be used to RESTART an interrupted calculation
         MAX_SCF 30
         EPS_SCF 1.0E-6 ! accuracy of the SCF procedure, for OT typically 1.0E-6 - 1.0E-7, for diagonalization may have to be smaller
         &OT
            ! an accurate preconditioner suitable also for larger systems
            PRECONDITIONER FULL_SINGLE_INVERSE
            ! the most robust choice (DIIS might sometimes be faster, but not as stable).
            MINIMIZER DIIS
         &END OT
         &OUTER_SCF ! repeat the inner SCF cycle 10 times
            MAX_SCF 10
            EPS_SCF 1.0E-6 ! must match the above
         &END
         ! do not store the wfn during MD
         &PRINT
            &RESTART ON
            &END
         &END
      &END SCF

      ! specify the exchange and correlation treatment
      !&XC
      !   ! use a PBE functional
      !   &XC_FUNCTIONAL
      !      &PBE
      !      &END
      !   &END XC_FUNCTIONAL
      !   ! adding Grimme's D3 correction (by default without C9 terms)
      !   &VDW_POTENTIAL
      !      POTENTIAL_TYPE PAIR_POTENTIAL
      !      &PAIR_POTENTIAL
      !         PARAMETER_FILE_NAME dftd3.dat
      !         TYPE DFTD3
      !         REFERENCE_FUNCTIONAL PBE
      !         R_CUTOFF [angstrom] 16
      !      &END
      !   &END VDW_POTENTIAL
      !&END XC

    ! specify the exchange and correlation treatment
    &XC
      ! use a PBE0 functional
      &XC_FUNCTIONAL
       &PBE
         ! 75% GGA exchange
         SCALE_X 0.75
         ! 100% GGA correlation
         SCALE_C 1.0
       &END PBE
      &END XC_FUNCTIONAL
      &HF
        ! 25 % HFX exchange
        FRACTION 0.25
        ! Important to improve scaling from O(N^4) to O(N)
        &SCREENING
          ! important parameter to get stable HFX calcs (contributions to hfx smaller than EPS_SCHWARZ are not considered)
          EPS_SCHWARZ 1.0E-6
          ! needs a good (GGA) initial guess
          ! screening on the product between maximum of density matrix elements and ERI
          SCREEN_ON_INITIAL_P TRUE
        &END
        &INTERACTION_POTENTIAL
          ! for condensed phase systems
          POTENTIAL_TYPE TRUNCATED
          ! should be less than half the cell
          CUTOFF_RADIUS  6.0
          ! data file needed with the truncated operator
          T_C_G_DATA ./t_c_g.dat
        &END
        &MEMORY
          ! In MB per MPI rank.. use as much as need to get in-core operation
          MAX_MEMORY 4000
          EPS_STORAGE_SCALING 0.1
        &END
      &END
      ! adding Grimme's D3 correction (by default without C9 terms)
      &VDW_POTENTIAL
         POTENTIAL_TYPE PAIR_POTENTIAL
         &PAIR_POTENTIAL
            PARAMETER_FILE_NAME dftd3.dat
            TYPE DFTD3
            REFERENCE_FUNCTIONAL PBE0
            R_CUTOFF [angstrom] 16
         &END
      &END VDW_POTENTIAL
    &END XC

   &END DFT
   ! description of the system
   &SUBSYS
      &CELL
         ! unit cells that are orthorhombic are more efficient with CP2K
         ABC [angstrom] 12.42 12.42 12.42
      &END CELL

      ! atom coordinates can be in the &COORD section,
      ! or provided as an external file.
      &TOPOLOGY
         COORD_FILE_NAME water.xyz
         COORD_FILE_FORMAT XYZ
      &END

      ! MOLOPT basis sets are fairly costly,
      ! but in the 'DZVP-MOLOPT-SR-GTH' available for all elements
      ! their contracted nature makes them suitable
      ! for condensed and gas phase systems alike.
      &KIND H
         BASIS_SET DZVP-GTH
         POTENTIAL GTH-PBE-q1
      &END KIND
      &KIND O
         BASIS_SET DZVP-GTH
         POTENTIAL GTH-PBE-q6
      &END KIND
   &END SUBSYS
&END FORCE_EVAL
```
