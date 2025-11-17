
play_again = True

while play_again:
    print("⚔️ SOUL FIGHTER: LAST SURVIVOR ⚔️")
    print()
    print("You wake up on a cold, empty beach...")
    print("Your head aches. Your memory is blank.")
    print("Then you hear it — deep, hungry growls behind you.")
    print("Zombies. Too many of them.")
    print()
    print("Run. Hide. Fight.")
    print("Your fate begins now...\n")

    end_of_game = True

    while end_of_game:
        choice = int(input(
            "What will you do?\n"
            "1. Hide in the jungle\n"
            "2. Search the beach for supplies\n"
            "Choose an option: "
        ))

        # ------------------------- JUNGLE PATH -------------------------
        if choice == 1:
            print("\nYou rush into the thick jungle. The air is humid.")
            print("Branches snap behind you... something is following.\n")

            end_of_path1 = True

            while end_of_path1:
                path1 = int(input(
                    "What will you do now?\n"
                    "1. Climb a tall tree to hide\n"
                    "2. Run deeper into the jungle\n"
                    "3. Grab a large stick and prepare to fight\n"
                    "Choose an option: "
                ))

                # ---------- TREE PATH ----------
                if path1 == 1:
                    print("\nYou climb a tall tree and look down.")
                    print("Zombies shuffle below you...\n")

                    end_of_path1a = True

                    while end_of_path1a:
                        path1a = int(input(
                            "What next?\n"
                            "1. Jump to another tree\n"
                            "2. Throw something to distract them\n"
                            "Choose an option: "
                        ))

                        if path1a == 1:
                            print("\nYou jump... the branch snaps!")
                            print("You fall straight into the zombies.\nGAME OVER.")
                            end_of_game = False
                            end_of_path1 = False
                            break

                        elif path1a == 2:
                            print("\nYou throw a rock far away.")
                            print("The zombies follow the noise and leave.")
                            print("From the treetop, you spot a safe town.\nYOU ESCAPED!")
                            end_of_game = False
                            end_of_path1 = False
                            break

                        else:
                            print("Please choose a valid option.\n")

                # ---------- RIVER PATH ----------
                elif path1 == 2:
                    print("\nYou run deeper into the jungle...")
                    print("You reach a cold, fast-flowing river.\n")

                    end_of_path1b = True

                    while end_of_path1b:
                        path1b = int(input(
                            "What will you do?\n"
                            "1. Swim across the river\n"
                            "2. Follow the river downstream\n"
                            "Choose an option: "
                        ))

                        if path1b == 1:
                            print("\nThe water is freezing and strong...")
                            print("You are pulled under.\nGAME OVER.")
                            end_of_game = False
                            end_of_path1 = False
                            break

                        elif path1b == 2:
                            print("\nYou follow the river and find a damaged boat.")
                            print("You fix it just enough to escape.\nYOU WIN!")
                            end_of_game = False
                            end_of_path1 = False
                            break

                        else:
                            print("Please choose a valid option.\n")

                # ---------- FIGHT PATH ----------
                elif path1 == 3:
                    print("\nYou grab a stick and swing with all your strength.")
                    print("But the zombie leaps forward and bites your arm...")
                    print("You turn into one of them.\nGAME OVER.")
                    end_of_game = False
                    end_of_path1 = False
                    break

                else:
                    print("Please choose a valid option.\n")

        # ------------------------- BEACH PATH -------------------------
        elif choice == 2:
            print("\nYou walk along the quiet beach.")
            print("Something feels wrong...\n")
            print("You see:")
            print("• A washed-up backpack")
            print("• A flare gun buried in the sand")
            print("• Bloody footprints leading to the cliffs\n")

            end_of_path2 = True

            while end_of_path2:
                path2 = int(input(
                    "What will you pick?\n"
                    "1. The backpack\n"
                    "2. The flare gun\n"
                    "3. Follow the bloody footprints\n"
                    "Choose an option: "
                ))

                # ---------- BACKPACK PATH ----------
                if path2 == 1:
                    print("\nInside the backpack you find:")
                    print("• Food")
                    print("• A small medical kit")
                    print("• A torn journal page\n")
                    print("The journal says:")
                    print("• A zombie nest is near the cliffs")
                    print("• A safe bunker is hidden near the palm trees\n")

                    end_of_path2a = True

                    while end_of_path2a:
                        path2a = int(input(
                            "Where will you go?\n"
                            "1. To the cliffs\n"
                            "2. Search for the bunker\n"
                            "Choose an option: "
                        ))

                        if path2a == 1:
                            print("\nThe cliffside crumbles beneath your feet...")
                            print("You fall into a swarm of zombies.\nGAME OVER.")
                            end_of_game = False
                            end_of_path2 = False
                            break

                        elif path2a == 2:
                            print("\nYou find the hidden bunker!")
                            print("The steel door closes just as zombies appear.")
                            print("You are finally safe.\nYOU WIN!")
                            end_of_game = False
                            end_of_path2 = False
                            break

                        else:
                            print("Please choose a valid option.\n")

                # ---------- FLARE GUN PATH ----------
                elif path2 == 2:
                    print("\nYou fire the flare at a zombie.")
                    print("It burns... but the dry grass catches fire!")
                    print("The wildfire surrounds you.\nGAME OVER.")
                    end_of_game = False
                    end_of_path2 = False
                    break

                # ---------- FOOTPRINTS / CAVE PATH ----------
                elif path2 == 3:
                    print("\nYou follow the bloody footprints into a dark cave...")
                    print("Inside, you find a wounded survivor.\n")
                    print("\"They're coming...\" he whispers.\n")

                    end_of_path2c = True

                    while end_of_path2c:
                        path2c = int(input(
                            "What will you do?\n"
                            "1. Help the survivor\n"
                            "2. Leave the cave quietly\n"
                            "3. Explore deeper\n"
                            "Choose an option: "
                        ))

                        if path2c == 1:
                            print("\nThe survivor turns suddenly — he was infected!")
                            print("He bites you.\nGAME OVER.")
                            end_of_game = False
                            end_of_path2 = False
                            break

                        elif path2c == 2:
                            print("\nYou slip out of the cave silently.")
                            print("You survive... but danger still lurks.\nYOU WIN! (Safe, but not saved.)")
                            end_of_game = False
                            end_of_path2 = False
                            break

                        elif path2c == 3:
                            print("\nThe cave shakes violently!")
                            print("Rocks fall and trap you inside.\nGAME OVER.")
                            end_of_game = False
                            end_of_path2 = False
                            break

                        else:
                            print("Please choose a valid option.\n")

                else:
                    print("Please choose a valid option.\n")

        else:
            print("Please choose a valid option.\n")

    # ------------------------- PLAY AGAIN -------------------------
    again = input("\nDo you want to play again? (yes/no): ").lower()

    if again == "yes":
        print("\nWelcome back!\n")
        play_again = True
    else:
        play_again = False
        print("\nThanks for playing Soul Fighter ✨⚔️!\n")
