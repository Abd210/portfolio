/* portfolio_app/static/portfolio_app/js/scripts.js */

// Animate skill proficiency on hover
document.addEventListener('DOMContentLoaded', function() {
    const skills = document.querySelectorAll('.skills-list li');
    skills.forEach(skill => {
        skill.addEventListener('mouseenter', () => {
            skill.style.transform = 'scale(1.1)';
            skill.style.transition = 'transform 0.3s';
        });
        skill.addEventListener('mouseleave', () => {
            skill.style.transform = 'scale(1)';
        });
    });
});

// Placeholder for adding project links via modal
document.addEventListener('DOMContentLoaded', function() {
    const addLinks = document.querySelectorAll('.add-link');
    addLinks.forEach(link => {
        link.addEventListener('click', function(event) {
            event.preventDefault();
            const projectId = this.getAttribute('data-project-id');
            // Implement modal functionality here
            alert('Functionality to add links will be implemented here.');
        });
    });
});
