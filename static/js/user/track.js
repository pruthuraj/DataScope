var back = document.getElementById("back");

var retrievedData = null
var retrievedPassword = null
window.onload = function(){

    // Retrieving data
     retrievedData = localStorage.getItem('user');
     retrievedPassword = localStorage.getItem('password');
    if ( retrievedData == null || retrievedData == 'null' || retrievedData == '') {
        window.location.href = 'http://127.0.0.1:8080/login';
    }else{
        istheredata = true;
        console.log(retrievedData,retrievedPassword);
    }

};



  var back = document.getElementById("back");

  back.addEventListener("click",e =>{
      window.location.href = "http://127.0.0.1:8080/home/?username="+retrievedData+"&password="+retrievedPassword;
  })