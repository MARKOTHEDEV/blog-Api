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
        // console.log(this.hero_section_Datecreated)
        
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



    displayBlogDetail(data){

        // first set the h1 or the title of the page
        // this code handles all the contenton the  hero section
        this.ui.title.innerText =data.title
        this.ui.blogDetailhero_image.style.backgroundImage = `url(${data.contentHeader})`
        this.ui.hero_section_authorImage.src = data.authorImage
        this.ui.hero_section_Datecreated.innerText =data.dateCreated
    }


    run(){
        this.getBlogDetails(this.url)
        .then(data =>{
            console.log('data',data)
            this.displayBlogDetail(data)
        })
        .catch(err=>{
            console.log(err)
        })
    }

 
}




blogDetail = new BlogDetails(`/api/blog/blog/${blogId}/`)

blogDetail.run()