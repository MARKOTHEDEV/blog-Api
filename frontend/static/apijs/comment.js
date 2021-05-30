

class Comment extends Authorization{



    constructor(commentContainer){
        super()
        // this holds all the comment that will be listed in the wepage
        this.commentContainer = document.querySelector(commentContainer);
        // this just holds the div that shows how many comment we have 
        this.noOfComments = document.querySelector('#noOfComments');
        // this holds the form to create a comment
        this.createCommentWrapper = document.querySelector('#createCommentWrapper');

    }

    displayCreateCommentForm(){
        if(this.AuthUser !== null && this.createCommentWrapper.innerHTML !== '' ){
            this.createCommentWrapper.innerHTML = ` 
            
                    <h3 class="mb-5">Leave a comment</h3>
                    <form id="createCommentForm" class="p-5 bg-light">
                        <div class="form-group">
                        <label for="name">Name *</label>
                        <input type="text"  class="form-control" value="${this.AuthUser.name}" id="name" disabled>
                        </div>
            
                        <div class="form-group">
                        <label for="message">Comment</label>
                        <textarea name="" id="CreatecommentInput" cols="30" rows="10" class="form-control"></textarea>
                        </div>
                        <div class="form-group">
                          
                        <input type="submit"  id="submitNewComment" value="Post Comment" class="btn btn-primary">
                        </div>
                    </form>
            `
        }
    }

   async getAllComment(url){
     let resp = await fetch(url)
    
     let respData =  await resp.json()

    //  return  respData
    
        comment.displayAllComment(respData)

    }


    displayAllComment(data){
        // console.log(data)
        let blogCommentBtn,CommentUpdateForm;

        this.noOfComments.innerText =`${data.length} Comments`;
        
        this.commentContainer.innerHTML = '';
        
        if(Array.isArray(data)){
           

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
        else{
            // console.log(data,"YYU ")
            blogCommentBtn = `
            <button class="bg-danger btn deleteCommentBtn" data-commentID="${data.id}"  style="color: white;">Delete</button>
        <button class="bg-success btn updateCommentBtn " data-commentID="${data.id}" style="color: white;"  >Update</button>    
            `
            // this is the form that will handle our updating of comment
        CommentUpdateForm =`
            <form action="#" class=" updateCommentForm remove">
                <input type="text" class="form-control updateCommentInput" placeholder="Correct Your comment....">
                
                <input type="submit" class="btn bg-success submitCommentUpdate" data-commentID="${data.id}" style="color:white;" value="Update">
            </form>
        `

    
        this.commentContainer.innerHTML += `
        <li class="comment" id="comment">
            <div class="vcard">
            <img src="${data.commenterimage}" alt="Image placeholder">
            </div>
            <div class="comment-body">
            <h3>${data.commenterName}</h3>
            
            <p>${data.comment}</p>
            <br>
            ${
                //before the user can update check if he is logged in
                this.AuthUser !== null ?
                        // so if this is true show the update and delete button
                    data.user ===this.AuthUser.id ? blogCommentBtn
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
                    data.user ===this.AuthUser.id ? CommentUpdateForm
                :
                    //else dont show any thing  that the reason for the empty string
                ''
            :  //else dont show any thing 
            ''
        }
                        

                    
        </li>
        <br>
        ` 
        }

        // create the form that creates comment that if user is logged in
        




    }

}










async function sendDataToBackend(url,requestType,blogId,data=null){


    let resp = await fetch(url, {
        method: requestType, // or 'PUT'
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken':csrftoken,
         Authorization:`token ${JSON.parse(sessionStorage.getItem('userToken'))}`,

        },
        body: JSON.stringify(data),
      })

    let respData = await resp.json()
    let status =  resp.status
    return {
        respData,status
    }
}   


comment = new Comment('#commentListContainer');

comment.displayCreateCommentForm()

function loadSubmitNewComment(){
    'THIS WAS CREATED BECAUSE WHEN WE LOAD THE PAGE CHANCES ARE THE API HAS NOT RETURN THE COMMENTS YET'
    "SO WE CREATED THE FUNCTION IN A WAY THAT ONCE THE COMMENT ARRIVE IN THE HTML IT WILL LOAD OUR CREAD FORM"
    let submitNewComment = document.querySelector('#submitNewComment')
// let createCommentForm = document.querySelector('#createCommentForm')

submitNewComment.addEventListener('click',e=>{
    e.preventDefault()
    let createForm = e.target.parentElement.parentElement
    
    let Newcomment = createForm[1].value;
    let url ='/api/blog/comment/'
    sendDataToBackend(url,'POST',blogId,data={"comment":Newcomment,"blog":blogId})
    .then(data=>{
        comment.getAllComment(`/api/blog/comment/${blogId}/`)
    })        
    })

}

comment.getAllComment(`/api/blog/comment/${blogId}/`)
.then(data=>{
    loadSubmitNewComment()
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
            updateCommentForm =e.target.parentElement.querySelector('.updateCommentForm');
            updateCommentForm.classList.remove('remove')
            let updateCommentInput = updateCommentForm.querySelector('.updateCommentInput')
            updateCommentInput.value = commentbodyContent.innerText
            
        }

        if(e.target.className.includes('submitCommentUpdate')){
            // this is what actually sends it to the back End
            let updateCommentInputField = updateCommentForm.querySelector('.updateCommentInput')
            // console.log(e.target.dataset.commentid)
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

                    // console.log(data)
                    
                }      
            })

        }
        
        
        
    
    })

 
    
    

    
})


//end of getAllcomment promise

