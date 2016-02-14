import sys
import os
import pdb

class Plugin:
    def load(self, plugin_location):
        data = {};
        pluginPath = os.path.dirname(sys.modules[self.__class__.__module__].__file__);
        pluginPath = os.path.join(pluginPath, plugin_location)
        try:
            execfile(pluginPath, data);
        except:
            raise ValueError("Plugin doesn't exist");
        return data['export']
