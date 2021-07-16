from code_challenges.stack_and_queue import Node

class CustomError(Exception):
  """Creates a custom error Exception"""
  pass

# --------------------------------------------------

class AnimalShelter:

  def __init__(self, first=None, last=None):
    """Creates an empty "animal shelter" instance"""
    self.first_animal = first
    self.last_animal = last
    self.animal_count = 0

  def enqueue(self, animal=None):
    """Creates an "animal" object (dog or cat)
    Adds it to the back of the shelter's "waiting list"
    If list is empty, it will set it as the first animal in the list"""
    if animal != "dog" or animal != "cat":
      raise CustomError("Must enter 'dog' or 'cat'")

    new_animal = Node(animal) # creates new animal object

    if self.first_animal is None: # if shelter is empty
      self.first_animal = new_animal # set new animal as first in list
      self.last_animal = new_animal # set new animal as last in list
    else: # if shelter is not empty
      self.last_animal.next = new_animal # set shelter's CURRENT last animal's "next" to new animal
      self.last_animal = new_animal # set new animal as last in list
    
    self.animal_count += 1 # increase shelter's animal count by 1

  def dequeue(self, pref):
    """Takes a "cat" or "dog" preference and returns first animal in shelter's waiting list that matches"""

    pref_animal = None # temp variable to hold first animal that matches preference

    if self.first_animal is None: #if there are no animal objects in AnimalShelter
      raise CustomError("The shelter currently has no animals")

    else: 
      loop_counter = self.animal_count # use the shelter's animal counter to determine how many times to loop through queue
      while loop_counter > 0: # while there are still animals we haven't checked in list
        while self.first_animal.value != pref: # while first animal in list doesn't match pref

          # ---- REMOVE ANIMAL FROM LIST AND MOVE IT TO THE BACK----
          not_pref = self.first_animal # set current first animal to temp variable
          self.first_animal = not_pref.next # set next animal to first in list
          self.last_animal.next = not_pref # set current last animal's "next" to the not-preferred animal
          self.last_animal = not_pref # set not-preferred animal to last in list





        # if self.first_animal.value != pref:
        #   not_preferred = self.first_animal # temp variable to hold animal not matching preference
        #   self.first_animal = not_preferred.next

        #   self.last_animal.next = not_preferred
        #   self.last 
      


# ---------------------------------------------