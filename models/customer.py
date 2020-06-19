from flask_restplus import fields
def createCustomerSchema(api):

    reservation = api.model('Reservation', {
        'id_store' : fields.String('ID of the store.'),   
        'date': fields.Date(required=True, description='The availability date'),
        'time': fields.DateTime(required=True, description='The availability time')
    })

    customerModel = api.model('Customer', {
        'username' : fields.String(required=True, description='Username for the customer.'),
        'name' : fields.String(required=True,description='Name of the customer.'),
        'phone' : fields.String(required=True,description='Phone number for the customer.'),
        'password' : fields.String(required=True, description='Password for the user.'),
        'reservations':fields.List(fields.Nested(reservation, required=False, description='List of Reservations made by the customer'))
    })
    return customerModel

def deleteCustomerSchema(api):

    objectId= api.model('objectId',{
        "$oid": fields.String()
    })
    id=api.model('id',{
        "_id": fields.Nested(objectId)
    })
    return id


def getCustomerSchema(api):
    reservation = api.model('Reservation', {
        'id_store' : fields.String('ID of the store.'),   
        'date': fields.Date(required=True, description='The availability date'),
        'time': fields.DateTime(required=True, description='The availability time')
    })

    customerModel = api.model('Customer', {
        'username' : fields.String(required=True, description='Username for the customer.'),
        'name' : fields.String(required=True,description='Name of the customer.'),
        'phone' : fields.String(required=True,description='Phone number for the customer.'),
        'reservations':fields.List(fields.Nested(reservation, required=False, description='List of Reservations made by the customer'))
    })
    return customerModel

