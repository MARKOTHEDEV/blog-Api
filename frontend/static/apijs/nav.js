

let user = JSON.parse(sessionStorage.getItem('user'))
let userToken = JSON.parse(sessionStorage.getItem('userToken'))
let navlinksForAuthUsers = document.querySelector('#navlinksForAuthUsers')
let navlinksForUnAuthUsers = document.querySelector('#navlinksForUnAuthUsers')
let userNavLinkName = document.querySelector('#userNavLinkName')



if(user === null && userToken === null){
    //if the person is not logged in 
    // navlinksForAuthUsers.style.display='none';
    navlinksForAuthUsers.remove()
}
else{
    //if the person is  logged in 
    userNavLinkName.innerText =`Hello ${user.email}`
    navlinksForUnAuthUsers.remove()
}