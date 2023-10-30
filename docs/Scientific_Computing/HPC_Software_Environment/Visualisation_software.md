---
created_at: '2019-01-16T20:51:18Z'
hidden: false
label_names:
- support
- application
- visualisation
position: 13
title: Visualisation software
vote_count: 1
vote_sum: 1
zendesk_article_id: 360000700295
zendesk_section_id: 360000040056
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

NeSI provides a variety of visualisation software solutions via modules.
Available software and software versions vary between the Mahuika and
Māui Ancil systems. Additional software can be provided upon request,
see section [Supported
Applications](https://support.nesi.org.nz/hc/en-gb/sections/360000040076-Supported-Applications).

Most software only requires a CPU node to run, but some software, in
particular high-performance 3D visualisation software, can utilise a GPU
node for better performance. Where possible, both CPU and GPU variants
of the same software are provided for maximum flexibility; please make
sure to select the correct module version as described below.

Apart from interactive operation, many visualisation solutions also
support batch mode ("headless") operation, allowing users to submit
large visualisation jobs to the HPC.

In the following installed packages are listed for:

-   Scripting Languages with Visualisation Capabilities

-   2D Visualisation Software

-   3D Visualisation Software

# Scripting Languages with Visualisation Capabilities

## Python

The Python language comes with packages such as "matplotlib" for
general-purpose 2D visualisation, or "vtk" (see VTK section on this
page) for 3D visualisation.

### Available Modules

<table style="height: 508px; width: 781px;">
<tbody>
<tr class="odd" style="height: 21px;">
<td class="wysiwyg-text-align-center"
style="width: 307px; height: 21px"><strong>Module Name</strong></td>
<td class="wysiwyg-text-align-center"
style="width: 67px; height: 21px"><strong>Mahuika</strong></td>
<td class="wysiwyg-text-align-center"
style="width: 88px; height: 21px"><strong>Māui Ancil</strong></td>
<td class="wysiwyg-text-align-center"
style="width: 319px; height: 21px"><strong>Comment</strong></td>
</tr>
<tr class="even" style="height: 21px;">
<td style="width: 307px; height: 21px">Anaconda2/5.2.0-GCC-7.1.0</td>
<td style="width: 67px; height: 21px"> </td>
<td class="wysiwyg-text-align-center"
style="width: 88px; height: 21px">✔</td>
<td style="width: 319px; height: 21px">Anaconda distribution of Python
2</td>
</tr>
<tr class="odd" style="height: 21px;">
<td style="width: 307px; height: 21px">Anaconda2/2019.10-GCC-7.1.0</td>
<td style="width: 67px; height: 21px"> </td>
<td class="wysiwyg-text-align-center"
style="width: 88px; height: 21px">✔</td>
<td style="width: 319px; height: 21px">Anaconda distribution of Python
2</td>
</tr>
<tr class="even" style="height: 21px;">
<td style="width: 307px; height: 21px">Anaconda3/5.2.0-GCC-7.1.0</td>
<td style="width: 67px; height: 21px"> </td>
<td class="wysiwyg-text-align-center"
style="width: 88px; height: 21px">✔</td>
<td style="width: 319px; height: 21px">Anaconda distribution of Python
3</td>
</tr>
<tr class="odd" style="height: 21px;">
<td style="width: 307px; height: 21px">Anaconda3/2019.03</td>
<td style="width: 67px; height: 21px"> </td>
<td class="wysiwyg-text-align-center"
style="width: 88px; height: 21px">✔</td>
<td style="width: 319px; height: 21px">Anaconda distribution of Python
3</td>
</tr>
<tr class="even" style="height: 21px;">
<td
style="width: 307px; height: 21px">Anaconda3/2019.07-gimkl-2018b</td>
<td style="width: 67px; height: 21px"> </td>
<td class="wysiwyg-text-align-center"
style="width: 88px; height: 21px">✔</td>
<td style="width: 319px; height: 21px">Anaconda distribution of Python
3</td>
</tr>
<tr class="odd" style="height: 22px;">
<td style="width: 307px; height: 22px">Anaconda3/2020.02-GCC-7.1.0</td>
<td style="width: 67px; height: 22px"> </td>
<td class="wysiwyg-text-align-center"
style="width: 88px; height: 22px">✔</td>
<td style="width: 319px; height: 22px">Anaconda distribution of Python
3</td>
</tr>
<tr class="even" style="height: 21px;">
<td style="width: 307px; height: 21px">Miniconda3/4.4.10</td>
<td class="wysiwyg-text-align-center"
style="width: 67px; height: 21px">✔</td>
<td class="wysiwyg-text-align-center"
style="width: 88px; height: 21px"> </td>
<td style="width: 319px; height: 21px">Minimal Anaconda distribution of
Python 3</td>
</tr>
<tr class="odd" style="height: 21px;">
<td style="width: 307px; height: 21px">Miniconda3/4.5.12</td>
<td class="wysiwyg-text-align-center"
style="width: 67px; height: 21px">✔</td>
<td class="wysiwyg-text-align-center"
style="width: 88px; height: 21px"> </td>
<td style="width: 319px; height: 21px">Minimal Anaconda distribution of
Python 3</td>
</tr>
<tr class="even" style="height: 21px;">
<td style="width: 307px; height: 21px">Miniconda3/4.7.10</td>
<td class="wysiwyg-text-align-center"
style="width: 67px; height: 21px">✔</td>
<td class="wysiwyg-text-align-center"
style="width: 88px; height: 21px"> </td>
<td style="width: 319px; height: 21px">Minimal Anaconda distribution of
Python 3</td>
</tr>
<tr class="odd" style="height: 22px;">
<td style="width: 307px; height: 22px">Miniconda3/4.8.2</td>
<td class="wysiwyg-text-align-center"
style="width: 67px; height: 22px">✔</td>
<td style="width: 88px; height: 22px"> </td>
<td style="width: 319px; height: 22px">Minimal Anaconda distribution of
Python 3</td>
</tr>
<tr class="even" style="height: 22px;">
<td style="width: 307px; height: 22px">Miniconda3/4.8.3</td>
<td class="wysiwyg-text-align-center"
style="width: 67px; height: 22px">✔</td>
<td style="width: 88px; height: 22px"> </td>
<td style="width: 319px; height: 22px">Minimal Anaconda distribution of
Python 3</td>
</tr>
<tr class="odd">
<td style="width: 307px">Miniconda3/4.9.2</td>
<td class="wysiwyg-text-align-center" style="width: 67px">✔</td>
<td style="width: 88px"> </td>
<td style="width: 319px">Minimal Anaconda distribution of Python 3</td>
</tr>
<tr class="even" style="height: 21px;">
<td style="width: 307px; height: 21px">Python-GPU/3.6.3-gimkl-2017a</td>
<td class="wysiwyg-text-align-center"
style="width: 67px; height: 21px">✔</td>
<td class="wysiwyg-text-align-center"
style="width: 88px; height: 21px"> </td>
<td style="width: 319px; height: 21px">GPU-enabled Python 3</td>
</tr>
<tr class="odd" style="height: 21px;">
<td
style="width: 307px; height: 21px">Python-Geo/2.7.14-gimkl-2017a</td>
<td class="wysiwyg-text-align-center"
style="width: 67px; height: 21px">✔</td>
<td style="width: 88px; height: 21px"> </td>
<td style="width: 319px; height: 21px">Python 2 for geospatial
applications</td>
</tr>
<tr class="even" style="height: 21px;">
<td
style="width: 307px; height: 21px">Python-Geo/2.7.16-gimkl-2018b</td>
<td class="wysiwyg-text-align-center"
style="width: 67px; height: 21px">✔</td>
<td style="width: 88px; height: 21px"> </td>
<td style="width: 319px; height: 21px">Python 2 for geospatial
applications</td>
</tr>
<tr class="odd" style="height: 21px;">
<td style="width: 307px; height: 21px">Python-Geo/3.6.3-gimkl-2017a</td>
<td class="wysiwyg-text-align-center"
style="width: 67px; height: 21px">✔</td>
<td style="width: 88px; height: 21px"> </td>
<td style="width: 319px; height: 21px">Python 3 for geospatial
applications</td>
</tr>
<tr class="even" style="height: 21px;">
<td style="width: 307px; height: 21px">Python-Geo/3.7.3-gimkl-2018b</td>
<td class="wysiwyg-text-align-center"
style="width: 67px; height: 21px">✔</td>
<td style="width: 88px; height: 21px"> </td>
<td style="width: 319px; height: 21px">Python 3 for geospatial
applications</td>
</tr>
<tr class="odd" style="height: 22px;">
<td style="width: 307px; height: 22px">Python-Geo/3.8.2-gimkl-2020a</td>
<td class="wysiwyg-text-align-center"
style="width: 67px; height: 22px">✔</td>
<td style="width: 88px; height: 22px"> </td>
<td style="width: 319px; height: 22px">Python 3 for geospatial
applications</td>
</tr>
<tr class="even" style="height: 21px;">
<td style="width: 307px; height: 21px">Python/2.7.14-gimkl-2017a</td>
<td class="wysiwyg-text-align-center"
style="width: 67px; height: 21px">✔</td>
<td style="width: 88px; height: 21px"> </td>
<td style="width: 319px; height: 21px">Python 2 base packages</td>
</tr>
<tr class="odd" style="height: 21px;">
<td style="width: 307px; height: 21px">Python/2.7.16-gimkl-2018b</td>
<td class="wysiwyg-text-align-center"
style="width: 67px; height: 21px">✔</td>
<td style="width: 88px; height: 21px"> </td>
<td style="width: 319px; height: 21px">Python 2 base packages</td>
</tr>
<tr class="even" style="height: 21px;">
<td style="width: 307px; height: 21px">Python/2.7.16-intel-2018b</td>
<td class="wysiwyg-text-align-center"
style="width: 67px; height: 21px">✔</td>
<td style="width: 88px; height: 21px"> </td>
<td style="width: 319px; height: 21px">Python 2 base packages</td>
</tr>
<tr class="odd">
<td style="width: 307px">Python/2.7.18-gimkl-2020a</td>
<td class="wysiwyg-text-align-center" style="width: 67px">✔</td>
<td style="width: 88px"> </td>
<td style="width: 319px">Python 2 base packages</td>
</tr>
<tr class="even" style="height: 21px;">
<td style="width: 307px; height: 21px">Python/3.6.3-gimkl-2017a</td>
<td class="wysiwyg-text-align-center"
style="width: 67px; height: 21px">✔</td>
<td style="width: 88px; height: 21px"> </td>
<td style="width: 319px; height: 21px">Python 3 base packages</td>
</tr>
<tr class="odd" style="height: 21px;">
<td style="width: 307px; height: 21px">Python/3.7.3-gimkl-2018b</td>
<td class="wysiwyg-text-align-center"
style="width: 67px; height: 21px">✔</td>
<td style="width: 88px; height: 21px"> </td>
<td style="width: 319px; height: 21px">Python 3 base packages</td>
</tr>
<tr class="even" style="height: 21px;">
<td style="width: 307px; height: 21px">Python/3.8.1-gimkl-2018b</td>
<td class="wysiwyg-text-align-center"
style="width: 67px; height: 21px">✔</td>
<td style="width: 88px; height: 21px"> </td>
<td style="width: 319px; height: 21px">Python 3 base packages</td>
</tr>
<tr class="odd">
<td style="width: 307px">Python/3.8.2-gimkl-2020a</td>
<td class="wysiwyg-text-align-center" style="width: 67px">✔</td>
<td style="width: 88px"> </td>
<td style="width: 319px">Python 3 base packages</td>
</tr>
<tr class="even">
<td style="width: 307px">Python/3.9.5-gimkl-2020a</td>
<td class="wysiwyg-text-align-center" style="width: 67px">✔</td>
<td style="width: 88px"> </td>
<td style="width: 319px">Python 3 base packages</td>
</tr>
</tbody>
</table>

##  

## R

The R language comes with built-in 2D plotting capabilities that can be
extended with additional packages.

### Available Modules

<table style="height: 136px; width: 828.683px;">
<tbody>
<tr class="odd" style="height: 21px;">
<td class="wysiwyg-text-align-center"
style="width: 318px; height: 21px"><strong>Module Name</strong></td>
<td class="wysiwyg-text-align-center"
style="width: 68px; height: 21px"><strong>Mahuika</strong></td>
<td class="wysiwyg-text-align-center"
style="width: 92px; height: 21px"><strong>Māui Ancil</strong></td>
<td class="wysiwyg-text-align-center"
style="width: 335.683px; height: 21px"><strong>Comment</strong></td>
</tr>
<tr class="even" style="height: 21px;">
<td style="width: 318px; height: 21px">R/3.4.2-gimkl-2017a</td>
<td class="wysiwyg-text-align-center"
style="width: 68px; height: 21px"> ✔</td>
<td class="wysiwyg-text-align-center"
style="width: 92px; height: 21px"> </td>
<td style="width: 335.683px; height: 21px">R base package</td>
</tr>
<tr class="odd" style="height: 21px;">
<td style="width: 318px; height: 21px">R/3.5.0-gimkl-2017a</td>
<td class="wysiwyg-text-align-center"
style="width: 68px; height: 21px"> ✔</td>
<td class="wysiwyg-text-align-center"
style="width: 92px; height: 21px"> </td>
<td style="width: 335.683px; height: 21px">R base package</td>
</tr>
<tr class="even" style="height: 21px;">
<td style="width: 318px; height: 21px">R/3.5.1-gimkl-2017a</td>
<td class="wysiwyg-text-align-center"
style="width: 68px; height: 21px">✔</td>
<td class="wysiwyg-text-align-center"
style="width: 92px; height: 21px"> </td>
<td style="width: 335.683px; height: 21px">R base package</td>
</tr>
<tr class="odd" style="height: 21px;">
<td style="width: 318px; height: 21px">R/3.5.3-gimkl-2018b</td>
<td class="wysiwyg-text-align-center"
style="width: 68px; height: 21px">✔</td>
<td class="wysiwyg-text-align-center"
style="width: 92px; height: 21px"> </td>
<td style="width: 335.683px; height: 21px">R base package</td>
</tr>
<tr class="even" style="height: 21px;">
<td style="width: 318px; height: 21px">R/3.6.1-gimkl-2018b</td>
<td class="wysiwyg-text-align-center"
style="width: 68px; height: 21px">✔</td>
<td class="wysiwyg-text-align-center"
style="width: 92px; height: 21px"> </td>
<td style="width: 335.683px; height: 21px">R base package</td>
</tr>
<tr class="odd" style="height: 21px;">
<td style="width: 318px; height: 21px">R/3.6.2-gimkl-2020a</td>
<td class="wysiwyg-text-align-center"
style="width: 68px; height: 21px">✔</td>
<td class="wysiwyg-text-align-center"
style="width: 92px; height: 21px"> </td>
<td style="width: 335.683px; height: 21px">R base package</td>
</tr>
<tr class="even">
<td style="width: 318px">R/4.0.1-gimkl-2020a</td>
<td class="wysiwyg-text-align-center" style="width: 68px">✔</td>
<td style="width: 92px"> </td>
<td style="width: 335.683px">R base package</td>
</tr>
<tr class="odd" style="height: 21px;">
<td style="width: 318px; height: 21px">R/3.5.1-gimkl-2018b</td>
<td class="wysiwyg-text-align-center"
style="width: 68px; height: 21px"> </td>
<td class="wysiwyg-text-align-center"
style="width: 92px; height: 21px">✔</td>
<td style="width: 335.683px; height: 21px">R base package</td>
</tr>
<tr class="even">
<td style="width: 318px">R/3.6.1-gimkl-2018b</td>
<td style="width: 68px"> </td>
<td class="wysiwyg-text-align-center" style="width: 92px">✔</td>
<td style="width: 335.683px">R base package</td>
</tr>
<tr class="odd" style="height: 21px;">
<td style="width: 318px; height: 21px">R-Geo/3.6.1-gimkl-2018b</td>
<td class="wysiwyg-text-align-center"
style="width: 68px; height: 21px">✔</td>
<td class="wysiwyg-text-align-center"
style="width: 92px; height: 21px"> </td>
<td style="width: 335.683px; height: 21px">R for geospatial
applications</td>
</tr>
<tr class="even">
<td style="width: 318px">R-Geo/3.6.2-gimkl-2020a</td>
<td class="wysiwyg-text-align-center" style="width: 68px">✔</td>
<td style="width: 92px"> </td>
<td style="width: 335.683px">R for geospatial applications</td>
</tr>
<tr class="odd">
<td style="width: 318px">R-Geo/4.0.1-gimkl-2020a</td>
<td class="wysiwyg-text-align-center" style="width: 68px">✔</td>
<td style="width: 92px"> </td>
<td style="width: 335.683px">R for geospatial applications</td>
</tr>
<tr class="even" style="height: 21px;">
<td style="width: 318px; height: 21px">Rstudio/1.1.456</td>
<td class="wysiwyg-text-align-center"
style="width: 68px; height: 21px"> </td>
<td class="wysiwyg-text-align-center"
style="width: 92px; height: 21px">✔</td>
<td style="width: 335.683px; height: 21px">Rstudio IDE</td>
</tr>
</tbody>
</table>

##  

## NCL

The NCAR Command Language provides visualisation capabilities which are
mostly used in the weather and climate fields.

### Available Modules

<table style="height: 68px; width: 826px;">
<tbody>
<tr class="odd" style="height: 21px;">
<td class="wysiwyg-text-align-center"
style="width: 317.567px; height: 21px"><strong>Module Name</strong></td>
<td class="wysiwyg-text-align-center"
style="width: 68.25px; height: 21px"><strong>Mahuika</strong></td>
<td class="wysiwyg-text-align-center"
style="width: 91.9833px; height: 21px"><strong>Māui Ancil</strong></td>
<td class="wysiwyg-text-align-center"
style="width: 335.2px; height: 21px"><strong>Comment</strong></td>
</tr>
<tr class="even" style="height: 21px;">
<td style="width: 317.567px; height: 21px">NCL/6.2.0-GCC-7.1.0</td>
<td class="wysiwyg-text-align-center"
style="width: 68.25px; height: 21px"> </td>
<td class="wysiwyg-text-align-center"
style="width: 91.9833px; height: 21px"> ✔</td>
<td style="width: 335.2px; height: 21px">NCL base package</td>
</tr>
<tr class="odd" style="height: 21px;">
<td style="width: 317.567px; height: 21px">NCL/6.4.0-GCC-7.1.0</td>
<td class="wysiwyg-text-align-center"
style="width: 68.25px; height: 21px"> </td>
<td class="wysiwyg-text-align-center"
style="width: 91.9833px; height: 21px"> ✔</td>
<td style="width: 335.2px; height: 21px">NCL base package</td>
</tr>
<tr class="even">
<td style="width: 317.567px">NCL/6.6.2-intel-2018b</td>
<td class="wysiwyg-text-align-center" style="width: 68.25px"> ✔</td>
<td style="width: 91.9833px"> </td>
<td style="width: 335.2px">NCL base package</td>
</tr>
</tbody>
</table>

 

## MATLAB

The MATLAB programming language comes with built-in visualisation
capabilities.

### Available Modules

<table style="height: 68px; width: 811px;">
<tbody>
<tr class="odd" style="height: 21px;">
<td class="wysiwyg-text-align-center"
style="width: 317px; height: 21px"><strong>Module Name</strong></td>
<td class="wysiwyg-text-align-center"
style="width: 68px; height: 21px"><strong>Mahuika</strong></td>
<td class="wysiwyg-text-align-center"
style="width: 91px; height: 21px"><strong>Māui Ancil</strong></td>
<td class="wysiwyg-text-align-center"
style="width: 335px; height: 21px"><strong>Comment</strong></td>
</tr>
<tr class="even" style="height: 21px;">
<td style="width: 317px; height: 21px">MATLAB/2016b</td>
<td class="wysiwyg-text-align-center"
style="width: 68px; height: 21px">✔</td>
<td class="wysiwyg-text-align-center"
style="width: 91px; height: 21px">✔</td>
<td style="width: 335px; height: 21px"> </td>
</tr>
<tr class="odd" style="height: 21px;">
<td style="width: 317px; height: 21px">MATLAB/2017b</td>
<td class="wysiwyg-text-align-center"
style="width: 68px; height: 21px">✔</td>
<td class="wysiwyg-text-align-center"
style="width: 91px; height: 21px">✔</td>
<td style="width: 335px; height: 21px"> </td>
</tr>
<tr class="even" style="height: 21px;">
<td style="width: 317px; height: 21px">MATLAB/2018b</td>
<td class="wysiwyg-text-align-center"
style="width: 68px; height: 21px">✔</td>
<td class="wysiwyg-text-align-center"
style="width: 91px; height: 21px">✔</td>
<td style="width: 335px; height: 21px"> </td>
</tr>
<tr class="odd" style="height: 21px;">
<td style="width: 317px; height: 21px">MATLAB/2019b</td>
<td class="wysiwyg-text-align-center"
style="width: 68px; height: 21px">✔</td>
<td class="wysiwyg-text-align-center"
style="width: 91px; height: 21px">✔</td>
<td style="width: 335px; height: 21px"> </td>
</tr>
<tr class="even">
<td style="width: 317px">MATLAB/2020a</td>
<td class="wysiwyg-text-align-center" style="width: 68px">✔</td>
<td style="width: 91px"> </td>
<td style="width: 335px"> </td>
</tr>
<tr class="odd">
<td style="width: 317px">MATLAB/2020b</td>
<td class="wysiwyg-text-align-center" style="width: 68px">✔</td>
<td style="width: 91px"> </td>
<td style="width: 335px"> </td>
</tr>
<tr class="even">
<td style="width: 317px">MATLAB/2021a</td>
<td class="wysiwyg-text-align-center" style="width: 68px">✔</td>
<td style="width: 91px"> </td>
<td style="width: 335px"> </td>
</tr>
</tbody>
</table>

#  

# 2D Visualisation Software

## IRIS

IRIS is a Python-based visualisation tool that is mainly used in the
weather and climate fields.

### Available Modules

<table style="height: 68px; width: 826px;">
<tbody>
<tr class="odd" style="height: 21px;">
<td class="wysiwyg-text-align-center"
style="width: 317.567px; height: 21px"><strong>Module Name</strong></td>
<td class="wysiwyg-text-align-center"
style="width: 68.25px; height: 21px"><strong>Mahuika</strong></td>
<td class="wysiwyg-text-align-center"
style="width: 91.9833px; height: 21px"><strong>Māui Ancil</strong></td>
<td class="wysiwyg-text-align-center"
style="width: 335.2px; height: 21px"><strong>Comment</strong></td>
</tr>
<tr class="even" style="height: 21px;">
<td
style="width: 317.567px; height: 21px">Anaconda2/5.2.0-GCC-7.1.0</td>
<td class="wysiwyg-text-align-center"
style="width: 68.25px; height: 21px"> </td>
<td class="wysiwyg-text-align-center"
style="width: 91.9833px; height: 21px"> ✔</td>
<td style="width: 335.2px; height: 21px">IRIS v1.13.0</td>
</tr>
<tr class="odd" style="height: 21px;">
<td
style="width: 317.567px; height: 21px">Anaconda2/2019.10-GCC-7.1.0</td>
<td class="wysiwyg-text-align-center"
style="width: 68.25px; height: 21px"> </td>
<td class="wysiwyg-text-align-center"
style="width: 91.9833px; height: 21px">✔</td>
<td style="width: 335.2px; height: 21px">IRIS v2.2.1.dev0</td>
</tr>
<tr class="even" style="height: 21px;">
<td
style="width: 317.567px; height: 21px">Anaconda3/5.2.0-GCC-7.1.0</td>
<td class="wysiwyg-text-align-center"
style="width: 68.25px; height: 21px"> </td>
<td class="wysiwyg-text-align-center"
style="width: 91.9833px; height: 21px"> ✔</td>
<td style="width: 335.2px; height: 21px">IRIS v1.13.0 </td>
</tr>
<tr class="odd" style="height: 21px;">
<td style="width: 317.567px; height: 21px">Anaconda3/2019.03</td>
<td class="wysiwyg-text-align-center"
style="width: 68.25px; height: 21px"> </td>
<td class="wysiwyg-text-align-center"
style="width: 91.9833px; height: 21px">✔</td>
<td style="width: 335.2px; height: 21px">IRIS v1.13.0</td>
</tr>
<tr class="even">
<td style="width: 317.567px">Anaconda3/2020.02-GCC-7.1.0</td>
<td style="width: 68.25px"> </td>
<td class="wysiwyg-text-align-center" style="width: 91.9833px">✔</td>
<td style="width: 335.2px">IRIS v2.4.0</td>
</tr>
</tbody>
</table>

##  

## Ncview

Ncview is a visual browser for netCDF files.

### Available Modules

<table style="height: 32px; width: 825px;">
<tbody>
<tr class="odd" style="height: 21px;">
<td class="wysiwyg-text-align-center"
style="width: 317.167px; height: 21px"><strong>Module Name</strong></td>
<td class="wysiwyg-text-align-center"
style="width: 68.25px; height: 21px"><strong>Mahuika</strong></td>
<td class="wysiwyg-text-align-center"
style="width: 91.8667px; height: 21px"><strong>Māui Ancil</strong></td>
<td class="wysiwyg-text-align-center"
style="width: 334.717px; height: 21px"><strong>Comment</strong></td>
</tr>
<tr class="even">
<td style="width: 317.167px">ncview/2.1.7-gimkl-2018b</td>
<td class="wysiwyg-text-align-center" style="width: 68.25px">✔</td>
<td style="width: 91.8667px"> </td>
<td style="width: 334.717px"> </td>
</tr>
<tr class="odd" style="height: 21px;">
<td style="width: 317.167px; height: 21px">NCVIEW/2.1.8-GCC-7.1.0</td>
<td class="wysiwyg-text-align-center"
style="width: 68.25px; height: 21px"> </td>
<td class="wysiwyg-text-align-center"
style="width: 91.8667px; height: 21px"> ✔</td>
<td style="width: 334.717px; height: 21px"> </td>
</tr>
</tbody>
</table>

##  

## XCONV

XCONV is a visual browser for netCDF and Unified Model format files.

### Available Modules

<table style="height: 32px; width: 825px;">
<tbody>
<tr class="odd" style="height: 21px;">
<td class="wysiwyg-text-align-center"
style="width: 317.167px; height: 21px"><strong>Module Name</strong></td>
<td class="wysiwyg-text-align-center"
style="width: 68.25px; height: 21px"><strong>Mahuika</strong></td>
<td class="wysiwyg-text-align-center"
style="width: 91.8667px; height: 21px"><strong>Māui Ancil</strong></td>
<td class="wysiwyg-text-align-center"
style="width: 334.717px; height: 21px"><strong>Comment</strong></td>
</tr>
<tr class="even" style="height: 21px;">
<td style="width: 317.167px; height: 21px">XCONV/1.93</td>
<td class="wysiwyg-text-align-center"
style="width: 68.25px; height: 21px"> </td>
<td class="wysiwyg-text-align-center"
style="width: 91.8667px; height: 21px"> ✔</td>
<td style="width: 334.717px; height: 21px"> </td>
</tr>
</tbody>
</table>

#  

# 3D Visualisation Software

## ParaView

[ParaView](https://www.paraview.org/) is a high-performance 3D
visualisation tool. The headless versions only provide ParaView Server,
which can operate in batch mode, as well as in client-server operation.

For interactive sessions, it is highly recommended to use ParaView with
the NICE DCV cloud visualisation software for best performance.
Client-server mode, where a ParaView GUI runs on a local machine and
connects to a ParaView server on the HPC, is also an option but requires
much more network bandwidth than [NICE
DCV](https://support.nesi.org.nz/hc/en-gb/articles/360000719156) and
thus may be slower.

### Parallelisation

The CPU based versions of ParaView use the OpenSWR rasteriser as well as
the OSPRay ray tracer for rendering graphics. These support parallel
operation for better performance, but are configured to only use a
single core by default. Run the following commands *before* launching
ParaView GUI or ParaView Server if you want to use more cores (depending
on the number of cores available in your session):

    export KNOB_MAX_WORKER_THREADS=<number of cores>
    export OSPRAY_THREADS=<number of cores>

ParaView Server also supports parallel execution using MPI, see "Setting
up Client-Server Mode" below.

### Available Modules

<table style="height: 136px; width: 828.683px;">
<tbody>
<tr class="odd" style="height: 21px;">
<td class="wysiwyg-text-align-center"
style="width: 318px; height: 21px"><strong>Module Name</strong></td>
<td class="wysiwyg-text-align-center"
style="width: 68px; height: 21px"><strong>Mahuika</strong></td>
<td class="wysiwyg-text-align-center"
style="width: 92px; height: 21px"><strong>Māui Ancil</strong></td>
<td class="wysiwyg-text-align-center"
style="width: 335.683px; height: 21px"><strong>Comment</strong></td>
</tr>
<tr class="even" style="height: 21px;">
<td style="width: 318px; height: 21px">ParaView/5.3.0-gimkl-2017a</td>
<td class="wysiwyg-text-align-center"
style="width: 68px; height: 21px">✔</td>
<td class="wysiwyg-text-align-center"
style="width: 92px; height: 21px"> </td>
<td style="width: 335.683px; height: 21px"> </td>
</tr>
<tr class="odd" style="height: 21px;">
<td
style="width: 318px; height: 21px">ParaView/5.4.1-gimkl-2017a-Python-2.7.14</td>
<td class="wysiwyg-text-align-center"
style="width: 68px; height: 21px">✔</td>
<td class="wysiwyg-text-align-center"
style="width: 92px; height: 21px"> </td>
<td style="width: 335.683px; height: 21px"> </td>
</tr>
<tr class="even" style="height: 21px;">
<td
style="width: 318px; height: 21px">ParaView/5.4.1-gimkl-2018b-Python-2.7.16</td>
<td class="wysiwyg-text-align-center"
style="width: 68px; height: 21px">✔</td>
<td class="wysiwyg-text-align-center"
style="width: 92px; height: 21px"> </td>
<td style="width: 335.683px; height: 21px"> </td>
</tr>
<tr class="odd" style="height: 21px;">
<td style="width: 318px; height: 21px">ParaView/5.4.1-gimpi-2018b</td>
<td class="wysiwyg-text-align-center"
style="width: 68px; height: 21px">✔</td>
<td class="wysiwyg-text-align-center"
style="width: 92px; height: 21px"> </td>
<td style="width: 335.683px; height: 21px"> </td>
</tr>
<tr class="even" style="height: 21px;">
<td
style="width: 318px; height: 21px">ParaView/5.5.2-gimpi-2018a-Server-EGL</td>
<td style="width: 68px; height: 21px"> </td>
<td class="wysiwyg-text-align-center"
style="width: 92px; height: 21px">✔</td>
<td style="width: 335.683px; height: 21px">Headless version for GPUs, no
GUI operation</td>
</tr>
<tr class="odd" style="height: 21px;">
<td
style="width: 318px; height: 21px">ParaView/5.5.2-gimpi-2018b-GUI-Mesa</td>
<td style="width: 68px; height: 21px"> </td>
<td class="wysiwyg-text-align-center"
style="width: 92px; height: 21px">✔</td>
<td style="width: 335.683px; height: 21px">GUI version for CPUs, no
headless operation</td>
</tr>
<tr class="even" style="height: 21px;">
<td
style="width: 318px; height: 21px">ParaView/5.5.2-gimpi-2018b-Server-OSMesa</td>
<td style="width: 68px; height: 21px"> </td>
<td class="wysiwyg-text-align-center"
style="width: 92px; height: 21px">✔</td>
<td style="width: 335.683px; height: 21px">Headless version for CPUs, no
GUI operation</td>
</tr>
<tr class="odd" style="height: 21px;">
<td
style="width: 318px; height: 21px">ParaView/5.6.0-gimkl-2018b-Python-3.7.3</td>
<td class="wysiwyg-text-align-center"
style="width: 68px; height: 21px"> </td>
<td style="width: 92px; height: 21px"> </td>
<td style="width: 335.683px; height: 21px"> </td>
</tr>
<tr class="even" style="height: 21px;">
<td
style="width: 318px; height: 21px">ParaView/5.6.0-gimpi-2017a-Server-OSMesa</td>
<td class="wysiwyg-text-align-center"
style="width: 68px; height: 21px">✔</td>
<td style="width: 92px; height: 21px"> </td>
<td style="width: 335.683px; height: 21px">Headless version for CPUs, no
GUI operation</td>
</tr>
<tr class="odd" style="height: 21px;">
<td style="width: 318px; height: 21px">ParaView/5.6.0-gimpi-2018b</td>
<td class="wysiwyg-text-align-center"
style="width: 68px; height: 21px">✔</td>
<td style="width: 92px; height: 21px"> </td>
<td style="width: 335.683px; height: 21px"> </td>
</tr>
<tr class="even">
<td style="width: 318px">ParaView/5.6.0-gimkl-2018b-Python-3.7.3</td>
<td class="wysiwyg-text-align-center" style="width: 68px">✔</td>
<td style="width: 92px"> </td>
<td style="width: 335.683px"> </td>
</tr>
<tr class="odd">
<td style="width: 318px">ParaView/5.9.0-gimkl-2020a-Python-3.8.2</td>
<td class="wysiwyg-text-align-center" style="width: 68px">✔</td>
<td style="width: 92px"> </td>
<td style="width: 335.683px"> </td>
</tr>
</tbody>
</table>

###  

### Setting up Client-Server Mode

If you want to use ParaView in client-server mode, use the following
setup:

-   Load one of the ParaView Server modules listed above and launch the
    server in your interactive visualisation session on the HPC:

<!-- -->

    mpiexec -np <number of MPI ranks> pvserver

-   Create an SSH tunnel for port "11111" from the HPC to your local
    machine using, e.g., the ssh program (Linux and MacOS) or MobaXterm
    (Windows)
-   Launch the ParaView GUI on your local machine and go to "File &gt;
    Connect"
-   Click on "Add Server", choose server type "Client / Server", host
    "localhost" (as we will be using the SSH tunnel), and port "11111",
    then click on "Configure"
-   Select the new server and click on "Connect"

## VisIt

VisIt is a high-performance 3D visualisation tool. At this point, only
GUI-based interactive sessions on CPUs via NICE DCV are supported, GPU
support and client-server operation will be added later.

### Available Modules

<table style="height: 47px; width: 829px;">
<tbody>
<tr class="odd" style="height: 21px;">
<td class="wysiwyg-text-align-center"
style="width: 318.85px; height: 21px"><strong>Module Name</strong></td>
<td class="wysiwyg-text-align-center"
style="width: 68.45px; height: 21px"><strong>Mahuika</strong></td>
<td class="wysiwyg-text-align-center"
style="width: 92.3px; height: 21px"><strong>Māui Ancil</strong></td>
<td class="wysiwyg-text-align-center"
style="width: 336.4px; height: 21px"><strong>Comment</strong></td>
</tr>
<tr class="even" style="height: 21px;">
<td
style="width: 318.85px; height: 21px">VisIt/2.13.3-gimpi-2018b-GUI-Mesa</td>
<td style="width: 68.45px; height: 21px"> </td>
<td class="wysiwyg-text-align-center"
style="width: 92.3px; height: 21px">✔</td>
<td style="width: 336.4px; height: 21px">GUI version for CPUs</td>
</tr>
</tbody>
</table>

##  

## VTK

The Visualization ToolKit (VTK) can be used for 3D visualisation in
various programming languages, in particular with the Python scripting
language.

### Available Modules

<table style="height: 41px; width: 828px;">
<tbody>
<tr class="odd" style="height: 21px;">
<td class="wysiwyg-text-align-center"
style="width: 318.517px; height: 21px"><strong>Module Name</strong></td>
<td class="wysiwyg-text-align-center"
style="width: 68.1167px; height: 21px"><strong>Mahuika</strong></td>
<td class="wysiwyg-text-align-center"
style="width: 92.15px; height: 21px"><strong>Māui Ancil</strong></td>
<td class="wysiwyg-text-align-center"
style="width: 336.217px; height: 21px"><strong>Comment</strong></td>
</tr>
<tr class="even" style="height: 21px;">
<td
style="width: 318.517px; height: 21px">VTK/6.3.0-gimkl-2017a-Python-2.7.14</td>
<td class="wysiwyg-text-align-center"
style="width: 68.1167px; height: 21px">✔</td>
<td class="wysiwyg-text-align-center"
style="width: 92.15px; height: 21px"> </td>
<td style="width: 336.217px; height: 21px">VTK6 with Python
bindings</td>
</tr>
<tr class="odd" style="height: 21px;">
<td
style="width: 318.517px; height: 21px">VTK/7.1.1-gimkl-2018b-Python-2.7.16</td>
<td class="wysiwyg-text-align-center"
style="width: 68.1167px; height: 21px">✔</td>
<td class="wysiwyg-text-align-center"
style="width: 92.15px; height: 21px"> </td>
<td style="width: 336.217px; height: 21px">VTK7 with Python
bindings</td>
</tr>
<tr class="even" style="height: 21px;">
<td
style="width: 318.517px; height: 21px">VTK/8.1.1-GCC-7.1.0-Anaconda2-5.2.0</td>
<td style="width: 68.1167px; height: 21px"> </td>
<td class="wysiwyg-text-align-center"
style="width: 92.15px; height: 21px">✔</td>
<td style="width: 336.217px; height: 21px">VTK8 with Python
bindings</td>
</tr>
</tbody>
</table>

 
