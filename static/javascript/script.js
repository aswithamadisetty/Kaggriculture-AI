// Auto-render Markdown content
document.addEventListener('DOMContentLoaded', function() {
    // If using marked.js, render markdown content
    const contentDivs = document.querySelectorAll('#response-content');
    
    contentDivs.forEach(div => {
        const content = div.innerHTML;
        // If content contains markdown indicators, render it
        if (content.includes('#')) {
            try {
                div.innerHTML = marked.parse(content);
            } catch(e) {
                console.log('Markdown parse error:', e);
            }
        }
    });
    
    // Clear history button
    const clearBtn = document.getElementById('clear-history');
    if (clearBtn) {
        clearBtn.addEventListener('click', function() {
            if (confirm('Are you sure you want to clear all history?')) {
                fetch('/clear-history', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    }
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        location.reload();
                    }
                });
            }
        });
    }
});

// Form submission loading states
document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', function() {
        const submitBtn = this.querySelector('button[type="submit"]');
        if (submitBtn) {
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Processing...';
        }
    });
});