const body = document.querySelector('body');
const sidebar = body.querySelector('nav');
const toggle = body.querySelector(".toggle");
const modeSwitch = body.querySelector(".toggle-switch");
const modeText = body.querySelector(".mode-text");

toggle.addEventListener("click", () => {
    sidebar.classList.toggle("close");
});

modeSwitch.addEventListener("click", () => {
    body.classList.toggle("dark");
    modeText.innerText = body.classList.contains("dark") ? "Light mode" : "Dark mode";
});

document.querySelectorAll('.submenu-toggle').forEach(toggle => {
toggle.addEventListener('click', (event) => {
event.preventDefault();
const parentContainer = toggle.closest('.submenu-container');
parentContainer.classList.toggle('active');
});
});

document.addEventListener("DOMContentLoaded", () => {

    document.querySelectorAll('.submenu-toggle').forEach(toggle => {
        toggle.addEventListener('click', (event) => {
            event.preventDefault();

        });
    });
});


document.addEventListener('DOMContentLoaded', function() {
    const menuPrincipal = document.getElementById('menu-principal');
    const menuRecruitment = document.getElementById('menu-recruitment');
    const menuOccupationalSafety = document.getElementById('menu-occupational-safety');
    
    const recruitmentLink = document.getElementById('recruitment-link');
    const backRecruitment = document.getElementById('back-recruitment');
    const backOccupationalSafety = document.getElementById('back-occupational-safety');
    const occupationalSafetyLink = document.getElementById('occupational-safety-link');  
    
    function showMenu(menuToShow, menuToHide) {
        menuToHide.classList.add('hidden');
        menuToShow.classList.remove('hidden');
    }

    recruitmentLink.addEventListener('click', function(e) {
        e.preventDefault(); 
        showMenu(menuRecruitment, menuPrincipal); 
    });

    // Quando clicar em "Back" no menu de Recruitment
    backRecruitment.addEventListener('click', function(e) {
        e.preventDefault();
        showMenu(menuPrincipal, menuRecruitment); 
    });

    backOccupationalSafety.addEventListener('click', function(e) {
        e.preventDefault();
        showMenu(menuPrincipal, menuOccupationalSafety); 
    });

    occupationalSafetyLink.addEventListener('click', function(e) {
        e.preventDefault();
        showMenu(menuOccupationalSafety, menuPrincipal); 
    });
});

