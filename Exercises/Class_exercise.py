# Write code below 💖

class Pokemon:
  def __init__(self, entry, name, types, description, is_caught, height, ability):
    self.entry = entry
    self.name = name
    self.types = types
    self.description = description
    self.is_caught = is_caught
    self.height = height
    self.ability = ability

  def speak(self):
    print(self.name *2)

  def display_details(self):
    print("Entry Number: " + str(self.entry) + "\n"
    "Name: " + self.name + "\n"
    "Type: " + self.types + "\n"
    "Description: " + self.description)

tangela = Pokemon(114, "Tangela", "Erba", "Le liane blu che nascondono il suo corpo sono rivestite di peli sottili.\nSi dice che soffra il solletico ", "Si", "1M", "Clorofilla/Fogliomanto")

tangela.display_details()
tangela.speak()