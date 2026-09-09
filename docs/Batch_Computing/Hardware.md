---
created_at: '2022-06-13T04:54:38Z'
description:  This page below outlines the available hardware.
tags:
 - gpu
---

A list of the currently available hardware.

If you are looking for information on maximum resource requests, see [Job Limits](Job_Limits.md).

## Compute Nodes

Your jobs will land on appropriately sized nodes automatically based on your CPU to memory ratio. For example in the Genoa partition:

- A job requesting ≤ 2 GB/core will run on a 2 GB/core node, or if full, a 4 GB/core node.
- A job requesting ≤ 4 GB/core will run on a 4 GB/core node, or if full, a 8 GB/core node.

And so on.
You will always get the amount of memory you requested, even if running on a node with a higher ratio.

<table>
    <tr>
        <td>Architecture</td>
        <td>Cores</td>
        <td colspan="2">Memory</td>
        <td>GPU</td>
        <td>Nodes</td>
    </tr>
    <tr>
        <td rowspan="2">2 x AMD Milan 7713 CPU<br>└ 8 x Chiplets<br>&nbsp;&nbsp;&nbsp;&nbsp;└ 8 x Cores</td>
        <td rowspan="2">128</td>
        <td>512GB</td>
        <td><em>(4GB / Core)</em></td>
        <td>-</td>
        <td>55</td>
    </tr>
    <tr>
        <td>1024GB</td>
        <td><em>(8GB / Core)</em></td>
        <td>-</td>
        <td>8</td>
    </tr>
    <tr id="gpu-milan-a100">
        <td>1 x AMD Milan 7713P CPU<br>└ 8 x Chiplets<br>&nbsp;&nbsp;&nbsp;&nbsp;└ 8 x Cores</td>
        <td>64</td>
        <td>512GB</td>
        <td><em>(8GB / Core)</em></td>
        <td>4 x NVIDIA HGX A100</td>
        <td>4</td>
    </tr>
    <tr>
        <td rowspan="5">2 x AMD Genoa 9634 CPU<br>└ 12 x Chiplets<br>&nbsp;&nbsp;&nbsp;&nbsp;└ 7 x Cores</td>
        <td rowspan="5">168</td>
        <td>384GB</td>
        <td><em>(2GB / Core)</em></td>
        <td>-</td>
        <td>44</td>
    </tr>
    <tr id="gpu-genoa-rtx6000">
        <td>768GB</td>
        <td><em>(4GB / Core)</em></td>
        <td>2 x NVIDIA RTX PRO 6000</td>
        <td>4</td>
    </tr>
    <tr>
        <td rowspan="3">1536GB</td>
        <td rowspan="3"><em>(8GB / Core)</em></td>
        <td>-</td>
        <td>8</td>
    </tr>
    <tr id="gpu-genoa-h100">
        <td>2 x NVIDIA H100 NVL</td>
        <td>4</td>
    </tr>
    <tr id="gpu-genoa-l4">
        <td>4 x NVIDIA L4</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2 x Intel Xeon Gold 6230 CPU<br>&nbsp;&nbsp;&nbsp;&nbsp;(Cascade Lake)</td>
        <td>40</td>
        <td>1.5TB</td>
        <td><em>(38GB / Core)</em></td>
        <td>-</td>
        <td>2</td>
    </tr>
    <tr>
        <td>4 x Intel Xeon Gold 6238M CPU<br>&nbsp;&nbsp;&nbsp;&nbsp;(Cascade Lake)</td>
        <td>88</td>
        <td>6TB</td>
        <td><em>(69GB / Core)</em></td>
        <td>-</td>
        <td>1</td>
    </tr>
</table>

!!! note "Memory figures"
    Memory shown is the amount physically installed. A small amount is reserved for the operating system,
    so the memory actually available to jobs is a few percent lower — for example a 512GB Milan node offers
    480GB to Slurm. A job requesting exactly the full per-core ratio across every core of a node will
    therefore not fit. Run `sinfo -o '%n %m'` for the exact schedulable figures.

!!! warning "hugemem"
    Jobs will not automatically land on the Intel 'hugemem' nodes. You must specifically request `--partition hugemem`.
    The CPU architecture is different enough from the milan and genoa nodes, you will probably have to recompile your software.


## GPUs

REANNZ HPC has a range of Graphical Processing Units (GPUs) to accelerate compute-intensive research and support more analysis at scale.

Depending on the type of GPU, you can access them in different ways, such as via batch scheduler (Slurm),
or Virtual Machines (VMs).

For information about how to request these GPUs in a Slurm job, see [Using GPUs](Using_GPUs.md).

<table>
    <tr>
        <td>Architecture</td>
        <td>Purpose/Note</td>
        <td>VRAM</td>
        <td>GPUs on Node</td>
        <td colspan="2">Nodes</td>
    </tr>
    <tr>
        <td>NVIDIA A100 SXM4</td>
        <td></td>
        <td>80GB</td>
        <td>4</td>
        <td><a href="#gpu-milan-a100">Milan</a></td>
        <td>4</td>
    </tr>
    <tr>
        <td>NVIDIA RTX PRO 6000</td>
        <td>Avoid for double precision floating point (fp64) as it is slow</td>
        <td>96GB</td>
        <td>2</td>
        <td><a href="#gpu-genoa-rtx6000">Genoa</a></td>
        <td>4</td>
    </tr>
    <tr>
        <td>NVIDIA H100 NVL</td>
        <td></td>
        <td>94GB</td>
        <td>2</td>
        <td><a href="#gpu-genoa-h100">Genoa</a></td>
        <td>4</td>
    </tr>
    <tr>
        <td>NVIDIA L4</td>
        <td>Avoid for double precision floating point (fp64) as it is slow</td>
        <td>24GB</td>
        <td>4</td>
        <td><a href="#gpu-genoa-l4">Genoa</a></td>
        <td>4</td>
    </tr>
</table>

### Choosing a GPU

A rough guide to which GPU suits which kind of work. See [Using GPUs](Using_GPUs.md)
for how to request a specific type.

<table>
    <tr>
        <td>Workload</td>
        <td>Best fit</td>
        <td>Avoid</td>
    </tr>
    <tr>
        <td>fp64 HPC (VASP, Quantum ESPRESSO, CP2K, OpenFOAM, Gaussian)</td>
        <td>H100 NVL, then A100</td>
        <td>L4, RTX PRO 6000</td>
    </tr>
    <tr>
        <td>Molecular dynamics (GROMACS, AMBER, OpenMM)</td>
        <td>RTX PRO 6000 ≳ H100 NVL &gt; A100</td>
        <td>L4</td>
    </tr>
    <tr>
        <td>4-GPU tightly-coupled</td>
        <td>A100 <em>(only option — see <a href="#gpu-milan-a100">Milan</a>)</em></td>
        <td>everything else</td>
    </tr>
    <tr>
        <td>2-GPU communication-bound</td>
        <td>H100 NVL <em>(600GB/s NVLink between the pair)</em></td>
        <td>RTX PRO 6000, L4</td>
    </tr>
    <tr>
        <td>Working set larger than 24GB</td>
        <td>A100, H100 NVL, RTX PRO 6000</td>
        <td>L4</td>
    </tr>
    <tr>
        <td>Single-GPU fine-tuning, large-model inference</td>
        <td>RTX PRO 6000 or H100 NVL</td>
        <td>L4</td>
    </tr>
    <tr>
        <td>Small-model inference, video encoding, teaching</td>
        <td>L4 <em>(best performance per watt)</em></td>
        <td>-</td>
    </tr>
</table>

!!! note "Multi-node GPU jobs"
    GPUDirect RDMA is not currently enabled, and the GPU nodes are split across
    two InfiniBand switches. Keep GPU jobs within a single node.

### GPU specifications

Peak **dense** throughput per GPU.

!!! note "Dense figures, datasheets will show higher speeds"
    Datasheets often quote tensor figures twice as large as the ones below,
    marked with an asterisk for "with sparsity". Those speeds rely on *structured
    sparsity*: Tensor cores can skip zeros in a weight
    matrix, provided exactly two of every four consecutive values are zero. Half
    the multiplies, so twice the rate.

<table>
    <tr>
        <td></td>
        <td>NVIDIA A100 SXM4</td>
        <td>NVIDIA RTX PRO 6000</td>
        <td>NVIDIA H100 NVL</td>
        <td>NVIDIA L4</td>
    </tr>
    <tr>
        <td>Architecture</td>
        <td>Ampere GA100</td>
        <td>Blackwell GB202</td>
        <td>Hopper GH100</td>
        <td>Ada AD104</td>
    </tr>
    <tr>
        <td>FP64</td>
        <td>9.7 TFLOPS</td>
        <td>~1.9 TFLOPS</td>
        <td>30 TFLOPS</td>
        <td>~0.5 TFLOPS</td>
    </tr>
    <tr>
        <td>FP64 tensor</td>
        <td>19.5 TFLOPS</td>
        <td>-</td>
        <td>60 TFLOPS</td>
        <td>-</td>
    </tr>
    <tr>
        <td>FP32</td>
        <td>19.5 TFLOPS</td>
        <td>~120 TFLOPS</td>
        <td>60 TFLOPS</td>
        <td>30.3 TFLOPS</td>
    </tr>
    <tr>
        <td>TF32 tensor</td>
        <td>156 TFLOPS</td>
        <td>~126 TFLOPS</td>
        <td>418 TFLOPS</td>
        <td>60 TFLOPS</td>
    </tr>
    <tr>
        <td>FP16 / BF16 tensor</td>
        <td>312 TFLOPS</td>
        <td>~250 TFLOPS</td>
        <td>836 TFLOPS</td>
        <td>121 TFLOPS</td>
    </tr>
    <tr>
        <td>FP8 tensor</td>
        <td>-</td>
        <td>~500 TFLOPS</td>
        <td>1,671 TFLOPS</td>
        <td>242 TFLOPS</td>
    </tr>
    <tr>
        <td>FP4 tensor</td>
        <td>-</td>
        <td>~2,000 TFLOPS</td>
        <td>-</td>
        <td>-</td>
    </tr>
    <tr>
        <td>INT8 tensor</td>
        <td>624 TOPS</td>
        <td>~1,000 TOPS</td>
        <td>1,671 TOPS</td>
        <td>242 TOPS</td>
    </tr>
    <tr>
        <td>VRAM</td>
        <td>80GB HBM2e</td>
        <td>96GB GDDR7 ECC</td>
        <td>94GB HBM3</td>
        <td>24GB GDDR6</td>
    </tr>
    <tr>
        <td>Memory bandwidth</td>
        <td>2.04TB/s</td>
        <td>~1.6TB/s</td>
        <td>3.94TB/s</td>
        <td>300GB/s</td>
    </tr>
    <tr>
        <td>TDP</td>
        <td>400W</td>
        <td>600W</td>
        <td>350-400W</td>
        <td>72W</td>
    </tr>
</table>

!!! warning "TF32 on the RTX PRO 6000"
    Unlike the A100 and H100, the RTX PRO 6000 gets no TF32 tensor speedup — TF32
    runs at roughly FP32 rate. PyTorch and cuBLAS defaults that rely on TF32 see no
    speedup on these cards; the gain has to come from BF16, FP8 or FP4.


If you have any questions about hardware or the status of anything listed in the table,
{% include "partials/support_request.html" %}.
