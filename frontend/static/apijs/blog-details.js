// blogId is comming from the js script that is directly placed to this one 
// it is a const so u can't change it




class BlogDetails{


    constructor(BlogDetailUrl){
        this.url = BlogDetailUrl
    }

    //this get the blog detail
   async getBlogDetails(url){

        let resp = await fetch(url)

        let respData = await resp.json()

        return respData
    }


    displayBlogDetail(data){

        
    }


    run(){
        this.getBlogDetails(this.url)
        .then(data =>{
            console.log('data',data)
        })
        .catch(err=>{
            console.log(err)
        })
    }

 
}




blogDetail = new BlogDetails(`/api/blog/blog/${blogId}/`)

blogDetail.run()