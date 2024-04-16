import PySimpleGUI as sg
import ntpath

sg.theme('DarkPurple7')  
files_opened = []

def ltab(i=0,mdata=None):
   window = sg.Window('Test', [[]])
   width,height, = window.get_screen_dimensions()
   return [[sg.Multiline(default_text='',disabled=False, 
                         size=(width,height),key=f'-multline{i}-', 
                         metadata=mdata)]]
   
def lexictablayout():
   return [[sg.Text('Numeros: ',key='-numbers-')],
           [sg.Multiline(default_text='',disabled=True,key='-numberslist-',expand_y=True, expand_x=True)],
           [sg.Text('Letras: ',key='-letters-')],
           [sg.Multiline(default_text='',disabled=True,key='-letterslist-',expand_y=True, expand_x=True)],
           [sg.Text('Caracteres Especiales: ',key='-specialc-')],
           [sg.Multiline(default_text='',disabled=True,key='-specialclist-',expand_y=True, expand_x=True)]]

def lexictab(window,values,ctab):
    if ctab is not None:
        text_to_analyse = values[f'-multline{ctab}-']
        from get_character import get_characters
        lexic_analised_text = get_characters(text_to_analyse)
        window['-numbers-'].update(f'Numeros: {lexic_analised_text['numbers']['count']}') 
        window['-numberslist-'].update(', '.join(lexic_analised_text['numbers']['list']))
        window['-letters-'].update(f'Letras: {lexic_analised_text['letters']['count']}')
        window['-letterslist-'].update(', '.join(lexic_analised_text['letters']['list']))
        window['-specialc-'].update(f'Carácteres Especiales: {lexic_analised_text['special_characters']['count']}')
        window['-specialclist-'].update(', '.join(lexic_analised_text['special_characters']['list']))
        window['-lexic-'].select()

def lexicwindow(values,ctab):
    if ctab is not None:
        sg.easy_print_close()
        text_to_analyse = values[f'-multline{ctab}-']
        from get_character import get_characters
        lexic_analised_text = get_characters(text_to_analyse)
        string_numeros = f"Numeros:\nCantidad: {lexic_analised_text['numbers']['count']}\nLista: {lexic_analised_text['numbers']['list']}\n\n"
        string_letras = f"Letras:\nCantidad: {lexic_analised_text['letters']['count']}\nLista: {lexic_analised_text['letters']['list']}\n\n"
        string_caracteres_especiales = f"Carácteres Especiales:\nCantidad: {lexic_analised_text['special_characters']['count']}\nLista: {lexic_analised_text['special_characters']['list']}\n"       
        sg.Print(string_numeros+string_letras+string_caracteres_especiales) 
        
def open_file(window,j,filename=None):
    if filename is None:
        filename = sg.popup_get_file('file to open', no_window=True)
    if filename !='':
        
        tabname = ntpath.basename(filename)
        with open(filename,'r') as file:
            text = file.read()
        print(files_opened)    
        if filename not in files_opened:
            files_opened.append(filename)
            
            window['-tabs-'].add_tab(sg.Tab(tabname,ltab(f'{tabname}{j}',filename),key=f'{tabname}{j}'))
            window[f'{tabname}{j}'].select()
            window.finalize

            ctab = window['-tabs-'].get()
            print(f'current tab {ctab}')
            window[f'-multline{ctab}-'].update(text)
            window[f'-texteditor-'].select()
            
        else:
            sg.popup_ok(f"El archivo {tabname} ya esta abierto")
            
def save_as(window,values):
    ctab = window['-tabs-'].get()
    if ctab is not None:
        try: # 'OUT OF INDEX' error in Trinket if 'CANCEL' button is clicked
            filename = sg.popup_get_file('Save File', save_as=True, no_window=True)
        except:
            return
        if filename not in (None,''):
            if not filename.endswith('.txt'):
                filename += '.txt'
            
            with open(filename,'w') as f:
                f.write(values[f'-multline{ctab}-'])
            close_file(window,values)
            open_file(window,values,filename)
        

def close_file (window,values):
    # Code that makes the current tab invisible
        ctab = window['-tabs-'].get() 
        file_to_close = window[f'-multline{ctab}-'].metadata
        if file_to_close in files_opened:
            files_opened.remove(file_to_close)
        window[values['-tabs-']].update('',visible=False)
    
    
def main_window():
    use_lexic_tab = True #Change to false to use a window for lexic analisis display
    tabgl = [[sg.Tab('New File',ltab(),key='0')]]
    tabg = sg.TabGroup(tabgl,key='-tabs-')
    tabggl = [[sg.Tab('Text Editor',[[tabg if use_lexic_tab else sg.Text('')]],key='-texteditor-')],
              [sg.Tab('Lexic Analisis',lexictablayout(),key='-lexic-')]]
    tabgg = sg.TabGroup(tabggl,key='-tabgroup-')
    layout = [[sg.Menu([['File', ['New File','Open','Save','Save As','---','Close']],['Analisis',['Lexic']]],  k='-CUST MENUBAR-',p=0)],
            [tabgg if use_lexic_tab else tabg]]
    i = 1
    j = 0
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
            open_file(window,j)
            j +=1
        if event == 'Save': # if user clicks Save
            ctab = window['-tabs-'].get()
            if ctab is not None: 
                file_to_save = window[f'-multline{ctab}-'].metadata   
                
                if file_to_save is not None:
                    print(file_to_save)
                    with open(file_to_save,'w') as file:
                        file.write(values[f'-multline{ctab}-'])
                else:
                    save_as(window,values) 
        if event == 'Save As': # if user clicks Save
            save_as(window,values) 
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
            close_file(window,values)
        if event == 'Lexic':
            ctab = window['-tabs-'].get()
            if use_lexic_tab:
                lexictab(window,values,ctab)
            else:
                lexicwindow(values,ctab)
        # if event == 'why':
        #     ctab = window['-tabs-'].get()
        #     print(ctab)
    window.close()

main_window()