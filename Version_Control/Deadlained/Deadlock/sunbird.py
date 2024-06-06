import importlib
from ..sunbird_feather import refresh_sunbird

def sunbird():
    modules = [
        'Version_Control.Deadlained.Celestial.Sun.sun',
        'Version_Control.Deadlained.LVX.Godforms.typhon',
        'Version_Control.Deadlained.LVX.Godforms.isis',
        'Version_Control.Deadlained.LVX.Godforms.apophis',
        'Version_Control.Deadlained.Deadlock.Deadlane.Shem_HaMephorash.Shem_HaMephorash',
        'Version_Control.Deadlained.GodHeads.zeus',
        'Version_Control.Deadlained.GodHeads.precis',
        'Version_Control.Deadlained.GodHeads.cardinaltron',
        'Version_Control.Deadlained.GodHeadVoices.characters.tsu.summit',
        'Version_Control.Deadlained.GodHeadVoices.characters.c.chaga',
        'Version_Control.Deadlained.LVX.LUX.LUX',
        'Version_Control.Deadlained.LVX.LUX.DUX',
        'Version_Control.Deadlained.LVX.LUX.DEX'
    ]

    new_hex = refresh_sunbird()
    for module in modules:
        try:
            importlib.import_module(module)
        except ModuleNotFoundError:
            print(f"Module {module} not found. Refreshed sunbird with new hex color: {new_hex}")

if __name__ == "__main__":
    sunbird()
