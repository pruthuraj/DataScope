var back = document.getElementById("back");



var type = document.getElementById("floatingSelect");
var retext = document.getElementById("labbel");
var reques = document.getElementById("reques");


window.onload = function(){

    // Retrieving data
    var retrievedData = localStorage.getItem('user');
    var retrievedPassword = localStorage.getItem('password');
    if ( retrievedData == null || retrievedData == 'null' || retrievedData == '') {
        window.location.href = 'http://127.0.0.1:8080/login';
    }else{
        istheredata = true;
        console.log(retrievedData,retrievedPassword);
        document.getElementById("REuser").placeholder = retrievedData;
    }

};

type.addEventListener("change",e =>{
    if (type.value == "request"){
        retext.textContent = "request";
    }else{
        retext.textContent = "complain"
    }
});

var subBtn = document.getElementById("subBtn");

subBtn.addEventListener("submit",e =>{
    window.location.href = ""
});

(function () {
    'use strict'
  
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.querySelectorAll('.needs-validation')
  
    // Loop over them and prevent submission
    Array.prototype.slice.call(forms)
      .forEach(function (form) {
        form.addEventListener('submit', function (event) {
          if (!form.checkValidity()) {
            event.preventDefault()
            event.stopPropagation()
          }
  
          form.classList.add('was-validated')
        }, false)
      })
  })()

