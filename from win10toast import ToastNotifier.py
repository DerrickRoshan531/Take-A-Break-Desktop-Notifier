from win10toast import ToastNotifier

toaster = ToastNotifier()
toaster.show_toast("Take Rest", 
                   "Rest is important for your brain and body.",
                   duration=60*60)
