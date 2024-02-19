class Gun:
	def __init__(self, name, ammo):
		self.name = name
		self.ammo = ammo

	def shoot(self):
		if self.ammo > 0:
			return "Firing {self.name}"
			self.ammo -= 1
		else:
			return (f"{self.name} is out of ammo")

	def reload(self):
		if ammo > 0:
			 self. ammo = 10 -ammo
           		 self.ammo += ammo
		else:
			self.ammo = ammo += 10
		return "Reloading"
	
	def is_empty(self):
		return self.ammo == 0