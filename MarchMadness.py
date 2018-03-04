"""
AutoCompleteEntry class taken from: https://gist.github.com/uroshekic/11078820
"""

from tkinter import *
import re
import DataImporter as di
import Predictor as pred

class AutocompleteEntry(Entry):
    def __init__(self, autocompleteList, *args, **kwargs):

        # Listbox length
        if 'listboxLength' in kwargs:
            self.listboxLength = kwargs['listboxLength']
            del kwargs['listboxLength']
        else:
            self.listboxLength = 8

        # Custom matches function
        if 'matchesFunction' in kwargs:
            self.matchesFunction = kwargs['matchesFunction']
            del kwargs['matchesFunction']
        else:
            def matches(fieldValue, acListEntry):
                pattern = re.compile('.*' + re.escape(fieldValue) + '.*', re.IGNORECASE)
                return re.match(pattern, acListEntry)
                
            self.matchesFunction = matches

        
        Entry.__init__(self, *args, **kwargs)
        self.focus()

        self.autocompleteList = autocompleteList
        
        self.var = self["textvariable"]
        if self.var == '':
            self.var = self["textvariable"] = StringVar()

        self.var.trace('w', self.changed)
        self.bind("<Right>", self.selection)
        self.bind("<Up>", self.moveUp)
        self.bind("<Down>", self.moveDown)
        
        self.listboxUp = False

    def changed(self, name, index, mode):
        if self.var.get() == '':
            if self.listboxUp:
                self.listbox.destroy()
                self.listboxUp = False
        else:
            words = self.comparison()
            if words:
                if not self.listboxUp:
                    self.listbox = Listbox(width=self["width"], height=self.listboxLength)
                    self.listbox.bind("<Button-1>", self.selection)
                    self.listbox.bind("<Right>", self.selection)
                    self.listbox.place(x=self.winfo_x(), y=self.winfo_y() + self.winfo_height())
                    self.listboxUp = True
                
                self.listbox.delete(0, END)
                for w in words:
                    self.listbox.insert(END,w)
            else:
                if self.listboxUp:
                    self.listbox.destroy()
                    self.listboxUp = False
        
    def selection(self, event):
        if self.listboxUp:
            self.var.set(self.listbox.get(ACTIVE))
            self.listbox.destroy()
            self.listboxUp = False
            self.icursor(END)

    def moveUp(self, event):
        if self.listboxUp:
            if self.listbox.curselection() == ():
                index = '0'
            else:
                index = self.listbox.curselection()[0]
                
            if index != '0':                
                self.listbox.selection_clear(first=index)
                index = str(int(index) - 1)
                
                self.listbox.see(index) # Scroll!
                self.listbox.selection_set(first=index)
                self.listbox.activate(index)

    def moveDown(self, event):
        if self.listboxUp:
            if self.listbox.curselection() == ():
                index = '0'
            else:
                index = self.listbox.curselection()[0]
                
            if index != END:                        
                self.listbox.selection_clear(first=index)
                index = str(int(index) + 1)
                
                self.listbox.see(index) # Scroll!
                self.listbox.selection_set(first=index)
                self.listbox.activate(index) 

    def comparison(self):
        return [ w for w in self.autocompleteList if self.matchesFunction(self.var.get(), w) ]




if __name__ == '__main__':
    root = Tk()
    # Get all team names from the data to populate the autocomplete.
    root.title('March Madness Predictor')
    name = di.DataImporter()
    autocompleteList = name.getAllTeamNames()
    # Matching funciton
    def matches(fieldValue, acListEntry):
        pattern = re.compile(re.escape(fieldValue) + '.*', re.IGNORECASE)
        return re.match(pattern, acListEntry)
    # Send team1 and team2 to go do calculation
    def calculate():
        # Highlight which input has issues
        if firstTeamInput.get() not in autocompleteList or len(firstTeamInput.get()) is 0:
            firstTeamInput.configure(bg='red')
        else:
            firstTeamInput.configure(bg='white')

        # Highlight which input has issues
        if secondTeamInput.get() not in autocompleteList or len(secondTeamInput.get()) is 0:
            secondTeamInput.configure(bg='red')
        else:
            secondTeamInput.configure(bg='white')
        if(firstTeamInput.get() in autocompleteList and secondTeamInput.get() in autocompleteList):
            firstTeamInput.configure(bg='white')
            secondTeamInput.configure(bg='white')
            # Send team values to the predictor to do analysis
            predictor = pred.Predictor()
            winner = predictor.doStuff(firstTeamInput.get(), secondTeamInput.get())
            message = 'Expected Winner: \n' + winner
        else:
            message = 'Please enter a valid team.'
        winnerLabel.configure(text=message)
        winnerLabel.grid(row=4, padx=10, pady=10)

    # Create widgets and place on the grid
    winnerLabel = Label(text="")
    firstTeamInput = AutocompleteEntry(autocompleteList, root, listboxLength=6, width=32, matchesFunction=matches)
    firstTeamInput.grid(row=0, padx=10, pady=10)    
    vsLabel = Label(text='VS')
    vsLabel.grid(row=1, padx=10, pady=10)
    secondTeamInput = AutocompleteEntry(autocompleteList, root, listboxLength=6, width=32, matchesFunction=matches)
    secondTeamInput.grid(row=2, padx=10, pady=10)  
    calculateButton = Button(text='Determine Winner',command=calculate)
    calculateButton.grid(row=3, padx=10, pady=10)
    quitButton = Button(text='Quit',command=quit)
    quitButton.grid(row=5, padx=10, pady=10)
    # root.geometry('{}x{}'.format(500,500))
    root.mainloop()