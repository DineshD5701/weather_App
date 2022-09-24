from tkinter import *
#pip install requests
import requests
root=Tk()
def getWeather(weather):
    city=textField.get()
    api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=80ab80d0e0a68ef849e95a15288dfd1c"
    

    _data=requests.get(api).json()
    condition=_data['weather'][0]['main']
    temp=int(_data['main']['temp']-273.15)
    pressure=_data['main']['pressure']
    humidity=_data['main']['humidity']
    wind_speed=_data['wind']['speed']
 

    final_info="Sky Condition:"+condition +"\n"+"Temp:"+str(temp)+"°c"+"\n"+"Pressure:"+str(pressure)        
    label.config(text=final_info)
    result="Humidity:"+str(humidity)+"\n"+"Wind Speed:"+str(wind_speed)
    label1.config(text=result)
    
    
    
root.title("Weather App")
root.config(bg="lightgreen")
a=Label(root,text="WEATHER APP",font=("poppins",25))
a.pack()

textField=Entry(root,justify="center",font=("poppins",20,"bold"))
textField.pack(pady=40)
textField.bind("<Return>",getWeather)
label=Label(root,font=("poppins",15))
label.pack()
label1=Label(root,font=("poppins",15))
label1.pack()
root.mainloop()
