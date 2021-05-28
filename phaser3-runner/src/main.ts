import 'Phaser'
import { createMap } from './map';
import { playerLoad, playerUpdate } from './player';

let config: Phaser.Types.Core.GameConfig = {
    type: Phaser.AUTO,
    width: "100%",
    height: "100%",
    physics: {
        default: 'arcade',
        arcade: {
            gravity: { y: 300 }
        }
    },
    scene: {
        preload: preload,
        create: create,
        update: update
    }
};

var game = new Phaser.Game(config);



function preload() {
    this.cameras.main.setBackgroundColor('#1F9EC8')
    this.load.image('platform', 'img/platformIndustrial_003.png');
    this.load.image('lampka', 'img/platformIndustrial_040.png');
    this.load.image('ground', 'img/platformIndustrial_005.png');
    this.load.image('platform_left', 'img/platformIndustrial_017.png');
    this.load.image('platform_right', 'img/platformIndustrial_018.png');
    this.load.image('kolce', 'img/platformIndustrial_052.png');
    this.load.spritesheet('sheet', 'img/platformIndustrial_sheet.png',
        { frameWidth: 70, frameHeight: 70 });

    this.load.spritesheet('player', 'img/player_tilesheet.png',
        { frameWidth: 80, frameHeight: 110 });

}


var player: Phaser.Physics.Arcade.Sprite;
var platforms: Phaser.Physics.Arcade.StaticGroup;
var kolce;
var meta;
var cursors;
function create() {
    createMap.bind(this)();
    playerLoad.bind(this)();

}

function update() {
    playerUpdate.bind(this)();
}