let position = player.position();
position = position.add(pos(10, 0, 0));



let widthX = randint(2, 20)
let widthY = randint(2, 30)
let height = randint(5, 8)
let floors = randint(0, 2)

buildHouse(position, widthX, widthY, height, floors)

function buildHouse(startPosition: Position, widthX: number, widthZ: number, height: number, floors: number = 0) {
    buildCube(startPosition, widthX, widthZ, height);
    for (let i = 0; i < floors; i++) {
        startPosition = startPosition.add(pos(0, height, 0))
        buildCube(startPosition, widthX, widthZ, height)
    }
    buildPiramide(startPosition.add(pos(-1, height + 1, -1)), widthX + 1, widthZ + 1);
}



function buildPiramide(startPosition: Position, widthX: number, widthZ: number) {
    let height = 0;
    while (widthX > 0 && widthZ > 0) {
        startPosition = startPosition.add(pos(1, 0, 1))
        for (let i = 0; i < widthX; i++) {
            for (let j = 0; j < widthZ; j++) {
                blocks.place(Block.PlanksDarkOak, world(startPosition.getValue(Axis.X) + i, startPosition.getValue(Axis.Y) + height, startPosition.getValue(Axis.Z) + j))
            }
        }
        widthX -= 2;
        widthZ -= 2;
        height += 1;
    }
}


function buildCube(startPosition: Position, widthX: number, widthZ: number, height: number) {
    let windowZ = randint(1, widthZ / 2)
    let windowX = randint(1, widthX / 2)

    for (let i = 0; i < widthX; i++) {
        for (let j = 0; j < widthZ; j++) {
            blocks.place(Block.PlanksAcacia, world(startPosition.getValue(Axis.X) + i, startPosition.getValue(Axis.Y), startPosition.getValue(Axis.Z) + j))
        }
    }

    for (let i = 0; i < widthX; i++) {
        for (let j = 0; j < height; j++) {
            if (j > 0 && i > (widthX / 2) - windowX && i < (widthX / 2) + windowX) {
                blocks.place(Block.Glass, world(startPosition.getValue(Axis.X) + i, startPosition.getValue(Axis.Y) + j, startPosition.getValue(Axis.Z)))

            } else {
                blocks.place(Block.Bricks, world(startPosition.getValue(Axis.X) + i, startPosition.getValue(Axis.Y) + j, startPosition.getValue(Axis.Z)))

            }
        }
    }

    for (let i = 0; i < widthX; i++) {
        for (let j = 0; j < height; j++) {
            if (j > 0 && i > (widthX / 2) - windowX && i < (widthX / 2) + windowX) {
                blocks.place(Block.Glass, world(startPosition.getValue(Axis.X) + i, startPosition.getValue(Axis.Y) + j, startPosition.getValue(Axis.Z) + widthZ))

            } else {
                blocks.place(Block.Bricks, world(startPosition.getValue(Axis.X) + i, startPosition.getValue(Axis.Y) + j, startPosition.getValue(Axis.Z) + widthZ))

            }
        }
    }

    for (let i = 0; i < widthZ; i++) {
        for (let j = 0; j < height; j++) {
            if (j > 0 && i > (widthZ / 2) - windowZ && i < (widthZ / 2) + windowZ) {
                blocks.place(Block.Glass, world(startPosition.getValue(Axis.X), startPosition.getValue(Axis.Y) + j, startPosition.getValue(Axis.Z) + i))
            } else {
                blocks.place(Block.Bricks, world(startPosition.getValue(Axis.X), startPosition.getValue(Axis.Y) + j, startPosition.getValue(Axis.Z) + i))

            }
        }
    }

    for (let i = 0; i <= widthZ; i++) {
        for (let j = 0; j < height; j++) {
            if (j > 0 && i > (widthZ / 2) - windowZ && i < (widthZ / 2) + windowZ) {
                blocks.place(Block.Glass, world(startPosition.getValue(Axis.X) + widthX, startPosition.getValue(Axis.Y) + j, startPosition.getValue(Axis.Z) + i))
            } else {
                blocks.place(Block.Bricks, world(startPosition.getValue(Axis.X) + widthX, startPosition.getValue(Axis.Y) + j, startPosition.getValue(Axis.Z) + i))
            }
        }
    }

    for (let i = 0; i <= widthX; i++) {
        for (let j = 0; j <= widthZ; j++) {

            blocks.place(Block.Bricks, world(startPosition.getValue(Axis.X) + i, startPosition.getValue(Axis.Y) + height, startPosition.getValue(Axis.Z) + j))

        }
    }
}