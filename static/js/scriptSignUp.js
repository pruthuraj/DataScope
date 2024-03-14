// <!-- Created By CodingNepal -->
const slidePage = document.querySelector(".slide-page");
const nextBtnFirst = document.querySelector(".firstNext");
const prevBtnSec = document.querySelector(".prev-1");
const nextBtnSec = document.querySelector(".next-1");
const prevBtnThird = document.querySelector(".prev-2");
const nextBtnThird = document.querySelector(".next-2");
const prevBtnFourth = document.querySelector(".prev-3");
const submitBtn = document.querySelector(".submit");
const progressText = document.querySelectorAll(".step p");
const progressCheck = document.querySelectorAll(".step .check");
const bullet = document.querySelectorAll(".step .bullet");
let current = 1;

// get values for their 

var gender = document.signform.gender;
gender = gender.options[gender.selectedIndex].text;
var bdate = document.signform.bdate;




nextBtnFirst.addEventListener("click", function(event){
  var fname = document.getElementById("fname");
  var lname = document.getElementById("lname");

  if(
    (fname.value == '') 
    &&
     (lname.value == '')
    ){
    alert("please fill both fields");
    console.log(fname+"error ")
    return
  }
  if(fname.value == ''){
    alert("first name can't be null");
    console.log(fname+"error ")
    return
  }
  if(lname.value == ''){
    alert("last name can't be null ");
    console.log(fname+"error ")
    return
  }

  event.preventDefault();
  slidePage.style.marginLeft = "-25%";
  bullet[current - 1].classList.add("active");
  progressCheck[current - 1].classList.add("active");
  progressText[current - 1].classList.add("active");
  current += 1;
});

nextBtnSec.addEventListener("click", function(event){
  var email = document.signform.email;
  var phnumber = document.signform.num;

  if(
    (email.value == '') 
    &&
     (phnumber.value == '')
    ){
    alert("please fill both fields");
    console.log("error ")
    return
  }
  if(email.value == ''){
    alert("email is null");
    console.log(email+"error ")
    return
  }
  if(phnumber.value == ''){
    alert("number is null ");
    console.log(lname+"error ")
    return
  }

  event.preventDefault();
  slidePage.style.marginLeft = "-50%";
  bullet[current - 1].classList.add("active");
  progressCheck[current - 1].classList.add("active");
  progressText[current - 1].classList.add("active");
  current += 1;
});

nextBtnThird.addEventListener("click", function(event){
  var bdate = document.signform.bdate;
  if(bdate.value == ''){
    alert("select your birthday")
    return
  }

  event.preventDefault();
  slidePage.style.marginLeft = "-75%";
  bullet[current - 1].classList.add("active");
  progressCheck[current - 1].classList.add("active");
  progressText[current - 1].classList.add("active");
  current += 1;
});

submitBtn.addEventListener("click", function(){
  var username = document.signform.usid;
  var password = document.signform.pass;
  if(username.value == '' || password.value ==''){
    return
  }

  bullet[current - 1].classList.add("active");
  progressCheck[current - 1].classList.add("active");
  progressText[current - 1].classList.add("active");
  current += 1;
});

prevBtnSec.addEventListener("click", function(event){
  event.preventDefault();
  slidePage.style.marginLeft = "0%";
  bullet[current - 2].classList.remove("active");
  progressCheck[current - 2].classList.remove("active");
  progressText[current - 2].classList.remove("active");
  current -= 1;
});
prevBtnThird.addEventListener("click", function(event){
  event.preventDefault();
  slidePage.style.marginLeft = "-25%";
  bullet[current - 2].classList.remove("active");
  progressCheck[current - 2].classList.remove("active");
  progressText[current - 2].classList.remove("active");
  current -= 1;
});
prevBtnFourth.addEventListener("click", function(event){
  event.preventDefault();
  slidePage.style.marginLeft = "-50%";
  bullet[current - 2].classList.remove("active");
  progressCheck[current - 2].classList.remove("active");
  progressText[current - 2].classList.remove("active");
  current -= 1;
});

