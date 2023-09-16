from app.databases.postgres import postgres_connection
db = postgres_connection.db


class Continent(db.Model):
    __tablename__ = 'continents'

    continent_id = db.Column(db.Integer, primary_key=True)
    continent_name = db.Column(db.String(255), nullable=False)

    def __init__(self, continent_name):
        self.continent_name = continent_name

    def __repr__(self):
        return f"<Continent {self.continent_name}>"


class Country(db.Model):
    __tablename__ = 'countries'

    country_id = db.Column(db.Integer, primary_key=True)
    country_name = db.Column(db.String(255), nullable=False)
    continent_id = db.Column(db.Integer, db.ForeignKey('continents.continent_id'), nullable=False)
    description = db.Column(db.Text)
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)

    # Define the relationship to the Continent model
    continent = db.relationship("Continent", back_populates="countries")

    def __init__(self, country_name, continent_id, description=None, longitude=None, latitude=None):
        self.country_name = country_name
        self.continent_id = continent_id
        self.description = description
        self.longitude = longitude
        self.latitude = latitude

    def __repr__(self):
        return f"<Country {self.country_name}>"


class Province(db.Model):
    __tablename__ = 'provinces'

    province_id = db.Column(db.Integer, primary_key=True)
    province_name = db.Column(db.String(255), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.country_id'), nullable=False)
    description = db.Column(db.Text)
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)

    # Define the relationship to the Country model
    country = db.relationship("Country", back_populates="provinces")

    # Add a one-to-many relationship to Destination
    destinations = db.relationship("Destination", back_populates="province")

    def __init__(self, province_name, country_id, description=None):
        self.province_name = province_name
        self.country_id = country_id
        self.description = description

    def __repr__(self):
        return f"<Province {self.province_name}>"


class Destination(db.Model):
    __tablename__ = 'destinations'

    destination_id = db.Column(db.Integer, primary_key=True)
    destination_name = db.Column(db.String(255), nullable=False)
    province_id = db.Column(db.Integer, db.ForeignKey('provinces.province_id'), nullable=False)
    description = db.Column(db.Text)
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)
    address = db.Column(db.String(255))
    things_to_do = db.Column(db.JSON)

    # Define the relationships to the Province model
    province = db.relationship("Province", back_populates="destinations")

    # Define the one-to-many relationship with DestinationImages
    images = db.relationship("DestinationImages", back_populates="destination")

    def __init__(self, destination_name, province_id=None, description=None, things_to_do=None):
        self.destination_name = destination_name
        self.province_id = province_id
        self.description = description
        self.things_to_do = things_to_do

    def __repr__(self):
        return f"<Destination {self.destination_name}>"


class DestinationImages(db.Model):
    __tablename__ = 'destination_images'

    image_id = db.Column(db.Integer, primary_key=True)
    destination_id = db.Column(db.Integer, db.ForeignKey('destinations.destination_id'), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)

    # Define the relationship to the Destination model
    destination = db.relationship("Destination", back_populates="images")

    def __init__(self, destination_id, image_url, description=None):
        self.destination_id = destination_id
        self.image_url = image_url
        self.description = description

    def __repr__(self):
        return f"<DestinationImage {self.image_url}>"


class Place(db.Model):
    __tablename__ = 'places'

    place_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    address = db.Column(db.String(255))
    type_id = db.Column(db.Integer, db.ForeignKey('types.type_id'), nullable=False)

    # Define the relationship to the Type model
    type = db.relationship('Type', backref='places')

    def __init__(self, name, description, latitude, longitude, address, type_id):
        self.name = name
        self.description = description
        self.latitude = latitude
        self.longitude = longitude
        self.address = address
        self.type_id = type_id

    def __repr__(self):
        return f"<Place {self.place_name}>"


class Type(db.Model):
    __tablename__ = 'types'

    type_id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(255), nullable=False)
    type_description = db.Column(db.Text)

    def __init__(self, type_name):
        self.type_name = type_name

    def __repr__(self):
        return f"<Type {self.type_name}>"