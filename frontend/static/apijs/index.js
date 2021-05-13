class UI{


    // displayContent(data,){}
}



class BlogIndex{

    constructor(){
        this.ui = new UI()
    }



    async getAllBlogPost(url){

      let   resp =  await fetch('/api/blog/blog/')

      let   respData =await resp.json()

        console.log(respData)

    }


    


}




blog = new BlogIndex()
console.log('Yo')
blog.getAllBlogPost()