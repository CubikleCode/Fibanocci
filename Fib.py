from tkinter import *

root=Tk()

root.title("Fibonacci")
root.geometry("400x400")

label_series = Label(root, text="Fibonacci Series: ")
label_total = Label(root)
label_spiral = Label(root)

def Fibionacci():
#couldn't get user imputs to work :(
    num=10
    first_num=0
    second_num=1
    sum=0
    sum2=0
    counter=1
    while(counter<=num):
        label_series["text"] += str(sum) + " "
        counter=counter+1
        first_num = second_num
        second_num = sum
        sum = first_num + second_num
        sum2=sum2+second_num
        label_total['text'] = "The Fibonacci Sum is "+str(sum2)
        
btn = Button(root, text = "Show Fibonacci Series", command=Fibionacci)
btn.pack()
label_series.pack()
label_total.pack()


root.mainloop()