from obstacle import *

objects = [[] for _ in range(5)]
collision_pairs = {}

def add_object(o, depth = 0):
    objects[depth].append(o)

def add_objects(ol, depth = 0):
    objects[depth] += ol


def update():
    for layer in objects:
        for o in layer:
            if hasattr(o, 'update'):  # 객체가 update 메서드를 가지고 있는지 확인
                o.update()


def render():
    for layer in objects:
        for o in layer:
            if hasattr(o, 'draw'):
                o.draw()

def is_collision_object(o):
    for layer in objects:
        for obj in layer:
            if hasattr(o, 'obstacle_type') and hasattr(obj, 'obstacle_type'):
                # 모두 Obstacle 클래스에 obstacle_type 속성이 있는 경우
                if o.obstacle_type == obj.obstacle_type:
                    return True
            elif o == obj:
                # 기타 객체들은 직접 비교
                return True
    return False
def remove_collision_object(o):
    for pairs in collision_pairs.values():
        if o in pairs[0]:
            pairs[0].remove(o)
        if o in pairs[1]:
            pairs[1].remove(o)


def remove_object(o):
    for layer in objects:
        if o in layer:
            layer.remove(o)
            remove_collision_object(o)
            del o
            print("Object removed")
            return
    raise ValueError('Cannot delete non-existing object')

def clear():
    for layer in objects:
        layer.clear()


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


def add_collision_pair(group, a, b):
    if group not in collision_pairs:
        print(f'Added new group {group}')
        collision_pairs[group] = [ [], [] ]
    if a:
        collision_pairs[group][0].append(a)
    if b:
        collision_pairs[group][1].append(b)


def handle_collisions():
    for group, pairs in collision_pairs.items():
        for a in pairs[0]:
            for b in pairs[1]:
                if collide(a, b):
                    a.handle_collision(group, b)
                    b.handle_collision(group, a)

