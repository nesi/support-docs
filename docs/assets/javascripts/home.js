
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('div.grid.cards a img').forEach(img => {
        const originalSrc = img.getAttribute('src');
        const hoverSrc = originalSrc.replace(/(\.[^/.?#]+)([?#].*)?$/, '-hover$1$2');
        // preload hover image and enable swapping only if it exists
        const pre = new Image();
        pre.onload = () => {
            const parent = img.parentElement;
            if (!parent) return;
            parent.addEventListener('mouseenter', () => img.setAttribute('src', hoverSrc));
            parent.addEventListener('mouseleave', () => img.setAttribute('src', originalSrc));
        };
        pre.src = hoverSrc;
    });
});
