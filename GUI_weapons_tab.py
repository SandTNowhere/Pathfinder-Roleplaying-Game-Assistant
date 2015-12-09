    def _create_weapons_tab(self, character):
            content = ttk.Frame(character, padding=(3,3,12,12))
            content.grid(column=0, row=0)

            wbuttonlbl = ttk.Label(content, text = " ")
            wbuttonnew = ttk.Button(content, text = "New", width = 10)
            wbuttonsave = ttk.Button(content, text = "Save", width = 10)
            wbuttonload = ttk.Button(content, text = "Load", width = 10)
            wbuttonexit = ttk.Button(content, text = "Exit", width = 10)
            
            """ attack stats declaration """
            bablbl = ttk.Label(content, text = "      Base Attack Bonus     ", background = 'black', foreground = 'white')
            reslbl = ttk.Label(content, text = "        Spell Resistance       ", background = 'black', foreground = 'white')
            cmblbl = ttk.Label(content, text = "    CMB    ", background = 'black', foreground = 'white')
            cmdlbl = ttk.Label(content, text = "    CMD    ", background = 'black', foreground = 'white')
            atkbon = ttk.Entry(content, width = 8)
            splres = ttk.Entry(content, width = 8)
            cmbtot = ttk.Entry(content, width = 4)
            cmbbab = ttk.Entry(content, width = 4)
            cmbstr = ttk.Entry(content, width = 4)
            cmbsiz = ttk.Entry(content, width = 4)
            cmdtot = ttk.Entry(content, width = 4)
            cmdcmb = ttk.Entry(content, width = 4)
            cmddex = ttk.Entry(content, width = 4)
            cmdl10 = ttk.Label(content, text = "10")
            cmdp01 = ttk.Label(content, text = "+")
            cmdp02 = ttk.Label(content, text = "+")
            cmde01 = ttk.Label(content, text = "=")
            cmbp01 = ttk.Label(content, text = "+")
            cmbp02 = ttk.Label(content, text = "+")
            cmbe01 = ttk.Label(content, text = "=")
            cmbtotlbl = ttk.Label(content, text = "Total", foreground = 'grey')
            cmbbablbl = ttk.Label(content, text = "B.A.B.", foreground = 'grey')
            cmbstrlbl = ttk.Label(content, text = "Str Mod", foreground = 'grey')
            cmbsizlbl = ttk.Label(content, text = "Size Mod", foreground = 'grey')
            cmdtotlbl = ttk.Label(content, text = "Total", foreground = 'grey')
            cmdcmblbl = ttk.Label(content, text = "CMB", foreground = 'grey')
            cmddexlbl = ttk.Label(content, text = "Dex Mod", foreground = 'grey')

            """ attack stats placement """
            bablbl.grid(column=1, row=2, columnspan=2, sticky=(W))
            reslbl.grid(column=4, row=2, columnspan=2, sticky=(W))
            cmblbl.grid(column=1, row=4)
            cmdlbl.grid(column=1, row=5)
            atkbon.grid(column=3, row=2, sticky=(W))
            splres.grid(column=6, row=2, sticky=(W))
            cmbtot.grid(column=3, row=4, sticky=(W))
            cmbbab.grid(column=4, row=4, sticky=(W))
            cmbstr.grid(column=5, row=4)
            cmbsiz.grid(column=6, row=4, sticky=(W))
            cmdtot.grid(column=3, row=5, sticky=(W))
            cmdcmb.grid(column=4, row=5, sticky=(W))
            cmddex.grid(column=5, row=5)
            cmdl10.grid(column=6, row=5, sticky=(W))
            cmdp01.grid(column=5, row=4, sticky=(W))
            cmdp02.grid(column=5, row=4, sticky=(E))
            cmde01.grid(column=3, row=4, sticky=(E))
            cmbp01.grid(column=5, row=5, sticky=(W))
            cmbp02.grid(column=5, row=5, sticky=(E))
            cmbe01.grid(column=3, row=5, sticky=(E))
            cmbtotlbl.grid(column=3, row=3, sticky=(W))
            cmbbablbl.grid(column=4, row=3, sticky=(W))
            cmbstrlbl.grid(column=5, row=3, sticky=(W))
            cmbsizlbl.grid(column=6, row=3, sticky=(W))
            cmdcmblbl.grid(column=4, row=6, sticky=(W))
            cmdtotlbl.grid(column=3, row=6, sticky=(W))
            cmddexlbl.grid(column=5, row=6, sticky=(W))

            """ weapons declaration """
            weapon1lbllbl = ttk.Label(content, text = "Weapon 1", background = 'black', foreground = 'white')
            weapon1atklbl = ttk.Label(content, text = "Attack Bonus", background = 'black', foreground = 'white')
            weapon1crtlbl = ttk.Label(content, text = "Critical", background = 'black', foreground = 'white')
            weapon1typlbl = ttk.Label(content, text = "Type", background = 'black', foreground = 'white')
            weapon1rnglbl = ttk.Label(content, text = "Range", background = 'black', foreground = 'white')
            weapon1ammlbl = ttk.Label(content, text = "Ammunition", background = 'black', foreground = 'white')
            weapon1damlbl = ttk.Label(content, text = "Damage", background = 'black', foreground = 'white')

            weapon1lblvar=StringVar()
            weapon1atkvar=StringVar()
            weapon1crtvar=StringVar()
            weapon1typvar=StringVar()
            weapon1rngvar=StringVar()
            weapon1ammvar=StringVar()
            weapon1damvar=StringVar()

            def updateweapon1(self, event=None):
                nonlocal weapon1lblvar
                nonlocal weapon1atkvar
                nonlocal weapon1crtvar
                nonlocal weapon1typvar
                nonlocal weapon1rngvar
                nonlocal weapon1ammvar
                nonlocal weapon1damvar
                weapon1_search_condition=str(' WHERE we_name="' + str(weapon1lblvar.get()).strip('{}[(,)]')+ '"')
                weapon1atkvar.set('Not Implemented') #search_db + Math
                weapon1crtvar.set(str(search_db('crit_rng', 'Weapons', weapon1_search_condition)).strip('{}[(,)]')+'/x'+str(search_db('crit_m', 'Weapons', weapon1_search_condition)).strip('{}[(,)]'))
                weapon1typvar.set(str(search_db('dam_type', 'Weapons', weapon1_search_condition)).strip('{}[(,)]'))
                weapon1rngvar.set(search_db('range', 'Weapons', weapon1_search_condition))
                weapon1ammvar.set('NA')
                weapon1damvar.set('Not Implemented') #search_db + Math
                
            weapon1lblbox = ttk.Combobox(content, width=42, textvariable=weapon1lblvar, values=search_db('we_name', 'Weapons', ' '))
            weapon1lblbox.bind('<<ComboboxSelected>>', updateweapon1)
            weapon1atkbox = ttk.Label(content, width=12, textvariable=weapon1atkvar, relief=RAISED) 
            weapon1crtbox = ttk.Label(content, width=10, textvariable=weapon1crtvar, relief=RAISED) 
            weapon1typbox = ttk.Label(content, width=10, textvariable=weapon1typvar, relief=RAISED) 
            weapon1rngbox = ttk.Label(content, width=10, textvariable=weapon1rngvar, relief=RAISED) 
            weapon1ammbox = ttk.Label(content, width=20, textvariable=weapon1ammvar, relief=RAISED) 
            weapon1dambox = ttk.Label(content, width=23, textvariable=weapon1damvar, relief=RAISED)

            
            weapon2lblvar=StringVar()
            weapon2atkvar=StringVar()
            weapon2crtvar=StringVar()
            weapon2typvar=StringVar()
            weapon2rngvar=StringVar()
            weapon2ammvar=StringVar()
            weapon2damvar=StringVar()

            def updateweapon2(self, event=None):
                nonlocal weapon2lblvar
                nonlocal weapon2atkvar
                nonlocal weapon2crtvar
                nonlocal weapon2typvar
                nonlocal weapon2rngvar
                nonlocal weapon2ammvar
                nonlocal weapon2damvar
                weapon2_search_condition=str(' WHERE we_name="' + str(weapon2lblvar.get()).strip('{}[(,)]')+ '"')
                weapon2atkvar.set('Not Implemented') #search_db + Math
                weapon2crtvar.set(str(search_db('crit_rng', 'Weapons', weapon2_search_condition)).strip('{}[(,)]')+'/x'+str(search_db('crit_m', 'Weapons', weapon2_search_condition)).strip('{}[(,)]'))
                weapon2typvar.set(str(search_db('dam_type', 'Weapons', weapon2_search_condition)).strip('{}[(,)]'))
                weapon2rngvar.set(search_db('range', 'Weapons', weapon2_search_condition))
                weapon2ammvar.set('NA')
                weapon2damvar.set('Not Implemented') #search_db + Math
                
            weapon2lblbox = ttk.Combobox(content, width=42, textvariable=weapon2lblvar, values=search_db('we_name', 'Weapons', ' '))
            weapon2lblbox.bind('<<ComboboxSelected>>', updateweapon2)
            weapon2atkbox = ttk.Label(content, width=12, textvariable=weapon2atkvar, relief=RAISED) 
            weapon2crtbox = ttk.Label(content, width=10, textvariable=weapon2crtvar, relief=RAISED) 
            weapon2typbox = ttk.Label(content, width=10, textvariable=weapon2typvar, relief=RAISED) 
            weapon2rngbox = ttk.Label(content, width=10, textvariable=weapon2rngvar, relief=RAISED) 
            weapon2ammbox = ttk.Label(content, width=20, textvariable=weapon2ammvar, relief=RAISED) 
            weapon2dambox = ttk.Label(content, width=23, textvariable=weapon2damvar, relief=RAISED)
            weapon2lbllbl = ttk.Label(content, text = "Weapon 2", background = 'black', foreground = 'white')
            weapon2atklbl = ttk.Label(content, text = "Attack Bonus", background = 'black', foreground = 'white')
            weapon2crtlbl = ttk.Label(content, text = "Critical", background = 'black', foreground = 'white')
            weapon2typlbl = ttk.Label(content, text = "Type", background = 'black', foreground = 'white')
            weapon2rnglbl = ttk.Label(content, text = "Range", background = 'black', foreground = 'white')
            weapon2ammlbl = ttk.Label(content, text = "Ammunition", background = 'black', foreground = 'white')
            weapon2damlbl = ttk.Label(content, text = "Damage", background = 'black', foreground = 'white')

            
            weapon3lblvar=StringVar()
            weapon3atkvar=StringVar()
            weapon3crtvar=StringVar()
            weapon3typvar=StringVar()
            weapon3rngvar=StringVar()
            weapon3ammvar=StringVar()
            weapon3damvar=StringVar()

            def updateweapon3(self, event=None):
                nonlocal weapon3lblvar
                nonlocal weapon3atkvar
                nonlocal weapon3crtvar
                nonlocal weapon3typvar
                nonlocal weapon3rngvar
                nonlocal weapon3ammvar
                nonlocal weapon3damvar
                weapon3_search_condition=str(' WHERE we_name="' + str(weapon3lblvar.get()).strip('{}[(,)]')+ '"')
                weapon3atkvar.set('Not Implemented') #search_db + Math
                weapon3crtvar.set(str(search_db('crit_rng', 'Weapons', weapon3_search_condition)).strip('{}[(,)]')+'/x'+str(search_db('crit_m', 'Weapons', weapon3_search_condition)).strip('{}[(,)]'))
                weapon3typvar.set(str(search_db('dam_type', 'Weapons', weapon3_search_condition)).strip('{}[(,)]'))
                weapon3rngvar.set(search_db('range', 'Weapons', weapon3_search_condition))
                weapon3ammvar.set('NA')
                weapon3damvar.set('Not Implemented') #search_db + Math
                
            weapon3lblbox = ttk.Combobox(content, width=42, textvariable=weapon3lblvar, values=search_db('we_name', 'Weapons', ' '))
            weapon3lblbox.bind('<<ComboboxSelected>>', updateweapon3)
            weapon3atkbox = ttk.Label(content, width=12, textvariable=weapon3atkvar, relief=RAISED) 
            weapon3crtbox = ttk.Label(content, width=10, textvariable=weapon3crtvar, relief=RAISED) 
            weapon3typbox = ttk.Label(content, width=10, textvariable=weapon3typvar, relief=RAISED) 
            weapon3rngbox = ttk.Label(content, width=10, textvariable=weapon3rngvar, relief=RAISED) 
            weapon3ammbox = ttk.Label(content, width=20, textvariable=weapon3ammvar, relief=RAISED) 
            weapon3dambox = ttk.Label(content, width=23, textvariable=weapon3damvar, relief=RAISED)
            weapon3lbllbl = ttk.Label(content, text = "Weapon 3", background = 'black', foreground = 'white')
            weapon3atklbl = ttk.Label(content, text = "Attack Bonus", background = 'black', foreground = 'white')
            weapon3crtlbl = ttk.Label(content, text = "Critical", background = 'black', foreground = 'white')
            weapon3typlbl = ttk.Label(content, text = "Type", background = 'black', foreground = 'white')
            weapon3rnglbl = ttk.Label(content, text = "Range", background = 'black', foreground = 'white')
            weapon3ammlbl = ttk.Label(content, text = "Ammunition", background = 'black', foreground = 'white')
            weapon3damlbl = ttk.Label(content, text = "Damage", background = 'black', foreground = 'white')


            weapon4lblvar=StringVar()
            weapon4atkvar=StringVar()
            weapon4crtvar=StringVar()
            weapon4typvar=StringVar()
            weapon4rngvar=StringVar()
            weapon4ammvar=StringVar()
            weapon4damvar=StringVar()

            def updateweapon4(self, event=None):
                nonlocal weapon4lblvar
                nonlocal weapon4atkvar
                nonlocal weapon4crtvar
                nonlocal weapon4typvar
                nonlocal weapon4rngvar
                nonlocal weapon4ammvar
                nonlocal weapon4damvar
                weapon4_search_condition=str(' WHERE we_name="' + str(weapon4lblvar.get()).strip('{}[(,)]')+ '"')
                weapon4atkvar.set('Not Implemented') #search_db + Math
                weapon4crtvar.set(str(search_db('crit_rng', 'Weapons', weapon4_search_condition)).strip('{}[(,)]')+'/x'+str(search_db('crit_m', 'Weapons', weapon4_search_condition)).strip('{}[(,)]'))
                weapon4typvar.set(str(search_db('dam_type', 'Weapons', weapon4_search_condition)).strip('{}[(,)]'))
                weapon4rngvar.set(search_db('range', 'Weapons', weapon4_search_condition))
                weapon4ammvar.set('NA')
                weapon4damvar.set('Not Implemented') #search_db + Math
                
            weapon4lblbox = ttk.Combobox(content, width=42, textvariable=weapon4lblvar, values=search_db('we_name', 'Weapons', ' '))
            weapon4lblbox.bind('<<ComboboxSelected>>', updateweapon4)
            weapon4atkbox = ttk.Label(content, width=12, textvariable=weapon4atkvar, relief=RAISED) 
            weapon4crtbox = ttk.Label(content, width=10, textvariable=weapon4crtvar, relief=RAISED) 
            weapon4typbox = ttk.Label(content, width=10, textvariable=weapon4typvar, relief=RAISED) 
            weapon4rngbox = ttk.Label(content, width=10, textvariable=weapon4rngvar, relief=RAISED) 
            weapon4ammbox = ttk.Label(content, width=20, textvariable=weapon4ammvar, relief=RAISED) 
            weapon4dambox = ttk.Label(content, width=23, textvariable=weapon4damvar, relief=RAISED)            
            weapon4lbllbl = ttk.Label(content, text = "Weapon 4" , background = 'black', foreground = 'white')
            weapon4atklbl = ttk.Label(content, text = "Attack Bonus", background = 'black', foreground = 'white')
            weapon4crtlbl = ttk.Label(content, text = "Critical", background = 'black', foreground = 'white')
            weapon4typlbl = ttk.Label(content, text = "Type", background = 'black', foreground = 'white')
            weapon4rnglbl = ttk.Label(content, text = "Range", background = 'black', foreground = 'white')
            weapon4ammlbl = ttk.Label(content, text = "Ammunition", background = 'black', foreground = 'white')
            weapon4damlbl = ttk.Label(content, text = "Damage", background = 'black', foreground = 'white')


            weapon5lblvar=StringVar()
            weapon5atkvar=StringVar()
            weapon5crtvar=StringVar()
            weapon5typvar=StringVar()
            weapon5rngvar=StringVar()
            weapon5ammvar=StringVar()
            weapon5damvar=StringVar()

            def updateweapon5(self, event=None):
                nonlocal weapon5lblvar
                nonlocal weapon5atkvar
                nonlocal weapon5crtvar
                nonlocal weapon5typvar
                nonlocal weapon5rngvar
                nonlocal weapon5ammvar
                nonlocal weapon5damvar
                weapon5_search_condition=str(' WHERE we_name="' + str(weapon5lblvar.get()).strip('{}[(,)]')+ '"')
                weapon5atkvar.set('Not Implemented') #search_db + Math
                weapon5crtvar.set(str(search_db('crit_rng', 'Weapons', weapon5_search_condition)).strip('{}[(,)]')+'/x'+str(search_db('crit_m', 'Weapons', weapon5_search_condition)).strip('{}[(,)]'))
                weapon5typvar.set(str(search_db('dam_type', 'Weapons', weapon5_search_condition)).strip('{}[(,)]'))
                weapon5rngvar.set(search_db('range', 'Weapons', weapon5_search_condition))
                weapon5ammvar.set('NA')
                weapon5damvar.set('Not Implemented') #search_db + Math
                
            weapon5lblbox = ttk.Combobox(content, width=42, textvariable=weapon5lblvar, values=search_db('we_name', 'Weapons', ' '))
            weapon5lblbox.bind('<<ComboboxSelected>>', updateweapon5)
            weapon5atkbox = ttk.Label(content, width=12, textvariable=weapon5atkvar, relief=RAISED) 
            weapon5crtbox = ttk.Label(content, width=10, textvariable=weapon5crtvar, relief=RAISED) 
            weapon5typbox = ttk.Label(content, width=10, textvariable=weapon5typvar, relief=RAISED) 
            weapon5rngbox = ttk.Label(content, width=10, textvariable=weapon5rngvar, relief=RAISED) 
            weapon5ammbox = ttk.Label(content, width=20, textvariable=weapon5ammvar, relief=RAISED) 
            weapon5dambox = ttk.Label(content, width=23, textvariable=weapon5damvar, relief=RAISED)
            weapon5lbllbl = ttk.Label(content, text = "Weapon 5", background = 'black', foreground = 'white')
            weapon5atklbl = ttk.Label(content, text = "Attack Bonus", background = 'black', foreground = 'white')
            weapon5crtlbl = ttk.Label(content, text = "Critical", background = 'black', foreground = 'white')
            weapon5typlbl = ttk.Label(content, text = "Type", background = 'black', foreground = 'white')
            weapon5rnglbl = ttk.Label(content, text = "Range", background = 'black', foreground = 'white')
            weapon5ammlbl = ttk.Label(content, text = "Ammunition", background = 'black', foreground = 'white')
            weapon5damlbl = ttk.Label(content, text = "Damage", background = 'black', foreground = 'white')


            """ weapons placement """

            weapon1lbllbl.grid(column = 1, row = 7, columnspan = 4, sticky = (W))
            weapon1atklbl.grid(column = 5, row = 7, columnspan = 1, sticky = (W))
            weapon1crtlbl.grid(column = 6, row = 7, columnspan = 1, sticky = (W))
            weapon1typlbl.grid(column = 1, row = 9, columnspan = 1, sticky = (W))
            weapon1rnglbl.grid(column = 2, row = 9, columnspan = 1, sticky = (W))
            weapon1ammlbl.grid(column = 3, row = 9, columnspan = 2, sticky = (W))
            weapon1damlbl.grid(column = 5, row = 9, columnspan = 2, sticky = (W))
            weapon1lblbox.grid(column = 1, row = 8, columnspan = 4, sticky = (W))
            weapon1atkbox.grid(column = 5, row = 8, columnspan = 1, sticky = (W))
            weapon1crtbox.grid(column = 6, row = 8, columnspan = 1, sticky = (W))
            weapon1typbox.grid(column = 1, row = 10, columnspan = 1, sticky = (W))
            weapon1rngbox.grid(column = 2, row = 10, columnspan = 1, sticky = (W))
            weapon1ammbox.grid(column = 3, row = 10, columnspan = 2, sticky = (W))
            weapon1dambox.grid(column = 5, row = 10, columnspan = 2, sticky = (W))

            weapon2lbllbl.grid(column = 1, row = 11, columnspan = 4, sticky = (W))
            weapon2atklbl.grid(column = 5, row = 11, columnspan = 1, sticky = (W))
            weapon2crtlbl.grid(column = 6, row = 11, columnspan = 1, sticky = (W))
            weapon2typlbl.grid(column = 1, row = 13, columnspan = 1, sticky = (W))
            weapon2rnglbl.grid(column = 2, row = 13, columnspan = 1, sticky = (W))
            weapon2ammlbl.grid(column = 3, row = 13, columnspan = 2, sticky = (W))
            weapon2damlbl.grid(column = 5, row = 13, columnspan = 2, sticky = (W))
            weapon2lblbox.grid(column = 1, row = 12, columnspan = 4, sticky = (W))
            weapon2atkbox.grid(column = 5, row = 12, columnspan = 1, sticky = (W))
            weapon2crtbox.grid(column = 6, row = 12, columnspan = 1, sticky = (W))
            weapon2typbox.grid(column = 1, row = 14, columnspan = 1, sticky = (W))
            weapon2rngbox.grid(column = 2, row = 14, columnspan = 1, sticky = (W))
            weapon2ammbox.grid(column = 3, row = 14, columnspan = 2, sticky = (W))
            weapon2dambox.grid(column = 5, row = 14, columnspan = 2, sticky = (W))

            weapon3lbllbl.grid(column = 1, row = 15, columnspan = 4, sticky = (W))
            weapon3atklbl.grid(column = 5, row = 15, columnspan = 1, sticky = (W))
            weapon3crtlbl.grid(column = 6, row = 15, columnspan = 1, sticky = (W))
            weapon3typlbl.grid(column = 1, row = 17, columnspan = 1, sticky = (W))
            weapon3rnglbl.grid(column = 2, row = 17, columnspan = 1, sticky = (W))
            weapon3ammlbl.grid(column = 3, row = 17, columnspan = 2, sticky = (W))
            weapon3damlbl.grid(column = 5, row = 17, columnspan = 2, sticky = (W))
            weapon3lblbox.grid(column = 1, row = 16, columnspan = 4, sticky = (W))
            weapon3atkbox.grid(column = 5, row = 16, columnspan = 1, sticky = (W))
            weapon3crtbox.grid(column = 6, row = 16, columnspan = 1, sticky = (W))
            weapon3typbox.grid(column = 1, row = 18, columnspan = 1, sticky = (W))
            weapon3rngbox.grid(column = 2, row = 18, columnspan = 1, sticky = (W))
            weapon3ammbox.grid(column = 3, row = 18, columnspan = 2, sticky = (W))
            weapon3dambox.grid(column = 5, row = 18, columnspan = 2, sticky = (W))

            weapon4lbllbl.grid(column = 1, row = 19, columnspan = 4, sticky = (W))
            weapon4atklbl.grid(column = 5, row = 19, columnspan = 1, sticky = (W))
            weapon4crtlbl.grid(column = 6, row = 19, columnspan = 1, sticky = (W))
            weapon4typlbl.grid(column = 1, row = 21, columnspan = 1, sticky = (W))
            weapon4rnglbl.grid(column = 2, row = 21, columnspan = 1, sticky = (W))
            weapon4ammlbl.grid(column = 3, row = 21, columnspan = 2, sticky = (W))
            weapon4damlbl.grid(column = 5, row = 21, columnspan = 2, sticky = (W))
            weapon4lblbox.grid(column = 1, row = 20, columnspan = 4, sticky = (W))
            weapon4atkbox.grid(column = 5, row = 20, columnspan = 1, sticky = (W))
            weapon4crtbox.grid(column = 6, row = 20, columnspan = 1, sticky = (W))
            weapon4typbox.grid(column = 1, row = 22, columnspan = 1, sticky = (W))
            weapon4rngbox.grid(column = 2, row = 22, columnspan = 1, sticky = (W))
            weapon4ammbox.grid(column = 3, row = 22, columnspan = 2, sticky = (W))
            weapon4dambox.grid(column = 5, row = 22, columnspan = 2, sticky = (W))

            weapon5lbllbl.grid(column = 1, row = 23, columnspan = 4, sticky = (W))
            weapon5atklbl.grid(column = 5, row = 23, columnspan = 1, sticky = (W))
            weapon5crtlbl.grid(column = 6, row = 23, columnspan = 1, sticky = (W))
            weapon5typlbl.grid(column = 1, row = 25, columnspan = 1, sticky = (W))
            weapon5rnglbl.grid(column = 2, row = 25, columnspan = 1, sticky = (W))
            weapon5ammlbl.grid(column = 3, row = 25, columnspan = 2, sticky = (W))
            weapon5damlbl.grid(column = 5, row = 25, columnspan = 2, sticky = (W))
            weapon5lblbox.grid(column = 1, row = 24, columnspan = 4, sticky = (W))
            weapon5atkbox.grid(column = 5, row = 24, columnspan = 1, sticky = (W))
            weapon5crtbox.grid(column = 6, row = 24, columnspan = 1, sticky = (W))
            weapon5typbox.grid(column = 1, row = 26, columnspan = 1, sticky = (W))
            weapon5rngbox.grid(column = 2, row = 26, columnspan = 1, sticky = (W))
            weapon5ammbox.grid(column = 3, row = 26, columnspan = 2, sticky = (W))
            weapon5dambox.grid(column = 5, row = 26, columnspan = 2, sticky = (W))

            wbuttonlbl.grid( column=1, row=27 )
            wbuttonnew.grid( column=1, row=28, sticky=(W) )
            wbuttonsave.grid( column=2, row=28, sticky=(W) )
            wbuttonload.grid( column=3, row=28, sticky=(W) )
            wbuttonexit.grid( column=4, row=28, sticky=(W) )
            
            character.add(content, text='Weapons')
