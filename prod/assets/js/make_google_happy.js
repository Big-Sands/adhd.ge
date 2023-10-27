// SEO optimizations

var liElements = document.querySelectorAll('li:not(.nav-item)');
var tdElements = document.querySelectorAll('td');

function updateClass() {

    if (window.innerWidth <= 768) {
        for (var i = 0; i < liElements.length; i++) {
            liElements[i].classList.add('my-4');
        }
        for (var i = 0; i < tdElements.length; i++) {
            tdElements[i].classList.add('py-4');
        }
    } else {
        for (var i = 0; i < liElements.length; i++) {
            liElements[i].classList.remove('my-4');
        }
        for (var i = 0; i < tdElements.length; i++) {
            tdElements[i].classList.remove('py-4');
        }
    }

}

updateClass();

// Add an event listener to update the class on window resize
window.addEventListener('resize', updateClass);
