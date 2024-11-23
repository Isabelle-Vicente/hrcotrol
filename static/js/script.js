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

document.addEventListener('DOMContentLoaded', function() {
    const menuPrincipal = document.getElementById('menu-principal');
    const menuRecruitment = document.getElementById('menu-recruitment');
    const menuDp = document.getElementById('menu-dp');
    const menuTraining = document.getElementById('menu-training');
    const menuOccupationalSafety = document.getElementById('menu-occupational-safety');
    
    const recruitmentLink = document.getElementById('recruitment-link');
    const dpLink = document.getElementById('dp-link');
    const trainingLink = document.getElementById('training-link');
    const occupationalSafetyLink = document.getElementById('occupational-safety-link');
    
    const backRecruitment = document.getElementById('back-recruitment');
    const backDp = document.getElementById('back-dp');
    const backTraining = document.getElementById('back-training');
    const backOccupationalSafety = document.getElementById('back-occupational-safety');
    
    function showMenu(menuToShow, menuToHide) {
        menuToHide.classList.add('hidden');
        menuToShow.classList.remove('hidden');
    }

    // Links para abrir menus
    recruitmentLink.addEventListener('click', function(e) {
        e.preventDefault();
        showMenu(menuRecruitment, menuPrincipal);
    });
    
    dpLink.addEventListener('click', function(e) {
        e.preventDefault();
        showMenu(menuDp, menuPrincipal);
    });

    trainingLink.addEventListener('click', function(e) {
        e.preventDefault();
        showMenu(menuTraining, menuPrincipal);
    });

    occupationalSafetyLink.addEventListener('click', function(e) {
        e.preventDefault();
        showMenu(menuOccupationalSafety, menuPrincipal);
    });

    // Links para voltar aos menus principais
    backRecruitment.addEventListener('click', function(e) {
        e.preventDefault();
        showMenu(menuPrincipal, menuRecruitment);
    });

    backDp.addEventListener('click', function(e) {
        e.preventDefault();
        showMenu(menuPrincipal, menuDp);
    });

    backTraining.addEventListener('click', function(e) {
        e.preventDefault();
        showMenu(menuPrincipal, menuTraining);
    });

    backOccupationalSafety.addEventListener('click', function(e) {
        e.preventDefault();
        showMenu(menuPrincipal, menuOccupationalSafety);
    });
});

