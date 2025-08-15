from ursina import *
from ursina.physics import *

app = Ursina()

# 🚗 Node-Beam Car Structure
class SoftBodyCar(Entity):
    def __init__(self, position=(0,1,0)):
        super().__init__()
        self.nodes = []
        self.beams = []
        self.position = position
        self.build_car()

    def build_car(self):
        # Create nodes
        for x in range(-1, 2):
            for y in range(0, 2):
                for z in range(-2, 3):
                    node = Entity(model='sphere', color=color.red, scale=0.2, position=self.position + Vec3(x, y, z)*0.5)
                    node.collider = 'sphere'
                    self.nodes.append(node)

        # Connect nodes with beams (springs)
        for i, a in enumerate(self.nodes):
            for j, b in enumerate(self.nodes):
                if i < j and distance(a.position, b.position) < 0.6:
                    beam = Entity(model='cube', color=color.gray, scale=(0.05, 0.05, distance(a.position, b.position)),
                                  position=(a.position + b.position)/2,
                                  rotation=(a.position, b.position))
                    self.beams.append((beam, a, b))

    def update(self):
        # Simulate spring tension
        for beam, a, b in self.beams:
            target_length = beam.scale_z
            current_length = distance(a.position, b.position)
            direction = (b.position - a.position).normalized()
            force = (current_length - target_length) * 0.5
            a.position += direction * force * time.dt
            b.position -= direction * force * time.dt

            # Update beam visuals
            beam.position = (a.position + b.position)/2
            beam.rotation = (a.position, b.position)
            beam.scale_z = distance(a.position, b.position)

        # Simple gravity
        for node in self.nodes:
            node.y -= 0.5 * time.dt

        # Ground collision
        for node in self.nodes:
            if node.y < 0.2:
                node.y = 0.2

# 🧱 Terrain and Obstacles
ground = Entity(model='plane', texture='white_cube', texture_scale=(20,20), scale=(20,1,20), collider='box', color=color.green)
ramp = Entity(model='cube', color=color.brown, scale=(5,0.5,10), position=(0,0.25,5), rotation_x=25)
wall = Entity(model='cube', color=color.gray, scale=(5,5,1), position=(0,2.5,15))

# 🎥 Camera
camera.position = (0, 10, -20)
camera.rotation_x = 30

# 🚗 Instantiate Car
car = SoftBodyCar()

# 🎮 Controls
def update():
    car.update()
    direction = Vec3(
        held_keys['d'] - held_keys['a'],
        0,
        held_keys['w'] - held_keys['s']
    ) * time.dt * 5

    for node in car.nodes:
        node.position += direction

    # Collision with wall triggers deformation
    for node in car.nodes:
        if node.intersects(wall).hit:
            node.scale *= 0.9
            node.color = color.orange

app.run()

