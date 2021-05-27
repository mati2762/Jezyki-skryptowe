
export function createMap() {

    //Bloki 8, 24
    //Klocek 0
    let height = this.cameras.main._height;
    this.platforms = this.physics.add.staticGroup();

    let width = 30
    for (let i = 0; i < width; i++) {
        for (let j = 0; j < 5; j++) {
            if (j == 0) {
                this.platforms.create((i * 70) + 35, height - 35, 'platform');
            }
            else {
                this.platforms.create((i * 70) + 35, height - 35 + (j * 70), 'ground');
            }
        }

    }

    //sciana lewa
    for (let i = 1; i < 20; i++) {
        this.platforms.create(35, height - (i * 70) - 35, 'sheet', 24);
    }

    //sciana prawa
    for (let i = 1; i < 20; i++) {
        this.platforms.create(((width - 1) * 70) + 35, height - (i * 70) - 35, 'sheet', 24);
    }


    createPlatform.bind(this)(750, height - 200, 5);
    createPlatform.bind(this)(450, height - 350, 2);
    createPlatform.bind(this)(750, height - 500, 10);
}


function createPlatform(x: number, y: number, length: number) {
    this.platforms.create(x, y, 'platform_left');
    for (let i = 1; i < length; i++) {
        this.platforms.create(x + (i * 70), y, 'platform');
    }
    this.platforms.create(x + (length * 70), y, 'platform_right');
}