def new_password(old_pass, new_pass):
    return new_pass is not old_pass and len(new_pass) > 6


print(new_password('oudewachtwoord', 'NieuweWachtwoord'))