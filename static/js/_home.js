var particles = null;
var datatable = document.getElementById("data");
var colorOnMouseEnter = ["#F7EEDD","#ACE2E1","#41C9E2","#008DDA"];
var colorOnMouseLeave = ['#333333','#76ABAE','#3f3f3f','#f3f3f3'];
var ParticlesColor = colorOnMouseLeave;
var hint = document.getElementById("hint");
var help = document.getElementById("help");
var brake = document.getElementById("basic-url")

window.onload = function(){
    
    var retrievedData = localStorage.getItem('user');
    var retrievedPassword = localStorage.getItem('password');
    if ( retrievedData == null || retrievedData == 'null' || retrievedData == '') {
        window.location.href = 'http://127.0.0.1:8080/login';
    }else{
        istheredata = true;
    }
    console.log(retrievedData,retrievedData);
    mineBtn.disabled = true;
    hint.style.display = "none";
    help.style.display = "none";
    datatable.style.display = "none";

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
    pause()
};

function pause() {
  particles.pauseAnimation();
}

function resume(){
  particles.resumeAnimation();
}


brake.addEventListener("focusin",e =>{
})
brake.addEventListener("focusout",e =>{
    hint.style.display = "none";
    help.style.display = "none";
})
brake.addEventListener("mouseenter",e =>{

    if(brake.value == '' || brake.value == null){
        hint.style.display = "contents";
        help.style.display = "contents";
        return
    }
})


var mineBtn = document.getElementById("mineBtn");
var datatable = document.getElementById("data");
mineBtn.addEventListener("click",e =>{
    if(brake.value == '' || brake.value == null){
        hint.style.display = "none";
        alert("id not found")
        return
    }
    datatable.style.display = "contents";
    // mineBtn.disabled = true;
    resume()
})

brake.addEventListener('input',e=>{
    if (brake.value.length < 10){
        mineBtn.disabled = true;
        return
    }
    mineBtn.disabled = false;
})

var back = document.getElementById("back");

back.addEventListener("click",e =>{
    window.location.href = "http://127.0.0.1:8080/home/?username=pruthu&password=pruthu";
})