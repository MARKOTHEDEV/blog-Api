// blogId is comming from the js script that is directly placed to this one 
// it is a const so u can't change it


class UI{
    constructor(){
        this.title = document.querySelector('#title');
        this.blogDetailhero_image = document.querySelector('#blogDetailhero_image');
        this.hero_section_categorie = document.querySelector('#hero_section_categorie');
        this.hero_section_authorName = document.querySelector('#hero_section_authorName')
        this.hero_section_Datecreated = document.querySelector('#hero_section_Datecreated');
        this.hero_section_authorImage = document.querySelector('#hero_section_authorImage')
        this.mainBlogDetails = document.querySelector('#mainBlogDetails')        
    }


    
}

class BlogDetails{


    constructor(BlogDetailUrl){
        this.url = BlogDetailUrl;
        this.ui = new UI()
    }

    //this get the blog detail
   async getBlogDetails(url){

        let resp = await fetch(url)

        let respData = await resp.json()

        return respData
    }


    displayHeroSection(data){
            // this code handles all the contenton the  hero section
            this.ui.title.innerText =data.title
            this.ui.blogDetailhero_image.style.backgroundImage = `url(${data.contentHeader})`
            this.ui.hero_section_authorImage.src = data.authorImage
            this.ui.hero_section_Datecreated.innerText =data.dateCreated
            this.ui.hero_section_authorName.innerText = data.authorName

    }

    displayBlogMainContent(data){
        //this display the blog post

        this.ui.mainBlogDetails.innerHTML =`
                <p id="firstPartOfContent">
                    ${data.blogPost}
            </p>
            <div class="row mb-5 mt-5">
            <div class="col-md-12 mb-4">
            <img src="${data.extrapics}" alt="Image placeholder" class="img-fluid rounded">
            </div>
            <div class="col-md-6 mb-4">
            <img src="${data.contentHeader}" alt="Image placeholder" class="img-fluid rounded">
            </div>
            <div class="col-md-6 mb-4">
            <img src="${data.introPics}" alt="Image placeholder" class="img-fluid rounded">
            </div>
            </div>
            <p>
            ${data.blogPost2}
                
            </p>
        
        
        `

    }
    displayBlogDetail(data){

        // first set the h1 or the title of the page
        
        this.displayHeroSection(data)
        this.displayBlogMainContent(data)
    }




    run(){
        this.getBlogDetails(this.url)
        .then(data =>{
            // console.log('data',data)
            this.displayBlogDetail(data)
        })
        // .catch(err=>{
        //     console.log(err)
        // })
    }

 
}




blogDetail = new BlogDetails(`/api/blog/blog/${blogId}/`)

blogDetail.run()



/*
get all comments using blog id

load comments to the ui
    there will be to mark up
            one for authenticated user --:
                            will have deletebtn or updatebtn
                            delete btn will send delete request to the server
                            updatebtn  will send update request to the server
                                --first display a form then we can press send 
            one for unauth user

create comment -- if authenticated

*/
class Comments{

    constructor(blogID){
        this.blogID = blogID

    }

    async getComments(url){
        // this code returns all the comments that has to do with the current blog popst
        resp = await fetch(url)
        
        respData = await resp.json()
        
        return respData
    }


    displayComment(){
        this.getComments('')
        .then(resp=>{
            // if user is authenticated then show him the auth version of the comment

            // else show him just plain content
        })

        .catch(err=>{
            // show error
        })
    }




}