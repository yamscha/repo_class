# Unlike lists, dictionaries store information in pairs
# ---------------------------------------------------------------

# A list of actors
actors = ["Tom Cruise", "Angelina Jolie", "Kristen Stewart", "Denzel Washington"]

# A dictionary of an actor
actor = {"name": "Zac Efron"}
print(actor["name"])

# ---------------------------------------------------------------

# A dictionary can contain multiple pairs of information
actress = {"name": "Anna Kendrick", 
           "genre": "Musicals", 
           "country": "United States"}

# ---------------------------------------------------------------

# A dictionary can contain multiple types of information
another_actor = {"name": "Sylvester Stallone", 
                 "age": 62, 
                 "goes to the gym": True, 
                 "best movies": ["Creed", "Rocky", "Rocky 5 (haha, just kidding)"]}
print(another_actor["name"] + " was in  " + another_actor["best movies"][0])
# ---------------------------------------------------------------

# A dictionary can even contain another dictionary
film = {"title": "Interstellar", 
        "revenue": {"United States":360, 
                     "China":250, 
                     "United Kingdom":73}}
print(film["title"] + " made " + "$" + str(film["revenue"]["United States"]) + "m in the US.")
# ---------------------------------------------------------------

#modify
my_dictionary = {"studs": ['Charles', "alan", "ray",'eddy' ]}
list_of_studs = my_dictionary["studs"]
idx_of_ray =list_of_studs.index("ray") 
list_of_studs[idx_of_ray] = "mayur"
print(my_dictionary)