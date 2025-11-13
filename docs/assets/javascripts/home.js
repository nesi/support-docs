document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('div.grid.cards a img.hover').forEach(img => {
        const originalSrc = img.getAttribute('src');
        const hoverSrc = originalSrc.replace(/(\.[^/.?#]+)([?#].*)?$/, '-hover$1$2');
        
        const parent = img.parentElement;
        if (!parent) return;
        
        parent.addEventListener('mouseenter', () => img.setAttribute('src', hoverSrc));
        parent.addEventListener('mouseleave', () => img.setAttribute('src', originalSrc));
    });
});
