


var cursors;
export function playerLoad() {
    let height = this.cameras.main._height;
    this.player = this.physics.add.sprite(550, height - 130, 'player');


    this.player.setBounce(0);

    this.anims.create({
        key: 'move',
        frames: this.anims.generateFrameNumbers('player', { start: 9, end: 10 }),
        frameRate: 10,
        repeat: -1
    });

    this.anims.create({
        key: 'jump',
        frames: [{ key: 'player', frame: 8 }],
        frameRate: 20
    });

    this.anims.create({
        key: 'turn',
        frames: [{ key: 'player', frame: 23 }],
        frameRate: 20
    });


    cursors = this.input.keyboard.createCursorKeys();
    this.physics.add.collider(this.player, this.platforms);
    this.cameras.main.startFollow(this.player, true, 0.08, 0.08);
    this.physics.add.overlap(this.player, this.kolce, gameOver.bind(this), null, this);
    this.physics.add.overlap(this.player, this.meta, win.bind(this), null, this);
}

let right = true;
export function playerUpdate() {

    if (right) {
        this.player.setFlipX(false)
    } else {
        this.player.setFlipX(true)
    }

    if (cursors.left.isDown) {
        right = false;
        this.player.setVelocityX(-160);
        this.player.anims.play('move', true);
    }
    else if (cursors.right.isDown) {
        right = true;
        this.player.setVelocityX(160);
        this.player.anims.play('move', true);
    }
    else {
        this.player.setVelocityX(0);
        this.player.anims.play('turn');
    }

    if (cursors.space.isDown && this.player.body.touching.down) {
        this.player.setVelocityY(-330);
    }

    if (Math.abs(this.player.body.newVelocity.y) > 1) {
        this.player.anims.play('jump');
    }
}

function gameOver(player, star) {
    const screenCenterX = this.cameras.main.worldView.x + this.cameras.main.width / 2;
    const screenCenterY = this.cameras.main.worldView.y + this.cameras.main.height / 2;
    const gameOver = this.add.text(screenCenterX - 150, screenCenterY - 100, "Game Over", { fontFamily: 'Arial', fontSize: 64, color: '#ff0000' });
    gameOver.stroke = '#000000';
    gameOver.setFontSize(100);
    this.scene.pause();
}


function win(player, star) {
    const screenCenterX = this.cameras.main.worldView.x + this.cameras.main.width / 2;
    const screenCenterY = this.cameras.main.worldView.y + this.cameras.main.height / 2;
    const gameOver = this.add.text(screenCenterX - 150, screenCenterY - 100, "You Win", { fontFamily: 'Arial', fontSize: 64, color: '#00ff00' });
    gameOver.stroke = '#000000';
    gameOver.setFontSize(100);
    this.scene.pause();
}