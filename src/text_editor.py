import PySimpleGUI as sg

sg.theme('DarkPurple7')  

def ltab(i=0):
   return [[sg.Multiline(default_text='',disabled=False, size=(800,33.5),key=f'-multline{i}-')]]
def main_window():
    tabgl = [[sg.Tab('New File',ltab(),key='0')]]
    tabg = sg.TabGroup(tabgl,key='-tabs-')
    layout = [[sg.Menu([['File', ['New File','Open','Close']], ['Edit', ['Edit Me', ]]],  k='-CUST MENUBAR-',p=0)],
            [tabg]]
    i = 1
    
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
                

                ctab = window['-tabs-'].get()
                print(ctab)
                window[ctab].update(title=tabname)
                window[f'-multline{ctab}-'].update(text)
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
            window[values['-tabs-']].update('',visible=False)
    window.close()

main_window()