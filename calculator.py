from tkinter import *
window = Tk()
window.geometry("280x280")
window.title("Calculator")
window.configure(background="#1C1C1C")
text=Text(window,bg="white",fg="black",width="24", height="2",)
text.place(x=50,y=20)

button1=Button(text="7",bg="#505050",fg="white",width="5",height="1",font=('SansSerif Bold',13))
button2=Button(text="8",bg="#505050",fg="white",width="5",height="1",font=('SansSerif Bold',13))
button3=Button(text="9",bg="#505050",fg="white",width="5",height="1",font=('SansSerif Bold',13))
button4=Button(text="X",bg="#FF9500",fg="white",width="5",height="1",font=('SansSerif Bold',13))

button5=Button(text="4",bg="#505050",fg="white",width="5",height="1",font=('SansSerif Bold',13))
button6=Button(text="5",bg="#505050",fg="white",width="5",height="1",font=('SansSerif Bold',13))
button7=Button(text="6",bg="#505050",fg="white",width="5",height="1",font=('SansSerif Bold',13))
button8=Button(text="-",bg="#FF9500",fg="white",width="5",height="1",font=('SansSerif Bold',13))

button9=Button(text="1",bg="#505050",fg="white",width="5",height="1",font=('SansSerif Bold',13))
button10=Button(text="2",bg="#505050",fg="white",width="5",height="1",font=('SansSerif Bold',13))
button11=Button(text="3",bg="#505050",fg="white",width="5",height="1",font=('SansSerif Bold',13))
button12=Button(text="+",bg="#FF9500",fg="white",width="5",height="1",font=('SansSerif Bold',13))

button13=Button(text="AC",bg="#D4D4D2",fg="white",width="9",height="1",font=('SansSerif Bold',13))
button14=Button(text="0",bg="#505050",fg="white",width="9",height="1",font=('SansSerif Bold',13))
button15=Button(text="/",bg="#FF9500",fg="white",width="5",height="1",font=('SansSerif Bold',13))

button1.place(x=13,y=80)
button2.place(x=83,y=80)
button3.place(x=153,y=80)
button4.place(x=223,y=80)

button5.place(x=13,y=125)
button6.place(x=83,y=125)
button7.place(x=153,y=125)
button8.place(x=223,y=125)

button9.place(x=13,y=170)
button10.place(x=83,y=170)
button11.place(x=153,y=170)
button12.place(x=223,y=170)

button13.place(x=15,y=220)
button14.place(x=115,y=220)
button15.place(x=223,y=220)

window.mainloop()
