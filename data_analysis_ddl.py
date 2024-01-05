analysis_options = ["Select an analysis option"
                   ,"Descriptive Statistical Summary (Mean, Median, Mode, Range, 2nd & 3rd interquartile range"
                   ,"Anova"]

statistical_methods = tk.StringVar()
stat_methods = ['Mean','Median','Max','Min']
statistical_methods.set(stat_methods[0])
stat_method_dropdown = tk.OptionMenu(frame, statistical_methods, *stat_methods)