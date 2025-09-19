from org.bukkit.event import EventPriority
from org.bukkit.event.player import PlayerJoinEvent

class ListenerPlugin(PythonListener):
    @PythonEventHandler(PlayerJoinEvent, EventPriority.NORMAL)
    def onEvent(self, event):
        player = event.getPlayer()
        player.sendMessage("welcome to Jonimods' server! Enjoy your stay...")

class SpawnEventPlugin(PythonPlugin):

    def onEnable(self):
        pluginManager = self.getServer().getPluginManager()
        listener = ListenerPlugin()
        pluginManager.registerEvents(listener, self)
        pass