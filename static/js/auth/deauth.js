var logout = document.getElementById('logout');

logout.addEventListener('click', function(){
    localStorage.setItem('user',null);
    localStorage.setItem('password', null)

    window.location.href = 'http://127.0.0.1:8080/login';
});