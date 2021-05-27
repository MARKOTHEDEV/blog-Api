class UI{

    constructor(){
        this.allPostContainer = document.querySelector('#allPostContainer')
        this.prevBtn = document.querySelector('#prev')
        this.nextBtn = document.querySelector('#next')
    }

    resetAllPostContainer(){
        this.allPostContainer.innerHTML =''
    }

    //this method display all the content on the index.html page
    displayContent(BlogPosts){
        // this data passed is an array

        // we going to da the pagination settings here
        this.setPagination(BlogPosts)
        // console.log(BlogPosts)
        //based on the categories  we apply the right bootstrap background color  
        let ListOfcategory =    {'Politics':'bg-danger',
                            'Travel':'bg-success',
                            'Tech':'bg-primary',
                            'Sports':'bg-warning',
                            'Entertainment':'bg-primary'}
        
        
        BlogPosts.results.forEach(post => {
            // console.log(post)
            // location.origin -- will get the website name
            // and we just append the etra link to it using good old concatenation style
            this.allPostContainer.innerHTML += `
            
            <div class="col-lg-4 mb-4">
                        <div class="entry2">
                              <a  data-id="" href="${location.origin+"/blog-detail/"+post.id+"/"}"><img src="${post.introPics}" alt="Image" class="img-fluid rounded"></a>
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
                                     <h2><a href="${location.origin+"/blog-detail/"+post.id+"/"}">${post.title}</a></h2>
                                  <div class="post-meta align-items-center text-left clearfix">
                                      <figure class="author-figure mb-0 mr-3 float-left"><img src="${post.authorImage}" alt="Image" class="img-fluid"></figure>
                                      <span class="d-inline-block mt-1">By <a href="#">${post.authorName}</a></span>
                                      <span>&nbsp;-&nbsp; ${post.dateCreated}</span>
                                  </div>
                            
                                  <p>${post.introContent}</p>
                        
                                  <p><a href="${location.origin+"/blog-detail/"+post.id+"/"}">Read More</a></p>
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
      let respStatus = resp.status
    //   console.log(respData)

    
      this.ui.displayContent(respData)
    
    }

    
    

    


}


// location.origin

blog = new BlogIndex()
console.log('Yo')
// urlTogetBlogPost this can be either url to get all blog post or url to get filterd post
// as at now index and category.html are sharing this js file
blog.getAllBlogPost(urlTogetBlogPost)

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


let searchTextByAuthorOrPostName = document.querySelector('#searchTextByAuthorOrPostName')

searchTextByAuthorOrPostName.addEventListener('keyup',e=>{
    let searchText = e.target.value
    // console.log(blog)
    // this method rest the ui For to display the content
    blog.ui.resetAllPostContainer()
    blog.getAllBlogPost(`/api/blog/blog/?searchPost=${searchText}`)

})

// create a search event listener 