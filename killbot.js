const mineflayer = require('mineflayer')
const { pathfinder, goals: { GoalFollow } } = require('mineflayer-pathfinder')

const bot = mineflayer.createBot({host: 'localhost', port: ***, username: 'Bot'})
const mcData = require('minecraft-data')(bot.version)
foundplayer = false
bot.loadPlugin(pathfinder)

function playerkill() {
  playerdead = false
  foundplayer = false
  const findloop = setInterval(() => {
    if (foundplayer !== true) {
      entity = bot.nearestEntity()
      if (entity !== null) {
        if (entity.type === 'player') {
          foundplayer = true
          clearInterval(findloop)
        }
      }
    }
  }, 10) 
    const killloop = setInterval(() => {
        if (playerdead === false) { 
          bot.pathfinder.setGoal(new GoalFollow(entity, 1))
          bot.on('goal_reached', () => {
            playerdead = false
            bot.attack(entity)
          })
          bot.on('entitySpawn', (entity) => { 
            playerdead = true
          })
        } else {
          clearInterval(killloop)
          bot.end() 
        }
    }, 500)
}

bot.on('spawn', () => {
  bot.chat("/clear @p")  
  bot.chat("/gamemode survival @a")  
  bot.chat('/give @p netherite_sword{Enchantments:[{id:"minecraft:sharpness",lvl:10},{id:"minecraft:fire_aspect",lvl:10}]} 1')
  bot.chat('/replaceitem entity @p armor.head minecraft:netherite_helmet{Enchantments:[{id:"minecraft:protection",lvl:10},{id:"minecraft:thorns",lvl:10}]} 1')
  bot.chat('/replaceitem entity @p armor.chest minecraft:netherite_chestplate{Enchantments:[{id:"minecraft:protection",lvl:10},{id:"minecraft:thorns",lvl:10}]} 1')
  bot.chat('/replaceitem entity @p armor.legs minecraft:netherite_leggings{Enchantments:[{id:"minecraft:protection",lvl:10},{id:"minecraft:thorns",lvl:10}]} 1')
  bot.chat('/replaceitem entity @p armor.feet minecraft:netherite_boots{Enchantments:[{id:"minecraft:protection",lvl:10},{id:"minecraft:thorns",lvl:10}]} 1')
  
  playerkill()
})
