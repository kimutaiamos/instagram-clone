$(document).ready(function () {
    // Collapse Navbar when the scroll is triggered
    var navbarCollapse = function () {
        if ($("#navMain").offset().top > 40) {
            $("#navMain").addClass("navbar-shrink");
        } else {
            $("#navMain").removeClass("navbar-shrink");
        }
    };
    // Collapse the nav bar if page is not at the top
    navbarCollapse();
    // Collapse the navbar when there is scroll activity
    $(window).scroll(navbarCollapse);
})


// When the user clicks on div, open the popup
function myFunction() {
  var popup = document.getElementById("myPopup");
  popup.classList.toggle("show");
}
