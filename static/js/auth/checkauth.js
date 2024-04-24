window.onload = function(){

    // Retrieving data
    var retrievedData = localStorage.getItem('user');
    var retrievedPassword = localStorage.getItem('password');
    if ( retrievedData == null || retrievedData == 'null' || retrievedData == '') {
    }else{
        window.location.href = 'http://127.0.0.1:8080/home/?username=' + retrievedData + '&password=' + retrievedPassword;

        istheredata = true;
    }
    console.log(retrievedData,retrievedData);
};