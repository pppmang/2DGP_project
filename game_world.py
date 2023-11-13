objects = [[] for _ in range(4)]

# fill here
# 충돌 그룹 정보를 DICTIONARY 로 표현.
collision_pairs = {} # { 'boy:ball' : [boy], [ball1, ball2,.....] }


def add_object(o, depth = 0):
    objects[depth].append(o)


def add_objects(ol, depth = 0):
    objects[depth] += ol


def update():
    for layer in objects:
        for o in layer:
            o.update()


def render():
    for layer in objects:
        for o in layer:
            o.draw()


# fill here
def add_collision_pairs(group, a, b):   # add_collision_pair('boy:ball', None, ball)
    if group not in collision_pairs:    # DICTIONARY 에 키 group 이 존재하지 않음.
        print(f'New Group {group} added...')
        collision_pairs[group] = [[], []]
    if a:
        collision_pairs[group][0].append(a)
    if b:
        collision_pairs[group][1].append(b)


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
            del o       # 완전히 없애기 위함.
            return
    raise ValueError('Cannot delete non existing object')


def clear():
    for layer in objects:
        layer.clear()


# fill here
def collide(a, b):      # 강의자료 p.10 처럼 코드 작성
    la, ba, ra, ta = a.get_bb()
    lb, bb, rb, tb = b.get_bb()

    if la > rb: return False
    if ra < lb: return False
    if ta < bb: return False
    if ba > tb: return False

    return True


def handle_collisions():
    for group, pairs in collision_pairs.items():    # key와 value 가 같이 나오게 된다.
        for a in pairs[0]:
            for b in pairs[1]:
                if collide(a, b):
                    a.handle_collision(group, b)
                    b.handle_collision(group, a)
