


class CreateUserForm{
    constructor(loginform,url,redirectUrl,formName){
        this.loginform = loginform;
        this.createUSerUrl =url;
        this.SuccessRedirectUrl =redirectUrl
        this.formName = formName
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
                   if(input !== null){
                        // so we will get the exact form group 
                    let formGroup = input.parentElement
                    
            
                    formGroup.querySelector('.message').innerText = '';
                   }

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
  

            if(Array.isArray(data.email) || Array.isArray(data.password)  || Array.isArray(data.name) || Array.isArray(data.non_field_errors)){
           
  
                if(Array.isArray(data.password)){
                
                    this.sendErrorToUi('#password',data.password[0])
                }

                if(Array.isArray(data.non_field_errors)){
                
                    this.sendErrorToUi('#password',data.non_field_errors[0])
                }
    
    
                else if(Array.isArray(data.name)){
                    
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
  
            }
            else{
                
                if(this.formName === 'loginForm'){
                    sessionStorage.setItem('userToken',JSON.stringify(data))
                }
                window.location.href = this.SuccessRedirectUrl
                // alert('SS');
            }
            

        })
        // end of .then


    }

}








let CreateUserBtn = document.querySelector('#CreateUserBtn')


if(CreateUserBtn !== null){
    CreateUserBtn.addEventListener('click',e=>{
        e.preventDefault()
    
        let password,email,name,data
    
        password = document.querySelector('#password')
        email = document.querySelector('#email')
        name = document.querySelector('#name')
    
        data = {"password":password.value,"email":email.value,"name":name.value}
    
        let form = new CreateUserForm(document.querySelector('#loginForm'),'/api/users/create-user/',loginUrl,'CreateUserForm')
    
        form.submit(data)
    })    
}




let loginBtn = document.querySelector('#loginBtn')


if(loginBtn !== null){




    loginBtn.addEventListener('click',e=>{
        e.preventDefault()
    
        let password,email
    
        password = document.querySelector('#password')
        email = document.querySelector('#email')
        
    
        data = {"password":password.value,"email":email.value}
    
        let form = new CreateUserForm(document.querySelector('#loginForm'),'/api/users/login/','/','loginForm')
    
        form.submit(data)
    })
    
    
    

}
