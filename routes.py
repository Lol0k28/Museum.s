from flask import render_template, redirect
from flask_login import login_user, logout_user, login_required, current_user
from os import path

from forms import AddMuseumForm, AddArtefactForm, AddCommentForm, RegisterForm, AuthorizationForm, UserOpinion
from models import Museum, Artefact, Commentaries, Opinion, User
from ext import app

bottom_img = [
    {"img": "Dadiani.png"},
    {
        "img": "Louvre.webp"},
    {"img": "Egipto.avif"}
]
tbc = [
    {"TBC-logo": "TBC-logo.png"}
]


@app.route("/info")
def info():
    museum_info = Museum.query.all()
    return render_template("Info.html", museum_info=museum_info, imgs=bottom_img, logo=tbc)


@app.route("/artefacts", methods=["POST", "GET"])
def artefact():
    artefacts3 = Artefact.query.all()
    return render_template("artefacts.html", imgs=bottom_img, logo=tbc, artefacts3=artefacts3)


@app.route("/edit-museum/<int:index>", methods=["POST", "GET"])
@login_required
def edit_museum(index):
    if current_user.role != "Admin":
        return redirect("/")

    museum_info = Museum.query.get(index)
    form = AddMuseumForm(info=museum_info.info, title=museum_info.title, country=museum_info.country,
                         img=museum_info.img)
    if form.validate_on_submit():
        museum_info.title = form.title.data
        museum_info.info = form.info.data
        museum_info.country = form.country.data
        museum_info.img = form.img.data.filename
        file_dir = path.join(app.root_path, "static", form.img.data.filename)
        form.img.data.save(file_dir)
        museum_info.save()
        return redirect("/info")
    return render_template("add-museum.html", form=form)


@app.route("/edit-artefact/<int:index>", methods=["POST", "GET"])
@login_required
def edit_artefact(index):
    if current_user.role != "Admin":
        return redirect("/")
    artefacts3 = Artefact.query.get(index)
    form = AddArtefactForm(artefact_museum=artefacts3.artefact_museum, info=artefacts3.info, title=artefacts3.title,
                           img=artefacts3.img)
    if form.validate_on_submit():
        artefacts3.title = form.title.data
        artefacts3.info = form.info.data
        artefacts3.artefact_museum = form.artefact_museum.data
        artefacts3.img = form.img.data.filename
        file_dir = path.join(app.root_path, "static", form.img.data.filename)
        form.img.data.save(file_dir)
        artefacts3.save()
        return redirect("/artefacts")
    return render_template("add-artefact.html", form=form)


@app.route("/delete-museum/<int:index>", methods=["POST", "GET"])
@login_required
def delete_museum(index):
    if current_user.role != "Admin":
        return redirect("/")
    museum_info = Museum.query.get(index)
    museum_info.delete()
    return redirect("/info")


@app.route("/delete-artefact/<int:index>", methods=["POST", "GET"])
@login_required
def delete_artefact(index):
    if current_user.role != "Admin":
        return redirect("/")
    artefacts3 = Artefact.query.get(index)
    artefacts3.delete()
    return redirect("/artefacts")


@app.route("/")
def home():
    muz_info = [
        {
            "img": "Tbilisi.jpg",
            "info": "ეს არის საქართველოს დედაქალაქი თბილისი, ზედა მარცხენა კუთხეში თქვენ დაინახავთ მთაწმინდას,"
                    "სადაც არის განლაგებული პარკი ბომბორა, თბილისის ანზა, ციხე ნარიყალა და ბევრი სხვა."
                    "ქვემო ნაწილი სავსეა ძველი თბილისის სახლებით, აბანოებით და ა.შ. , ასევე დაინახავდით"
                    " მდინარე მტკვარს და მის ცნობილ შუშის ხიდს.", "drp1": "Georgian National Museum",
            "drp2": "Dadiani Palace Museum",
            "drp3": "Georgian Museum of Fine Arts"}
    ]
    muz_info2 = [
        {
            "img": "Paris.jpg",
            "info": "ეს არის საფრანგეთის დედაქალაქი პარიზი. წინ თქვენ ხედავთ მსოფლიოში ცნობილ ეიფელის კოშკს, "
                    "ქვემოთ განლაგებული პარიზის ულამაზეს ქუჩებს და ა.შ.",
            "drp1": "Louvre Museum", "drp2": "Palace of Versailles", "drp3": "Centre Pompidou-Metz"}
    ]
    muz_info3 = [
        {
            "img": "Cairo.jpg",
            "info": "ეს არის ეგვიპტის დედაქალაქი კაირო, დედაქალაქის უმეტეს ნაწილზე გაედინება მდინარე ნილე.",
            "drp1": "The Egyptian Museum in Cairo", "drp2": "The Coptic Museum", "drp3": "Prince Mohamed Ali Palace"}
    ]

    return render_template("Home.html", info=muz_info, info2=muz_info2, info3=muz_info3, imgs=bottom_img,
                           logo=tbc)


@app.route("/add_museum", methods=["POST", "GET"])
@login_required
def add_museum():
    if current_user.role != "Admin":
        return redirect("/")
    form = AddMuseumForm()
    if form.validate_on_submit():
        new_museum = Museum(title=form.title.data, img=form.img.data.filename, info=form.info.data,
                            country=form.country.data)
        new_museum.create()

        file_dir = path.join(app.root_path, "static", form.img.data.filename)
        form.img.data.save(file_dir)
        return redirect("/info")

    return render_template("add-museum.html", imgs=bottom_img, logo=tbc, form=form)


@app.route("/comment", methods=["POST", "GET"])
@login_required
def add_comment():
    comment_info = Commentaries.query.all()
    form = AddCommentForm()
    if form.validate_on_submit():
        new_comment = Commentaries(username=form.username.data, comment=form.comment.data)
        new_comment.create()
        return redirect("/comment")
    return render_template("add-comment.html", form=form, comment_info=comment_info)


@app.route("/add_artefact", methods=["POST", "GET"])
@login_required
def add_artefact():
    if current_user.role != "Admin":
        return redirect("/")
    form = AddArtefactForm()
    if form.validate_on_submit():
        new_artefact = Artefact(title=form.title.data, img=form.img.data.filename, info=form.info.data,
                                artefact_museum=form.artefact_museum.data)
        new_artefact.create()

        file_dir = path.join(app.root_path, "static", form.img.data.filename)
        form.img.data.save(file_dir)
        return redirect("/artefacts")

    return render_template("add-artefact.html", imgs=bottom_img, logo=tbc, form=form)


@app.route("/contact", methods=["POST", "GET"])
def contacts():
    contact_info = [
        {"top-name": "მობილური", "name": "(+995) 123456789", "info": "ოპერატორების სამუშაო დრო 09:00-დან 21:00-მდე",
         "img": "Interior-National-Gallery-of-Art-Washington-DC.webp"},
        {"top-name": "მეილი", "name": "MUSEUMS.s@gmail.com", "info": "თუ რაიმე პრობლემა შეგექმნათ დაგვიკავშირდით",
         "img": "Random-museum.jpg"},
        {"top-name": "მუზეუმები", "name": "-------", "info": "ეწვიეთ მსოფლიო მუზეუმებს ფოტოს დაჭერით |",
         "img": "Pictures-museum.webp"},
        {"top-name": "დახმარება", "name": "-------", "info": "დამატებითი ინფორაციისთვის ეწვიეთ ჩვენს ფილიალს",
         "img": "Statues-museums.jpg"}
    ]
    form = UserOpinion()
    if form.validate_on_submit():
        new_opinion = Opinion(opinion=form.opinion.data)
        new_opinion.create()
        return redirect("/contact")
    return render_template("contact.html", imgs=bottom_img, contact_info=contact_info, logo=tbc, form=form)


@app.route("/register", methods=["GET", "POST"])
def registration():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data)
        user.create()

        return redirect("/login")
    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = AuthorizationForm()
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)

        return redirect("/")
    return render_template("authorization.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")


@app.route("/museums/<int:index>")
@login_required
def view_museums(index):
    museum_info = Museum.query.get(index)
    return render_template("view-museum.html", imgs=bottom_img, logo=tbc, museum_info=museum_info)



