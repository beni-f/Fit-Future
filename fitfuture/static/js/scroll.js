// Function to check if element is in view
function isInViewport(element) {
    var rect = element.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}

// Function to handle scroll event
function handleScroll() {
    var articles = document.querySelectorAll('.articles');
    articles.forEach(function(article) {
        if (isInViewport(article)) {
            article.classList.add('fade-in');
        }
    });
}

// Add scroll event listener
window.addEventListener('scroll', handleScroll);

// Initially check for articles in view on page load
document.addEventListener('DOMContentLoaded', handleScroll);

