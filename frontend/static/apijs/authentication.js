


class Authorization{


    constructor(){
        this.userToken =  JSON.parse(sessionStorage.getItem('userToken'))
        this.AuthUser = JSON.parse(sessionStorage.getItem('user'));
       
    }

    checkIfAuthUserOwnsPost(authorID){
        //this returns true if the login user is the same with the author that created the post 
            
            if(this.AuthUser === null){
                //this means the user is not logged in or the browers had some errors storing the user object
                return false
            }
            else{
                return authorID === this.AuthUser.id
            }
    }

    checkIfUserIsLoggedIn(){
        if(user === null && userToken === null){
            //if the person is not logged in 
            return false
        }
        else{
            //if the person is  logged in 
            return true
        }
    }


}


