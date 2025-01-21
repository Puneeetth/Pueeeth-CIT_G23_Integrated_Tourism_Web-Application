from datetime import datetime as dt
import os
import random
from datetime import datetime, timedelta
from flask import Flask, render_template, redirect, request, session
import datetime
from flask import redirect, session
from flask import render_template, url_for
import firebase_admin
import random
from flask import Flask, request
from firebase_admin import credentials, firestore
TEMPLATE_DIR = os.path.abspath('templates')
STATIC_DIR = os.path.abspath('static')
app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = 'static/upload'
app.secret_key = 'Event@12345'
cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred)

@app.route('/userviewbookings', methods=['POST','GET'])
def userviewbookings():
    try:
        db = firestore.client()
        newdb_ref = db.collection('searchevent')
        dbdata = newdb_ref.get()
        userid = session['userid']
        data,total=[],0
        for doc in dbdata:
            #print(doc.to_dict())
            #print(f'{doc.id} => {doc.to_dict()}')
            temp=doc.to_dict()
            if(int(temp['UserId'])==int(userid)):
                data.append(doc.to_dict())
                if(temp['PaymentStatus']=='NotDone'):
                    total+=int(temp['Amount'])
        return render_template("userviewbookings.html", data=data, total=total)
    except Exception as e:
        return str(e)

@app.route('/', methods=['POST','GET'])
def homepage():
    try:
        return render_template("index.html")
    except Exception as e:
        return str(e)

@app.route('/paymentsuccesspage', methods=['POST','GET'])
def paymentsuccesspage():
    try:
        args = request.args
        payment_id = args['payment_id']
        amount = args['amount']
        personname = args['personname']
        phonenum = args['phonenum']
        instrument_type = args['instrument_type']
        billing_instrument = args['billing_instrument']
        status = args['status']
        currency = args['currency']
        purpose = args['purpose']
        return render_template("userpaymentsuccesspage.html",
        payment_id=payment_id, amount=amount, personname=personname,
        phonenum=phonenum, instrument_type=instrument_type,
        billing_instrument=billing_instrument, status=status,
        currency=currency, purpose=purpose)
    except Exception as e:
        return str(e)

@app.route('/logout', methods=['POST','GET'])
def logout():
    try:
        return render_template("index.html")
    except Exception as e:
        return str(e)

@app.route('/about', methods=['POST','GET'])
def aboutpage():
    return render_template("About.html")

@app.route('/services', methods=['POST','GET'])
def services():
    return render_template("services.html")

@app.route('/gallery', methods=['POST','GET'])
def gallery():
    return render_template("gallery.html")

@app.route('/adminlogin', methods=['POST','GET'])
def adminlogin():
    return render_template("adminlogin.html")

@app.route('/userlogin', methods=['POST','GET'])
def userlogin():
    return render_template("userlogin.html")

@app.route('/stafflogin', methods=['POST','GET'])
def stafflogin():
    return render_template("stafflogin.html")

@app.route('/newuser', methods=['POST','GET'])
def newuser():
    return render_template("newuser.html")

"""
@app.route('/adminviewusers')
def adminviewusers():
    mydb = getConnection();
    cursor = mydb.cursor()
    cursor.execute(
        ''' Select * from newcustomer''')
    rows = cursor.fetchall()

    cursor.execute(
        ''' Desc newcustomer''')
    cols = cursor.fetchall()
    size = len(cols)
    length=[]
    for x in range(0,size):
        length.append(x)
    return render_template("adminviewusers.html", rows=rows, cols=cols,
                           length=length)
"""
@app.route('/adminviewhotels', methods=['POST','GET'])
def adminviewhotels():
    try:
        db = firestore.client()
        newdb_ref = db.collection('newhotel')
        dbdata = newdb_ref.get()
        data=[]
        for doc in dbdata:
            #print(doc.to_dict())
            #print(f'{doc.id} => {doc.to_dict()}')
            data.append(doc.to_dict())
        return render_template("adminviewhotels.html", data=data)
    except Exception as e:
        return str(e)

@app.route('/usersearchhotel', methods=['POST','GET'])
def usersearchhotel():
    try:
        db = firestore.client()
        newdb_ref = db.collection('newhotel')
        dbdata = newdb_ref.get()
        data=[]
        for doc in dbdata:
            #print(doc.to_dict())
            #print(f'{doc.id} => {doc.to_dict()}')
            data.append(doc.to_dict())
        return render_template("usersearchhotels.html", data=data)
    except Exception as e:
        return str(e)

@app.route('/adminviewcabs', methods=['POST','GET'])
def adminviewcabs():
    try:
        db = firestore.client()
        newdb_ref = db.collection('newcab')
        dbdata = newdb_ref.get()
        data=[]
        for doc in dbdata:
            #print(doc.to_dict())
            #print(f'{doc.id} => {doc.to_dict()}')
            data.append(doc.to_dict())
        return render_template("adminviewcabs.html", data=data)
    except Exception as e:
        return str(e)

@app.route('/usersearchcab', methods=['POST','GET'])
def usersearchcab():
    try:
        db = firestore.client()
        newdb_ref = db.collection('newcab')
        dbdata = newdb_ref.get()
        data=[]
        for doc in dbdata:
            #print(doc.to_dict())
            #print(f'{doc.id} => {doc.to_dict()}')
            data.append(doc.to_dict())
        return render_template("usersearchcabs.html", data=data)
    except Exception as e:
        return str(e)

@app.route('/adminviewusers', methods=['POST','GET'])
def adminviewusers():
    try:
        db = firestore.client()
        newstaff_ref = db.collection('newuser')
        staffdata = newstaff_ref.get()
        data=[]
        for doc in staffdata:
            #print(doc.to_dict())
            #print(f'{doc.id} => {doc.to_dict()}')
            data.append(doc.to_dict())
        return render_template("adminviewusers.html", data=data)
    except Exception as e:
        return str(e)

"""
@app.route('/staffviewusers')
def staffviewusers():
    mydb = getConnection();
    cursor = mydb.cursor()
    cursor.execute(
        ''' Select * from newcustomer''')
    rows = cursor.fetchall()

    cursor.execute(
        ''' Desc newcustomer''')
    cols = cursor.fetchall()
    size = len(cols)
    length=[]
    for x in range(0,size):
        length.append(x)
    return render_template("staffviewusers.html", rows=rows, cols=cols,
                           length=length)
"""
@app.route('/staffviewusers', methods=['POST','GET'])
def staffviewusers():
    try:
        db = firestore.client()
        newstaff_ref = db.collection('newuser')
        staffdata = newstaff_ref.get()
        data=[]
        for doc in staffdata:
            #print(doc.to_dict())
            #print(f'{doc.id} => {doc.to_dict()}')
            data.append(doc.to_dict())
        return render_template("staffviewusers.html", data=data)
    except Exception as e:
        return str(e)

@app.route('/adminmainpage', methods=['POST','GET'])
def adminmainpage():
    return render_template("adminmainpage.html")

@app.route('/adminaddstaff', methods=['POST','GET'])
def adminaddstaff():
    return render_template("adminaddstaff.html")

@app.route('/adminaddevent', methods=['POST','GET'])
def adminaddevent():
    return render_template("adminaddevent.html")

"""
@app.route('/adminviewevents')
def adminviewevents():
    mydb = getConnection();
    cursor = mydb.cursor()
    cursor.execute(
        ''' Select * from newevent''')
    rows = cursor.fetchall()
    cursor.execute(
        ''' Desc newevent''')
    cols = cursor.fetchall()
    size = len(cols)
    length = []
    for x in range(0, size):
        length.append(x)
    return render_template("adminviewevents.html", rows=rows, cols=cols,
                           length=length)
"""
@app.route('/adminviewevents', methods=['POST','GET'])
def adminviewevents():
    try:
        db = firestore.client()
        newstaff_ref = db.collection('newevent')
        staffdata = newstaff_ref.get()
        data=[]
        for doc in staffdata:
            #print(doc.to_dict())
            #print(f'{doc.id} => {doc.to_dict()}')
            data.append(doc.to_dict())
        return render_template("adminviewevents.html", data=data)
    except Exception as e:
        return str(e)

"""
@app.route('/staffviewevents')
def staffviewevents():
    mydb = getConnection();
    cursor = mydb.cursor()
    cursor.execute(
        ''' Select * from newevent''')
    rows = cursor.fetchall()
    cursor.execute(
        ''' Desc newevent''')
    cols = cursor.fetchall()
    size = len(cols)
    length = []
    for x in range(0, size):
        length.append(x)
    return render_template("staffviewevents.html", rows=rows, cols=cols,
                           length=length)
"""
@app.route('/staffviewevents', methods=['POST','GET'])
def staffviewevents():
    try:
        db = firestore.client()
        newstaff_ref = db.collection('newevent')
        staffdata = newstaff_ref.get()
        data=[]
        for doc in staffdata:
            #print(doc.to_dict())
            #print(f'{doc.id} => {doc.to_dict()}')
            data.append(doc.to_dict())
        return render_template("staffviewevents.html", data=data)
    except Exception as e:
        return str(e)

@app.route('/adminviewstaffs', methods=['POST','GET'])
def adminviewstaffs():
    try:
        db = firestore.client()
        newstaff_ref = db.collection('newstaff')
        staffdata = newstaff_ref.get()
        data = []
        for doc in staffdata:
            # print(doc.to_dict())
            # print(f'{doc.id} => {doc.to_dict()}')
            data.append(doc.to_dict())
        return render_template("adminviewstaffs.html", data=data)
    except Exception as e:
        return str(e)
"""
@app.route('/adminviewreports')
def adminviewreports():
    try:
        db = firestore.client()
        newstaff_ref = db.collection('searchevent')
        staffdata = newstaff_ref.get()
        data = []
        for doc in staffdata:
            # print(doc.to_dict())
            # print(f'{doc.id} => {doc.to_dict()}')
            data.append(doc.to_dict())
        return render_template("adminviewreports.html", data=data)
    except Exception as e:
        return str(e)

@app.route('/staffviewreports')
def staffviewreports():
    try:
        db = firestore.client()
        newstaff_ref = db.collection('searchevent')
        staffdata = newstaff_ref.get()
        data = []
        for doc in staffdata:
            # print(doc.to_dict())
            # print(f'{doc.id} => {doc.to_dict()}')
            data.append(doc.to_dict())
        return render_template("staffviewreports.html", data=data)
    except Exception as e:
        return str(e)
"""
@app.route('/adminviewcontacts', methods=['POST','GET'])
def adminviewcontacts():
    try:
        db = firestore.client()
        newstaff_ref = db.collection('newcontact')
        staffdata = newstaff_ref.get()
        data = []
        for doc in staffdata:
            # print(doc.to_dict())
            # print(f'{doc.id} => {doc.to_dict()}')
            data.append(doc.to_dict())
        return render_template("adminviewcontacts.html", data=data)
    except Exception as e:
        return str(e)

@app.route('/adminlogincheck', methods=['POST','GET'])
def adminlogincheck():
    if request.method == 'POST':
        uname = request.form['uname']
        pwd = request.form['pwd']
    ##print("Uname : ", uname, " Pwd : ", pwd)
    if uname == "admin" and pwd == "admin":
        return render_template("adminmainpage.html")
    else:
        return render_template("adminlogin.html", msg="UserName/Password is Invalid")

@app.route('/contact',methods=['POST','GET'])
def contactpage():
    try:
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            subject = request.form['subject']
            message = request.form['message']
            id = str(random.randint(1000, 9999))
            json = {'id': id,
                    'ContactName': name,
                    'Message': message, 'Subject': subject,
                    'EmailId': email}
            db = firestore.client()
            db_ref = db.collection('newcontact')
            id = json['id']
            db_ref.document(id).set(json)
            msg="Contact Added Success"
            return render_template("contact.html",msg=msg)
        else:
            return render_template("contact.html")
    except Exception as e:
        return str(e)

@app.route('/userviewprofile', methods=['POST','GET'])
def userviewprofile():
    try:
        id=session['userid']
        print("Id",id)
        db = firestore.client()
        newdb_ref = db.collection('newuser')
        data = newdb_ref.document(id).get().to_dict()
        print(data)
        return render_template("userviewprofile.html", data=data)
    except Exception as e:
        return str(e)
        return render_template("userlogin.html", msg=e)

@app.route('/staffviewprofile', methods=['POST','GET'])
def staffviewprofile():
    try:
        id=session['userid']
        print("Id",id)
        db = firestore.client()
        newdb_ref = db.collection('newstaff')
        data = newdb_ref.document(id).get().to_dict()
        print(data)
        return render_template("staffviewprofile.html", data=data)
    except Exception as e:
        return str(e)
        return render_template("stafflogin.html", msg=e)

@app.route('/userlogincheck', methods=['POST','GET'])
def userlogincheck():
    try:
        if request.method == 'POST':
            uname = request.form['uname']
            pwd = request.form['pwd']
            db = firestore.client()
            print("Uname : ", uname, " Pwd : ", pwd);
            newdb_ref = db.collection('newuser')
            dbdata = newdb_ref.get()
            data = []
            flag = False
            for doc in dbdata:
                data = doc.to_dict()
                if (data['UserName'] == uname and data['Password'] == pwd):
                    flag = True
                    session['userid'] = data['id']
                    break
            if (flag):
                print("Login Success")
                return render_template("usermainpage.html")
            else:
                return render_template("userlogin.html", msg="UserName/Password is Invalid")
    except Exception as e:
        return str(e)
        return render_template("userlogin.html", msg=e)

@app.route('/stafflogincheck', methods=['POST','GET'])
def stafflogincheck():
    try:
        if request.method == 'POST':
            uname = request.form['uname']
            pwd = request.form['pwd']
            db = firestore.client()
            print("Uname : ", uname, " Pwd : ", pwd);
            newdb_ref = db.collection('newstaff')
            dbdata = newdb_ref.get()
            data = []
            flag = False
            for doc in dbdata:
                data = doc.to_dict()
                if (data['UserName'] == uname and data['Password'] == pwd):
                    flag = True
                    session['userid'] = data['id']
                    break
            if (flag):
                print("Login Success")
                return render_template("staffmainpage.html")
            else:
                return render_template("stafflogin.html", msg="UserName/Password is Invalid")
    except Exception as e:
        return render_template("userlogin.html", msg=e)

@app.route('/admindeletestaff', methods=['POST','GET'])
def admindeletestaff():
    try:
        args = request.args
        id = args.get("id")
        db = firestore.client()
        db.collection("newstaff").document(id).delete()
    except Exception as e:
        return redirect (url_for("adminviewstaffs.html"))
    return redirect (url_for("adminviewstaffs.html"))

@app.route('/admindeleteevent', methods=['POST','GET'])
def admindeleteevent():
    try:
        args = request.args
        id = args.get("id")
        db = firestore.client()
        db.collection("newevent").document(id).delete()
        return redirect(url_for("adminviewevents.html"))
    except Exception as e:
        return redirect(url_for("adminviewevents.html"))
"""
@app.route('/staffviewreports')
def staffviewreports():
    try:
        db = firestore.client()
        newstaff_ref = db.collection('newreport')
        staffdata = newstaff_ref.get()
        data = []
        for doc in staffdata:
            # print(doc.to_dict())
            # print(f'{doc.id} => {doc.to_dict()}')
            data.append(doc.to_dict())
        return render_template("adminviewcontacts.html", data=data)
    except Exception as e:
        return str(e)
"""
@app.route('/contact', methods=['POST','GET'])
def contactPage():
    return render_template("contact.html")

@app.route('/addcontact', methods=['POST','GET'])
def addcontact():
    msg=""
    if request.method == 'POST':
        cname = request.form['cname']
        subject = request.form['subject']
        message = request.form['message']
        email = request.form['email']
        id = str(random.randint(1000, 9999))
        json = {'id': id,
                'ContactName': cname,
                'Message': message, 'Subject': subject,
                'EmailId': email}
        db = firestore.client()
        db_ref = db.collection('newcontact')
        id = json['id']
        db_ref.document(id).set(json)
        msg = "Contact Added Success"
        return render_template("contact.html", msg=msg)
    return render_template("contact.html", msg=msg)

@app.route('/adduser', methods=['POST','GET'])
def adduser():
    msg=""
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        uname = request.form['uname']
        pwd = request.form['pwd']
        email = request.form['email']
        phnum = request.form['phnum']
        address = request.form['address']
        id = str(random.randint(1000, 9999))
        json = {'id': id,
                'FirstName': fname,'LastName':lname,'Address':address,
                'EmailId': email, 'PhoneNum': phnum,
                'UserName': uname, 'Password':pwd}
        db = firestore.client()
        db_ref = db.collection('newuser')
        db_ref.document(id).set(json)
        msg = "User Added Success"
    return render_template("newuser.html", msg=msg)

@app.route('/addstaff', methods=['POST','GET'])
def addstaff():
    msg=""
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        uname = request.form['uname']
        pwd = request.form['pwd']
        email = request.form['email']
        phnum = request.form['phnum']
        address = request.form['address']
        id = str(random.randint(1000, 9999))
        json = {'id': id,
                'FirstName': fname,'LastName':lname,'Address':address,
                'EmailId': email, 'PhoneNumber': phnum,
                'UserName': uname, 'Password':pwd}
        db = firestore.client()
        db_ref = db.collection('newstaff')
        db_ref.document(id).set(json)
        msg = "Staff Added Success"
    return render_template("adminaddstaff.html", msg=msg)

@app.route('/adminaddhotel', methods=['POST','GET'])
def adminaddhotel():
    msg=""
    if request.method == 'POST':
        hname = request.form['hname']
        htype = request.form['htype']
        email = request.form['email']
        price = request.form['price']
        phnum = request.form['phnum']
        address = request.form['address']
        id = str(random.randint(1000, 9999))
        json = {'id': id, 'Price':price,
                'HotelName': hname,'HotelType':htype,'Address':address,
                'EmailId': email, 'PhoneNumber': phnum}
        db = firestore.client()
        db_ref = db.collection('newhotel')
        db_ref.document(id).set(json)
        msg = "Hotel Added Success"
    return render_template("adminaddhotel.html", msg=msg)

@app.route('/adminaddcab', methods=['POST','GET'])
def adminaddcab():
    msg=""
    if request.method == 'POST':
        cname = request.form['cname']
        fname = request.form['fname']
        lname = request.form['lname']
        ctype = request.form['ctype']
        price = request.form['price']
        email = request.form['email']
        phnum = request.form['phnum']
        address = request.form['address']
        id = str(random.randint(1000, 9999))
        json = {'id': id,'DriverFirstName':fname,
                'DriverLastName': lname,'Price':price,
                'CabName': cname,'CabType':ctype,'Address':address,
                'EmailId': email, 'PhoneNumber': phnum}
        db = firestore.client()
        db_ref = db.collection('newcab')
        db_ref.document(id).set(json)
        msg = "Cab Added Success"
    return render_template("adminaddcab.html", msg=msg)

@app.route('/addevent', methods=['POST','GET'])
def addevent():
    msg=""
    if request.method == 'POST':
        ename = request.form['ename']
        etype = request.form['etype']
        price = request.form['price']
        comments = request.form['comments']
        id = str(random.randint(1000, 9999))
        json = {'id': id,
                'EventName': ename,'EventType':etype,
                'Price': price, 'Comments': comments}
        db = firestore.client()
        db_ref = db.collection('newevent')
        db_ref.document(id).set(json)
        msg = "Event Added Success"
    return render_template("adminaddevent.html", msg=msg)

@app.route('/usersearchevent', methods=['POST','GET'])
def usersearchevent():
    try:
        db = firestore.client()
        newstaff_ref = db.collection('newevent')
        staffdata = newstaff_ref.get()
        data = []
        for doc in staffdata:
            # print(doc.to_dict())
            # print(f'{doc.id} => {doc.to_dict()}')
            data.append(doc.to_dict())
        return render_template("usersearchevents.html", data=data)
    except Exception as e:
        return str(e)

@app.route('/usersearchcab1', methods=['POST','GET'])
def usersearchcab1():
    args = request.args
    eventid = args.get("id")
    userid=session['userid']
    db = firestore.client()
    newdb_ref = db.collection('newuser')
    userdata = newdb_ref.document(userid).get().to_dict()
    newdb_ref = db.collection('newcab')
    eventdata = newdb_ref.document(eventid).get().to_dict()
    print("Event Data : ", eventdata, " User Data : ", userdata)
    return render_template("usersearchcabs1.html", userdata=userdata, eventdata=eventdata)

@app.route('/usersearchhotel1', methods=['POST','GET'])
def usersearchhotel1():
    args = request.args
    eventid = args.get("id")
    userid=session['userid']
    db = firestore.client()
    newdb_ref = db.collection('newuser')
    userdata = newdb_ref.document(userid).get().to_dict()
    newdb_ref = db.collection('newhotel')
    eventdata = newdb_ref.document(eventid).get().to_dict()
    print("Event Data : ", eventdata, " User Data : ", userdata)
    return render_template("usersearchhotels1.html", userdata=userdata, eventdata=eventdata)

@app.route('/usersearchevent1', methods=['POST','GET'])
def usersearchevent1():
    args = request.args
    eventid = args.get("id")
    userid=session['userid']
    db = firestore.client()
    newdb_ref = db.collection('newuser')
    userdata = newdb_ref.document(userid).get().to_dict()
    newdb_ref = db.collection('newevent')
    eventdata = newdb_ref.document(eventid).get().to_dict()
    print("Event Data : ", eventdata, " User Data : ", userdata)
    return render_template("usersearchevents1.html", userdata=userdata, eventdata=eventdata)

@app.route('/usersearchevent2', methods=['POST','GET'])
def usersearchevent2():
    if request.method == 'POST':
        ename = request.form['ename']
        etype = request.form['etype']
        eventid = request.form['eid']
        userid = request.form['cid']
        cname = request.form['cname']
        days = request.form['days']
        price = request.form['price']
        amount = request.form['amount']

        db = firestore.client()
        newdb_ref = db.collection('newuser')
        userdata = newdb_ref.document(userid).get().to_dict()
        newdb_ref = db.collection('newevent')
        eventdata = newdb_ref.document(eventid).get().to_dict()

        if(eventdata):
            ename = eventdata['EventName']
            etype=eventdata['EventType']
            price = eventdata['Price']
            #comments = eventdata['Comments']

            id = str(random.randint(1000, 9999))
            json = {'id': id, 'UserId':userid,'EventId':eventid,
                    'FullName': userdata['FirstName'] + userdata['LastName'],
                    'EventName': ename, 'EventType': etype,
                    'Amount': amount,'SelectedType':'Event',
                    'Price':price, 'Days':days,'PaymentStatus':'NotDone',
                    'Status':'Requested'}
            db = firestore.client()
            db_ref = db.collection('searchevent')
            db_ref.document(id).set(json)
        return redirect(url_for("userviewbookings"))

@app.route('/usersearchcab2', methods=['POST','GET'])
def usersearchcab2():
    if request.method == 'POST':
        cname = request.form['cname']
        ctype = request.form['ctype']
        cid = request.form['cid']
        userid = request.form['uid']
        uname = request.form['cname']
        days = request.form['days']
        price = request.form['price']
        amount = request.form['amount']

        db = firestore.client()
        newdb_ref = db.collection('newuser')
        userdata = newdb_ref.document(userid).get().to_dict()
        newdb_ref = db.collection('newcab')
        eventdata = newdb_ref.document(cid).get().to_dict()
        if(eventdata):
            ename = eventdata['CabName']
            etype=eventdata['CabType']
            price = eventdata['Price']
            #drivername=str(eventdata['DriverFirstName'])+" "+str(eventdata['DriverLastName'])

            id = str(random.randint(1000, 9999))
            json = {'id': id, 'UserId':userid,'EventId':cid,
                    'SelectedType':'Cab',
                    'FullName': userdata['FirstName'] + userdata['LastName'],
                    'EventName': ename, 'EventType': etype,
                    'Amount': amount,
                    'Price':price, 'Days':days,'PaymentStatus':'NotDone',
                    'Status':'Requested'}
            db = firestore.client()
            db_ref = db.collection('searchevent')
            db_ref.document(id).set(json)
        return redirect(url_for("userviewbookings"))

@app.route('/usersearchhotel2', methods=['POST','GET'])
def usersearchhotel2():
    if request.method == 'POST':
        hname = request.form['hname']
        htype = request.form['htype']
        hid = request.form['hid']
        userid = request.form['uid']
        uname = request.form['uname']
        days = request.form['days']
        price = request.form['price']
        amount = request.form['amount']

        db = firestore.client()
        newdb_ref = db.collection('newuser')
        userdata = newdb_ref.document(userid).get().to_dict()
        newdb_ref = db.collection('newhotel')
        eventdata = newdb_ref.document(hid).get().to_dict()

        if(eventdata):
            ename = eventdata['HotelName']
            etype=eventdata['HotelType']
            price = eventdata['Price']
            #comments = eventdata['Comments']

            id = str(random.randint(1000, 9999))
            json = {'id': id, 'UserId':userid,'EventId':hid,
                   'SelectedType':'Hotel',
                    'FullName': userdata['FirstName'] + userdata['LastName'],
                    'EventName': ename, 'EventType': etype,
                    'Amount': amount,
                    'Price':price, 'Days':days,'PaymentStatus':'NotDone',
                    'Status':'Requested'}
            db = firestore.client()
            db_ref = db.collection('searchevent')
            db_ref.document(id).set(json)
        return redirect(url_for("userviewbookings"))

@app.route('/staffviewreports', methods=['POST','GET'])
def staffviewreports():
    try:
        db = firestore.client()
        newstaff_ref = db.collection('searchevent')
        dbdata = newstaff_ref.get()
        data = []
        for doc in dbdata:
            # print(doc.to_dict())
            # print(f'{doc.id} => {doc.to_dict()}')
            data.append(doc.to_dict())
        return render_template("staffviewreports.html", data=data)
    except Exception as e:
        return str(e)

@app.route('/adminviewreports', methods=['POST','GET'])
def adminviewreports():
    try:
        db = firestore.client()
        newstaff_ref = db.collection('searchevent')
        dbdata = newstaff_ref.get()
        data = []
        for doc in dbdata:
            # print(doc.to_dict())
            # print(f'{doc.id} => {doc.to_dict()}')
            data.append(doc.to_dict())
        return render_template("adminviewreports.html", data=data)
    except Exception as e:
        return str(e)

@app.route('/userviewreports', methods=['POST','GET'])
def userviewreports():
    try:
        userid = session['userid']
        db = firestore.client()
        newstaff_ref = db.collection('searchevent')
        dbdata = newstaff_ref.get()
        data = []
        for doc in dbdata:
            temp=doc.to_dict()
            if(temp['UserId']==userid):
                data.append(doc.to_dict())
        return render_template("userviewreports.html", data=data)
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)