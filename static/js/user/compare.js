var back = document.getElementById("back");
var colorOnMouseEnter = ["#F7EEDD","#ACE2E1","#41C9E2","#008DDA"];
var colorOnMouseLeave = ['#333333','#76ABAE','#3f3f3f','#f3f3f3'];
var ParticlesColor = colorOnMouseLeave;
var brake = document.getElementById("basic-url")
var compare = document.getElementById("comparebtn");
back.addEventListener("click",e =>{
    window.location.href = "http://127.0.0.1:8080/home/?username=pruthu&password=pruthu";
})
var particles = null;



window.onload = function(){
    
    var retrievedData = localStorage.getItem('user');
    var retrievedPassword = localStorage.getItem('password');
    if ( retrievedData == null || retrievedData == 'null' || retrievedData == '') {
        window.location.href = 'http://127.0.0.1:8080/login';
    }else{
        istheredata = true;
        console.log(retrievedData,retrievedData);
    }

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


compare.addEventListener("click",e =>{
    if(brake.value == '' || brake.value == null){
        hint.style.display = "none";
        alert("enter product")
        return
    }else{
        getElementById('bo').style.display = 'contents';
        compare.disabled = true;
        resume()
    }
})

brake.addEventListener('input',e=>{
    compare.disabled = false;
    pause()
})