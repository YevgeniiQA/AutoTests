from time import sleep
from Brain_testing import brain


def test_e2e():
    # Open the site
    brain.open()
    # Choose city
    brain.ch_city()
    # Show shops
    brain.sh_map()
    # brain.verif_count_sh()
    # Start site page
    brain.st_page()
    # Login and check the name
    brain.login()
    # Search goods and verification
    brain.search('Ноутбук')
    # Verification search result
    brain.verif_sch()
    # Start site page
    brain.st_page()
    # Choose network equipment
    brain.mer_obl()
    # Choose antennas WI-FI
    brain.сh_ant_wf()
    # Sorting by price
    brain.sort_price()
    # Filter and verification
    brain.filter()
    brain.verif_ftr()
    # Choose 1st good
    brain.shoose_fst_g()
    # Purchase of goods
    brain.buy()
    brain.close_buy_win()
    # Verification of basket
    brain.sh_basket()
    brain.verif_count_g()
    brain.clear_bas()
    brain.verif_empty_bas()
    # Profile changes
    brain.user_pers_data()
    brain.ch_us_ln('Тестов')
    brain.user_pers_data()
    brain.ch_us_ln('Тестовский')
    # brain.user_pers_data()
    brain.verif_us_ln()
    # Logout and verification
    brain.user_pers_data()
    brain.user_exit()

    sleep(2)
