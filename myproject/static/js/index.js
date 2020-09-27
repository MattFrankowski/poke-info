// toggle between hiding and showing dropdown content
function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}

// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
        let dropdowns = document.getElementsByClassName("dropdown-content");
        let openDropdown = dropdowns[0]
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
    }
}