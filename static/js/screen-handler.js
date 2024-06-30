document.addEventListener("DOMContentLoaded", function () {
  const headerContent = document.getElementById("header-content");
  const originalContent = headerContent.innerHTML;
  const smallContent = "<small>Hi I'm a </small> Python Developer";

  function updateContent() {
    if (window.innerWidth < 769) {
      headerContent.innerHTML = smallContent;
    } else {
      headerContent.innerHTML = originalContent;
      // Reinitialize the typewriter effect if needed
      const elements = document.getElementsByClassName("typewrite");
      for (let i = 0; i < elements.length; i++) {
        const toRotate = elements[i].getAttribute("data-type");
        const period = elements[i].getAttribute("data-period");
        if (toRotate) {
          new TxtType(elements[i], JSON.parse(toRotate), period);
        }
      }
    }
  }

  // Initial check
  updateContent();

  // Add event listener for window resize
  window.addEventListener("resize", updateContent);
});
