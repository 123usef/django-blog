                                                   # django-blog
Creatinng a news blog using django framework


![home](https://user-images.githubusercontent.com/71194059/154836972-59cdf89e-278e-4ae9-b774-912bcb43500f.png)

                                     # Landing Page Content:
## Header:
* Will contain Two links Login/Register. 
* If the user is already logged in,then the link will be Logout.
* If the logged-in user is an admin,then there will be another link called Manage Blog that will redirect
    the admin to the administration page to make the admin CRUD Operations.


                                            # Register
                                            
![register](https://user-images.githubusercontent.com/71194059/154838364-c8814cb1-d740-4d99-bfd9-f6b2df6e7462.png)
* Username
* Email
* Password
* Password Confirmation

                                                # login
                                                
![login](https://user-images.githubusercontent.com/71194059/154838330-706e5d56-df5c-4dc0-96fd-1ed0d6336f2e.png)
* The form contains 2 fields. Username & PW.
* Password will be shown in asterisks. when the user clicks on login, 
* if he is blocked then redirect him back to the login page with a message (sorry you are blocked contact the admin)
* if he isn’t blocked then he will be authenticated.

                                         # manageblog/admin panel 
                                         
![manage blog users](https://user-images.githubusercontent.com/71194059/154838030-a9c0881c-81d8-4cc0-ac41-c6bd719f9522.png)

## Admin user characteristics:
* Admin users can make CRUD on posts.
* Admin user can make CRUD on categories
* Admin users can block or unblock users.
* Admin users can promote a normal user to an admin user so that he

### will be able to log into the admin screen.
* Admin users can CRUN on forbidden words.
* The Admin page will contain links
( users, posts, categories, forbidden words ).
When Admin clicks on the Posts Link, it would list all posts, with links to :
 *edit, 
 *delete 
 *create.
The same will be applied to categories 
forbidden words.


* When Admin clicks on Users Link
* it would list all the users 
  in case The user is also an admin, his row will be colored red. Else it will be a normal row. Or display is Admin equals to True.
* For normal users, there should be a button that enables the admin to either lock or unlock this user from logging into the system. 
* And for the Admin users, this button is not available So, an admin cannot lock another admin.

                                                  # category
                                                  
![category](https://user-images.githubusercontent.com/71194059/154838291-a44d73b7-0ee7-4f98-a867-b449dc124d42.png)

## Sidebar:
* Will contain all the available categories.
* with a button beside them be subscribe or unsubscribe if the user is already subscribed to this category.
* when a category is chosen it will be redirected to a page that contains all the posts belonging to this category. Sorted by date of publish.


![image](https://user-images.githubusercontent.com/71194059/154839060-7f91d834-2034-4370-99b3-630bcfc621f8.png)

* when click on subscribe to a category confirmation email would be sent to the user with this message
(Hello - user name - you have subscribed successfully in - category name - welcome aboard )

                                              # create post

![create post](https://user-images.githubusercontent.com/71194059/154838807-a24d5616-d594-4a33-a772-c243ca7f8580.png)

                                                   # post
                                                   
![posts](https://user-images.githubusercontent.com/71194059/154838830-17c010ff-6443-4750-b48a-d6b4fad6ed51.png)

## Post Page Content:
* Title
* Post Picture
* Content of the post
* The category that this post is under
* Comments section
* Tags related

![image](https://user-images.githubusercontent.com/71194059/154840312-beafc690-190a-4066-b7cf-1949d5b97543.png)

## Post Page Characteristics:
* Each comment shows the time of the comment and the username who wrote the comment.
* There will be a reply on comment (Bonus)
* Add comment Section. User must be signed in to can submit a comment (enter the text and a submit button to submit the comment)
* If the comment contains inappropriate words, it will show like
******
# To start django project:

* Set up a virtual environment
* Install Django
* Pin your project dependencies
* Set up a Django project
* Start a Django app

# import 

* from django.core.mail import send_mail
* from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Developed By:
https://github.com/YasminaMohamed99
https://github.com/TarekEldebsy94
https://github.com/lightmaher
https://github.com/123usef
https://github.com/salma25128
