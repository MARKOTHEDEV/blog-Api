


class LoginForm{
    constructor(loginform){
        this.loginform = loginform;
        this.createUSerUrl ='/api/users/create-user/';
    }

    async sendDataToBackEnd(url,data){

      let  resp = await fetch(url, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              'X-CSRFToken':csrftoken
            },
            body: JSON.stringify(data),
          })
    let respData = await resp.json()

    return respData

    }
    submit(data){
        console.log(data)
        this.sendDataToBackEnd(this.createUSerUrl,data)
        .then(data=>{
            if(Array.isArray(data.password)){
                alert(data.password[0]);
            }
           else if(Array.isArray(data.email)){
            alert(data.email[0]);

            }   

            else{
                // redirect to login page
                alert(data,': redirect to login page');
            }
            

        })

    }

}







let loginBtn = document.querySelector('#loginBtn')

loginBtn.addEventListener('click',e=>{
    e.preventDefault()

    let password,email,name,data

    password = document.querySelector('#password')
    email = document.querySelector('#email')
    name = document.querySelector('#name')

    data = {"password":password.value,"email":email.value,"name":name.value}

    let form = new LoginForm(document.querySelector('#loginForm'))

    form.submit(data)
})