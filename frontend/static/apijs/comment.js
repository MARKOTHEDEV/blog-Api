

class Comment extends Authorization{



    constructor(commentContainer){
        super()
        this.commentContainer = document.querySelector(commentContainer);

    }

   async getAllComment(url){
     let resp = await fetch(url)
    
     let respData = await resp.json()

     return  respData
    }

    displayAllComment(url){
        this.getAllComment(url)
        .then(data=>{
            console.log(data)
        })

    }

}



comment = new Comment('#commentListContainer')

comment.displayAllComment(`/api/blog/comment/${blogId}/`)