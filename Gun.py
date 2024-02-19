class Gun:
    def __init__(self, name, ammo):
        self.name = name
        self.ammo = ammo

    def shoot(self):
        if self.ammo > 0:
            self.ammo -= 1
        else:
            raise Exception(f"{self.name} is out of ammo")

    def reload(self):
        if self.ammo > 0:
            self.ammo = 10 - self.ammo
            self.ammo += self.ammo
        else:
            self.ammo = self.ammo + 10
        return "Reloading"

    def is_empty(self):
        return self.ammo == 0
