










class UserProfile{
    //this class get the authenticated user token and saves the user object to session storage

    async getUserObject(url){
        // this function goes to the back end to get the user

        const resp = await fetch(url, {
            method: 'GET', // or 'PUT'
            headers: {
                Authorization: `Token ${JSON.parse(sessionStorage.getItem('userToken'))}`,
                'Content-Type': 'application/json',
            }
          })
        const respData = await resp.json()

        return respData
    }

    start(url){

        this.getUserObject(url)
        .then(data=>{
            if(data.detail){
                alert(data.detail)
            }
            else{
                // console.log(data)
                sessionStorage.setItem('user',JSON.stringify(data))
            }
        })

    }

}


