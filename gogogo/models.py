from google.appengine.ext import db

class Agency(db.Model):
	"""
		Public transportation agency
	"""
	name = db.StringListProperty()
	
	url = db.StringProperty()
	
	timezone = db.StringProperty()
	
	phone = db.StringProperty()

class Stops(db.Model):
	# An ID that uniquely identifies a stop or station. Multiple routes may use the same stop. 
	sid = db.StringProperty()
	
	# Optional field
	code = db.StringProperty()
	
	# name of the Stop (Multiple language)
	name = db.StringListProperty()
	
	desc = db.StringListProperty()

	# latitude and longitude value, it won't use the indexing function from BigTable. Use geohash instead
	latlng = db.GeoPtProperty()
	
	geohash = db.StringProperty()
	
	url = db.LinkProperty()
	
	location_type = db.IntegerProperty()
	
	parent_station = db.SelfReferenceProperty()
	
class Routes(db.Model):	
	rid = db.StringProperty()
	
	#agency = db.ReferenceProperty(agency)
	
	short_name = db.StringListProperty()
	
	long_name = db.StringListProperty()
	
	desc = db.StringListProperty()
	
	type = db.IntegerProperty()
	
	url = db.LinkProperty()
	
	color = db.StringProperty()
	
	text_color = db.StringProperty()