window.onload = function(){

    // Retrieving data
    var retrievedData = localStorage.getItem('user');
    var retrievedPassword = localStorage.getItem('password');
    if ( retrievedData == null || retrievedData == 'null' || retrievedData == '') {
        window.location.href = 'http://127.0.0.1:8080/login';
    }else{
        istheredata = true;
    }
    console.log(retrievedData,retrievedData);
};