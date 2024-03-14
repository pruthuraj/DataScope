



window.onload = function () {
    Particles.init({
        
    // normal options
    selector: '.background',
    maxParticles:200,
    speed:0.7,
    color:'#333333',
    sizeVariations: 3, 
    connectParticles:true,
    // options for breakpoints
    responsive: [{
            breakpoint:768,
            options: {
                maxParticles:200,
                color:'#48F2E3',
                connectParticles:false
            }
        }, 
        {
            breakpoint:425,
            options: {
                maxParticles:100,
                connectParticles:true
            }
        }, 
        {
            breakpoint:320,
            options: {
                maxParticles:0
                // disables particles.js
            }
        }
    ]
    });
};

const toggleBtn = document.querySelector('.menu');
const toggleBtnIcon = toggleBtn.querySelector('i');
const dropDownMenu = document.querySelector('.dropdown-menu');

toggleBtn.onclick = function () {
    dropDownMenu.classList.toggle('open');
    const isOpen = dropDownMenu.classList.contains('open');
    toggleBtnIcon.classList.toggle('fa-bars', !isOpen);
    toggleBtnIcon.classList.toggle('fa-xmark', isOpen);
};



function pause() {
    particles.pauseAnimation();
}

function resume() {
    particles.resumeAnimation();
}