var particles = null;
var datatable = document.getElementById("data");
var colorOnMouseEnter = ["#F7EEDD","#ACE2E1","#41C9E2","#008DDA"];
var colorOnMouseLeave = ['#333333','#76ABAE','#3f3f3f','#f3f3f3'];
var ParticlesColor = colorOnMouseLeave;
var hint = document.getElementById("hint");
var help = document.getElementById("help");




window.onload = function(){

    // hint.style.display = "none";
    help.style.display = "none";
    // datatable.style.display = "none";

    particles = Particles.init({
    // normal options
    selector: '.background',
    maxParticles:250,
    speed:0.7,
    color:ParticlesColor,
    sizeVariations: 3, 
    connectParticles:true,
    // options for breakpoints
    responsive: [{
            breakpoint:768,
            options: {
                maxParticles:150,
                color:['#48F2E3','#76ABAE','#3f3f3f','#f3f3f3'],
                connectParticles:true
            }
        }, 
        {
            breakpoint:425,
            options: {
                color: '#48F2E3',
                maxParticles:50,
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

function pause() {
  particles.pauseAnimation();
}

function resume(){
  particles.resumeAnimation();
}

var brake = document.getElementById("basic-url")
brake.addEventListener("focusin",e =>{
    pause();
})
brake.addEventListener("focusout",e =>{
    resume();
})
brake.addEventListener("mouseenter",e =>{

    if(brake.value == '' || brake.value == null){
        
        help.style.display = "contents";
        return
    }

    pause();
})
brake.addEventListener("mouseleave",e =>{
    resume();
})


var mineBtn = document.getElementById("mineBtn");
var datatable = document.getElementById("data");
mineBtn.addEventListener("click",e =>{
    if(brake.value == '' || brake.value == null){
        hint.style.display = "none";
        alert("url not found")
        return
    }
    datatable.style.display = "contents";
})



