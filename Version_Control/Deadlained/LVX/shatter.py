def shatter(godhead, godform):
    from Deadlock.Deadlane.Shem_HaMephorash.Shem_HaMephorash import ShemHaMephorash
    resolver = ShemHaMephorash(godhead, godform)
    resolver.resolve_conflict()
    return resolver.godform is None
