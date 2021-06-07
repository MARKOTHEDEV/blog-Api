
/* basically 
it logical if we dont have a user or authtocken saved in the broweser
is either the user has logged out
or
the user has deleted them
*/

if((JSON.parse(sessionStorage.getItem('user')) === null) && (JSON.parse(sessionStorage.getItem('userToken')) === null)){
    location.href = '/'
    
}