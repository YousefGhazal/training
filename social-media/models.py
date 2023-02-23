from datetime import datetime


class User:
    data = []

    def __init__(self, fname: str, lname: str, email: str) -> None:
        self.fname = fname
        self.lname = lname
        self.email = email
        User.data.append(self)


class Profile:
    data = []

    def __init__(self, about: str, skill: list, user: User) -> None:
        self.about = about
        self.skill = skill
        self.user = user
        Profile.data.append(self)


class Post:
    data = []

    def __init__(self, text: str, user: User) -> None:
        self.text:str = text
        self.date = datetime.now()
        self.user = user
        Post.data.append(self)


class Like:
    data = []

    def __init__(self, post: Post, user: User) -> None:
        self.post = post
        self.user = user
        Like.data.append(self)


class Comment:
    data = []

    def __init__(self, text, post: Post, user: User) -> None:
        self.post = post
        self.user = user
        self.text = text
        Comment.data.append(self)


user = User("yousef", "yasser", "email.com")
user1 = User("yousef", "yasser", "email.com")
pro = Profile("bbb", ["ll", "pp"], user1)
post = Post("post text hh", user1)
com = Comment("rrr", post, user1)

# - input => keyword , output => list of posts 
print(Post.data[0].text)
p_word = input()
def get_posts_by_keyword(word):
    for i in Post.data:
        arr = i.text.split()
        if word in arr:
            print(i)

get_posts_by_keyword(p_word)

# input => post.text , output => list of data form comment
# k_post = input()
# def get_comments(post):
#     comments = []
#     for i in Comment.data:
#         if i.post.text == post:
#             comments.append(i)
#     print(comments)


# get_comments(k_post)

# input => user.fname , output => list of data form post

# u_post = input()


# def get_posts(user):
#     posts = []
#     for i in Post.data:
#         if i.user.fname == user:
#             posts.append(i)
#     print(posts)


# get_posts(u_post)


"""
- save class data in list 
- input => class name , output => class data
"""
# key = input()
# def get_data(key):
#     arr = {
#         "User": User.data,
#         "Profile": Profile.data,
#         "Post": Post.data,
#         "Like": Like.data,
#         "Comment": Comment.data,
#     }
#     if key in arr.keys() :
#         print(arr[key])


# get_data(key)


"""

"""
