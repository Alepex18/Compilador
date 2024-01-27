import PySimpleGUI as sg

sg.theme('DarkPurple7')  

def ltab(i=0,mdata=None):
   window = sg.Window('Test', [[]])
   width,height, = window.get_screen_dimensions()
   return [[sg.Multiline(default_text='',disabled=False, size=(width,height),key=f'-multline{i}-', metadata=mdata)]]

def main_window():
    tabgl = [[sg.Tab('New File',ltab(),key='0')]]
    tabg = sg.TabGroup(tabgl,key='-tabs-')
    layout = [[sg.Menu([['File', ['New File','Open','Save','Close']], ['Edit', ['Edit Me', ]]],  k='-CUST MENUBAR-',p=0)],
            [tabg]]
    i = 1
    files_opened = []
    # Create the Window
    window = sg.Window('Test', layout,resizable=True)
    
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED: # if user closes window
            break
        if event == 'New File': # if user clicks Add Tab
            tabg.add_tab(sg.Tab(f'New File {i}',ltab(i),key=i))
            window[i].select()
            i += 1
            window.finalize
        if event == 'Open': # if user clicks Open
            filename = sg.popup_get_file('file to open', no_window=True)
            print(filename)
            if filename !='':
                import ntpath
                tabname = ntpath.basename(filename)
                with open(filename,'r') as file:
                    text = file.read()
                print(files_opened)    
                if tabname not in files_opened:
                    files_opened.append(filename)
                    
                    tabg.add_tab(sg.Tab(f'New File {i}',ltab(i,filename),key=i))
                    window[i].select()
                    i += 1
                    window.finalize

                    ctab = window['-tabs-'].get()
                    print(ctab)
                    window[ctab].update(title=tabname)
                    window[f'-multline{ctab}-'].update(text)
                    
                else:
                    sg.popup_ok(f"El archivo {tabname} ya esta abierto")
        if event == 'Save':
            ctab = window['-tabs-'].get() 
            file_to_save = window[f'-multline{ctab}-'].metadata   
            
            if file_to_save is not None:
                print(file_to_save)
                with open(file_to_save,'w') as file:
                    file.write(values[f'-multline{ctab}-'])     
        if event == 'Close': # if user clicks Close
            # Code to actually delete the tab (isn't working well)
            
            """ #get the index of the tab that is selected
            index = window["-tabs-"].TKNotebook.index('current')
            #remove the selected tab from the TabGroup.TKNotebook
            #TabGroup.TkNotebook is part of the structure for how a TabGroup is defined
            window["-tabs-"].TKNotebook.forget(window["-tabs-"].TKNotebook.select())
            #Remove the tab_element from the list of tabs (TabGroup.Rows)
            window["-tabs-"].Rows.pop(index)
            #Update the TabCount(part of the structure of TabGroups)
            window["-tabs-"].TabCount -= 1
            window.refresh """
            
            # Code that makes the current tab invisible
            ctab = window['-tabs-'].get() 
            file_to_close = window[f'-multline{ctab}-'].metadata
            if file_to_close in files_opened:
                files_opened.remove(file_to_close)
                
            window[values['-tabs-']].update('',visible=False)
            
    window.close()

main_window()