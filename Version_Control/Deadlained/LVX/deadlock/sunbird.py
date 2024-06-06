import importlib
from Version_Control.Deadlained.sunbird_feather import refresh_sunbird

def sunbird():
    modules = [
        'Version Control.Deadlained.Celestial.Sun.sun',
        'Version Control.Deadlained.LVX.Godforms.typhon',
        'Version Control.Deadlained.LVX.Godforms.isis',
        'Version Control.Deadlained.LVX.Godforms.apophis',
        'Version Control.Deadlained.Deadlock.Deadlane.Shem_HaMephorash.Shem_HaMephorash',
        'Version Control.Deadlained.GodHeads.zeus',
        'Version Control.Deadlained.GodHeads.precis',
        'Version Control.Deadlained.GodHeads.cardinaltron',
        'Version Control.Deadlained.GodHeadVoices.characters.tsu.summit',
        'Version Control.Deadlained.GodHeadVoices.characters.c.chaga',
        'Version Control.Deadlained.LVX.LUX.LUX',
        'Version Control.Deadlained.LVX.LUX.DUX',
        'Version Control.Deadlained.LVX.LUX.DEX'
    ]

    new_hex = refresh_sunbird()
    for module in modules:
        try:
            importlib.import_module(module)
        except ModuleNotFoundError:
            print(f"Module {module} not found. Refreshed sunbird with new hex color: {new_hex}")

if __name__ == "__main__":
    sunbird()
