namespace SpriteKind {
    export const emerald = SpriteKind.create()
    export const fruit = SpriteKind.create()
    export const Nila = SpriteKind.create()
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile76`, function (sprite, location) {
    current_level += 1
    startlevel()
})
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    createtextmessage("       Hi I am Chloe   Avoid bananas and if you touch the banana then a bat will come and hurt me, jump on them to defeat them and collect the emeralds and rare nilas for the onward journey.")
})
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    game.reset()
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.fruit, function (sprite, otherSprite) {
    otherSprite.destroy()
    battt = sprites.create(img`
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
        `, SpriteKind.Enemy)
    animation.runImageAnimation(
    battt,
    assets.animation`battt`,
    50,
    true
    )
    battt.setPosition(Chloe.x + 80, Chloe.y - 80)
    battt.follow(Chloe)
    music.powerDown.play()
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile24`, function (sprite, location) {
    current_level += 1
    startlevel()
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (Chloe.vy == 0) {
        Chloe.vy = -135
    }
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile73`, function (sprite, location) {
    game.over(true)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`lava`, function (sprite, location) {
    game.over(false)
})
function createtextmessage (text: string) {
    projectile = sprites.createProjectileFromSide(img`
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
        `, 52, 52)
    story.spriteSayText(projectile, text)
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.Nila, function (sprite, otherSprite) {
    music.baDing.play()
    info.changeScoreBy(10)
    otherSprite.destroy()
    sprite.say("Yess", 900)
})
function startlevel () {
    scene.setBackgroundColor(9)
    scene.setBackgroundImage(assets.image`background`)
    if (current_level == 0) {
        tiles.setTilemap(tilemap`level1`)
    } else if (current_level == 1) {
        tiles.setTilemap(tilemap`level2`)
    } else if (current_level == 2) {
        tiles.setTilemap(tilemap`level3`)
    } else if (current_level == 3) {
        tiles.setTilemap(tilemap`level4`)
    } else if (current_level == 4) {
        tiles.setTilemap(tilemap`level5`)
    } else {
        game.over(true)
    }
    Chloe.ay = 350
    scene.cameraFollowSprite(Chloe)
    tiles.placeOnRandomTile(Chloe, assets.tile`myTile38`)
    info.setLife(6)
    for (let value of sprites.allOfKind(SpriteKind.Enemy)) {
        value.destroy()
    }
    for (let value of sprites.allOfKind(SpriteKind.emerald)) {
        value.destroy()
    }
    for (let value of sprites.allOfKind(SpriteKind.fruit)) {
        value.destroy()
    }
    for (let value of sprites.allOfKind(SpriteKind.Nila)) {
        value.destroy()
    }
    for (let value of tiles.getTilesByType(assets.tile`myTile38`)) {
        tiles.setTileAt(value, assets.tile`transparency16`)
    }
    for (let value2 of tiles.getTilesByType(assets.tile`myTile35`)) {
        Emerald = sprites.create(assets.image`emerald`, SpriteKind.emerald)
        animation.runImageAnimation(
        Emerald,
        [img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `],
        170,
        true
        )
        tiles.placeOnTile(Emerald, value2)
        tiles.setTileAt(value2, assets.tile`transparency16`)
    }
    for (let value3 of tiles.getTilesByType(assets.tile`myTile36`)) {
        Banana = sprites.create(img`
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
            `, SpriteKind.fruit)
        tiles.placeOnTile(Banana, value3)
        tiles.setTileAt(value3, assets.tile`transparency16`)
    }
    for (let value of tiles.getTilesByType(assets.tile`myTile60`)) {
        Nila = sprites.create(img`
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
            `, SpriteKind.Nila)
        animation.runImageAnimation(
        Nila,
        [img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `],
        170,
        true
        )
        tiles.placeOnTile(Nila, value)
        tiles.setTileAt(value, assets.tile`transparency16`)
    }
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile61`, function (sprite, location) {
    current_level += 1
    startlevel()
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.emerald, function (sprite, otherSprite) {
    music.baDing.play()
    info.changeScoreBy(1)
    otherSprite.destroy()
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    otherSprite.destroy()
    if (Chloe.y < otherSprite.y) {
        info.changeScoreBy(2)
        music.powerUp.play()
        sprite.say("Oh Yeah", 900)
    } else {
        info.changeLifeBy(-1)
        music.jumpDown.play()
        sprite.say("Ouch", 900)
    }
})
let Nila: Sprite = null
let Banana: Sprite = null
let Emerald: Sprite = null
let projectile: Sprite = null
let battt: Sprite = null
let Chloe: Sprite = null
let current_level = 0
current_level = 0
Chloe = sprites.create(img`
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
    `, SpriteKind.Player)
controller.moveSprite(Chloe, 100, 0)
startlevel()
info.setScore(0)
Chloe.say("Hey there please press \"W\" or up arrow on your keyboard", 6000)
game.onUpdate(function () {
    Chloe.setImage(img`
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
        `)
    if (Chloe.vy < 0) {
        Chloe.setImage(img`
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
            `)
    } else if (Chloe.x % 2 == 0) {
        Chloe.setImage(img`
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
            `)
    }
    if (Chloe.vx < 0) {
        Chloe.image.flipX()
    }
})
game.onUpdateInterval(500, function () {
	
})
