// Open (or create) a database
var password = document.getElementById('password')
var username =  document.getElementById('username')
var btn =  document.getElementById('btn')
istheredata = false; 
window.onload = function(){

    // Retrieving data
    var retrievedData = localStorage.getItem('user');
    var retrievedpassword = localStorage.getItem('password');
    if ( retrievedData == null ) {
        istheredata = false;
    }else{
        istheredata = true;
    }
    console.log(retrievedData,retrievedpassword);
};





btn.addEventListener('click', function(){
    
    localStorage.setItem('user',username.value);
    localStorage.setItem('password', password.value);
});