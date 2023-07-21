class DataSource:
    def __init__(self):
        self.objects = {
            1: {'id': 1, 'name': 'Object1', 'owner_id': 100},
            2: {'id': 2, 'name': 'Object2', 'owner_id': 200},
            # Add more objects here
        }

    def get_object_by_id(self, obj_id):
        return self.objects.get(obj_id)
