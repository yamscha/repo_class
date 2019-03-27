# Create and use a database called "Dumpster_DB"
use Dumpster_DB

# Create the "divers" collection and then insert a couple documents into it
db.divers.insert({"name":"Davey", "yearsDiving":10, "stillDiving":"True", "bestFinds":["Flat Screen", "Ruby Collar", "$100"]})

db.divers.insert({"name":"Jeanie", "yearsDiving":1, "stillDiving":"True", "bestFinds":["Movie Theater Chairs", "Music Box"]})

db.divers.insert({"name":"Boppo", "yearsDiving":5, "stillDiving":"True", "bestFinds":["Half-Eaten Hamburger", "Some Goop"]})

# Update 'yearsDiving' so that it is one year higher for each diver
db.divers.Update({"name":"Davey"},{$set:{"yearsDiving":11}})
db.divers.Update({"name":"Jeanie"},{$set:{"yearsDiving":2}})
db.divers.Update({"name":"Boppo"},{$set:{"yearsDiving":6}})

# Update 'stillDiving' to False for Davey
db.divers.Update({"name":"Davey"},{$set:{"stillDiving":"False"}})

# Add a new value to Jeanie's "bestFinds"
db.divers.Update({"name":"Jeanie"},{$push:{"bestFinds":"Mona Lisa"}})

# Remove Boppo from the collection
db.divers.remove({"name":"Boppo"})