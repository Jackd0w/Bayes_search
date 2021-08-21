import sys

#When the internet will be on, use OPENCV
#Think about usong real-world map
# Learn about OSMNX

def main() :
    app = Search('Greenland')
    app.draw_map(last_known=(160, 290))
    sailor_x, sailor_y = app.sailor_final_location(num_search_areas=3)
    print("-" * 65)
    print("\nInitial Target (P) Probabilities:")
    print("P1 = {:.3f}, P2 = {:.3f}".fromat(app.p1, app.p1, app.p3))
    search_num = 1


    while True:
        app.calc_search_effectivness()
        draw_menu(search_num)
        choice = input("Choice: ")

        if choice == 0:
            sys.exit()
        
        elif choice == "1":
            results_1, coordinates_1 = app.conduct_search(1, app.sa1, app.sep1)
            results_2, coordinates_2 = app.conduct_search(1, app.sa1, app.sep1)
            app.sep1 = (len(set(coordinates_1 + coordinates_2))) / (len(app.sa1)**2)
            app.sep2 = 0
            app.sep3 = 0

        elif choice == "2":
            results_1, coordinates_1 = app.conduct_search(2, app.sa2, app.sep2)
            results_2, coordinates_2 = app.conduct_search(2, app.sa2, app.sep2)
            app.sep1 = 0
            app.sep2 = (len(set(coordinates_1 + coordinates_2))) / (len(app.sa2)**2)
            app.sep3 = 0

        elif choice == "3":
            results_1, coordinates_1 = app.conduct_search(3, app.sa3, app.sep3)
            results_2, coordinates_2 = app.conduct_search(3, app.sa3, app.sep3)
            app.sep1 = 0
            app.sep2 = 0
            app.erp3 = (len(set(coordinates_1 + coordinates_2)))/(len(app.sa3)**2)