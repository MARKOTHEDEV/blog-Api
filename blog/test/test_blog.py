from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth import get_user_model
from  blog import models,serializer
from rest_framework import status


import blog

def create_user(**kwargs):
    'this function helps us create a user it jus an helper function that prevent us from writing reated code'

    return get_user_model().objects.create_user(**kwargs)

def create_blogpost(**params):
    'helper funtion that create a blog post on call of it'
    return models.Blog.objects.create(**params)

CREATE_POST_URL  = reverse('blog-list')

def update_post_url(id):
    return reverse('blog-detail',args=[id,])

print(update_post_url(1))
print(CREATE_POST_URL)

class TestBlogAuthUser(TestCase):
    'this test is for auth users'

    def setUp(self):
        self.client = APIClient()
        paylaod =   {'name':'matthew','email':'marko2@gmail.com','password':'YouCrazyWIthProgramming'}  
        self.user = create_user(**paylaod)
        self.client.force_authenticate(self.user)

    def test_user_create_blog(self):
        blogpost = {'title':'heloo world','blogPost':'thedhbfdbfrd'}
        resp = self.client.post(CREATE_POST_URL,blogpost)



        self.assertEqual(resp.status_code,status.HTTP_201_CREATED)
        isBlogExits = models.Blog.objects.filter(author=self.user,title=resp.data.get('title')).exists()
        self.assertTrue(isBlogExits)




    def test_partial_upate_blog_post(self):
        blogpost = {'title':'heloo world','blogPost':'thedhbfdbfrd','author':self.user}
        # create_blogpost(**blogpost)
        # we have created the blog so now let try to update it
        # createBlogResp =   self.client.post(CREATE_POST_URL,blogpost)
        createBlogResp =   models.Blog.objects.create(**blogpost)
        # print(createBlogResp)
        # self.client.force_authenticate(self.user)
        resp = self.client.patch(f'/api/blog/blog/{createBlogResp.id}/',{'title':'Yo(Updated by marko)'})
        
        # print(createBlogResp.data.get('id'))
        createBlogResp.refresh_from_db()
        self.assertEqual(resp.status_code,status.HTTP_200_OK)
        # self.assertEqual(resp.data.results.get('title'),'Yo(Updated by marko)')
        
        # print(models.Blog.objects.get(id=createBlogResp.id))
        self.assertTrue(models.Blog.objects.filter(id=createBlogResp.id,title='Yo(Updated by marko)').exists())

    def test_if_anyAuth_user_can_update_post_that_are_not_thier_own(self):
        blogpost = {'title':'heloo world','blogPost':'thedhbfdbfrd'}
        # create_blogpost(**blogpost)
        # we have created the blog so now let try to update it
        createBlogResp =   self.client.post(CREATE_POST_URL,blogpost)
        # now we create another user 
        payload = {'name':'matthew22','email':'newUser@gmail.com','password':'YouCrazyWIthProgramming'}
        # this new user has no right to delete another user post so we gonna test that
        newUser = create_user(**payload)
        # login the new user 
        self.client.force_authenticate(newUser)
        # test if he can update another persons post
        # print(createBlogResp.get('id'))
        resp = self.client.patch(f"/api/blog/blog/{createBlogResp.data.get('id')}/",{'title':'Yo(Updated by marko)'})

        self.assertEqual(resp.status_code,status.HTTP_403_FORBIDDEN)
        # let check if the post was updated
        self.assertFalse(models.Blog.objects.filter(id=createBlogResp.data.get('id'),title='Yo(Updated by marko)').exists())

        # status


    def test_if_anyAuth_user_can_delete_post_that_are_not_thier_own(self):
        'this test if any body can delete a author post'

        """
            Steps:
                we create a 2 author
                we create a post with author 1 when he was logged in 
                we logged author 1 out
                we logged in auhor two and test if author 2 can delete author 1 post

                IT RETUNRS HTTP_403_FORBIDDEN
        """
        payload = {'name':'matthew','email':'newUser@gmail.com','password':'YouCrazyWIthProgramming'}
        # this new user has no right to delete another user post so we gonna test that
        newUser = create_user(**payload)
        # now we created a blog post using the self.user as the author of this blog post
        # now we will test if another user can delete
        blogpost = {'title':'heloo world','blogPost':'thedhbfdbfrd'}
        # we have created the blog so now let try to update it
        createBlogResp =   self.client.post(CREATE_POST_URL,blogpost)
        self.assertEqual(createBlogResp.status_code,status.HTTP_201_CREATED)


        # now let log in the new user
        # and try to delete another Author blog post 

        self.client.force_authenticate(newUser)
        
        deleteBlogPostresp = self.client.delete(f"/api/blog/blog/{createBlogResp.data.get('id')}/")
        self.assertEqual(deleteBlogPostresp.status_code,status.HTTP_403_FORBIDDEN)
        self.assertTrue(models.Blog.objects.filter(id=createBlogResp.data.get('id')).exists())

        




    def test_delete_post(self):
        'this post helps test deletion of post'
        # first we need to create a post with a logged in user
        blogpost = {'title':'heloo world','blogPost':'thedhbfdbfrd'}
        # we have to test if it was created first
        createBlogResp =   self.client.post(CREATE_POST_URL,blogpost)
        self.assertEqual(createBlogResp.status_code,status.HTTP_201_CREATED)
        # let check if the post was created
        self.assertTrue(models.Blog.objects.filter(id=createBlogResp.data.get('id')).exists())
        # we have created the blog so now let try to delete the BlogPost it

        # dont be confused! 
        # the 
        # update_post_url is the same as a detail view that accept an id to identify the object
        #  we want to perform task on
        deleteBlogPostresp = self.client.delete(f"/api/blog/blog/{createBlogResp.data.get('id')}/")
        
        self.assertEqual(deleteBlogPostresp.status_code,status.HTTP_204_NO_CONTENT)
        self.assertFalse(models.Blog.objects.filter(id=createBlogResp.data.get('id')).exists())



class TestBlogUser(TestCase):
    'this class test both auth and unauth user on how they use the non-authticated part of the website'

    def setUp(self):
        self.client = APIClient()
        
        

    def test_get_post_by_categories(self):
        """i will create 3 blog post 2 belonging to the tech category and 1 Travel
            and will test to get the travel category
        """
        
        paylaod =   {'name':'matthew','email':'marko2@gmail.com','password':'YouCrazyWIthProgramming'}  
        author = create_user(**paylaod)
        blogpostForTech = {'title':'heloo world','blogPost':'thedhbfdbfrd','category':'Tech','author':author}
        techPost1 = create_blogpost(**blogpostForTech)
        techPost2 = create_blogpost(**blogpostForTech)
        blogpostForTravel = {'title':'heloo world','blogPost':'thedhbfdbfrd','category':'Travel','author':author}
        # print(blogpostForTravel.get('category'))
        TravelPost1 = create_blogpost(**blogpostForTravel)
        
        TravelPost1SerializedData = serializer.BlogSerializer(TravelPost1)
        # /api/blog/blog/politics/filterby/ this is the url that filters accorign to category
        resp = self.client.get(CREATE_POST_URL,{'category':'Travel'})
        # we only have one category with the name of Travel in the database 
        # so we expecting one results
        self.assertEqual(len(resp.data.get('results')),1)
        # this is to test if the category are same
        self.assertEqual(resp.data.get('results')[0].get('category'),TravelPost1SerializedData.data.get('category'))

    
    def test_searchFunctionality(self):
        "this is to test the search function by title"
        paylaod =   {'name':'matthew','email':'marko2@gmail.com','password':'YouCrazyWIthProgramming'}  
        author = create_user(**paylaod)
        techPost1 = create_blogpost(title='heloo world',blogPost='thedhbfdbfrd',category='Tech',author=author)
        techPost2 = create_blogpost(title='Yo',blogPost='hfekwdefevfedh',category='Tech',author=author)
        # techPost2 = create_blogpost(**blogpostForTech)
        TechPost1SerializedData = serializer.BlogSerializer(techPost1)
        resp = self.client.get(CREATE_POST_URL,{'searchPost':'heloo world'})
        

        self.assertEqual(len(resp.data.get('results')),1)
        self.assertEqual(resp.data.get('results')[0].get('title'),TechPost1SerializedData.data.get('title'))



        


class TestUnAuthBlogUSer(TestCase): 
    'this class test the un auth users=>on how they use the blog'

    def setUp(self):
        self.client = APIClient()
        self.payload = {'name':'matthew','email':'marko2@gmail.com','password':'YouCrazyWIthProgramming'}
    





    def test_unAuth_user_create_blogPost(self):
        blogpost = {'title':'heloo world','blogPost':'thedhbfdbfrd'}
        resp = self.client.post(CREATE_POST_URL,blogpost)
        
        user = create_user(**self.payload)


        self.assertEqual(resp.status_code,status.HTTP_401_UNAUTHORIZED)
        isBlogExits = models.Blog.objects.filter(author=user,title=resp.data.get('title'))
        self.assertFalse(isBlogExits)

    def test_if_a_unAuth_user_can_view_a_blog_post(self):
        # firt create a user
        user = create_user(**self.payload)
        blogParams = {'author':user,'title':'jimmy Zang','blogPost':'Lorem ipsom'}
        blogPost = create_blogpost(**blogParams)
        # CREATE_POST_URL -- this url also serve as a get all blog post
        resp = self.client.get(CREATE_POST_URL)

        self.assertEqual(resp.status_code,status.HTTP_200_OK)

    def test_if_a_unAuth_user_can_view_a_blog_specific_post(self):
        # firt create a user
        user = create_user(**self.payload)

        blogParams = {'author':user,'title':'jimmy Zang','blogPost':'Lorem ipsom'}
        blogPost = create_blogpost(**blogParams)
        
        resp = self.client.get(update_post_url(blogPost.id))
        # print(resp.data)
        self.assertEqual(resp.status_code,status.HTTP_200_OK)




