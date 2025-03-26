from django.shortcuts import render
from .Services import PlayerOperations


def home(request):
    return render(request,"index.html")


def login(request):
    if request.method=="POST":
        id=request.POST.get("userid")
        ps=request.POST.get("password")
        if id=="adesh" and ps=="AJ273":
            page='iplnformation.html'

        else:
            page='LoginFailed.html'

    return render(request,page)
           
        
def failed(request):
    return render(request,"LoginFailed.html")

def deleteplayer(request):
    return render(request,"DeletPlayerName.html")

def delete(request):
    if request.method=="POST":
        pid=str(request.POST.get("player_name"))
        obj=PlayerOperations()
        mess=obj.deleteplayer(pid)
        print(mess)
        return render(request,"Delete.html",{"message":mess})
    return render(request,"Delete.html")

def addplayer(request):
    return render(request,'AddPlayerInformation.html')


def success(request):
   if request.method=="POST":
      try:
        nm=request.POST.get("player_name")
        age = int(request.POST.get("player_age", 0))  # Default to 0 if empty
        country=request.POST.get("player_country")
        team=request.POST.get("ipl_team")
        price = float(request.POST.get("player_price", 0.0))  # Default to 0.0 if empty
        
        obj=PlayerOperations()
        mess=obj.addnewplayertodb(nm,age,country,team,price)
      except:
        print("error in data")
   return render(request,"PlayerAdded.html")

def IPLInformation(request):
    return render(request,"iplnformation.html")

def searchplayer(request):
    return render(request,"searchplayer.html")



def search(request):
    
    if request.method=="POST":
        try:
           team=request.POST.get("team")
           obj=PlayerOperations()
           data=obj.searchplayerfromteam(team)
           if data:
                return render(request,"search.html",{"data":data})
           else:
                 return render(request,"error.html")
        except:
            return render(request,"error.html")
            

def allplayers(request):
    obj=PlayerOperations()
    data=obj.allplayerlist()
    
    return render(request,"allplayerlist.html",{"playerdata":data})

    

def searchplayerhistry(request):
    return render(request,"searchplayerhistry.html")



def resulthistry(request):
    if request.method=="POST":
        try:
          nm=request.POST.get("playernm")
          obj=PlayerOperations()
          data=obj.playerhistry(nm)

        except:
            print("error in data")

    return render(request,"resulthistry.html",{"playerdata":data})
        
    
        
    
        
           
    



    