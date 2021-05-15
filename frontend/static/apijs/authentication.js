


class LoginForm{
    constructor(loginform){
        this.loginform = loginform;
        this.createUSerUrl ='/api/users/create-user/';
    }


    sendErrorToUi(inputID,message){
        //input represents the html input filed
        let input = document.querySelector(inputID)
        // so we will get the exact form group 
        let formGroup = input.parentElement
        

        formGroup.querySelector('.message').innerText = message;
    }

        //this methods clears the error message for new error message to enter for better user expirence
        clearErrorMessages(){
                //input represents the html input filed
                ['#password','#email','#name'].forEach(inputID=>{
                    let input = document.querySelector(inputID)
                    // so we will get the exact form group 
                    let formGroup = input.parentElement
                    
            
                    formGroup.querySelector('.message').innerText = '';
                })

            }
    
  
        async sendDataToBackEnd(url,data){
    // this method send a POST REQUEST TO create user 
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
        this.clearErrorMessages()

        this.sendDataToBackEnd(this.createUSerUrl,data)
        // start of .then
        .then(data=>{
            if(Array.isArray(data.password)){
                
                this.sendErrorToUi('#password',data.password[0])
            }


            if(Array.isArray(data.name)){
                
                this.sendErrorToUi('#name',data.name[0])
            }


           else if(Array.isArray(data.email)){
               let emailMessage = data.email[0]
                // this if state ment is just to format the the string in a more understand able tone...
                if(emailMessage === 'myuser with this email already exists.'){
                    emailMessage = emailMessage.replace('myuser','User')
                }
                // then we send the error to the ui
                this.sendErrorToUi('#email',emailMessage)


            }   

            else{
                // we save the user obj in the session storge for easy access
                // sessionStorage.setItem('user',JSON.stringify(data))
                // redirect to login page
                //this loginUrl is a const it coming from the signup.html there is a script tag that created it..
                window.location.href = loginUrl
                
            }
            

        })
        // end of .then


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