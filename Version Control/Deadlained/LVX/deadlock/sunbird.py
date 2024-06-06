import importlib

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

    for module in modules:
        importlib.import_module(module)

if __name__ == "__main__":
    sunbird()
