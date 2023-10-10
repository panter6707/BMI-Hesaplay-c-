import tkinter

window = tkinter.Tk()
window.title("MKYLisans BMI Hesaplama")
window.config(width=300,height=300,padx=300, pady=300)

def bosluk_mky():
    bosluk_mky1 = tkinter.Label(width=100)
    bosluk_mky1.pack()




def calculate_bmi():
    height = height_input_mky.get()
    weight = weight_input_mky.get()

    if weight == "" or height == "":
        result_label_mky.config(text="Lütfen boy ve kilonuzu Giriniz!!!")
    else:
        try:
            bmi_mky = float(weight) / ((float(height) / 100) ** 2)
            result_string = write_result_MKYLisans(bmi_mky)
            result_label_mky.config(text= result_string)
        except:
            result_label_mky.config(text="Düzgün bir sayı giriniz.")



weight_input_label_mky = tkinter.Label(text="Kilonuzu Giriniz (Kg cinsinde)")
weight_input_label_mky.pack()

bosluk_mky()

weight_input_mky = tkinter.Entry(width=50, font=("times", 20, "bold"), bg= "light blue", fg="red")
weight_input_mky.pack()

bosluk_mky()

height_input_label_mkyLisans = tkinter.Label(text="Boyunuzu Giriniz (cm cinsinden)")
height_input_label_mkyLisans.pack()

height_input_mky = tkinter.Entry(width=50,font=("times", 20, "bold"), bg= "light blue", fg="red")
height_input_mky.pack()


bosluk_mky()
bosluk_mky()

calculate_buttom_mky = tkinter.Button(text="Hesaplama Yap",width=50,font=("times", 20, "bold"), bg= "light blue", fg="red",pady=50, command=calculate_bmi)
calculate_buttom_mky.pack()

result_label_mky = tkinter.Label(width=50,font=("times", 20, "bold"), bg= "light blue", fg="red",pady=50)
result_label_mky.pack()

def write_result_MKYLisans(bmi_mky):
    result_string = f"Sizin BMI nız : {round(bmi_mky,2)}. Sizin "
    if bmi_mky <=16:
        result_string += "Çok Zayıfsınız!"
    elif bmi_mky >16 and bmi_mky <=17:
        result_string += "Orta Derece Zayıfsınız"
    elif bmi_mky >17 and bmi_mky <=18.5:
        result_string += "Hafif Zayıfsınız"
    elif bmi_mky > 18.5 and bmi_mky <= 25:
        result_string += "Normalsiniz"
    elif bmi_mky > 25 and bmi_mky <= 30:
        result_string += "Şişmansınız"
    elif bmi_mky > 30 and bmi_mky <= 35:
        result_string += "1. Sınıf Obezsiniz"
    elif bmi_mky > 35 and bmi_mky <= 40:
        result_string += "2. Sınıf Obezsiniz"
    else:
        result_string += "3. Sınıf Obezsiniz"
    return result_string




window.mainloop()