class Enemy:
    def __init__(self, **kwargs):
        self.dt = {**kwargs}

    def get_enemy(self):
        return self.dt