class Soundscape:
    def __init__(self, area_id, sounds=None):
        self.area_id = area_id
        self.sounds = sounds or []

    def add_sound(self, sound):
        if sound not in self.sounds:
            self.sounds.append(sound)

    def list_sounds(self):
        return self.sounds
