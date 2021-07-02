let team1=document.getElementById("Name1")
let team2=document.getElementById("Name2")

let Toss=document.querySelector(".Toss_value")

let val1=document.createElement('option')
let val2=document.createElement('option')
val1.id=("Name_1")
val2.id="Name_2"


function Add_Element(Id)
{
    console.log(Id)
    if(Id==1)
    { 
        val1.value=team1.value
        val1.innerHTML=team1.value
        Toss.add(val1)
    }
    else{
        val2.value=team2.value
        val2.innerHTML=team2.value
        Toss.add(val2)

    }
   

}

// Removing Element Teams input
function Remove_Element(Id)
{
    console.log(Id.id,' ',Toss.options[1])
    if(Toss.options[1].id==Id.id)Toss.remove(1);
    else Toss.remove(2);
}



team1.addEventListener("change",function(){
    let Team_2=document.getElementById("Name_2")
    let Team_1=document.getElementById("Name_1")
    if(Team_2!=null)
    {
        if((val2).innerHTML==team1.value)
        {
            alert("Pick a different team")
            team1.value=""
            if(Team_1!=null)
            {
                Remove_Element(Name_1)
            }
        }
        else 
        {
            if(Team_1==null)Add_Element(1)
            else Team_1.innerHTML=team1.value

        }
        
    }
    else
    {
        if(Team_1==null)Add_Element(1)
        else Team_1.innerHTML=team1.value
    }
})



team2.addEventListener("change",function(){
    let Team_2=document.getElementById("Name_2")
    let Team_1=document.getElementById("Name_1")
    
    if(Team_1!=null)
    {
        console.log(Team_1.innerHTML,' ',team2.value)
        if((val1).innerHTML==team2.value)
        {
            alert("Pick a different team")
            team2.value=""
            if(Team_2!=null)
            {
                Remove_Element(Name_2)
            }
        }
        else {
            if(Team_2==null)Add_Element(2)
            else Team_2.innerHTML=team2.value
        }
        
    }
    else{
            if(Team_2==null)Add_Element(2)
            else Team_2.innerHTML=team2.value
    }
})








