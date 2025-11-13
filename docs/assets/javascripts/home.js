document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('div.grid.cards a img.hover').forEach(img => {
        const originalSrc = img.getAttribute('src');
        const hoverSrc = originalSrc.replace(/(\.[^/.?#]+)([?#].*)?$/, '-hover$1$2');
        
        const parent = img.parentElement;
        if (!parent) return;
        
        // preload hover image
        const pre = new Image();
        pre.src = hoverSrc;
        
        // attach listeners immediately (don't wait for onload)
        parent.addEventListener('mouseenter', () => img.setAttribute('src', hoverSrc));
        parent.addEventListener('mouseleave', () => img.setAttribute('src', originalSrc));
    });
});
