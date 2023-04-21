from time import sleep
from Brain_testing import brain


def test_e2e():
    # Open the site
    brain.open()
    #Choose city
    brain.ch_city()
    # Show shops
    brain.sh_map()
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
    # Shoose network equipment
    brain.mer_obl()

    brain.sh_ant_wf()

    brain.sort_price()

    brain.filter()
    brain.verif_ftr()

    brain.shoose_fst_g()

    brain.buy()
    brain.close_buy_win()

    brain.sh_basket()
    brain.verif_count_g()
    brain.clear_bas()
    brain.verif_empty_bas()

    brain.user_pers_data()
    brain.ch_us_ln('Тестов')
    brain.user_pers_data()
    brain.ch_us_ln('Тестовский')
    brain.user_pers_data()
    brain.verif_us_ln()

    sleep(3)


