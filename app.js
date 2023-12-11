const menu = document.querySelector('#mobile-menu')
const menuLinks = document.querySelector('.navbar__menu')



menu.addEventListener ('click', function() {
    menu.classList.toggle('isactive')
    menuLinks.classList.toggle('active')
})

screenHeight = window.innerWidth;
screenWidth = window.innerHeight;

print(screenHeight)
print(screenWidth)