

class Comment extends Authorization{



    constructor(commentContainer){
        super()
        this.commentContainer = document.querySelector(commentContainer);
        this.noOfComments = document.querySelector('#noOfComments');

    }

   async getAllComment(url){
     let resp = await fetch(url)
    
     let respData = await resp.json()

    //  return  respData
    
        comment.displayAllComment(respData)

    }

//     blog: 17
// ​​
// comment: "Ye ye by zlatan the post is senseless"
// ​​
// commenterimage: "/media/user.jpg"
// ​​
// id: 6
// ​​
// user: 1
    displayAllComment(data){
        console.log(data)
        let blogCommentBtn,CommentUpdateForm;

        this.noOfComments.innerText =`${data.length} Comments`;
        
        this.commentContainer.innerHTML = '';
        data.forEach(element=>{
            //this blgCommentBtn was sperated beacuse of this error  ${} javascript was complainng that i have to many nested ${}
            blogCommentBtn = `
            <button class="bg-danger btn deleteCommentBtn" data-commentID="${element.id}"  style="color: white;">Delete</button>
          <button class="bg-success btn updateCommentBtn " data-commentID="${element.id}" style="color: white;"  >Update</button>
    
          `
            // this is the form that will handle our updating of comment
         CommentUpdateForm =`
         <form action="#" class=" updateCommentForm remove">
            <input type="text" class="form-control updateCommentInput" placeholder="Correct Your comment....">
            
            <input type="submit" class="btn bg-success submitCommentUpdate" data-commentID="${element.id}" style="color:white;" value="Update">
         </form>


         `

        
            this.commentContainer.innerHTML += `
            <li class="comment" id="comment">
                <div class="vcard">
                <img src="${element.commenterimage}" alt="Image placeholder">
                </div>
                <div class="comment-body">
                <h3>${element.commenterName}</h3>
                
                <p>${element.comment}</p>
                <br>
                ${
                    //before the user can update check if he is logged in
                    this.AuthUser !== null ?
                            // so if this is true show the update and delete button
                        element.user ===this.AuthUser.id ? blogCommentBtn
                       :
                        //else dont show any thing  that the reason for the empty string
                       ''
                :  //else dont show any thing 
                ''
             }
                <br>
             ${
                //before the user can update check if he is logged in
                    this.AuthUser !== null ?
                            // so if this is true show the update and delete button
                        element.user ===this.AuthUser.id ? CommentUpdateForm
                    :
                        //else dont show any thing  that the reason for the empty string
                    ''
                :  //else dont show any thing 
                ''
            }
                            

                        
            </li>
            <br>
            `
        })
    }

}















comment = new Comment('#commentListContainer');

comment.getAllComment(`/api/blog/comment/${blogId}/`)
.then(data=>{
    // since it an async code we need to do this in the promise
    // or else "deleteCommentBtn" -- will return false because it ran before the api call finished
    // let deleteCommentBtn = document.querySelector('#deleteCommentBtn')
    let commentListContainer = document.querySelector('#commentListContainer')
    let updateCommentForm = document.querySelector('.updateCommentForm')
    
    let updateCommentBtn = document.querySelector('.updateCommentBtn');
    // console.log(deleteCommentBtn)
    commentListContainer.addEventListener('click',e=>{
        e.preventDefault()
        let commentID =e.target.dataset.commentid
        if(e.target.className.includes('deleteCommentBtn')){
            fetch(`/api/blog/comment/${commentID}/`, {
                method: 'DELETE',
                headers:{
                    Authorization:`token ${JSON.parse(sessionStorage.getItem('userToken'))}`
                }
            })
            .then(data=>data.status)
            .then(data=>{
                if(data==204){
                    comment.getAllComment(`/api/blog/comment/${blogId}/`)
                    
                }
            })
        }
        
        
        
        if(e.target.className.includes('updateCommentBtn')){
            // WHat this if statement Does is to fill the updateCommentInput and Get it ready---
            //  for Sending it to the backend
            // this query will go up to the parent element and search for the particular comment we want to update
            let commentbodyContent = e.target.parentElement.querySelector('.comment-body p')
            
            updateCommentForm.classList.remove('remove')
            let updateCommentInput = updateCommentForm.querySelector('.updateCommentInput')
            updateCommentInput.value = commentbodyContent.innerText
            
        }

        if(e.target.className.includes('submitCommentUpdate')){
            // this is what actually sends it to the back End
            let updateCommentInputField = updateCommentForm.querySelector('.updateCommentInput')
            console.log(e.target.dataset.commentid)
            let data = {'comment':updateCommentInputField.value}
            

            fetch(`/api/blog/comment/${e.target.dataset.commentid}/`, {
                method: 'PATCH',
                headers:{
                    'Content-Type': 'application/json',
                    // 'X-CSRFToken':csrftoken,
                    
                    Authorization:`token ${JSON.parse(sessionStorage.getItem('userToken'))}`
                },
                body: JSON.stringify(data)
            })
            .then(data=>data.status)
            .then(data=>{
               
                if(data==200){
                    comment.getAllComment(`/api/blog/comment/${blogId}/`)
                    
                }      
            })

        }
        
        
        
    
    })


})
//end of getAllcomment promise



