class UI{

    constructor(){
        this.allPostContainer = document.querySelector('#allPostContainer')
        this.prevBtn = document.querySelector('#prev')
        this.nextBtn = document.querySelector('#next')
    }


    //this method display all the content on the index.html page
    displayContent(BlogPosts){
        // this data passed is an array

        // we going to da the pagination settings here
        this.setPagination(BlogPosts)

        //based on the categories  we apply the right bootstrap background color  
        let ListOfcategory =    {'Politics':'bg-danger',
                            'Travel':'bg-success',
                            'Tech':'bg-primary',
                            'Sports':'bg-warning',
                            'Entertainment':'bg-primary'}
        
        
        BlogPosts.results.forEach(post => {
            console.log(post)
            this.allPostContainer.innerHTML += `
            
            <div class="col-lg-4 mb-4">
                        <div class="entry2">
                              <a  data-id="" href="blog-detail/${post.id}/"><img src="${post.introPics}" alt="Image" class="img-fluid rounded"></a>
                              <div class="excerpt">
                                    <span class="post-category text-white  ${
                                        
                                        post.category== 'Politics'? ListOfcategory.Politics  
                                            : 
                                        post.category== 'Travel'? ListOfcategory.Travel
                                            :
                                        post.category== 'Sports'? ListOfcategory.Sports
                                            :
                                        post.category== 'Tech'? ListOfcategory.Tech 
                                        :
                                        ListOfcategory.Entertainment
                                        
                                        } mb-3">${post.category}</span>
                                     <h2><a href="blog-detail/${post.id}/">${post.title}</a></h2>
                                  <div class="post-meta align-items-center text-left clearfix">
                                      <figure class="author-figure mb-0 mr-3 float-left"><img src="${post.authorImage}" alt="Image" class="img-fluid"></figure>
                                      <span class="d-inline-block mt-1">By <a href="#">${post.authorName}</a></span>
                                      <span>&nbsp;-&nbsp; ${post.dateCreated}</span>
                                  </div>
                            
                                  <p>${post.introContent}</p>
                        
                                  <p><a href="blog-detail/${post.id}/">Read More</a></p>
                              </div>
                        </div>
                  </div>
            
            `
        }); 
    }

    //this sets a new attribute to the buttons the value of the atrribute will either be null or a url to the next page
    setPagination(data){

        this.prevBtn.setAttribute('data-prev',data.previous)
        this.nextBtn.setAttribute('data-next',data.next)

       

    }   


}



class BlogIndex{

    constructor(){
        this.ui = new UI()
    }



    async getAllBlogPost(url){

      let   resp =  await fetch(url)

      let   respData =await resp.json()
        // console.log(respData.results)

      this.ui.displayContent(respData)
    
    }

    
    

    


}




blog = new BlogIndex()
console.log('Yo')
blog.getAllBlogPost('/api/blog/blog/')

let prevBtn = document.querySelector('#prev');
let nextBtn = document.querySelector('#next')

prevBtn.addEventListener('click',e=>{
    e.preventDefault()
    // console.log(e.target)
    let prev = e.target.dataset.prev;

    if(prev === "null"){
        
        e.target.classList.add('remove')
        nextBtn.classList.remove('remove')
    }
    else{
        // e.target.classList.pop('remove')

        blog.ui.allPostContainer.innerHTML =''
    }
    
    console.log('prev',prev)
    blog.getAllBlogPost(prev)
    
})



nextBtn.addEventListener('click',e=>{
    e.preventDefault()
    let next =e.target.dataset.next;
    
    if(next === "null"){
        
        // 
    }  
    else{
        

        blog.ui.allPostContainer.innerHTML ='';

    }    
    
    
    blog.getAllBlogPost(next)


})