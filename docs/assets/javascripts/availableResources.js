(async function () {
    const resp = await fetch('./assets/partition-list.json');
    const data = await resp.json();
    const tbody = document.querySelector('#partitions tbody');

    function parseTresConfigured(s) {
      const out = {};
      if (!s) return out;
      // split on commas, trim
      s.split(',').forEach(tok => {
        const [k, v] = tok.split('=').map(x => x && x.trim());
        if (!k || v == null) return;
        out[k] = v;
      });
      return out;
    }

    function parseMemToMB(memStr) {
      if (!memStr) return 0;
      const m = memStr.match(/^(\d+)([KMG]?)/i);
      if (!m) return 0;
      const n = Number(m[1]);
      const unit = (m[2] || '').toUpperCase();
      switch (unit) {
        case 'G': return n * 1024;
        case 'K': return n / 1024;
        default: return n; // M or no suffix -> treat as MB
      }
    }

    function sumGpusFromConfigured(cfgStr) {
      if (!cfgStr) return 0;
      let sum = 0;
      // match patterns like "gres/gpu=24" or "gres/gpu:h100=8"
      const regex = /gres\/gpu(?:[:][^=]*)?=([0-9]+)/g;
      let m;
      while ((m = regex.exec(cfgStr)) !== null) {
        sum += Number(m[1]);
      }
      return sum;
    }

    function humanGB(mb) {
      return (mb / 1024).toFixed(2) + ' GB';
    }

    for (const p of (data.partitions || [])) {
      const name = p.name || '';
      const nodesCount = Number(p.nodes && p.nodes.total) || 0;
      const totalCpus = Number(p.cpus && p.cpus.total) || 0;
      const coresPerNode = nodesCount ? (totalCpus / nodesCount) : 0;

      const tresCfg = (p.tres && p.tres.configured) || '';
      const tresMap = parseTresConfigured(tresCfg);

      // memory total from tres configured (mem=...M) if present
      const memTotalMB = parseMemToMB(tresMap['mem'] || tresMap['mem='] || (tresCfg.match(/mem=([0-9]+[KMG]?)/i) && tresCfg.match(/mem=([0-9]+[KMG]?)/i)[1]) || '');
      // fallback: if memTotalMB is 0 and defaults.partition_memory_per_node set, use that * nodes
      let memoryPerNodeMB = 0;
      if (memTotalMB && nodesCount) {
        memoryPerNodeMB = memTotalMB / nodesCount;
      } else if (p.defaults && p.defaults.partition_memory_per_node && p.defaults.partition_memory_per_node.set) {
        memoryPerNodeMB = Number(p.defaults.partition_memory_per_node.number) || 0;
      } else if (p.defaults && p.defaults.partition_memory_per_cpu && p.defaults.partition_memory_per_cpu.set) {
        // if only memory per cpu is set, compute per node using coresPerNode
        const memPerCpu = Number(p.defaults.partition_memory_per_cpu.number) || 0;
        memoryPerNodeMB = memPerCpu * coresPerNode;
      }

      // memory per core
      const memoryPerCoreMB = coresPerNode ? (memoryPerNodeMB / coresPerNode) : 0;

      // GPUs - sum occurrences in configured string
      const gpus = sumGpusFromConfigured(tresCfg);

      const tr = document.createElement('tr');
      tr.innerHTML = `
        <td>${name}</td>
        <td class="numeric">${isFinite(coresPerNode) ? Math.round(coresPerNode) : '—'}</td>
        <td class="numeric">${memoryPerNodeMB ? humanGB(memoryPerNodeMB) : '—'}</td>
        <td class="numeric">${memoryPerCoreMB ? humanGB(memoryPerCoreMB) : '—'}</td>
        <td class="numeric">${gpus || 0}</td>
        <td class="numeric">${nodesCount}</td>
      `;
      tbody.appendChild(tr);
    }
  })()
//   .catch(err => {
//     console.error(err);
//     tbody.insertAdjacentHTML('beforeend','<p style="color:red">Failed to load partition data.</p>');
//   });
