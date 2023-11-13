import tkinter as tk
from tkinter import ttk
import os
import random


# Get the current directory of the project file
project_dir = os.path.dirname(os.path.realpath(__file__))



def close():
    app.quit()

def start_game():
    # Remove the main menu widgets
    game_label.grid_forget()
    author_label.grid_forget()
    start_game_btn.grid_forget()
    quit_game_btn.grid_forget()

    def start_actual_game():
        # Remove the introduction page widgets
        introduction_label.grid_forget()
        intro_text.grid_forget()
        continue_btn.grid_forget()
        back_to_main.grid_forget()

        #Character Creation
        character_creation()

    def show_main_menu():
        # Remove the introduction page widgets
        introduction_label.grid_forget()
        intro_text.grid_forget()
        continue_btn.grid_forget()
        back_to_main.grid_forget()

        # Re-display the main menu widgets
        game_label.grid(column=1, row=1, pady=10)
        author_label.grid(column=1, row=2, pady=10)
        start_game_btn.grid(column=1, row=3, pady=5)
        quit_game_btn.grid(column=1, row=4, pady=5)

    # Create the introduction page widgets using ttk
    introduction_label = ttk.Label(app, text="Welcome to KMITL FE Student Simulator", style="Title.TLabel")
    introduction_label.grid(column=1, row=1, pady=10)
    
    intro_text = ttk.Label(app, text="This is a game where you get to live your life as a Financial Engineering Student at KMITL!", style="Subtitle.TLabel")
    intro_text.grid(column=1, row=2, pady=10)
    
    # Add a "Continue" button to start the game
    continue_btn = ttk.Button(app, text="Continue", style="Primary.TButton", command=start_actual_game)
    continue_btn.grid(column=1, row=3, pady=5)

    # Back to Main Menu Button
    back_to_main = ttk.Button(app, text="Back to Main Menu", style="Secondary.TButton", command=show_main_menu)
    back_to_main.grid(column=1, row=4, pady=5)

app = tk.Tk()
#app.state('zoomed') 
app.title("KMITL Financial Engineering Student Simulator")
app.geometry("800x640")

# Define styles for ttk widgets
style = ttk.Style(app)
style.configure("Title.TLabel", font=("Arial", 24))
style.configure("Subtitle.TLabel", font=("Arial", 12))
style.configure("Subtitle2.TLabel", font=("Arial", 10))
style.configure("Primary.TButton", font=("Arial", 18))
style.configure("Secondary.TButton", font=("Arial", 18))

#SPECIAL POINTS (idk why but I have to put it here lmfao)
remaining_points = 40  # Declare remaining_points as a global variable
final_player_info = {}
final_player_stats = {}
final_player_modifiers = {}
final_player_secatts = {}
final_player_skills = {}

def character_creation():
    #Character Creation Title
    character_creation_label = ttk.Label(app, text="Character Creation", style="Title.TLabel")
    character_creation_label.grid(column=0, row=0, sticky="sw")

    #SPECIAL
    def update_all_sec_atts():
        update_hp()
        update_unarmed()
        update_ac()

    def update_hp():
        hp = 10+player_modifiers["Constitution"]
        sec_atts["Hit Points"] = hp
        stats_labels["Hit Points"].config(text=f"Hit Points: {hp}")
    def update_unarmed():
        unarmed_dmg = stats["Strength"] + 1
        sec_atts["Unarmed Damage"] = unarmed_dmg
        stats_labels["Unarmed Damage"].config(text=f"Unarmed Damage: {unarmed_dmg}")
    def update_ac():
        ac = 10+player_modifiers["Dexterity"]
        sec_atts["Armor Class"] = ac
        stats_labels["Armor Class"].config(text=f"Armor Class: {ac}")
    
    def update_points():
        global remaining_points
        total_points = 75
        spent_points = sum(stats.values())
        remaining_points = total_points - spent_points
        if remaining_points < 0:
            remaining_points = 0
        points_label.config(text=f"Points Remaining: {remaining_points}")

    def increase_stat(stat):
        global remaining_points  
        if stats[stat] < 15 and remaining_points > 0:
            stats[stat] += 1
            update_points()
            update_all_sec_atts()
            modifier_check(stat)
            stats_labels[stat].config(text=f"{stat}: {stats[stat]}")

    def decrease_stat(stat):
        global remaining_points
        if stats[stat] > 8:
            stats[stat] -= 1
            update_points()
            update_all_sec_atts()
            modifier_check(stat)
            stats_labels[stat].config(text=f"{stat}: {stats[stat]}")

    def modifier_check(stat):
        global final_player_secatts
        global final_player_info
        global final_player_modifiers
        global final_player_stats
        global final_player_skills
        
        stats_mod =  (stats[stat]-10)//2
        stats_mod_label[stat].config(text=f"{stat} Modifier: {stats_mod}")
        player_modifiers.update({stat: stats_mod})
        if stat == "Strength":
            dnd_skills.update({"Athletics": stats_mod})
            modifier_label["Athletics"].config(text=f"{stats_mod}")
        elif stat == "Wisdom":
            dnd_skills.update({"Self Control": stats_mod})
            modifier_label["Self Control"].config(text=f"{stats_mod}")
        elif stat == "Charisma":
            dnd_skills.update({"Persuasion": stats_mod})
            modifier_label["Persuasion"].config(text=f"{stats_mod}")
            dnd_skills.update({"Music": stats_mod})
            modifier_label["Music"].config(text=f"{stats_mod}")
            dnd_skills.update({"Social Skills": stats_mod})
            modifier_label["Social Skills"].config(text=f"{stats_mod}")
            dnd_skills.update({"Rizz": stats_mod})
            modifier_label["Rizz"].config(text=f"{stats_mod}")
        elif stat == "Intelligence":
            dnd_skills.update({"Economics": stats_mod})
            modifier_label["Economics"].config(text=f"{stats_mod}")
            dnd_skills.update({"English": stats_mod})
            modifier_label["English"].config(text=f"{stats_mod}")
            dnd_skills.update({"Insight": stats_mod})
            modifier_label["Insight"].config(text=f"{stats_mod}")
            dnd_skills.update({"Tech": stats_mod})
            modifier_label["Tech"].config(text=f"{stats_mod}")
            dnd_skills.update({"Math": stats_mod})
            modifier_label["Math"].config(text=f"{stats_mod}")
        final_player_stats = stats
        print(final_player_stats)
        
        final_player_modifiers = player_modifiers
        print(final_player_modifiers)
        
        final_player_skills = dnd_skills
        print(final_player_skills)
        
        final_player_secatts = sec_atts
        print(final_player_secatts)
        print(final_player_info)
        
        print()
            
    

    special_frame = ttk.LabelFrame(app, text="Primary Attributes")
    special_frame.grid(column=0, row=1, padx=5, rowspan=2, sticky="ew")

    stats = {
        "Strength": 8, 
        "Dexterity": 8,
        "Constitution": 8,
        "Intelligence": 8, 
        "Wisdom": 8, 
        "Charisma": 8
    }

    stats_labels = {}
    stats_mod_label = {}
    player_modifiers = {"Strength": -1, "Dexterity": -1, "Constitution": -1, "Intelligence": -1, "Wisdom": -1, "Charisma": -1}

    for i, (stat, value) in enumerate(stats.items()):
        stats_labels[stat] = ttk.Label(special_frame, text=f"{stat}: {value}")
        stats_labels[stat].grid(row=i, column=0, padx=5, pady=5, sticky="w")
        inc_button = ttk.Button(special_frame, text="+", command=lambda stat=stat: increase_stat(stat))
        inc_button.grid(row=i, column=2)
        dec_button = ttk.Button(special_frame, text="-", command=lambda stat=stat: decrease_stat(stat))
        dec_button.grid(row=i, column=3)
        stats_mod_label[stat] = ttk.Label(special_frame, text = f"{stat} Modifier: -1")
        stats_mod_label[stat].grid(row=i, column=1, padx=5, sticky="w")
    
    points_label = ttk.Label(special_frame, text="Points Remaining: 27")
    points_label.grid(row=len(stats), padx=10, pady=10)

    #General Info. Notebook
    notebook = ttk.Notebook(app)
    notebook.grid(column=0, row=3,sticky="ew", padx=5, pady=5)

    # create frames
    frame1 = ttk.Frame(notebook, width=200, height=280)
    frame2 = ttk.Frame(notebook, width=200, height=280)

    frame1.pack(fill='both', expand=True)
    frame2.pack(fill='both', expand=True)

    # add frames to notebook

    notebook.add(frame1, text='General Information')
    notebook.add(frame2, text='Appearance')

    #Name
    name_lf = ttk.Labelframe(frame1, text ="Name")
    name_lf.grid(column=0, row=0, padx=5, pady=5, columnspan=2, sticky="ew")

    nick_name_label = ttk.Label(name_lf, text = "Nickname:")
    nick_name_label.grid(column=0, row=0, padx=5, pady=5,sticky="ew")

    nick_name_entry = ttk.Entry(name_lf, show=None, font=('Arial', 10))
    nick_name_entry.grid(column=1, row=0, padx=5,pady=5, sticky="ew")

    full_name_label = ttk.Label(name_lf, text = "Full Name:")
    full_name_label.grid(column=2, row=0, padx=5,pady=5, sticky="ew")

    last_name_entry = ttk.Entry(name_lf, show=None, font=('Arial', 10))
    last_name_entry.grid(column=3, row=0, padx=5,pady=5, sticky="ew")

    #Gender
    def get_selected_gender():
        player_gender = selected_gender.get()
        if player_gender == "Male":
            ac_hairs = m_hairs
            hairstyle_drop["values"] = ac_hairs
        elif player_gender == "Female":
            ac_hairs = f_hairs
            hairstyle_drop["values"] = ac_hairs
        else:
            ac_hairs = u_hairs
            hairstyle_drop["values"] = ac_hairs
        update_char_sum()
    selected_gender = tk.StringVar()

    gender_label = ttk.Labelframe(frame1, text ="Choose your gender")
    gender_label.grid(column=0, row=1, padx=3, pady=3, sticky="ew")

    male_button = ttk.Radiobutton(gender_label, text="Male", value="Male", variable=selected_gender, command=get_selected_gender)
    male_button.pack(padx=5, pady=5, side=tk.LEFT)

    female_button = ttk.Radiobutton(gender_label, text="Female", value="Female", variable=selected_gender, command=get_selected_gender)
    female_button.pack(padx=5, pady=5, side=tk.LEFT)

    other_button = ttk.Radiobutton(gender_label, text="Other", value="Other", variable=selected_gender, command=get_selected_gender)
    other_button.pack(padx=5, pady=5, side=tk.LEFT)

    #Races
    nationalities = ["Thai", "Chinese", "Vietnamese", "Burmese (Myanmar)", "Laotian (Lao)", "Cambodian (Khmer)", "Malaysian", "Indonesian", "Indian", "Japanese", "Korean", "Russian", "British", "American", "German"]
    
    race_lf = ttk.LabelFrame(frame1, text="Race")
    race_lf.grid(column=0, row=2, padx=3, pady=3, sticky="ew")

    race_drop = ttk.Combobox(race_lf, state="readonly", values=nationalities)
    race_drop.pack(padx=5, pady=5, side=tk.LEFT)
    


    #Preferences
    prefs = ["Men", "Women", "Both", "None"]
    
    pref_lf = ttk.LabelFrame(frame1, text="Preferences")
    pref_lf.grid(column=1, row=2, padx=3, pady=3, sticky="ew")

    pref_drop = ttk.Combobox(pref_lf, state="readonly", values=prefs)
    pref_drop.pack(padx=5, pady=5, side=tk.LEFT)

    #Age
    age_lf = ttk.Labelframe(frame1,text="Choose your age")
    age_lf.grid(column=1, row=1, padx=3, pady=3, sticky="ew")

    age_slider = ttk.Scale(age_lf, from_= 16, to=24, orient="horizontal")
    age_slider.grid(column=0, row=0, padx=3, pady=3,sticky="ew")
    current_age_var = tk.StringVar(value="Age: ")
    def update_current_age(value):
        current_age_var.set(f"Age: {round(float(value))}")
    update_current_age(16)

    age_slider.configure(command=update_current_age)

    current_age = ttk.Label(age_lf, textvariable=current_age_var)
    current_age.grid(column=1, row=0, sticky="ew")

    #Hair
    # Men's haircuts
    m_hairs = ["Bowl Cut", "Mullet", "Crew Cut", "Undercut", "Taper Fade"]

    # Women's haircuts
    f_hairs = ["Pixie Cut", "Rat Tail", "Bob Cut", "Layered Hair", "Beach Waves"]

    u_hairs = m_hairs + f_hairs

    hair_lf = ttk.LabelFrame(frame2, text="Hair")
    hair_lf.grid(column=0, row=0, padx=5, pady=5, columnspan=2, sticky="ew")
    
    hairstyle_label = ttk.Label(hair_lf, text = "Styles:")
    hairstyle_label.grid(column=0, row=0, pady=5, sticky="ew")
    hairstyle_drop = ttk.Combobox(hair_lf, state="readonly")
    hairstyle_drop.grid(column=1, row=0, padx=5, pady=5, sticky="ew")

    hair_colors_label = ttk.Label(hair_lf, text = "Colors:")
    hair_colors_label.grid(column=2, row=0, pady=5, sticky="ew")
    hair_colors_drop = ttk.Combobox(hair_lf, state="readonly", values=["Black", "Brown", "Blonde", "Red", "Gray", "White", "Blue", "Green", "Purple", "Pink"])
    hair_colors_drop.grid(column=3, row=0, padx=5, pady=5, sticky="ew")


    #Height
    height_lf = ttk.Labelframe(frame2,text="Height")
    height_lf.grid(column=0, row=1, padx=5, pady=5, sticky="ew")

    height_slider = ttk.Scale(height_lf, from_= 130, to=200, orient="horizontal", )
    height_slider.grid(column=0, row=0, padx=3, pady=3,sticky="ew")

    current_height_var = tk.StringVar()

    def update_current_height(value):
        current_height_var.set(f"{round(float(value))} cm")
    update_current_height(130)

    height_slider.configure(command=update_current_height)

    current_height = ttk.Label(height_lf, textvariable=current_height_var)
    current_height.grid(column=1, row=0, sticky="ew")

    #Eye Colors
    eye_colors = ["blue", "green", "brown", "hazel", "gray", "amber", "violet"]

    eye_lf = ttk.LabelFrame(frame2, text="Eye Color")
    eye_lf.grid(column=1, row=1, padx=5, pady=5, sticky="ew")

    eye_drop = ttk.Combobox(eye_lf, state="readonly", values=eye_colors)
    eye_drop.pack(padx=5, pady=5)

    #secondary attributes frame
    sec_att_lf = ttk.Labelframe(app, text="Secondary Attributes")
    sec_att_lf.grid(column=1, row=1, padx=5, sticky="nsew", rowspan=2)

    sec_atts = {
        "Hit Points": 10+player_modifiers["Constitution"],
        "Armor Class": 10+player_modifiers["Dexterity"],
        "Unarmed Damage": 1+stats["Strength"],
    }
    
    for i, (stat, value) in enumerate(sec_atts.items()):
        stats_labels[stat] = ttk.Label(sec_att_lf, text=f"{stat}: {value}")
        stats_labels[stat].grid(row=i, column=0, padx=5, pady=5, sticky="w")

    #skills label_frame
    skills_lf = ttk.LabelFrame(app, text="Skills")
    skills_lf.grid(column=2, row=1,sticky="nsew", padx=5)


    dnd_skills = {
        "Rizz": player_modifiers["Charisma"],
        "Music": player_modifiers["Charisma"],
        "Self Control":player_modifiers["Wisdom"],
        "Economics": player_modifiers["Intelligence"],
        "Athletics":player_modifiers[ "Strength"], #GYM
        "English": player_modifiers["Intelligence"], #Eng
        "Insight": player_modifiers["Intelligence"], #For Logic class lmfao
        "Tech": player_modifiers["Intelligence"],
        "Math": player_modifiers["Intelligence"],
        "Persuasion": player_modifiers["Charisma"],
        "Social Skills": player_modifiers["Charisma"],
    }

    skill_label = {}
    modifier_label = {}
    
    for i, (skill, modifier) in enumerate(dnd_skills.items()):

        skill_label[skill] = ttk.Label(skills_lf, text=f"{skill}")
        skill_label[skill].grid(column=0, row=i, sticky="w")

        skills_lf.columnconfigure(1, weight=1)
        modifier_label[skill] = ttk.Label(skills_lf, text=f"{modifier}")
        modifier_label[skill].grid(column=2, row=i, sticky="e")
    
    sum_box = ttk.LabelFrame(app, text="Character Summary")
    sum_box.grid(column=1, columnspan=2,row=3, sticky="nsew", padx=5)

    char_sum_1 = ttk.Label(sum_box, text="zamn")
    char_sum_1.grid(column=0, row=0, sticky="nsew", pady=5, padx=5)
    char_sum_2 = ttk.Label(sum_box, text="zamn")
    char_sum_2.grid(column=1, row=0, sticky="nsew", pady=5, padx=5)
    def update_char_sum():
        global final_player_info
        char_sum_1.config(text=f'Your full name: {last_name_entry.get()} \nYour gender: {selected_gender.get()} \nYour {current_age_var.get()}\nYour Race: {race_drop.get()} \nYour Preference: {pref_drop.get()}', wraplength=150)
        char_sum_2.config(text=f'Your Hairstyle: {hairstyle_drop.get()} \nYour Hair Color: {hair_colors_drop.get()} \nYour Height: {current_height_var.get()}\nYour Eye Color: {eye_drop.get()}', wraplength=150)
        final_player_info["Full Name"] = last_name_entry.get()
        final_player_info["Nick Name"] = nick_name_entry.get()
        final_player_info["Gender"] = selected_gender.get()
        final_player_info["Age"] = int((current_age_var.get()).replace("Age: ", ""))
        final_player_info["Race"] = race_drop.get()
        final_player_info["Preference"] = pref_drop.get()
        final_player_info["Hairstyle"] = hairstyle_drop.get()
        final_player_info["Hair Color"] = hair_colors_drop.get()
        final_player_info["Height"] = int((current_height_var.get()).replace("cm", ""))
        final_player_info["Eye Color"] = eye_drop.get()

    update_char_sum()
    
    def hide_cc():
        character_creation_label.grid_forget()
        special_frame.grid_forget()
        notebook.grid_forget()
        sec_att_lf.grid_forget()
        sum_box.grid_forget()
        skills_lf.grid_forget()
        start_game_fr()

    update_char_sum_btn = ttk.Button(sum_box, text="Update Character Description", padding=5, command=update_char_sum)
    update_char_sum_btn.grid(column=1, row=1, sticky="se")
    finish_cc = ttk.Button(sum_box, text="Continue to the Actual Game", padding=5, command=hide_cc)
    finish_cc.grid(column=1, row=2, sticky="se")
wallet_balance = 350
def start_game_fr():
    global wallet_balance
    def update_wallet(num):
        global wallet_balance
        wallet_balance = wallet_balance + num
        wallet_label.config(text=f"Wallet Balance: {wallet_balance} THB")

    
    def get_answer():
        player_answer = selected_answer.get()
        return player_answer


    def hide_quiz():
        quiz_frame.grid_forget()
    
    def show_quiz_frame():
        quiz_frame.grid(column=0, row=1, sticky=tk.NSEW, pady=5, columnspan=2)

    selected_answer = tk.StringVar()
    
    def show_quiz(text_1, value_1, state_1, text_2, value_2, state_2, text_3, value_3, state_3, text_4, value_4, state_4):

        quiz_btn_1.config(text=f"{text_1}", value=f"{value_1}", state=state_1, variable=selected_answer)
        quiz_btn_2.config(text=f"{text_2}", value=f"{value_2}", state=state_2, variable=selected_answer)
        quiz_btn_3.config(text=f"{text_3}", value=f"{value_3}", state=state_3, variable=selected_answer)
        quiz_btn_4.config(text=f"{text_4}", value=f"{value_4}",state=state_4, variable=selected_answer)
        quiz_btn_1.grid(column=0, row=1, sticky=tk.W)
        quiz_btn_2.grid(column=0, row=2, sticky=tk.W)
        quiz_btn_4.grid(column=1, row=2, sticky=tk.W)
        quiz_btn_3.grid(column=1, row=1, sticky=tk.W)


            
    
    def change_options(text_1, command_1, text_2, command_2):
        global test4
        global test5
        test4 = ttk.Button(btn_frame, text=f"{text_1}", command=lambda: change_dialogue(f"{command_1}"))
        test4.grid(column=1, row=0, sticky=tk.NSEW, padx=5)
        if text_2 == "-":
            test5 = ttk.Button(btn_frame, text=f"{text_2}", command=lambda: change_dialogue(f"{command_2}"), state=tk.DISABLED)
            test5.grid(column=1, row=1, sticky=tk.NSEW, padx=5)
        else:
            test5 = ttk.Button(btn_frame, text=f"{text_2}", command=lambda: change_dialogue(f"{command_2}"))
            test5.grid(column=1, row=1, sticky=tk.NSEW, padx=5)

    
    def change_img(img_name):
        global background_image_resized  # You don't need to redefine photo each time
        
        # Load the new image
        new_photo = tk.PhotoImage(file=project_dir + "\\" + img_name)

        # Calculate the subsample factors based on the desired size
        x_factor = new_photo.width() // 600
        y_factor = new_photo.height() // 340

        # Resize the new image
        background_image_resized = new_photo.subsample(x_factor, y_factor)

        # Update the image in the Label
        canvas.create_image(0,0, anchor=tk.NW, image=background_image_resized)
        scene.config(image=background_image_resized)
        scene.image = background_image_resized  # Keep a reference
    
    def overlay(img_name):
        global overlay_image_resized
        new_photo = tk.PhotoImage(file=project_dir + "\\" + img_name)
        
        overlay_image_resized = new_photo.subsample(background_image.width() // 600, background_image.height() // 340)
        canvas.create_image(0, 50, anchor=tk.NW, image=overlay_image_resized)
        scene2.config(image=overlay_image_resized)
        scene2.image = overlay_image_resized  # Keep a reference

    def change_dialogue(dialogue):
        dialogue_fr.config(text=f"{dialogue}")
        
        #Tuesday
        
        if dialogue_fr["text"] == "Narrator: You can choose to go to class now and be early, or sleep a bit more and go EXACTLY on time.":
            change_options(
                            "Leave now and get to class early", 
                           "Narrator: You choose to leave your dorm early and go to class.You get to the classroom and you hear noises from inside. It seems some people have arrived before you.",
                           "Sleep in a bit more",
                           "Narrator: You choose to sleep in a bit more, but you still arrive to class on time. You get to the classroom. Judging by the noise, only a few people are there (no one goes to class on time).",
            )
        
        elif dialogue_fr["text"] =="Narrator: You choose to leave your dorm early and go to class.You get to the classroom and you hear noises from inside. It seems some people have arrived before you.":
            
            change_img("scenes\Classroom Door BG.png")
            change_options(
                            "Go in the classroom", 
                           "Narrator: Inside the classroom, you see 1 girl and 2 guys.",
                           "Go in the classroom (Loudly)",
                           "Narrator: Inside the classroom, you see 1 girl and 2 guys. Your loud entrance startles them a bit.",
            )
        
        elif dialogue_fr["text"] =="Narrator: You choose to sleep in a bit more, but you still arrive to class on time. You get to the classroom. Judging by the noise, only a few people are there (no one goes to class on time).":
            change_img("scenes\Classroom Door BG.png")
            change_options(
                            "Go in the classroom", 
                           "Narrator: Inside the classroom, you see 1 girl and 2 guys.",
                           "Go in the classroom (Loudly)",
                           "Narrator: Inside the classroom, you see 1 girl and 2 guys. Your loud entrance startles them a bit.",
            )
        
        elif dialogue_fr["text"] =="Narrator: Inside the classroom, you see 1 girl and 2 guys." or dialogue_fr["text"] == "Narrator: Inside the classroom, you see 1 girl and 2 guys. Your loud entrance startles them a bit.":
            change_img("scenes\Classroom Interior BG.png")
            change_options(
                            "Say hi to the girl", 
                           "Jaja: OoooOOoo A new student! Haiiii :3. My name is Jaja by the way. What's your name?",
                           "Say hi to the boys",
                           "Lion: Hey! You must be the new transfer student! What's your name?",
            )

        elif dialogue_fr["text"] == "Jaja: OoooOOoo A new student! Haiiii :3. My name is Jaja by the way. What's your name?":
            overlay("characters\Jaja\Jaja-Smile.png")
            change_options(
                            f"My name is {final_player_info['Nick Name']}", 
                           f"Jaja: Nice to meet you, {final_player_info['Nick Name']}. You should go say hi to the other guys!",
                           "-",
                           "-",
            )
            
        
        elif dialogue_fr["text"] == f"Jaja: Nice to meet you, {final_player_info['Nick Name']}. You should go say hi to the other guys!":
            change_options(
                            f"Go say hi to the other guys", 
                           f"Lion: Hey! You must be the new transfer student! What's your name?",
                           "-",
                           "-",
            )
        
        elif dialogue_fr["text"] == "Lion: Hey! You must be the new transfer student! What's your name?":
            overlay("characters\Lion\Lion-Smile.png")
            change_options(
                            f"My name is {final_player_info['Nick Name']}", 
                           f"Lion: Nice to meet you, {final_player_info['Nick Name']}. This is my friend Ping Pong.",
                           "-",
                           "-",
            )

        elif dialogue_fr["text"] == f"Lion: Nice to meet you, {final_player_info['Nick Name']}. This is my friend Ping Pong.":
            change_options(
                            f"Say hi to Ping Pong", 
                           f"Ping Pong: Hi! I'm Ping Pong, Oh look here comes Dave and Deno",
                           "-",
                           "-",
            )
        
        elif dialogue_fr["text"] == "Ping Pong: Hi! I'm Ping Pong, Oh look here comes Dave and Deno":
            overlay("characters\PP\PP-Smile.png")
            change_options(
                            f"Turn around to see Dave and Deno", 
                           f"Deno (Local Stoner): What's good gang.",
                           "-",
                           "-",
            )
        
        elif dialogue_fr["text"] == "Deno (Local Stoner): What's good gang.":
            overlay("characters\Deno\Deno-Smile.png")
            change_options(
                            f"Next", 
                           f"Dave (Third Head of the Zenin Clan): Hello Children, I have arrived.",
                           "-",
                           "-",
            )

        elif dialogue_fr["text"] == "Dave (Third Head of the Zenin Clan): Hello Children, I have arrived.":
            overlay("characters\Dave\Dave-Smile.png")
            change_options(
                            f"Next", 
                           f"Narrator: You check your phone and you see this message: \nProfessor Joe: 'Class start at 9:45 pls'\nDave (Third Head of the Zenin Clan): Don't worry about that, he's always late.",
                           "-",
                           "-",
            )
        
        elif dialogue_fr["text"] == "Narrator: You check your phone and you see this message: \nProfessor Joe: 'Class start at 9:45 pls'\nDave (Third Head of the Zenin Clan): Don't worry about that, he's always late.":
            change_options(
                            f"Next", 
                           f"Narrator: Time has passed and Professor Joe has finally arrived to class.",
                           "-",
                           "-",
            )

        elif dialogue_fr["text"] == "Narrator: Time has passed and Professor Joe has finally arrived to class.":
            overlay("characters\profs\Joe.png")
            change_options(
                            f"Next", 
                           f"Professor Joe: Hello class, today we'll be learning about Sufficient and Necessary Conditions.A sufficient condition is something that, if it happens, guarantees the occurrence of another event. On the other hand, a necessary condition is something that must happen for an event to occur, but its occurrence alone doesn't guarantee the event will happen.",
                           "-",
                           "-",
            )
        
        elif dialogue_fr["text"] == "Professor Joe: Hello class, today we'll be learning about Sufficient and Necessary Conditions.A sufficient condition is something that, if it happens, guarantees the occurrence of another event. On the other hand, a necessary condition is something that must happen for an event to occur, but its occurrence alone doesn't guarantee the event will happen.":
            change_options(
                            f"Next", 
                           f"Professor Joe: For example, having bread is SUFFICIENT to make a sandwich. Which means bread is a sufficient condition for making a sandwich. However, a sandwich NEEDS to have a filling to qualify as a sandwich. Which means that a filling is a necessary condition for something to be a sandwich.",
                           "-",
                           "-",
            )
        
        elif dialogue_fr["text"] == "Professor Joe: For example, having bread is SUFFICIENT to make a sandwich. Which means bread is a sufficient condition for making a sandwich. However, a sandwich NEEDS to have a filling to qualify as a sandwich. Which means that a filling is a necessary condition for something to be a sandwich.":
            change_options(
                            f"Next", 
                           f"Professor Joe: You there, can you give me an example of a necessary condition? *He points at you*\nCome up to the black board and write it on the board for us.",
                           "-",
                           "-",
            )
        
        elif dialogue_fr["text"] == "Professor Joe: You there, can you give me an example of a necessary condition? *He points at you*\nCome up to the black board and write it on the board for us.":
            change_options(
                            f"Go up to the black board.", 
                           f"Narrator: You are now in front of the blackboard, chalk in hand.\nInfo: You must pick the right answer. However, you can also roll for the related skill to eliminate 1 \nor more wrong answers. In this case, it is the Insight skill, and you must roll higher than 10 to eliminate the wrong answer(s).",
                           "-",
                           "-",
            )

        elif dialogue_fr["text"] == "Narrator: You are now in front of the blackboard, chalk in hand.\nInfo: You must pick the right answer. However, you can also roll for the related skill to eliminate 1 \nor more wrong answers. In this case, it is the Insight skill, and you must roll higher than 10 to eliminate the wrong answer(s).":
            show_quiz_frame()
            show_quiz(
                "Having three sides is necessary for being a Triangle.", "Right", tk.NORMAL,
                "Flight is necessary for being a bird.",'Wrong 1', tk.NORMAL,
                "Rain is necessary for wet ground", 'Wrong 2', tk.NORMAL,
                "Being white is necessary for being American.", "Wrong 3", tk.NORMAL
            )
            change_options(
                            f"Roll to eliminate options", 
                           f"logic_insight_check_1",
                           "-",
                           "-",
            )
        
        elif dialogue_fr["text"] == "logic_insight_check_1":
            show_quiz_frame()
            rolled = random.choice(d20)
            if rolled + final_player_skills["Insight"] < 10:
                change_dialogue(f"[FAILED]\nYou rolled: {rolled}, Your Modifier: {final_player_skills['Insight']}, Total: {rolled+final_player_skills['Insight']}\nNarrator: No options have been eliminated. Choose an answer before proceeding.")
                checks_dict["logic_insight_check_1"] = "Failed"
                show_quiz(
                "Having three sides is necessary for being a Triangle.", "Right", tk.NORMAL,
                "Flight is necessary for being a bird.",'Wrong 1', tk.NORMAL,
                "Rain is necessary for wet ground", 'Wrong 2', tk.NORMAL,
                "Being white is necessary for being American.", "Wrong 3", tk.NORMAL
            )
                change_options(
                            f"Submit Answer", 
                           f"logic_insight_quiz_1",
                           "-",
                           "-",
                )
            elif rolled + final_player_skills["Insight"] >= 10:
                change_dialogue(f"[SUCCESS]\nYou rolled: {rolled}, Your Modifier: {final_player_skills['Insight']}, Total: {rolled+final_player_skills['Insight']}\nNarrator: 2 options have been eliminated. Choose an answer before proceeding.")
                checks_dict["logic_insight_check_1"] = "Pass"
                show_quiz(
                "Having three sides is necessary for being a Triangle.", "Right", tk.NORMAL,
                "Flight is necessary for being a bird.",'Wrong 1', tk.DISABLED,
                "Rain is necessary for wet ground", 'Wrong 2', tk.DISABLED,
                "Being white is necessary for being American.", "Wrong 3", tk.NORMAL
            )
                change_options(
                            f"Submit Answer", 
                           f"logic_insight_quiz_1",
                           "-",
                           "-",
                )
        
        elif dialogue_fr["text"] == "logic_insight_quiz_1":
            if get_answer() == "Right":
                selected_answer.set(" ")
                change_dialogue("Professor: Yes, that is correct, you may return to your seat.")
                hide_quiz()
                checks_dict["logic_insight_quiz_1"] = "Pass"
                change_options(
                            f"Next", 
                           f"Deno (Local Stoner): That's some real stuff bro.",
                           "-",
                           "-",
                )
                
            else:
                change_dialogue("Professor: Hmm, that doesn't look correct. That's fine, let's see if someone else can do it. You may return to your seat.")
                selected_answer.set(" ")
                hide_quiz()
                checks_dict["logic_insight_quiz_1"] = "Failed"
                change_options(
                            f"Next", 
                           f"Deno (Local Stoner): It's fine dude, everyone makes mistakes.",
                           "-",
                           "-",
                )
        
        elif dialogue_fr["text"] == "Deno (Local Stoner): It's fine dude, everyone makes mistakes." or dialogue_fr["text"] == "Deno (Local Stoner): That's some real stuff bro.":
            overlay("characters\Deno\Deno-Smile.png")
            change_options(
                            f"Next", 
                           f"Narrator: Time has passed again and it is now lunch time.\nProfessor Joe: Alright class, thank you very much for coming to class today, enjoy your lunch.",
                           "-",
                           "-",
                )

        elif dialogue_fr["text"] == "Narrator: Time has passed again and it is now lunch time.\nProfessor Joe: Alright class, thank you very much for coming to class today, enjoy your lunch.":
            overlay("characters\profs\Joe.png")
            change_options(
                            f"Next", 
                           f"Jaja (the prettiest girl in class): Heyy, do you want to come eat lunch with us?",
                           "-",
                           "-",
                )

        elif dialogue_fr["text"] == "Jaja (the prettiest girl in class): Heyy, do you want to come eat lunch with us?":
            overlay("characters\Jaja\Jaja-Smile.png")
            change_options(
                            f"Sure!", 
                           f"Narrator: You are now eating your lunch with Dave, Ping Pong, Lion, Deno, Jaja, and Saipan, in Cafeteria A.\nThe lunch you bought costs 50 THB.",
                           "No thanks, I'd rather eat alone",
                           "Narrator: You are now eating your lunch alone in Cafeteria A.\nThe lunch you bought costs 50 THB.",
                )

        elif dialogue_fr["text"] == "Narrator: You are now eating your lunch alone in Cafeteria A.\nThe lunch you bought costs 50 THB." or dialogue_fr["text"] == "Narrator: You are now eating your lunch with Dave, Ping Pong, Lion, Deno, Jaja, and Saipan, in Cafeteria A.\nThe lunch you bought costs 50 THB.":
            update_wallet(-50)
            change_img("scenes\Caf A BG.png")
            overlay("characters\Transparent.png")
            if dialogue_fr["text"] == "Narrator: You are now eating your lunch alone in Cafeteria A.\nThe lunch you bought costs 50 THB.":
                change_options(
                            f"Next", 
                           f"Narrator: While you are eating alone, a girl approaches you.",
                           "-",
                           "-",
                )
                checks_dict["tues_lunch"] = "Alone"
            elif dialogue_fr["text"] == "Narrator: You are now eating your lunch with Dave, Ping Pong, Lion, Deno, Jaja, and Saipan, in Cafeteria A.\nThe lunch you bought costs 50 THB.":
                change_options(
                            f"Next", 
                           f"Saipan (The Artist): Lion, why are you watching the same guy making steak on your phone again.",
                           "-",
                           "-",
                )
                checks_dict["tues_lunch"] = "Group"

        #SOLO LUNCH
        elif dialogue_fr["text"] == "Narrator: While you are eating alone, a girl approaches you.":
            overlay("characters\Proud\Proud-Smile.png")
            if checks_dict["logic_insight_quiz_1"] == "Failed":
                change_options(
                            f"Next", 
                            f"(???): Hey you. I saw you in class failing to do the example on the board. I don't get the topic either. So I think we should study it together. Here's my Instagram. My name is Proud, by the way. Text me or I will make you regret it.\n\nNarrator: She hands you a piece of paper with her Instagram handle written on it.",
                            "-",
                            "-",
                )
            elif checks_dict["logic_insight_quiz_1"] == "Pass":
                change_options(
                            f"Next", 
                            f"(???): Hey you. I saw you in class doing the example on the board. I don't get the topic, but I want to. So I want you to help me understand it later. Here's my Instagram. My name is Proud, by the way. Text me or I will make you regret it.\n\nNarrator: She hands you a piece of paper with her Instagram handle written on it.",
                            "-",
                            "-",
                )

        
        #Tues Group Lunch
        elif dialogue_fr["text"] == "Saipan (The Artist): Lion, why are you watching the same guy making steak on your phone again.":
            overlay("characters\Saipan\Saipan-Smile.png")
            change_options(
                            f"Next", 
                           f"Lion: I am watching him because I like steak, Saipan, why is it so hard for you to understand that?",
                           "-",
                           "-",
            )

        elif dialogue_fr["text"] == "Lion: I am watching him because I like steak, Saipan, why is it so hard for you to understand that?":
            overlay("characters\Lion\Lion-Smile.png")
            change_options(
                            f"Next", 
                           f"Saipan (The Artist): Ok, whatever man, just watch what you want to I guess.",
                           "-",
                           "-",
            )
        
        elif dialogue_fr["text"] == "Saipan (The Artist): Ok, whatever man, just watch what you want to I guess.":
            overlay("characters\Saipan\Saipan-Smile.png")
            change_options(
                            f"Next", 
                           f"Narrator: Right after Saipan finishes her sentence, a girl you don't recognize approaches the table.",
                           "-",
                           "-",
            )
        
        elif dialogue_fr["text"] == "Narrator: Right after Saipan finishes her sentence, a girl you don't recognize approaches the table.":
           overlay("characters\Proud\Proud-Smile.png")
           if checks_dict["logic_insight_quiz_1"] == "Failed":
            change_options(
                        f"Next", 
                        f"(???): Hey you. I saw you in class failing to do the example on the board. I don't get the topic either. So I think we should study it together. Here's my Instagram. My name is Proud, by the way. Text me or I will make you regret it.\n\nNarrator: She hands you a piece of paper with her Instagram handle written on it.",
                        "-",
                        "-",
            )
           elif checks_dict["logic_insight_quiz_1"] == "Pass":
            change_options(
                            f"Next", 
                           f"(???): Hey you. I saw you in class doing the example on the board. I don't get the topic, but I want to. So I want you to help me understand it later. Here's my Instagram. My name is Proud, by the way. Text me or I will make you regret it.\n\nNarrator: She hands you a piece of paper with her Instagram handle written on it.",
                           "-",
                           "-",
            )
            
        elif dialogue_fr["text"] == "(???): Hey you. I saw you in class doing the example on the board. I don't get the topic, but I want to. So I want you to help me understand it later. Here's my Instagram. My name is Proud, by the way. Text me or I will make you regret it.\n\nNarrator: She hands you a piece of paper with her Instagram handle written on it." or dialogue_fr["text"] == "(???): Hey you. I saw you in class failing to do the example on the board. I don't get the topic either. So I think we should study it together. Here's my Instagram. My name is Proud, by the way. Text me or I will make you regret it.\n\nNarrator: She hands you a piece of paper with her Instagram handle written on it.":
            if checks_dict["tues_lunch"] == "Group":
                if final_player_info["Gender"] == "Male":
                    change_options(
                                f"Next", 
                            f"Narrator: As Proud walks away, Lion pipes up.\nLion: Dude, I think she just asked you out. Now give me her Instagram before I hit you on the head.",
                            "-",
                            "-",
                    )
                else:
                    change_options(
                            f"Next", 
                            f"Narrator: As Proud walks away, Saipan pipes up.\nSaipan (The Artist): I don't know man, she seems a bit suspicious. I'd be careful around her.",
                            "-",
                            "-",
                    )
            elif checks_dict["tues_lunch"] == "Alone":
                change_options(
                            f"Continue eating your lunch", 
                           f"Narrator: As she walks away, you continue eating your lunch.",
                           "-",
                           "-",
                )
        
        elif dialogue_fr["text"] == f"Narrator: As Proud walks away, Saipan pipes up.\nSaipan (The Artist): I don't know man, she seems a bit suspicious. I'd be careful around her.":
            overlay("characters\Saipan\Saipan-Smile.png")
            change_options(
                            f"Next", 
                           f"Narrator: After you finish eating your lunch, you arrive in front of your next class, Introduction to Programming.",
                           "-",
                           "-",
                )
        
        elif dialogue_fr["text"] == f"Narrator: As she walks away, you continue eating your lunch.":
            overlay("characters\Transparent.png")
            change_options(
                            f"Next", 
                           f"Narrator: After you finish eating your lunch, you arrive in front of your next class, Introduction to Programming.",
                           "-",
                           "-",
                )
        

        elif dialogue_fr["text"] == "Narrator: As Proud walks away, Lion pipes up.\nLion: Dude, I think she just asked you out. Now give me her Instagram before I hit you on the head.":
            overlay("characters\Lion\Lion-Smile.png")
            change_options(
                            f"Next", 
                           f"Yacht (The Hottest Guy): Lion leave {final_player_info['Nick Name']} alone bruh. You're just salty because you have zero rizz. If you were as handsome as me, girls would give you their Instagram before you even ask them.",
                           "-",
                           "-",
                )
        
        elif dialogue_fr["text"] == f"Yacht (The Hottest Guy): Lion leave {final_player_info['Nick Name']} alone bruh. You're just salty because you have zero rizz. If you were as handsome as me, girls would give you their Instagram before you even ask them.":
            overlay("characters\Yacht\Yacht-Smile.png")
            change_options(
                            f"Continue eating your lunch", 
                           f"Narrator: After you finish eating your lunch, you arrive in front of your next class, Introduction to Programming.",
                           "-",
                           "-",
                )
        
        elif dialogue_fr["text"] == f"Narrator: After you finish eating your lunch, you arrive in front of your next class, Introduction to Programming.":
            overlay("characters\Transparent.png")
            change_img("scenes\Classroom Door BG.png")
            change_options(
                            f"Go inside the classroom", 
                           f"Narrator: Inside the classroom, there are two people working on Python code in the corner of the room. One of them is a short-haired girl and the other is handsome boy with glasses.",
                           "-",
                           "-",
                )

        elif dialogue_fr["text"] == f"Narrator: After you finish eating your lunch, you arrive in front of your next class, Introduction to Programming.":
            overlay("characters\Transparent.png")
            change_img("scenes\Classroom Door BG.png")
            change_options(
                            f"Go inside the classroom", 
                           f"Narrator: Inside the classroom, there are two people working on Python code in the corner of the room. One of them is a short-haired girl and the other is handsome boy with glasses.",
                           "-",
                           "-",
                )
            
        elif dialogue_fr["text"] == f"Narrator: Inside the classroom, there are two people working on Python code in the corner of the room. One of them is a short-haired girl and the other is handsome boy with glasses.":
            change_img("scenes\Programming Room BG.png")
            change_options(
                            f"Next", 
                           f"Jaja (the prettiest girl in class): Hey, do you want to come sit with us? We're gonna play Stardew Valley!",
                           "-",
                           "-",
                )
        
        elif dialogue_fr["text"] == f"Jaja (the prettiest girl in class): Hey, do you want to come sit with us? We're gonna play Stardew Valley!":
            overlay("characters\Jaja\Jaja-Smile.png")
            change_options(
                            f"Sure!", 
                           f"Narrator: You choose go sit with Jaja, Saipan, Lion, Ping Pong, Dave, and Yacht",
                           f"I think I'll go sit with those guys.",
                           f"Narrator: You choose to go sit next to the two people looking at Python code, they seem to be very intelligent people, unlike the people you ate lunch with. The girl notices you and says hi to you.\nJis (the GOAT): Hi, what's your name?",
                )
        
        #Programming sit with Gang
        elif dialogue_fr["text"] == f"Narrator: You choose go sit with Jaja, Saipan, Lion, Ping Pong, Dave, and Yacht":
            checks_dict["sit_with_goats"] = False
            overlay("characters\Jaja\Jaja-Smile.png")
            change_options(
                            f"Next", 
                           f"Narrator: You sit and watch Jaja play Stardew Valley, as you watch her farm for vegetables, you notice a slight change in the atmosphere. The lights go out. A worried look fills Dave’s eyes.\nDave (Third Head of the Zenin Clan): He has come.",
                           f"-",
                           f"-",
                )
        
        elif dialogue_fr["text"] == f"Narrator: You sit and watch Jaja play Stardew Valley, as you watch her farm for vegetables, you notice a slight change in the atmosphere. The lights go out. A worried look fills Dave’s eyes.\nDave (Third Head of the Zenin Clan): He has come.":
            change_img("scenes\Programming Room BG - Dark.png")
            overlay("characters\Dave\Dave-Neutral.png")
            change_options(
                            f"Next.", 
                           f"Narrator: The lights turn back on and in the light, you see in the middle of the room, a large ominous figure.\n(???): “Hello class” \nNarrator: It’s Professor Sun.",
                           f"-",
                           f"-",
                )

        #Programming Sit with GOATs
        elif dialogue_fr["text"] == f"Narrator: You choose to go sit next to the two people looking at Python code, they seem to be very intelligent people, unlike the people you ate lunch with. The girl notices you and says hi to you.\nJis (the GOAT): Hi, what's your name?":
            checks_dict["sit_with_goats"] = True
            overlay("characters\Jis\Jis-Smile.png")
            change_options(
                            f"My name is {final_player_info['Nick Name']}.", 
                           f"Jis (the GOAT): Nice to meet you {final_player_info['Nick Name']}. My name is Jis, if you have any questions about Python you can ask me! But Gun isn’t here right now, I’ll introduce you to him when he gets here.",
                           f"-",
                           f"-",
                )
        
        elif dialogue_fr["text"] == f"Jis (the GOAT): Nice to meet you {final_player_info['Nick Name']}. My name is Jis, if you have any questions about Python you can ask me! But Gun isn’t here right now, I’ll introduce you to him when he gets here.":
            overlay("characters\Jis\Jis-Smile.png")
            change_options(
                            f"Next.", 
                           f"Narrator: You decide that you need to go to the bathroom but as you attempt to leave your chair, you suddenly trip, your world goes upside down and you are now falling. But… You didn't fall down, you open your eyes and see a very handsome face, eyes glowing like the solemn moonlight, jawline so sharp, it can cut wood and teeth as white as pearls.",
                           f"-",
                           f"-",
                )
            
        elif dialogue_fr["text"] == f"Narrator: You decide that you need to go to the bathroom but as you attempt to leave your chair, you suddenly trip, your world goes upside down and you are now falling. But… You didn't fall down, you open your eyes and see a very handsome face, eyes glowing like the solemn moonlight, jawline so sharp, it can cut wood and teeth as white as pearls.":
            overlay("characters\Gun\Gun-Smile.png")
            change_options(
                            f"Next.", 
                           f"Narrator: “Are you okay?”\nThe handsome face asks. All you can get out are a couple of stammers.\n“That was quite the fall, I hope you didn't injure yourself”\nHe says as he gets you back on your feet, checking you for injuries.",
                           f"-",
                           f"-",
                )
            
        elif dialogue_fr["text"] == f"Narrator: “Are you okay?”\nThe handsome face asks. All you can get out are a couple of stammers.\n“That was quite the fall, I hope you didn't injure yourself”\nHe says as he gets you back on your feet, checking you for injuries.":
            overlay("characters\Gun\Gun-Smile.png")
            change_options(
                            f"Uhmm uhh- hi…", 
                           f"Jis (the GOAT): And this is Gun, you can ask the both of us for any help with python.",
                           f"Th-thank you",
                           f"Jis (the GOAT): And this is Gun, you can ask the both of us for any help with python.",
                )
            
        elif dialogue_fr["text"] == f"Jis (the GOAT): And this is Gun, you can ask the both of us for any help with python.":
            overlay("characters\Jis\Jis-Smile.png")
            change_options(
                            f"Next", 
                           f"Gun (the GOAT): You’re welcome, as Jis said, I’m Gun, any help you think you need with coding or anything else, just know, I’m always here for you.",
                           f"-",
                           f"-",
                )
            
        elif dialogue_fr["text"] == f"Gun (the GOAT): You’re welcome, as Jis said, I’m Gun, any help you think you need with coding or anything else, just know, I’m always here for you.":
            overlay("characters\Gun\Gun-Smile.png")
            change_options(
                            f"Next", 
                           f"Narrator: As you struggle to thank him again, you notice a slight change in the room.",
                           f"-",
                           f"-",
                )
        
        elif dialogue_fr["text"] == f"Narrator: As you struggle to thank him again, you notice a slight change in the room.":
            overlay("characters\Gun\Gun-Smile.png")
            change_options(
                            f"Next.", 
                           f"Narrator: You feel the air around you get colder, as everyone’s demeanor changes.\nGun (the GOAT): He’s here (in a shaken voice)\nNarrator: As tension rises, the lights suddenly go out.",
                           f"-",
                           f"-",
                )
        
        elif dialogue_fr["text"] == f"Narrator: You feel the air around you get colder, as everyone’s demeanor changes.\nGun (the GOAT): He’s here (in a shaken voice)\nNarrator: As tension rises, the lights suddenly go out.":
            change_img("scenes\Programming Room BG - Dark.png")
            overlay("characters\Gun\Gun-Smile.png")
            change_options(
                            f"Next.", 
                           f"Narrator: The lights turn back on and in the light, you see in the middle of the room, a large ominous figure.\n(???): “Hello class” \nNarrator: It’s Professor Sun.",
                           f"-",
                           f"-",
                )

        elif dialogue_fr["text"] == f"Narrator: The lights turn back on and in the light, you see in the middle of the room, a large ominous figure.\n(???): “Hello class” \nNarrator: It’s Professor Sun.":
            change_img("scenes\Programming Room BG.png")
            overlay("characters\profs\Sun.png")
            change_options(
                            f"Next.", 
                           f"Professor Sun: Oh-hoh?\nNarrator: Professor Sun notices you as he slightly turns toward you. All of the sudden, you find him arching over you, 5 inches away from your face. You find yourself unable to speak in his presence, you struggle to get anything out of your throat, let alone breathe, you try to calm yourself down but you can’t seem to muster up any thoughts at all.",
                           f"-",
                           f"-",
                )
        
        elif dialogue_fr["text"] == f"Professor Sun: Oh-hoh?\nNarrator: Professor Sun notices you as he slightly turns toward you. All of the sudden, you find him arching over you, 5 inches away from your face. You find yourself unable to speak in his presence, you struggle to get anything out of your throat, let alone breathe, you try to calm yourself down but you can’t seem to muster up any thoughts at all.":
            overlay("characters\profs\Sun - Copy.png")
            change_options(
                            f"Next.", 
                           f"Professor Sun: It seems we have a new student on board! Welcome, welcome!",
                           f"-",
                           f"-",
                )
        
        elif dialogue_fr["text"] == f"Professor Sun: It seems we have a new student on board! Welcome, welcome!":
            overlay("characters\profs\Sun.png")
            change_options(
                            f"Next.", 
                           f"Narrator: Professor Sun walks giddily to his desk, you find yourself able to breathe again.\nProfessor Sun: So class, today we will be taking a look at lists today and we will be having a small quiz in class today so, I hope you’re ready",
                           f"-",
                           f"-",
                )
        
        elif dialogue_fr["text"] == f"Narrator: Professor Sun walks giddily to his desk, you find yourself able to breathe again.\nProfessor Sun: So class, today we will be taking a look at lists today and we will be having a small quiz in class today so, I hope you’re ready":
            overlay("characters\profs\Sun.png")
            if checks_dict["sit_with_goats"] == True:
                change_options(
                            f"Next.", 
                           f"Jis (the GOAT): Make sure to focus in class okay? Professor Sun might call on you for a question since you're a new student.",
                           f"-",
                           f"-",
                )
            elif checks_dict["sit_with_goats"] == False:
                change_options(
                            f"Next.", 
                           f"Narrator: As Professor Sun starts his lecture, Jaja and the others start playing games, watch YouTube, and other things that are not at all related to Python. Lion is asleep already.\nYou feel compelled to be distracted as well. You must make a self control roll to focus on class (roll higher than 15).",
                           f"-",
                           f"-",
                )
        
        elif dialogue_fr["text"] == f"Jis (the GOAT): Make sure to focus in class okay? Professor Sun might call on you for a question since you're a new student.":
            overlay("characters\Jis\Jis-Smile.png")
            change_options(
                            f"Next.", 
                           f"Professor Sun: Lists are containers that can store various types of data, such as strings, integers, float values, boolean values, or even other lists! Today we'll learn about list slicing, list indices, and list comprehension!",
                           f"-",
                           f"-",
                )
        
        elif dialogue_fr["text"] == f"Narrator: As Professor Sun starts his lecture, Jaja and the others start playing games, watch YouTube, and other things that are not at all related to Python. Lion is asleep already.\nYou feel compelled to be distracted as well. You must make a self control roll to focus on class (roll higher than 15).":
            overlay("characters\Jaja\Jaja-Smile.png")
            change_options(
                            f"Roll for self control", 
                           f"programming_self_control_check_1",
                           f"-",
                           f"-",
                )
        
        elif dialogue_fr["text"] == f"programming_self_control_check_1":
            rolled = random.choice(d20)
            overlay("characters\Transparent.png")
            if rolled + final_player_skills["Self Control"] < 15:
                checks_dict["programming_self_control_check_1"] = "Fail"
                change_dialogue(f"[FAILED]\nRequired to pass: 15, You rolled: {rolled}, Your Modifier: {final_player_skills['Self Control']}, Total: {rolled+final_player_skills['Self Control']}\nNarrator: You are now distracted, Professor Sun's lecture goes into your ear and out the other.")
                change_options(
                            f"Next.", 
                           f"Narrator: Professor Sun points at you and calls out while you are zoning out.\nProfessor Sun: You there! What is a list enclosed by? Square brackets, parentheses, curly brackets or quotation marks?\n\nNarrator: Roll 15 or higher in 'Tech' skill to eliminate wrong options.",
                           f"-",
                           f"-",
                )
            elif rolled + final_player_skills["Self Control"] >= 15:
                checks_dict["programming_self_control_check_1"] = "Pass"
                change_dialogue(f"[SUCCESS]\nRequired to pass: 15, You rolled: {rolled}, Your Modifier: {final_player_skills['Self Control']}, Total: {rolled+final_player_skills['Self Control']}\nNarrator: You resist your urges and listen to Professor Sun intently.")
                change_options(
                            f"Next.", 
                           f"Professor Sun: Lists are containers that can store various types of data, such as strings, integers, float values, boolean values, or even other lists! Today we'll learn about list slicing, list indices, and list comprehension!",
                           f"-",
                           f"-",
                )
        
        elif dialogue_fr["text"] == f"Narrator: Professor Sun points at you and calls out while you are zoning out.\nProfessor Sun: You there! What is a list enclosed by? Square brackets, parentheses, curly brackets or quotation marks?\n\nNarrator: Roll 15 or higher in 'Tech' skill to eliminate wrong options.":
            overlay("characters\profs\Sun.png")
            show_quiz_frame()
            show_quiz(
                "Parentheses ().", "Wrong 1", tk.NORMAL,
                "Square brackets [].",'Right', tk.NORMAL,
                "Curly brackets {}.", 'Wrong 2', tk.NORMAL,
                "Quotation marks ' '.", "Wrong 3", tk.NORMAL
            )
            change_options(
                            f"Roll to eliminate options", 
                           f"programming_tech_check_1",
                           "-",
                           "-",
            )
        
        elif dialogue_fr["text"] == f"programming_tech_check_1":
            rolled = random.choice(d20)
            if rolled + final_player_skills["Tech"] < 15:
                checks_dict["programming_tech_check_1"] = "Fail"
                change_dialogue(f"[FAILED]\nRequired to pass: 15, You rolled: {rolled}, Your Modifier: {final_player_skills['Tech']}, Total: {rolled+final_player_skills['Tech']}\nNarrator: No options have been eliminated. Choose an answer before proceeding.")
                change_options(
                            f"Submit answer.", 
                           f"programming_tech_quiz_1",
                           f"-",
                           f"-",
                )
            elif rolled + final_player_skills["Tech"] >= 15:
                checks_dict["programming_tech_check_1"] = "Pass"
                change_dialogue(f"[SUCCESS]\nRequired to pass: 15, You rolled: {rolled}, Your Modifier: {final_player_skills['Tech']}, Total: {rolled+final_player_skills['Tech']}\nNarrator: 2 options have been eliminated. Choose an answer before proceeding.")
                change_options(
                            f"Submit answer.", 
                           f"programming_tech_quiz_1",
                           f"-",
                           f"-",
                )

           
    
    checks_dict = {}
    d20 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    # Dialogue
    dialogue_box = ttk.LabelFrame(app, text="Dialogue Box")
    dialogue_box.grid(column=0, row=2, sticky="nsew", padx=10, pady=10, columnspan=2)

    # Stats Notebook
    stats_nb = ttk.Notebook(app)
    stats_nb.grid(column=2, row=2, sticky="ew", padx=5, pady=5)
    frame1 = ttk.Frame(stats_nb, width=200, height=100)
    frame2 = ttk.Frame(stats_nb, width=200, height=100)
    frame3 = ttk.Frame(stats_nb, width=200, height=100)

    frame1.pack(fill='both', expand=True)
    frame2.pack(fill='both', expand=True)

    stats_nb.add(frame1, text='Skills')
    stats_nb.add(frame2, text='Stats')
    stats_nb.add(frame3, text = 'Misc')
    
    skill_label = {}
    modifier_label= {}

    for i, (skill, modifier) in enumerate(final_player_skills.items()):
        if i >= 6: break

        skill_label[skill] = ttk.Label(frame1, text=f"{skill}")
        skill_label[skill].grid(column=0, row=i, sticky="w")

        modifier_label[skill] = ttk.Label(frame1, text=f"{modifier}")
        modifier_label[skill].grid(column=2, row=i, sticky="e")
    
    
    for i, (skill, modifier) in enumerate(final_player_skills.items()):
        if i<6: continue
    
        skill_label[skill] = ttk.Label(frame1, text=f"{skill}")
        skill_label[skill].grid(column=3, row=i-6, sticky="w")

        modifier_label[skill] = ttk.Label(frame1, text=f"{modifier}")
        modifier_label[skill].grid(column=4, row=i-6, sticky="e")
    
    stat_label = {}
    stat_num = {}
    stat_mod = {}

    for i, (stat, num) in enumerate(final_player_stats.items()):
        stat_label[stat] = ttk.Label(frame2, text=f"{stat}")
        stat_label[stat].grid(column=0, row=i, sticky="w")

        stat_num[stat] = ttk.Label(frame2, text=f"{num}")
        stat_num[stat].grid(column=2, row=i, sticky="e")

        frame2.columnconfigure(3, weight=1)

        stat_mod[stat] = ttk.Label(frame2, text=f"{final_player_modifiers[stat]}")
        stat_mod[stat].grid(column=4, row=i, sticky="w")
    
    stats_labels = {}
    for i, (stat, value) in enumerate(final_player_secatts.items()):
        stats_labels[stat] = ttk.Label(frame3, text=f"{stat}: {value}")
        stats_labels[stat].grid(row=i, column=0, padx=5, sticky="w")
    
    wallet_label = ttk.Label(frame3, text=f"Wallet Balance: {wallet_balance} THB")
    wallet_label.grid(column=0, row=3, sticky=tk.W, padx=5)

    #Buttons Frame
    btn_frame = ttk.LabelFrame(app, text="Options")
    btn_frame.grid(column=2, row=3, sticky=tk.E, padx=10)
    app.columnconfigure(2, weight=0)

    # Load the initial image
    background_image = tk.PhotoImage(file=project_dir + "\\" + "scenes\Dorm BG.png")
    background_image_resized = background_image.subsample(background_image.width() // 600, background_image.height() // 340)

    canvas = tk.Canvas(app, width=background_image_resized.width() , height=background_image_resized.height())
    canvas.grid(column=0, row=0, rowspan=2, columnspan=3, sticky="ns", pady=10)
    
    canvas.create_image(0,0, anchor=tk.NW, image=background_image_resized)
    scene = ttk.Label(canvas, image=background_image_resized)
    scene.image = background_image_resized

    overlay_image = tk.PhotoImage(file=project_dir + "\\" + "scenes\Transparent.png")
    overlay_image_resized =overlay_image.subsample(background_image.width() // 600, background_image.height() // 340)
    scene2 = ttk.Label(canvas, image=overlay_image_resized)
    scene2.image = overlay_image_resized
    canvas.create_image(0, 50, anchor=tk.NW, image=overlay_image_resized)
    
    dialogue_fr = ttk.Label(dialogue_box, text="Narrator: You wake up in your dorm room. It is currently Tuesday morning, and you have Logic and Critical Thinking class.", justify="left", wraplength=550)
    dialogue_fr.grid(column=0, row=0, sticky=tk.NSEW, pady=5, columnspan=2)

    test4 = ttk.Button(btn_frame, text="Next", command=lambda: change_dialogue("Narrator: You can choose to go to class now and be early, or sleep a bit more and go EXACTLY on time."))
    test4.grid(column=1, row=0, sticky=tk.NSEW, padx=5)
    test5 = ttk.Button(btn_frame, text="-")
    test5.grid(column=1, row=1, sticky=tk.NSEW, padx=5)

    quiz_frame = ttk.Frame(dialogue_box)
    quiz_frame.grid(column=0, row=1, sticky=tk.NSEW, pady=5, columnspan=2)

    quiz_btn_1 = ttk.Radiobutton(quiz_frame, text="Having three sides is necessary for being a Triangle.", value="Right")
    quiz_btn_2 = ttk.Radiobutton(quiz_frame, text="Flight is necessary for being a bird.", value="Wrong 1")
    quiz_btn_3 = ttk.Radiobutton(quiz_frame, text="Rain is necessary for wet ground", value="Wrong 2")
    quiz_btn_4 = ttk.Radiobutton(quiz_frame, text="Being white is necessary for being American", value="Wrong 3")

    hide_quiz()

    

    
    
app.columnconfigure(0, weight=1)
app.columnconfigure(2, weight=1)
app.rowconfigure(0, weight=1)
app.rowconfigure(5, weight=1)

game_label = ttk.Label(app, text="KMITL Financial Engineering Student Simulator", style="Title.TLabel")
game_label.grid(column=1, row=1, pady=10)

author_label = ttk.Label(app, text="Made by: Thongtada (Lion) Thongsawang for Python Project", style="Subtitle.TLabel")
author_label.grid(column=1, row=2, pady=10)

start_game_btn = ttk.Button(app, text="Start Game", style="Primary.TButton", command=start_game)
start_game_btn.grid(column=1, row=3, pady=5)

quit_game_btn = ttk.Button(app, text="Quit Game", style="Secondary.TButton", command=close)
quit_game_btn.grid(column=1, row=4, pady=5)

app.mainloop()