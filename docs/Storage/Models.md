---
created_at: '2026-05-13'
description: "Centrally maintained large language models available on Mahuika at /opt/nesi/models."
tags:
    - gpu
    - machine learning
    - storage
hide: toc
---

To avoid unneccicery storage use, we maintain readonly versions of popular models in `/opt/nesi/models`, if you can use this please do.
If you need a model that is not listed here, please {% include "partials/support_request.html" %} with the model name, source, and a brief description of your use case.

## Available models

<table>
<thead>
<tr>
<th>Model</th>
<th>Licence</th>
<th>Path</th>
<th>Slurm</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="2"><a href="https://ollama.com/library/llama3.1">Llama 3.1</a></td>
<td rowspan="2"><a href="https://huggingface.co/meta-llama/Llama-3.1-8B/blob/main/LICENSE">Meta Llama 3.1</a></td>
<td><pre><code>/opt/nesi/models/gguf/llama3.1/llama3.1-8b.gguf</code></pre></td>
<td><pre><code>#SBATCH --gpus-per-node=l4:1</code></pre></td>
</tr>
<tr>
<td><pre><code>/opt/nesi/model/gguf/llama3.1/llama3.1-70b.gguf</code></pre></td>
<td><pre><code>#SBATCH --partition=milan
#SBATCH --gpus-per-node=a100:1</code></pre></td>
</tr>
<tr>
<td rowspan="3"><a href="https://ollama.com/library/deepseek-r1">DeepSeek-R1</a></td>
<td rowspan="3"><a href="https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B/blob/main/LICENSE">MIT</a></td>
<td><pre><code>/opt/nesi/model/gguf/deepseek-r1/deepseek-r1-7b.gguf</code></pre></td>
<td><pre><code>#SBATCH --gpus-per-node=l4:1</code></pre></td>
</tr>
<tr>
<td><pre><code>/opt/nesi/model/gguf/deepseek-r1/deepseek-r1-32b.gguf</code></pre></td>
<td><pre><code>#SBATCH --partition=genoa
#SBATCH --gpus-per-node=a100:1</code></pre></td>
</tr>
<tr>
<td><pre><code>/opt/nesi/model/gguf/deepseek-r1/deepseek-r1-70b.gguf</code></pre></td>
<td><pre><code>#SBATCH --partition=milan
#SBATCH --gpus-per-node=a100:1</code></pre></td>
</tr>
<tr>
<td rowspan="2"><a href="https://ollama.com/library/qwen3">Qwen3</a></td>
<td rowspan="2"><a href="https://huggingface.co/Qwen/Qwen3-14B/blob/main/LICENSE">Apache 2.0</a></td>
<td><pre><code>/opt/nesi/model/gguf/qwen3/qwen3-14b.gguf</code></pre></td>
<td><pre><code>#SBATCH --gpus-per-node=l4:1</code></pre></td>
</tr>
<tr>
<td><pre><code>/opt/nesi/model/gguf/qwen3/qwen3-32b.gguf</code></pre></td>
<td><pre><code>#SBATCH --partition=genoa
#SBATCH --gpus-per-node=a100:1</code></pre></td>
</tr>
<tr>
<td rowspan="2"><a href="https://ollama.com/library/qwen2.5">Qwen2.5</a></td>
<td rowspan="2"><a href="https://huggingface.co/Qwen/Qwen2.5-14B-Instruct/blob/main/LICENSE">Apache 2.0</a></td>
<td><pre><code>/opt/nesi/model/gguf/qwen2.5/qwen2.5-7b.gguf</code></pre></td>
<td><pre><code>#SBATCH --gpus-per-node=l4:1</code></pre></td>
</tr>
<tr>
<td><pre><code>/opt/nesi/model/gguf/qwen2.5/qwen2.5-14b.gguf</code></pre></td>
<td><pre><code>#SBATCH --gpus-per-node=l4:1</code></pre></td>
</tr>
<tr>
<td><a href="https://ollama.com/library/gemma3">Gemma 3</a></td>
<td><a href="https://huggingface.co/google/gemma-3-27b/blob/main/LICENSE">Gemma</a></td>
<td><pre><code>/opt/nesi/model/gguf/gemma3/gemma3-27b.gguf</code></pre></td>
<td><pre><code>#SBATCH --partition=genoa
#SBATCH --gpus-per-node=a100:1</code></pre></td>
</tr>
</tbody>
</table>

The **Slurm** column shows the minimum GPU flags required, your actual throughput will depend on the queue size.
See [Hardware](../Batch_Computing/Hardware.md) for a full list of available GPUs.

!!! warning "L4 GPUs have no double-precision floating point"
    The L4 is an inference-optimised GPU. It is suitable for running quantised models but should not be used for model training or workflows that require FP64 precision.


## Related
    - [Ollama](../Software/Available_Applications/ollama.md).
    - [Hardware](../Batch_Computing/Hardware.md).
