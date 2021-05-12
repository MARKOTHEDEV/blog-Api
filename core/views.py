from rest_framework.response import Response
from rest_framework.decorators import api_view



@api_view(['GET',])
def documentation(request):

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
            
        ]}
    ]

    return Response(docs)