
enemies = {}

player = {}
player.x = 100
player.y = 595

enemiesBullets = {}

bullets = {}
bullets_generation_tick = 30
isGoingToOpositeDirection = false
distanceTraveled = 0
changesOfDirection = 0
bulletIndex = 1
enemyBulletIndex = 1

numberOfEnemiesInRow = 8
numberOfRowsWithEnemys = 6

isGameOver = false
isWin = false


function isOutOfEnemy()
	for it, enemy in pairs(enemies) do
		return false
	end
	return true
end


function removeUnnecessaryBullets()
	for it, bullet in pairs(bullets) do
		if bullet.body:getY() > 1000 or bullet.body:getY() < 0 then
			table.remove(bullets, it)
		end
	end
	for it, enemyBullet in pairs(enemiesBullets) do
		if enemyBullet.body:getY() > 1000 or enemyBullet.body:getY() < 0 then
			table.remove(enemiesBullets, it)
		end
	end
end


function enemyMoveDown()
	maxY = 0
	for it, enemy in pairs(enemies) do
		enemy.body:setY(enemy.body:getY() + 10)
		if enemy.body:getY() > maxY then
			maxY = enemy.body:getY()
		end
	end
	if maxY >= player.body:getY() - 20 then
		isGameOver = true
	end
end


function enemyMoving()
	move = 1
	if isGoingToOpositeDirection then
		move = -1
	end
	for it, enemy in pairs(enemies) do
		if enemy.isEvenRow then
			enemy.body:setX(enemy.body:getX() - move)
		else
			enemy.body:setX(enemy.body:getX() + move)
		end
	end
end


function createEnemy(posX, posY, id, isEvenRow, canShoot)
	enemy = {}
	enemy.timer = 0
	enemy.timeToShoot = math.random(100, 500)
	enemy.canShoot = canShoot
	enemy.isEvenRow = isEvenRow
	enemy.image = love.graphics.newImage('images/invader.png')
	enemy.body = love.physics.newBody(world, enemy.x,enemy.y, "static")
	enemy.body:setX(posX)
	enemy.body:setY(posY)
	enemy.body:setBullet(false)
	enemy.shape = love.physics.newRectangleShape(30,20)   
	enemy.f = love.physics.newFixture(enemy.body, enemy.shape)
	enemy.f:setUserData(id)
	enemy.f:setGroupIndex(1)
	table.insert(enemies, enemy)
end


function player:shoot()
	if bullets_generation_tick <= 0 then
		bullets_generation_tick = 15
		bullet = {}
		bullet.x = player.body:getX() + 23
		bullet.y = 565
		bullet.body = love.physics.newBody(world, bullet.x,bullet.y, "dynamic")
		bullet.body:setBullet(true)
		bullet.shape = love.physics.newRectangleShape(5,20)   
		bullet.f = love.physics.newFixture(bullet.body, bullet.shape)
		bullet.f:setUserData("PlayerBullet" .. bulletIndex)
		bullet.f:setGroupIndex(1)
		bulletIndex = bulletIndex + 1
		table.insert(bullets, bullet)
		love.audio.stop()
		love.audio.play(player_shoot_sound)
	end
end


function enemiesAtack()
	for it, enemy in pairs(enemies) do
		if enemy.canShoot then
			enemyShoot(enemy)
		end
	end
end


function enemyShoot(enemy)
	enemy.timer = enemy.timer + 1
	if enemy.timer >= enemy.timeToShoot then
		enemy.timer = 0
		enemyBullet = {}
		enemyBullet.x = enemy.body:getX() + 30
		enemyBullet.y = enemy.body:getY() + 50
		enemyBullet.body = love.physics.newBody(world, enemyBullet.x,enemyBullet.y, "dynamic")
		enemyBullet.body:setBullet(true)
		enemyBullet.shape = love.physics.newRectangleShape(5,20)   
		enemyBullet.f = love.physics.newFixture(enemyBullet.body, enemyBullet.shape)
		enemyBullet.f:setUserData("EnemyBullet" .. enemyBulletIndex)
		enemyBullet.f:setGroupIndex(2)
		enemyBullet.f:setCategory(2)
		enemyBullet.f:setMask(1)
		enemyBulletIndex = enemyBulletIndex + 1
		table.insert(enemiesBullets, enemyBullet)
	end
end


function love.load()
	world = love.physics.newWorld(0, 0, true)
	world:setCallbacks(beginContact, endContact, preSolve, postSolve)
	player.image = love.graphics.newImage('images/player.png')
	player.explose_shoot = love.audio.newSource('sounds/shoot.mp3','static')
	player.body = love.physics.newBody(world, player.x, player.y, "static")
	player.body:setX(player.x)
	player.body:setY(player.y)
	player.shape = love.physics.newRectangleShape(50,5)
	player.f = love.physics.newFixture(player.body, player.shape)
	player.f:setUserData("Player")
	player.f:setGroupIndex(2)
	player.f:setCategory(2)
	player.f:setMask(1)
	music = love.audio.newSource('sounds/music.mp3','static')
	player_shoot_sound = love.audio.newSource('sounds/shoot.mp3','static')
	--music:setLooping(true)
	--love.audio.play(music)
	index = 1
	isLastRow = false
	for j=0,(numberOfRowsWithEnemys - 1)*50,50 do
		if j == (numberOfRowsWithEnemys - 1)*50 then
			isLastRow = true
		end
		if j % 100 == 0 then
			for i=0,(numberOfEnemiesInRow - 1)*100,100 do
				createEnemy(i + 20, j, index, false, isLastRow)
				index = index + 1
			end
		else
			for i=0,(numberOfEnemiesInRow - 1)*100,100 do
				createEnemy(i + 50 + 20, j, index, true, isLastRow)
				index = index + 1
			end
		end
	end
end


function love.draw()
	love.graphics.setColor(1,1,1)
    for it, bullet in pairs(bullets) do
		love.graphics.polygon("fill", bullet.body:getWorldPoints(bullet.shape:getPoints()))
	end
	love.graphics.setColor(0.3,0.3,0.3)
	for it, enemyBullet in pairs(enemiesBullets) do
		love.graphics.polygon("fill", enemyBullet.body:getWorldPoints(enemyBullet.shape:getPoints()))
	end
	love.graphics.setColor(1,1,1)
	love.graphics.draw(player.image, player.body:getX()- 20, player.body:getY() - 15, 0, 0.3)
	--love.graphics.polygon("line", player.body:getWorldPoints(player.shape:getPoints()))
	
	for it, enemy in pairs(enemies) do
		love.graphics.draw(enemy.image, enemy.body:getX()-20, enemy.body:getY(), 0, 0.3)
		--love.graphics.polygon("line", enemy.body:getWorldPoints(enemy.shape:getPoints()))
	end
	
	if isWin or isGameOver then
		if isGameOver then
			love.graphics.setColor(1, 0, 0, 1)
			love.graphics.print("Game Over", 300, 250, 0, 4, 4)
		elseif isWin then
			love.graphics.setColor(0, 0, 1, 1)
			love.graphics.print("Winner", 300, 250, 0, 4, 4)
		end
	end
end


function love.update(dt)
	if isWin or isGameOver then
		return
	end
	world:update(dt)
	isWin = isOutOfEnemy()
	if love.keyboard.isDown('right') then
		if player.body:getX() > 750 then
			player.body:setX(750)
		end
		player.body:setX(player.body:getX() + 5)
	end
	if love.keyboard.isDown('left') then
		if player.body:getX() < 10 then
			player.body:setX(10)
		end
		player.body:setX(player.body:getX() - 5)
	end
	if love.keyboard.isDown('space') then
		player.shoot()
	end
	if love.keyboard.isDown('q') then
		love.event.quit()
	end

	for it, bullet in pairs(bullets) do
		bullet.body:applyForce(0, -500)
		--bullet.body:setY(bullet.body:getY() - 5)
	end
	
	for it, enemyBullet in pairs(enemiesBullets) do
		enemyBullet.body:applyForce(0, 200)
		--bullet.body:setY(bullet.body:getY() - 5)
	end
	
	if distanceTraveled >= 50 then
		if isGoingToOpositeDirection then
			isGoingToOpositeDirection = false
		else
			isGoingToOpositeDirection = true
		end
		distanceTraveled = 0
		changesOfDirection = changesOfDirection + 1
	end
	enemyMoving()
	if changesOfDirection >= 5 then
		enemyMoveDown()
		changesOfDirection = 0
	end
	distanceTraveled = distanceTraveled + 1
	bullets_generation_tick = bullets_generation_tick - 1
	
	enemiesAtack()
	removeUnnecessaryBullets()
end


function setNextEnemyToShoot(id)
	for it, enemy in pairs(enemies) do
		if enemy.f:getUserData() == id then
			enemy.canShoot = true
			return
		end
	end
end


function enemyRemove(id)
	for it, enemy in pairs(enemies) do
		if enemy ~= nil and enemy.f:isDestroyed()==false then
			if enemy.f:getUserData() == id then
				enemy.f:destroy()
				table.remove(enemies, it)
				if id - numberOfEnemiesInRow >= 1 then
					setNextEnemyToShoot(id - numberOfEnemiesInRow)
				end
				return 
			end
		end
	end
end


function bulletRemove(id)
	for it, bullet in pairs(bullets) do
		if bullet ~= nil and bullet.f:isDestroyed()==false then
			if bullet.f:getUserData() == id then
				bullet.f:destroy()
				table.remove(bullets, it)
				return 
			end
		end
	end
end


function beginContact(a, b, coll)
	if a:getGroupIndex() ~= b:getGroupIndex() then
		return;
	end
	if (a:getUserData() == "Player" and type(b:getUserData()) == "string" and string.find(b:getUserData(), "EnemyBullet") ~= nil)  or 
		(b:getUserData() == "Player" and type(a:getUserData()) == "string" and string.find(a:getUserData(), "EnemyBullet") ~= nil)  then
		isGameOver = true
	end
	if a:getBody():isBullet() and not b:getBody():isBullet() then
		enemyRemove(b:getUserData())
		bulletRemove(a:getUserData())
	elseif b:getBody():isBullet() and not a:getBody():isBullet()then
		enemyRemove(a:getUserData())
		bulletRemove(b:getUserData())
	end

end

function endContact(a, b, coll)
	
end

function preSolve(a, b, coll)
	
end

function postSolve(a, b, coll, normalimpulse, tangentimpulse)
	
end
