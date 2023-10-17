from flask import request
from . import api_blueprint
from . import models
from dogtor.db import  db


# Defining specific method functions, using single function
@api_blueprint.post("/users/auth")
def auth(request):
    data = request.data
    return data

               # General Routes
# owners - Ok
# pets - OK
# species - Ok
# users  - App´s Users | Vets
# procedures - Ok


# Users routes
@api_blueprint.route("/users/<int:user_id>", methods=["GET","PUT","DELETE"])
@api_blueprint.route("/users/", methods=["GET", "POST"])
def users_endpoint(user_id=None):
    try:
        data = request.get_json()
    except:
        pass

    if user_id is not None:
        users = models.User.query.get_or_404(user_id, 'User not found!!')

        if request.method == 'GET':
            return {
                    "id": users.id,
                    "username": users.username,
                    "email": users.email,
                    }

        if request.method == 'PUT':
            users.username = data['username']
            users.email = data['email']
            db.session.commit()
            return {"detail": f"User {users.email} was modified!!"}


    if request.method == 'GET':
        users_all = models.User.query.all()
        # Returning object stored on dict using list comprehension
        return [{
            "id": user.id,
            "username": user.username,
            "email": user.email,
        } for user in users_all]

    if request.method == "POST":
        # Creating object
        user_instance = models.User(
                                        username=data["username"],
                                        email=data["email"],
                                        )
        # Creating DB connection, and creating record
        db.session.add(user_instance)
        # Applying Changes
        db.session.commit()
        return {"detail":f"User {user_instance.email} created successfully!!"}


    if request.method == "DELETE":
        # Checking specie exist
        users = models.User.query.get_or_404(user_id, "User not Found!!")
        # Passing specie object to be deleted
        db.session.delete(users)
        # Committing changes
        db.session.commit()

        return {"detail": f"User {users.email} deleted successfully!!"}




# Pets routes
@api_blueprint.route("/pets/<int:pet_id>", methods=["GET", "PUT", "DELETE"])
@api_blueprint.route("/pets/", methods=["GET", "POST"])
def pets_endpoint(pet_id=None):
    try:
        data = request.get_json()
    except:
        pass

    if pet_id is not None:
        pets = models.Pet.query.get_or_404(pet_id, 'Owner not found!!')

        if request.method == 'GET':
            return {
                    "id": pets.id,
                    "name": pets.name,
                    "owner_id": pets.owner_id,
                    "age": pets.age,
                    "specie_id": pets.specie_id,
                    "record_id": pets.record_id
                    }

        if request.method == 'PUT':
            pets.first_name = data['first_name']
            pets.last_name = data['last_name']
            pets.phone = data['phone']
            pets.mobile = data['mobile']
            pets.email = data['email']
            db.session.commit()
            return {"detail": f"Pets {pets.email} was modified!!"}


    if request.method == 'GET':
        pets_all = models.Pet.query.all()
        # Returning object stored on dict using list comprehension
        return [{
            "id": specie.id,
            "first_name": specie.first_name,
            "last_name": specie.last_name,
            "phone": specie.phone,
            "mobile": specie.mobile,
            "email": specie.email
        } for specie in pets_all]

    if request.method == "POST":
        # Creating object
        pet_instance = models.Pet(
                                        first_name=data["first_name"],
                                        last_name=data["last_name"],
                                        phone = data["phone"],
                                        mobile=data["mobile"],
                                        email=data["email"]
                                        )
        # Creating DB connection, and creating record
        db.session.add(pet_instance)
        # Applying Changes
        db.session.commit()
        return {"detail":f"Pet {pet_instance.email} created successfully!!"}

    if request.method == "DELETE":
        # Checking specie exist
        pets = models.Pet.query.get_or_404(pet_id, "Pet not Found!!")
        # Passing specie object to be deleted
        db.session.delete(pets)
        # Committing changes
        db.session.commit()

        return {"detail": f"Pet {pets.email} deleted successfully!!"}





# Owners Routes
@api_blueprint.route("/owners/<int:owner_id>", methods=["GET", "PUT", "DELETE"])
@api_blueprint.route("/owners/", methods=["GET", "POST"])
def owners_endpoint(owner_id=None):
    try:
        data = request.get_json()
    except:
        pass

    if owner_id is not None:
        owners = models.Owner.query.get_or_404(owner_id, 'Owner not found!!')

        if request.method == 'GET':
            return {
                    "id": owners.id,
                    "first_name": owners.first_name,
                    "last_name": owners.last_name,
                    "phone": owners.phone,
                    "mobile": owners.mobile,
                    "email": owners.email
                    }

        if request.method == 'PUT':
            owners.first_name = data['first_name']
            owners.last_name = data['last_name']
            owners.phone = data['phone']
            owners.mobile = data['mobile']
            owners.email = data['email']
            db.session.commit()
            return {"detail": f"Owner {owners.email} was modified!!"}


    if request.method == 'GET':
        owner_all = models.Owner.query.all()
       # Returning object stored on dict using list comprehension
        return  [{
                    "id": owner.id,
                    "first_name": owner.first_name,
                    "last_name": owner.last_name,
                    "phone": owner.phone,
                    "mobile": owner.mobile,
                    "email": owner.email
                    }  for owner in owner_all]

    if request.method == "POST":
        # Creating object
        owner_instance = models.Owner(
                                        first_name=data["first_name"],
                                        last_name=data["last_name"],
                                        phone = data["phone"],
                                        mobile=data["mobile"],
                                        email=data["email"]
                                        )
        # Creating DB connection, and creating record
        db.session.add(owner_instance)
        # Applying Changes
        db.session.commit()
        return {"detail":f"Owner {owner_instance.email} created successfully!!"}


    if request.method == "DELETE":
        # Checking specie exist
        owners = models.Owner.query.get_or_404(owner_id, "Owner not Found!!")
        # Passing specie object to be deleted
        db.session.delete(owners)
        # Committing changes
        db.session.commit()

        return {"detail": f"Owner {owners.email} deleted successfully!!"}





# Species
@api_blueprint.route("/species/<int:specie_id>", methods=["GET", "PUT", "DELETE"])
@api_blueprint.route("/species/", methods=["GET", "POST"])
def species_endpoint(specie_id=None):
    # Using this to make it work when using GET request due body is empty.
    try:
        # Checking the request comes on json format
        data = request.get_json()
    except:
        pass
    if specie_id is not None:
        species = models.Specie.query.get_or_404(specie_id, "Specie not Found!!")
        if request.method == "GET":
            return {"id": species.id, "name":species.name}

        if request.method == 'PUT':
            species.name = data['name']
            db.session.commit()
            return {"detail": f"Specie {species.name} was modified!!"}

    if request.method == 'GET':
        species_all = models.Specie.query.all()
       # Returning object stored on dict using list comprehension
        return  [{"id":specie.id,"name":specie.name}  for specie in species_all]

    if request.method == "POST":
        # Creating object
        species_instance = models.Specie(name=data["name"])
        # Creating DB connection, and creating record
        db.session.add(species_instance)
        # Applying Changes
        db.session.commit()
        return {"detail":f"Specie {species_instance.name} created successful!!"}

    if request.method == "DELETE":
        # Checking specie exist
        species = models.Specie.query.get_or_404(specie_id, "Specie not Found!!")
        # Passing specie object to be deleted
        db.session.delete(species)
        # Committing changes
        db.session.commit()

        return {"detail": f"Specie  {species.email} deleted successfully!!"}


    # Procedures
@api_blueprint.route("/procedures/<int:procedure_id>", methods=["GET", "PUT", "DELETE"])
@api_blueprint.route("/procedures/", methods=["GET", "POST"])
def procedures_endpoint(record_id=None):
    try:
        # Checking the request comes on json format
        data = request.get_json()
    except:
        pass
    if record_id is not None:
        records = models.Record.query.get_or_404(record_id, "Record not Found!!")
        if request.method == "GET":
            return {"id": records.id, "name":records.name}

        if request.method == 'PUT':
            records.name = data['name']
            db.session.commit()
            return {"detail": f"Record {records.name} was modified!!"}

    if request.method == 'GET':
        records_all = models.Specie.query.all()
       # Returning object stored on dict using list comprehension
        return  [{"id":record.id,"name":record.name}  for record in records_all]

    if request.method == "POST":
        # Creating object
        record_instance = models.Record(name=data["name"])
        # Creating DB connection, and creating record
        db.session.add(record_instance)
        # Applying Changes
        db.session.commit()
        return {"detail":f"Record {record_instance.name} created successful!!"}

    if request.method == "DELETE":
        # Checking specie exist
        records = models.Record.query.get_or_404(record_id, "Record not Found!!")
        # Passing specie object to be deleted
        db.session.delete(records)
        # Committing changes
        db.session.commit()

        return {"detail": f"Record  {records.email} deleted successfully!!"}