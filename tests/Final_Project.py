from Brain_testing import brain


def test_e2e():
    # Open the site
    brain.open()
    # Choose city
    # brain.ch_city()
    # # Show shops
    # brain.sh_map()
    # # Start site page
    # brain.st_page()
    # # Login and check the name
    # brain.login()
    # # Search goods and verification
    brain.search('Ноутбук')
    brain.verif()
    brain.st_page()
    brain.mer_obl()


