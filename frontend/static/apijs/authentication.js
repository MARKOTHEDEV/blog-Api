


class Authorization{


    constructor(){
        
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




}


