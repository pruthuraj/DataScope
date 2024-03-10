const parallax_el = document.querySelectorAll(".parallax");

let xValues = 0,
    yValues = 0 ;

let rotateDegree = 0;

function update(curserPosition){
    parallax_el.forEach(el =>{
        let speedx = el.dataset.speedx;
        let speedy = el.dataset.speedy;
        let speedz = el.dataset.speedz;
        let rotaleSpeed = el.dataset.rotation;


        let isInLeft = (parseFloat(getComputedStyle(el).left) < window.innerWidth / 2) ? 1 : -1; 
        let zValues = (curserPosition - parseFloat(getComputedStyle(el).left) * isInLeft * 0.1);
        
        // translateZ(${zValues * speedz}px)
        el.style.transform = `
        perspective(2300px)
        rotateY(${rotateDegree * rotaleSpeed}deg)
        translateX(calc(-50% + ${-xValues * speedx}px))
        translateY(calc(-50% + ${yValues * speedy}px))
        `
    })
}


update(0)

    window.addEventListener("mousemove",(e)=>{
        xValues = e.clientX - window.innerWidth / 2;
        yValues = e.clientY - window.innerHeight / 2;
        
        rotateDegree = xValues / (window.innerWidth / 2) * 20;

        update(e.clientX)
        parallax_el.forEach(el =>{
            let speedx = el.dataset.speedx;
            let speedy = el.dataset.speedy;
            let speedz = el.dataset.speedz;
            let rotaleSpeed = el.dataset.rotation;
    
    
            let isInLeft = (parseFloat(getComputedStyle(el).left) < window.innerWidth / 2) ? 1 : -1; 
            let zValues = (e.clientX - parseFloat(getComputedStyle(el).left) * isInLeft * 0.1);
            
            // translateZ(${zValues * speedz}px)
            el.style.transform = `
            perspective(2300px)
            rotateY(${rotateDegree * rotaleSpeed}deg)
            translateX(calc(-50% + ${-xValues * speedx}px))
            translateY(calc(-50% + ${yValues * speedy}px))
            `
        })

        // console.log(xValues,yValues)
    })

// let timeline = gsap.timeline();

// parallax_el.forEach(el=>{
//     timeline.from(
//         el,
//         {
//             top: `${el.offsetHeight / 2 + el.dataset.distance}px`,
//             duration:3.5
//         },1
//     );
// })