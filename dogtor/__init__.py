from flask import Flask, request

# Creates application, if requires further config, must be placed on this file
def create_app():
    app = Flask(__name__)

    # @app.route()  # Instance flask decorator
    # owners - Ok
    # pets - OK
    # species - Ok
    # users  - App´s Users | Vets
    # procedures - Ok
    users = [
        {
            "id": 1,
            "username": "rock",
            "email": "rock@gmail.com",
        },
        {
            "id": 2,
            "username": "arthur",
            "email": "arthur@gmail.com",
        },
        {
            "id": 3,
            "username": "chris",
            "email": "chris@gmail.com",
        },
    ]

    # Defining specific method functions, using single function
    @app.post("/users/auth")
    def auth():
        data = request.data
        return data

    # Users routes
    @app.route("/users/<int:user_id>", methods=["GET","PUT","DELETE"])
    @app.route("/users/", methods=["GET", "POST"])
    def users_endpoint(user_id=None):
        if user_id:
            found_user = None
            for user in users:
                if user["id"] == user_id:
                    found_user = user

            if request.method == "PUT":
                return {"detail": f"User {found_user['username']} modified"}
            if request.method == "DELETE":
                return {"detail": f"User {found_user['username']} deleted"}

            return found_user

        if request.method == "POST":
            data = request.data
            return {"detail": f"User {data['username']} created"}

        return users


    # Pets routes
    @app.route("/pets/<int:pet_id>", methods=["GET", "PUT", "DELETE"])
    @app.route("/pets/", methods=["GET", "POST"])
    def pets_endpoint(pet_id=None):
        if pet_id:
            found_pet = None
            for user in users:
                if user["id"] == pet_id:
                    found_pet = user

            if request.method == "PUT":
                return {"detail": f"Pet {found_pet['username']} modified"}
            if request.method == "DELETE":
                return {"detail": f"Pet {found_pet['username']} deleted"}

            return found_pet

        if request.method == "POST":
            data = request.data
            return {"detail": f"Pet {data['username']} created"}

        return users



    # Owners Routes
    @app.route("/owners/<int:owner_id>", methods=["GET", "PUT", "DELETE"])
    @app.route("/owners/", methods=["GET", "POST"])
    def owners_endpoint(owner_id=None):
        if owner_id:
            found_owner = None
            for user in users:
                if user["id"] == owner_id:
                    found_owner = user

            if request.method == "PUT":
                return {"detail": f"Owner {found_owner['username']} modified"}
            if request.method == "DELETE":
                return {"detail": f"Owner {found_owner['username']} deleted"}

            return found_owner

        if request.method == "POST":
            data = request.data
            return {"detail": f"Owner {data['username']} created"}

        return users




    # Species
    @app.route("/species/<int:specie_id>", methods=["GET", "PUT", "DELETE"])
    @app.route("/species/", methods=["GET", "POST"])
    def species_endpoint(specie_id=None):
        if specie_id:
            found_specie = None
            for user in users:
                if user["id"] == specie_id:
                    found_specie = user

            if request.method == "PUT":
                return {"detail": f"Specie {found_specie['username']} modified"}
            if request.method == "DELETE":
                return {"detail": f"Specie {found_specie['username']} deleted"}

            return found_specie

        if request.method == "POST":
            data = request.data
            return {"detail": f"Specie {data['username']} created"}

        return users




    # Procedures
    @app.route("/procedures/<int:procedure_id>", methods=["GET", "PUT", "DELETE"])
    @app.route("/procedures/", methods=["GET", "POST"])
    def procedures_endpoint(procedure_id=None):
        if procedure_id:
            found_procedure = None
            for user in users:
                if user["id"] == procedure_id:
                    found_procedure = user

            if request.method == "PUT":
                return {"detail": f"Procedure {found_procedure['username']} modified"}
            if request.method == "DELETE":
                return {"detail": f"Procedure {found_procedure['username']} deleted"}

            return found_procedure

        if request.method == "POST":
            data = request.data
            return {"detail": f"Procedure {data['username']} created"}

        return users


    return app
