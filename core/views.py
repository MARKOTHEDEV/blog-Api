from rest_framework.response import Response
from rest_framework.decorators import api_view



@api_view(['GET',])
def documentation(request):
    'this view just renders the documentation Of the entire api'
    docs = [
        {'Intro':'To deal with this Api they are two main urls "users/" and "blog/" '},

        {'users':[
            {'login end point-->to get your Token':'/api/users/login/'},
            {'create a new user':'/api/users/create-user/'},
            {'To get a specific user-- get req':'/api/users/myprofile/user.id/'},
            {'To update user --- patch':'/api/users/myprofile/user.id/'},
            {'To delete  user --- delete request':'/api/users/myprofile/user.id/'},
        ]},

        {'blog':[
            {'To get all blog post -- get':"/api/blog/blog/"},
            {'To get a blog post -- get':"/api/blog/blog/blog.id/"},
            {'To get a blog post to update if u are the owner u will have access -- patch':"/api/blog/blog/blog.id/"},
            {'To get a blog post to delete if u are the owner u will have access -- delete':"/api/blog/blog/blog.id/"},
        ]},

        {'comment':[
            {'to get all comment of a particular post -- GET':'/api/blog/comment/blog_id/'},
            {'to create a post -->POST':r'/api/blog/comment/    FOR THIS WE need to sumbit this data to through a POST request ==> "{comment:comment-data,blog:blog.id}" '},
            {'update a particular comment u have to be the owner  -- PATCH request':r"/api/blog/comment/comment_id/ -- send this data {'comment':'MARKOTHEDEV'}"},
            {'To Delete a particular comment u have to be the owner  -- DELETE request':r"/api/blog/comment/comment_id/"},
            
        ]}
    ]

    return Response(docs)