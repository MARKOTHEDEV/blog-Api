

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
        let blogCommentBtn;

        this.noOfComments.innerText =`${data.length} Comments`;
        
        this.commentContainer.innerHTML = '';
        data.forEach(element=>{
            //this blgCommentBtn was sperated beacuse of this error  ${} javascript was complainng that i have to many nested ${}
            blogCommentBtn = `
            <button class="bg-danger btn deleteCommentBtn" data-commentID="${element.id}"  style="color: white;">Delete</button>
          <button class="bg-success btn updateCommentBtn " data-commentID="${element.id}" style="color: white;"  >Update</button>
    
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
    // console.log(deleteCommentBtn)
    commentListContainer.addEventListener('click',e=>{
        e.preventDefault()
     
        if(e.target.className.includes('deleteCommentBtn')){
            fetch(`/api/blog/comment/${e.target.dataset.commentid}/`, {
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

    
    
    })


})
//end of getAllcomment promise



