# names=["ahmed","mona","ali"]
# passwords=["123","1122",""]
# x=""
#
#
# def search(x):
#     for i in range(len(names)):
#         if names[i]==x:
#
#             return i
# while True:
#     x = input("please enter the user_name")
#     value=search(x)
#     if value !=None:
#         if passwords[search(x)]=="":
#             new_password=input("this account does not have password write one ")
#             passwords[search(x)]=new_password
#         else:
#             y=input("please enter the password \n")
#             if y==passwords[search(x)]:
#
#                 print("welcom sir")
#             else:
#                 print("wrong password ")
#     else:
#         print("wrong user_name")
import random
x=random.randint(1,100)
names=["fhjskldf","fdjhsklfhn","difjdiksfj"]
print(random.choice(names))


@app.route('/edittime', methods=['GET','POST'])
def edittime():
    if request.method=="POST":
        course_id = request.form.get('course_id')
        start_time = request.form.get('start_time')

        # Get the course from the database
        course = Course.query.get(course_id)

        if course:
            # Update the course time with the new value
            course.online_start_time = start_time
            db.session.commit()
            # Redirect or perform any other necessary actions
            return redirect("/dash")
    return render_template("time.html",course_id=course_id )

@app.route('/edit_course_time/<int:course_id>', methods=['GET', 'POST'])
def edit_course_time(course_id):
    course = Course.query.get(course_id)
    if course:
        if request.method == 'POST':
            # Update the course time with the new value
            course.online_start_time = request.form['start_time']
            db.session.commit()
            return redirect("/dash")
        return render_template('time.html', course=course)
    else:
        return 'Course not found', 404