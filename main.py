@namespace
class SpriteKind:
    emerald = SpriteKind.create()
    fruit = SpriteKind.create()
    Nila = SpriteKind.create()

def on_up_pressed():
    createtextmessage("       Hi I am Chloe   Avoid bananas and if you touch the banana then a bat will come and hurt me, jump on them to defeat them and collect the emeralds and rare nilas for the onward journey.")
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_b_pressed():
    game.reset()
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_on_overlap(sprite, otherSprite):
    global battt
    otherSprite.destroy()
    battt = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.enemy)
    animation.run_image_animation(battt, assets.animation("""
        battt
    """), 50, True)
    battt.set_position(Chloe.x + 80, Chloe.y - 80)
    battt.follow(Chloe)
sprites.on_overlap(SpriteKind.player, SpriteKind.fruit, on_on_overlap)

def on_overlap_tile(sprite, location):
    global current_level
    current_level += 1
    startlevel()
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile24
    """),
    on_overlap_tile)

def on_a_pressed():
    if Chloe.vy == 0:
        Chloe.vy = -135
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_overlap_tile2(sprite, location):
    game.over(False)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        lava
    """),
    on_overlap_tile2)

def createtextmessage(text: str):
    global projectile
    projectile = sprites.create_projectile_from_side(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        52,
        52)
    story.sprite_say_text(projectile, text)

def on_on_overlap2(sprite, otherSprite):
    info.change_score_by(10)
    otherSprite.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.Nila, on_on_overlap2)

def on_overlap_tile3(sprite, location):
    game.over(True, effects.confetti)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile57
    """),
    on_overlap_tile3)

def startlevel():
    global Emerald, Banana, Nila2
    scene.set_background_color(9)
    scene.set_background_image(assets.image("""
        background
    """))
    if current_level == 0:
        tiles.set_tilemap(tilemap("""
            level1
        """))
    elif current_level == 1:
        tiles.set_tilemap(tilemap("""
            level2
        """))
    elif current_level == 2:
        tiles.set_tilemap(tilemap("""
            level3
        """))
    else:
        game.over(True)
    Chloe.ay = 350
    scene.camera_follow_sprite(Chloe)
    tiles.place_on_random_tile(Chloe, assets.tile("""
        myTile38
    """))
    info.set_life(6)
    for value in sprites.all_of_kind(SpriteKind.enemy):
        value.destroy()
    for value2 in sprites.all_of_kind(SpriteKind.emerald):
        value2.destroy()
    for value3 in sprites.all_of_kind(SpriteKind.fruit):
        value3.destroy()
    for value4 in sprites.all_of_kind(SpriteKind.Nila):
        value4.destroy()
    for value5 in tiles.get_tiles_by_type(assets.tile("""
        myTile38
    """)):
        tiles.set_tile_at(value5, assets.tile("""
            transparency16
        """))
    for value22 in tiles.get_tiles_by_type(assets.tile("""
        myTile35
    """)):
        Emerald = sprites.create(assets.image("""
            emerald
        """), SpriteKind.emerald)
        animation.run_image_animation(Emerald,
            [img("""
                    . . . . . . 6 6 6 . . . . . . . 
                                . . . . . 6 7 7 7 6 . . . . . . 
                                . . . . 6 9 7 7 7 7 6 . . . . . 
                                . . . 6 9 7 7 7 7 7 7 6 . . . . 
                                . . 6 9 7 7 7 7 7 7 7 7 6 . . . 
                                . . 6 9 7 7 7 7 7 7 7 7 6 . . . 
                                . . 6 7 7 7 7 7 7 7 7 7 6 . . . 
                                . . 6 7 7 7 7 7 7 7 7 7 6 . . . 
                                . . 6 7 7 7 7 7 7 7 7 7 6 . . . 
                                . . 6 7 7 7 7 7 7 7 7 7 6 . . . 
                                . . 6 8 7 7 7 7 7 7 7 7 6 . . . 
                                . . 6 8 8 7 7 7 7 7 7 7 6 . . . 
                                . . . 6 8 8 7 7 7 7 7 6 . . . . 
                                . . . . 6 8 8 7 7 7 6 . . . . . 
                                . . . . . 6 8 7 7 6 . . . . . . 
                                . . . . . . 6 6 6 . . . . . . .
                """),
                img("""
                    . . . . . . 6 6 6 . . . . . . . 
                                . . . . . 6 7 7 7 6 . . . . . . 
                                . . . . 6 9 7 7 7 7 6 . . . . . 
                                . . . . 6 7 7 7 7 7 6 . . . . . 
                                . . . 6 9 7 7 7 7 7 7 6 . . . . 
                                . . . 6 9 7 7 7 7 7 7 6 . . . . 
                                . . . 6 7 7 7 7 7 7 7 6 . . . . 
                                . . . 6 7 7 7 7 7 7 7 6 . . . . 
                                . . . 6 7 7 7 7 7 7 7 6 . . . . 
                                . . . 6 7 7 7 7 7 7 7 6 . . . . 
                                . . . 6 8 7 7 7 7 7 7 6 . . . . 
                                . . . 6 8 7 7 7 7 7 7 6 . . . . 
                                . . . . 6 8 7 7 7 7 6 . . . . . 
                                . . . . 6 8 8 7 7 7 6 . . . . . 
                                . . . . . 6 8 7 7 6 . . . . . . 
                                . . . . . . 6 6 6 . . . . . . .
                """),
                img("""
                    . . . . . . 6 6 6 . . . . . . . 
                                . . . . . 6 7 7 7 6 . . . . . . 
                                . . . . . 6 7 7 7 6 . . . . . . 
                                . . . . . 6 7 7 7 6 . . . . . . 
                                . . . . 6 9 7 7 7 7 6 . . . . . 
                                . . . . 6 9 7 7 7 7 6 . . . . . 
                                . . . . 6 7 7 7 7 7 6 . . . . . 
                                . . . . 6 7 7 7 7 7 6 . . . . . 
                                . . . . 6 7 7 7 7 7 6 . . . . . 
                                . . . . 6 7 7 7 7 7 6 . . . . . 
                                . . . . 6 8 7 7 7 7 6 . . . . . 
                                . . . . 6 8 7 7 7 7 6 . . . . . 
                                . . . . . 6 7 7 7 6 . . . . . . 
                                . . . . . 6 8 7 7 6 . . . . . . 
                                . . . . . 6 8 7 7 6 . . . . . . 
                                . . . . . . 6 6 6 . . . . . . .
                """),
                img("""
                    . . . . . . 6 6 6 . . . . . . . 
                                . . . . . 6 7 7 7 6 . . . . . . 
                                . . . . . 6 7 7 7 6 . . . . . . 
                                . . . . . 6 7 7 7 6 . . . . . . 
                                . . . . . 6 7 7 7 6 . . . . . . 
                                . . . . . 6 7 7 7 6 . . . . . . 
                                . . . . . 6 7 7 7 6 . . . . . . 
                                . . . . . 6 7 7 7 6 . . . . . . 
                                . . . . . 6 7 7 7 6 . . . . . . 
                                . . . . . 6 7 7 7 6 . . . . . . 
                                . . . . . 6 7 7 7 6 . . . . . . 
                                . . . . . 6 7 7 7 6 . . . . . . 
                                . . . . . 6 7 7 7 6 . . . . . . 
                                . . . . . 6 8 7 7 6 . . . . . . 
                                . . . . . 6 8 7 7 6 . . . . . . 
                                . . . . . . 6 6 6 . . . . . . .
                """),
                img("""
                    . . . . . . 6 6 6 . . . . . . . 
                                . . . . . 6 7 7 7 6 . . . . . . 
                                . . . . . 6 7 7 7 6 . . . . . . 
                                . . . . . 6 7 7 7 6 . . . . . . 
                                . . . . . 6 7 7 7 6 . . . . . . 
                                . . . . . 6 7 7 7 6 . . . . . . 
                                . . . . . 6 7 7 7 6 . . . . . . 
                                . . . . . 6 7 7 7 6 . . . . . . 
                                . . . . . 6 7 7 7 6 . . . . . . 
                                . . . . . 6 7 7 7 6 . . . . . . 
                                . . . . . 6 7 7 7 6 . . . . . . 
                                . . . . . 6 7 7 7 6 . . . . . . 
                                . . . . . 6 7 7 7 6 . . . . . . 
                                . . . . . 6 8 7 7 6 . . . . . . 
                                . . . . . 6 8 7 7 6 . . . . . . 
                                . . . . . . 6 6 6 . . . . . . .
                """),
                img("""
                    . . . . . . 6 6 6 . . . . . . . 
                                . . . . . 6 7 7 7 6 . . . . . . 
                                . . . . . 6 7 7 7 6 . . . . . . 
                                . . . . . 6 7 7 7 6 . . . . . . 
                                . . . . 6 9 7 7 7 7 6 . . . . . 
                                . . . . 6 9 7 7 7 7 6 . . . . . 
                                . . . . 6 7 7 7 7 7 6 . . . . . 
                                . . . . 6 7 7 7 7 7 6 . . . . . 
                                . . . . 6 7 7 7 7 7 6 . . . . . 
                                . . . . 6 7 7 7 7 7 6 . . . . . 
                                . . . . 6 8 7 7 7 7 6 . . . . . 
                                . . . . 6 8 7 7 7 7 6 . . . . . 
                                . . . . . 6 7 7 7 6 . . . . . . 
                                . . . . . 6 8 7 7 6 . . . . . . 
                                . . . . . 6 8 7 7 6 . . . . . . 
                                . . . . . . 6 6 6 . . . . . . .
                """),
                img("""
                    . . . . . . 6 6 6 . . . . . . . 
                                . . . . . 6 7 7 7 6 . . . . . . 
                                . . . . 6 9 7 7 7 7 6 . . . . . 
                                . . . . 6 7 7 7 7 7 6 . . . . . 
                                . . . 6 9 7 7 7 7 7 7 6 . . . . 
                                . . . 6 9 7 7 7 7 7 7 6 . . . . 
                                . . . 6 7 7 7 7 7 7 7 6 . . . . 
                                . . . 6 7 7 7 7 7 7 7 6 . . . . 
                                . . . 6 7 7 7 7 7 7 7 6 . . . . 
                                . . . 6 7 7 7 7 7 7 7 6 . . . . 
                                . . . 6 8 7 7 7 7 7 7 6 . . . . 
                                . . . 6 8 7 7 7 7 7 7 6 . . . . 
                                . . . . 6 8 7 7 7 7 6 . . . . . 
                                . . . . 6 8 8 7 7 7 6 . . . . . 
                                . . . . . 6 8 7 7 6 . . . . . . 
                                . . . . . . 6 6 6 . . . . . . .
                """),
                img("""
                    . . . . . . 6 6 6 . . . . . . . 
                                . . . . . 6 7 7 7 6 . . . . . . 
                                . . . . 6 9 7 7 7 7 6 . . . . . 
                                . . . 6 9 7 7 7 7 7 7 6 . . . . 
                                . . 6 9 7 7 7 7 7 7 7 7 6 . . . 
                                . . 6 9 7 7 7 7 7 7 7 7 6 . . . 
                                . . 6 7 7 7 7 7 7 7 7 7 6 . . . 
                                . . 6 7 7 7 7 7 7 7 7 7 6 . . . 
                                . . 6 7 7 7 7 7 7 7 7 7 6 . . . 
                                . . 6 7 7 7 7 7 7 7 7 7 6 . . . 
                                . . 6 8 7 7 7 7 7 7 7 7 6 . . . 
                                . . 6 8 8 7 7 7 7 7 7 7 6 . . . 
                                . . . 6 8 8 7 7 7 7 7 6 . . . . 
                                . . . . 6 8 8 7 7 7 6 . . . . . 
                                . . . . . 6 8 7 7 6 . . . . . . 
                                . . . . . . 6 6 6 . . . . . . .
                """)],
            170,
            True)
        tiles.place_on_tile(Emerald, value22)
        tiles.set_tile_at(value22, assets.tile("""
            transparency16
        """))
    for value32 in tiles.get_tiles_by_type(assets.tile("""
        myTile36
    """)):
        Banana = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . f . 
                            . . . . . . . . . . . . . . f f 
                            . . . . . . . . . . . . . f f f 
                            f f . . . . . . . . . . f f 4 f 
                            f 5 f . . . . . . . . . f 5 4 f 
                            f 5 4 f f f . . . . . f f 5 4 f 
                            . f 5 4 4 f f . . . f f 5 5 f . 
                            . f 5 5 5 5 4 f f f 4 5 5 4 f . 
                            . . f f 4 5 5 5 5 5 5 5 4 f f . 
                            . . . f f 4 5 5 5 5 4 4 f f . . 
                            . . . . f f 5 5 4 4 4 f f . . . 
                            . . . . . . f f f f f . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.fruit)
        tiles.place_on_tile(Banana, value32)
        tiles.set_tile_at(value32, assets.tile("""
            transparency16
        """))
    for value6 in tiles.get_tiles_by_type(assets.tile("""
        myTile60
    """)):
        Nila2 = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . f f . . . . . . . 
                            . . . . . . f 8 8 f . . . . . . 
                            . . . . . f 8 8 8 8 f . . . . . 
                            . . . . f 8 8 8 8 8 8 f . . . . 
                            . . . f 8 8 9 8 8 8 8 8 f . . . 
                            . . f 8 8 9 8 8 8 8 8 8 8 f . . 
                            . . f 8 9 8 8 8 8 8 8 8 8 f . . 
                            . . f 8 9 8 8 8 8 8 8 8 8 f . . 
                            . . f 8 9 8 8 8 8 8 8 8 8 f . . 
                            . . f 8 9 8 8 8 8 8 8 8 8 f . . 
                            . . f 8 9 8 8 8 8 8 8 8 8 f . . 
                            . . f 8 8 8 8 8 8 8 8 8 8 f . . 
                            . . . f 8 8 8 8 8 8 8 8 f . . . 
                            . . . . f 8 8 8 8 8 8 f . . . . 
                            . . . . . f f f f f f . . . . .
            """),
            SpriteKind.Nila)
        animation.run_image_animation(Nila2,
            [img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . f f . . . . . . . 
                                . . . . . . f 8 8 f . . . . . . 
                                . . . . . f 8 8 8 8 f . . . . . 
                                . . . . f 8 8 8 8 8 8 f . . . . 
                                . . . f 8 8 9 8 8 8 8 8 f . . . 
                                . . f 8 8 9 8 8 8 8 8 8 8 f . . 
                                . . f 8 9 8 8 8 8 8 8 8 8 f . . 
                                . . f 8 9 8 8 8 8 8 8 8 8 f . . 
                                . . f 8 9 8 8 8 8 8 8 8 8 f . . 
                                . . f 8 9 8 8 8 8 8 8 8 8 f . . 
                                . . f 8 9 8 8 8 8 8 8 8 8 f . . 
                                . . f 8 8 8 8 8 8 8 8 8 8 f . . 
                                . . . f 8 8 8 8 8 8 8 8 f . . . 
                                . . . . f 8 8 8 8 8 8 f . . . . 
                                . . . . . f f f f f f . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . f f . . . . . . . 
                                . . . . . . f 8 8 f . . . . . . 
                                . . . . . f 8 8 8 8 f . . . . . 
                                . . . . f 8 8 8 8 8 8 f . . . . 
                                . . . . f 8 9 8 8 8 8 f . . . . 
                                . . . f 8 9 8 8 8 8 8 8 f . . . 
                                . . . f 8 8 8 8 8 8 8 8 f . . . 
                                . . . f 8 8 8 8 8 8 8 8 f . . . 
                                . . . f 8 8 8 8 8 8 8 8 f . . . 
                                . . . f 8 8 8 8 8 8 8 8 f . . . 
                                . . . f 8 8 8 8 8 8 8 8 f . . . 
                                . . . f 8 8 8 8 8 8 8 8 f . . . 
                                . . . . f 8 8 8 8 8 8 f . . . . 
                                . . . . f 8 8 8 8 8 8 f . . . . 
                                . . . . . f f f f f f . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . f f . . . . . . . 
                                . . . . . . f 8 8 f . . . . . . 
                                . . . . . . f 8 8 f . . . . . . 
                                . . . . . f 8 8 8 8 f . . . . . 
                                . . . . . f 8 8 8 8 f . . . . . 
                                . . . . f 8 9 8 8 8 8 f . . . . 
                                . . . . f 8 8 8 8 8 8 f . . . . 
                                . . . . f 8 8 8 8 8 8 f . . . . 
                                . . . . f 8 8 8 8 8 8 f . . . . 
                                . . . . f 8 8 8 8 8 8 f . . . . 
                                . . . . f 8 8 8 8 8 8 f . . . . 
                                . . . . f 8 8 8 8 8 8 f . . . . 
                                . . . . . f 8 8 8 8 f . . . . . 
                                . . . . . f 8 8 8 8 f . . . . . 
                                . . . . . . f f f f . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . f f . . . . . . . 
                                . . . . . . f 8 8 f . . . . . . 
                                . . . . . . f 8 8 f . . . . . . 
                                . . . . . . f 8 8 f . . . . . . 
                                . . . . . . f 8 8 f . . . . . . 
                                . . . . . f 8 8 8 8 f . . . . . 
                                . . . . . f 8 8 8 8 f . . . . . 
                                . . . . . f 8 8 8 8 f . . . . . 
                                . . . . . f 8 8 8 8 f . . . . . 
                                . . . . . f 8 8 8 8 f . . . . . 
                                . . . . . f 8 8 8 8 f . . . . . 
                                . . . . . f 8 8 8 8 f . . . . . 
                                . . . . . . f 8 8 f . . . . . . 
                                . . . . . . f 8 8 f . . . . . . 
                                . . . . . . f f f f . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . f f . . . . . . . 
                                . . . . . . f 8 8 f . . . . . . 
                                . . . . . . f 8 8 f . . . . . . 
                                . . . . . . f 8 8 f . . . . . . 
                                . . . . . . f 8 8 f . . . . . . 
                                . . . . . . f 8 8 f . . . . . . 
                                . . . . . . f 8 8 f . . . . . . 
                                . . . . . . f 8 8 f . . . . . . 
                                . . . . . . f 8 8 f . . . . . . 
                                . . . . . . f 8 8 f . . . . . . 
                                . . . . . . f 8 8 f . . . . . . 
                                . . . . . . f 8 8 f . . . . . . 
                                . . . . . . f 8 8 f . . . . . . 
                                . . . . . . f 8 8 f . . . . . . 
                                . . . . . . f f f f . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . f f . . . . . . . 
                                . . . . . . f 8 8 f . . . . . . 
                                . . . . . . f 8 8 f . . . . . . 
                                . . . . . . f 8 8 f . . . . . . 
                                . . . . . . f 8 8 f . . . . . . 
                                . . . . . f 8 8 8 8 f . . . . . 
                                . . . . . f 8 8 8 8 f . . . . . 
                                . . . . . f 8 8 8 8 f . . . . . 
                                . . . . . f 8 8 8 8 f . . . . . 
                                . . . . . f 8 8 8 8 f . . . . . 
                                . . . . . f 8 8 8 8 f . . . . . 
                                . . . . . f 8 8 8 8 f . . . . . 
                                . . . . . . f 8 8 f . . . . . . 
                                . . . . . . f 8 8 f . . . . . . 
                                . . . . . . f f f f . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . f f . . . . . . . 
                                . . . . . . f 8 8 f . . . . . . 
                                . . . . . . f 8 8 f . . . . . . 
                                . . . . . f 8 8 8 8 f . . . . . 
                                . . . . . f 8 8 8 8 f . . . . . 
                                . . . . f 8 9 8 8 8 8 f . . . . 
                                . . . . f 8 8 8 8 8 8 f . . . . 
                                . . . . f 8 8 8 8 8 8 f . . . . 
                                . . . . f 8 8 8 8 8 8 f . . . . 
                                . . . . f 8 8 8 8 8 8 f . . . . 
                                . . . . f 8 8 8 8 8 8 f . . . . 
                                . . . . f 8 8 8 8 8 8 f . . . . 
                                . . . . . f 8 8 8 8 f . . . . . 
                                . . . . . f 8 8 8 8 f . . . . . 
                                . . . . . . f f f f . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . f f . . . . . . . 
                                . . . . . . f 8 8 f . . . . . . 
                                . . . . . f 8 8 8 8 f . . . . . 
                                . . . . f 8 8 8 8 8 8 f . . . . 
                                . . . . f 8 9 8 8 8 8 f . . . . 
                                . . . f 8 9 8 8 8 8 8 8 f . . . 
                                . . . f 8 8 8 8 8 8 8 8 f . . . 
                                . . . f 8 8 8 8 8 8 8 8 f . . . 
                                . . . f 8 8 8 8 8 8 8 8 f . . . 
                                . . . f 8 8 8 8 8 8 8 8 f . . . 
                                . . . f 8 8 8 8 8 8 8 8 f . . . 
                                . . . f 8 8 8 8 8 8 8 8 f . . . 
                                . . . . f 8 8 8 8 8 8 f . . . . 
                                . . . . f 8 8 8 8 8 8 f . . . . 
                                . . . . . f f f f f f . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . f f . . . . . . . 
                                . . . . . . f 8 8 f . . . . . . 
                                . . . . . f 8 8 8 8 f . . . . . 
                                . . . . f 8 8 8 8 8 8 f . . . . 
                                . . . f 8 8 9 8 8 8 8 8 f . . . 
                                . . f 8 8 9 8 8 8 8 8 8 8 f . . 
                                . . f 8 9 8 8 8 8 8 8 8 8 f . . 
                                . . f 8 9 8 8 8 8 8 8 8 8 f . . 
                                . . f 8 9 8 8 8 8 8 8 8 8 f . . 
                                . . f 8 9 8 8 8 8 8 8 8 8 f . . 
                                . . f 8 9 8 8 8 8 8 8 8 8 f . . 
                                . . f 8 8 8 8 8 8 8 8 8 8 f . . 
                                . . . f 8 8 8 8 8 8 8 8 f . . . 
                                . . . . f 8 8 8 8 8 8 f . . . . 
                                . . . . . f f f f f f . . . . .
                """)],
            170,
            True)
        tiles.place_on_tile(Nila2, value6)
        tiles.set_tile_at(value6, assets.tile("""
            transparency16
        """))

def on_on_overlap3(sprite, otherSprite):
    info.change_score_by(1)
    otherSprite.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.emerald, on_on_overlap3)

def on_on_overlap4(sprite, otherSprite):
    otherSprite.destroy()
    if Chloe.y < otherSprite.y:
        info.change_score_by(2)
    else:
        info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap4)

Nila2: Sprite = None
Banana: Sprite = None
Emerald: Sprite = None
projectile: Sprite = None
battt: Sprite = None
Chloe: Sprite = None
current_level = 0
current_level = 0
Chloe = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . f . . . . . . . . . . . . . 
            . f f . . . . . . . f f . . . . 
            f f . . . . . . . . f f f f f . 
            f . . . . . . . . . f f f 5 f . 
            f f . f 1 f f f f 1 f f f f 3 . 
            . f f f f f 1 f f f 1 f f f f . 
            . . . f f 1 1 1 f f f f . . . . 
            . . . f . f . . f . f . . . . . 
            . . . f . f . . f . f . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
controller.move_sprite(Chloe, 100, 0)
startlevel()
info.set_score(0)
Chloe.say("Hey there please press \"W\" or up arrow on your keyboard",
    6000)

def on_on_update():
    Chloe.set_image(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . f . . . . . . . . . . . . . 
                . f f . . . . . . . f f . . . . 
                f f . . . . . . . . f f f f f . 
                f . . . . . . . . . f f f 5 f . 
                f f . f 1 f f f f 1 f f f f 3 . 
                . f f f f f 1 f f f 1 f f f f . 
                . . . f f 1 1 1 f f f f . . . . 
                . . . f . f . . f . f . . . . . 
                . . . f . f . . f . f . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . .
    """))
    if Chloe.vy < 0:
        Chloe.set_image(img("""
            . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . f f . . 
                        . . . . f f . . . . . . f f f f 
                        . . . . f . . . . . . . f f 5 f 
                        . . f f f . . . . . f f 1 f f 3 
                        . . f . . . . . . f f f f 1 f f 
                        . . f . . . . . . f f f f . . . 
                        . . f . . . . . f f 1 f f f f f 
                        . . f f . . . 1 f 1 1 1 f . . . 
                        . . . f f . f 1 f 1 f f f f f . 
                        . . . . f f f f f 1 . . . . . . 
                        . . . . . . f f f . . . . . . . 
                        . . . . . . f . f . . . . . . . 
                        . . . . . f f . f . . . . . . . 
                        . . . . . f . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
        """))
    elif Chloe.x % 2 == 0:
        Chloe.set_image(img("""
            . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . f . . . . . . . . . . . . . 
                        . f f . . . . . . . f f . . . . 
                        f f . . . . . . . . f f f f f . 
                        f . . . . . . . . . f f f 5 f . 
                        f f . f 1 f f f f 1 f f f f 3 . 
                        . f f f f f 1 f f f 1 f f f f . 
                        . . . f f 1 1 1 f f f f . . . . 
                        . . . f f . . . . f f . . . . . 
                        . . . f f . . . . f f . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
        """))
    if Chloe.vx < 0:
        Chloe.image.flip_x()
game.on_update(on_on_update)
