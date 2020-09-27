// toggle between hiding and showing dropdown content
function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}

// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
        let dropdown = document.getElementsByClassName("dropdown-content");
            if (dropdown.classList.contains('show')) {
                dropdown.classList.remove('show');
            }
    }
}